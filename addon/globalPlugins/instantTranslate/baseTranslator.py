# Copyright (C) 2013 - 2024 Mesar Hameed <mhameed@src.gnome.org>, Beka gozalishvili <beqaprogger@gmail.com>
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

import json
import os
import re
import threading
from time import time
from urllib.parse import urlencode

from logHandler import log

from .httpClient import DEFAULT_TIMEOUT, Session

# Each group has to be a class of possible breaking points for the writing script.
# Usually this is the major syntax marks, such as: full stop, comma, exclaim, question, etc.
ARABIC_BREAKS = "[،؛؟]"
# Thanks to Talori in the NVDA irc room:
# U+3000 to U+303F, U+FE10 to U+FE1F, U+FE30 to U+FE6F, U+FF01 to U+FF60
CHINESE_BREAKS = "[　-〿︐-︟︰-﹯！-｠]"
LATIN_BREAKS = r"[.,!?;:]"
SPLIT_PATTERN = re.compile("|".join((ARABIC_BREAKS, CHINESE_BREAKS, LATIN_BREAKS)))

def cachePath(fileName):
	return os.path.join(os.path.dirname(os.path.abspath(__file__)), fileName)


def encodedLength(text):
	return len(urlencode({"q": text})) - 2


def splitChunks(text, chunkSize, measure=len):
	sizes = [0]
	for char in text:
		sizes.append(sizes[-1] + measure(char))

	def sizeOf(start, end):
		return sizes[end] - sizes[start]

	def emit(start, end):
		while start < end:
			stop = start + 1
			while stop < end and sizeOf(start, stop + 1) <= chunkSize:
				stop += 1
			yield text[start:stop]
			start = stop

	pos = potentialPos = 0
	for splitMark in SPLIT_PATTERN.finditer(text):
		if sizeOf(pos, splitMark.start() + 1) < chunkSize:
			potentialPos = splitMark.start()
			continue
		yield from emit(pos, potentialPos + 1)
		pos = potentialPos + 1
		potentialPos = splitMark.start()
	yield from emit(pos, len(text))


class LanguageCache:
	def __init__(self, path, ttl, fetch, getContext=None):
		self.path = path
		self.ttl = ttl
		self.fetch = fetch
		self.getContext = getContext or (lambda: "")
		self._lock = threading.RLock()
		self._refreshing = False
		self._languages = None
		self._timestamp = 0
		self._context = None
		self._load()

	def _load(self):
		try:
			with open(self.path, "r", encoding="utf-8") as cacheFile:
				cached = json.load(cacheFile)
		except FileNotFoundError:
			return
		except Exception:
			log.warning("Instant translate: unreadable language cache %s" % self.path, exc_info=True)
			return
		self._languages = cached.get("languages")
		self._timestamp = cached.get("timestamp", 0)
		self._context = cached.get("context")

	def _save(self):
		cached = {
			"timestamp": self._timestamp,
			"context": self._context,
			"languages": self._languages,
		}
		try:
			with open(self.path, "w", encoding="utf-8") as cacheFile:
				json.dump(cached, cacheFile, ensure_ascii=False, indent="\t", sort_keys=True)
		except Exception:
			log.warning("Instant translate: cannot write language cache %s" % self.path, exc_info=True)

	@property
	def isStale(self):
		if self._languages is None:
			return True
		if self._context != self.getContext():
			return True
		return abs(time() - self._timestamp) > self.ttl

	def get(self, refresh=True):
		with self._lock:
			if refresh and self.isStale:
				self.refreshInBackground()
			return self._languages

	def refresh(self):
		try:
			languages = self.fetch()
		except Exception:
			log.warning("Instant translate: cannot fetch the supported languages", exc_info=True)
			return False
		if not languages:
			log.warning("Instant translate: the supported languages request returned nothing")
			return False
		with self._lock:
			self._languages = languages
			self._timestamp = time()
			self._context = self.getContext()
			self._save()
		return True

	def refreshInBackground(self):
		with self._lock:
			if self._refreshing:
				return
			self._refreshing = True
		def run():
			try:
				self.refresh()
			finally:
				with self._lock:
					self._refreshing = False
		threading.Thread(target=run, daemon=True, name="InstantTranslateLanguages").start()


class BaseTranslator(threading.Thread):
	backEndName = "base"
	maxChunkSize = 12000
	legacyCodes = {"iw": "he", "jw": "jv"}
	timeout = DEFAULT_TIMEOUT

	def __init__(
		self,
		langFrom,
		langTo,
		text,
		langSwap=None,
		chunkSize=None,
		onSuccess=None,
		onError=None,
		onProgress=None,
		onFinished=None,
	):
		super().__init__(name="InstantTranslate%s" % type(self).__name__, daemon=True)
		if langFrom != "auto" and langSwap is not None:
			raise ValueError(
				"langSwap=%r is only meaningful with langFrom='auto', got langFrom=%r"
				% (langSwap, langFrom)
			)
		self.langFrom = langFrom
		self.langTo = langTo
		self.text = text
		self.langSwap = langSwap
		self.chunkSize = chunkSize or self.maxChunkSize
		self.onSuccess = onSuccess
		self.onError = onError
		self.onProgress = onProgress
		self.onFinished = onFinished
		self.chunks = list(splitChunks(text, self.chunkSize, encodedLength))
		self.completedChunks = 0
		self.translation = ""
		self.detectedLanguage = ""
		self.error = False
		self._stopEvent = threading.Event()
		self.session = Session(timeout=self.timeout)

	@property
	def totalChunks(self):
		return len(self.chunks)

	@property
	def remainingChunks(self):
		return self.totalChunks - self.completedChunks

	@property
	def percentDone(self):
		if not self.totalChunks:
			return 100
		return int(round(self.completedChunks * 100.0 / self.totalChunks))

	def stop(self):
		self._stopEvent.set()
		try:
			self.session.close()
		except Exception:
			log.debug("Instant translate: cannot abort the request of %s" % self.backEndName, exc_info=True)

	@property
	def shouldStop(self):
		return self._stopEvent.is_set()

	def run(self):
		try:
			self._translateChunks()
		finally:
			self._reportOutcome()

	def _translateChunks(self):
		for index, chunk in enumerate(self.chunks):
			if self.shouldStop:
				return
			try:
				translation, detected = self.translateChunk(chunk, self.langTo)
				self.detectedLanguage = self.legacyCodes.get(detected, detected)
				if index == 0 and self.shouldSwap():
					self.langTo = self.langSwap
					translation, detected = self.translateChunk(chunk, self.langTo)
			except Exception:
				if self.shouldStop:
					return
				log.exception("Instant translate: %s cannot translate %r" % (self.backEndName, chunk))
				self.error = True
				return
			self.translation += translation
			self.completedChunks = index + 1
			self._report(self.onProgress)

	def _reportOutcome(self):
		if not self.shouldStop:
			self._report(self.onError if self.error else self.onSuccess)
		self._report(self.onFinished)

	def _report(self, callback):
		if callback is None:
			return
		try:
			callback(self)
		except Exception:
			log.exception("Instant translate: a %s callback failed" % self.backEndName)

	def shouldSwap(self):
		return (
			self.langSwap is not None
			and self.langFrom == "auto"
			and self.detectedLanguage == self.langTo
		)

	def translateChunk(self, chunk, langTo):
		raise NotImplementedError
