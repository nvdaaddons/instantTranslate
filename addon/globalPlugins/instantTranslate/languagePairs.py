# Copyright (C) 2026 Beka Gozalishvili <beqaprogger@gmail.com>
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

from collections import namedtuple

from logHandler import log
import addonHandler

from .langslist import getLanguageName

addonHandler.initTranslation()

PAIR_KEYS = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
MAX_PAIRS = len(PAIR_KEYS)
SEPARATOR = ":"


class LanguagePair(namedtuple("LanguagePair", ("langFrom", "langTo"))):

	@classmethod
	def parse(cls, value):
		langFrom, separator, langTo = value.partition(SEPARATOR)
		if not separator or not langFrom or not langTo:
			return None
		return cls(langFrom, langTo)

	def format(self):
		return "%s%s%s" % (self.langFrom, SEPARATOR, self.langTo)

	@property
	def label(self):
		# Translators: a language pair, listed in the language pairs dialog.
		return _("{lang1} to {lang2}").format(
			lang1=getLanguageName(self.langFrom, short=True),
			lang2=getLanguageName(self.langTo, short=True),
		)


def parsePairs(values):
	pairs = []
	for value in values or ():
		pair = LanguagePair.parse(value)
		if pair is None:
			log.warning("Instant translate: ignoring the malformed language pair %r" % (value,))
			continue
		pairs.append(pair)
		if len(pairs) == MAX_PAIRS:
			break
	return pairs


def formatPairs(pairs):
	return [pair.format() for pair in pairs[:MAX_PAIRS]]


def slotLabel(index, pair):
	# Translators: an entry of the language pairs list. {key} is the key of the layer activating the
	return _("{key}: {pair}").format(key=PAIR_KEYS[index], pair=pair.label)
