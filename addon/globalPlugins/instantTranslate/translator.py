# encoding: utf-8
#
# Copyright (C) 2013 - 2016 Mesar Hameed <mhameed@src.gnome.org>, Beqa gozalishvili
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

import os
import re
import sys
import ssl
import threading
from time import sleep
from random import randint
from logHandler import log

impPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(impPath)
import json
import urllib2
del sys.path[-1]

ssl._create_default_https_context = ssl._create_unverified_context
# Each group has to be a class of possible breaking points for the writing script.
# Usually this is the major syntax marks, such as:
# full stop, comma, exclaim, question, etc.
arabicBreaks = u'[،؛؟]'
# Thanks to Talori in the NVDA irc room:
# U+3000 to U+303F, U+FE10 to U+FE1F, U+FE30 to U+FE6F, U+FF01 to U+FF60
chineseBreaks = u'[　-〿︐-︟︰-﹯！-｠]'
latinBreaks = r'[.,!?;:]'
splitReg = re.compile(u"{arabic}|{chinese}|{latin}".format(arabic=arabicBreaks, chinese=chineseBreaks, latin=latinBreaks))

def splitChunks(text, chunksize):
	pos = 0
	potentialPos = 0
	for splitMark in splitReg.finditer(text):
		if (splitMark.start() - pos +1) < chunksize:
			potentialPos = splitMark.start()
			continue
		else:
			yield text[pos:potentialPos+1]
			pos = potentialPos + 1
			potentialPos = splitMark.start()
	yield text[pos:]

class Translator(threading.Thread):

	def __init__(self, lang_from, lang_to, text, lang_swap=None, chunksize=3000, *args, **kwargs):
		super(Translator, self).__init__(*args, **kwargs)
		self._stop = threading.Event()
		self.text = text
		self.chunksize = chunksize
		self.lang_to = lang_to
		self.lang_from = lang_from
		self.lang_swap = lang_swap
		self.translation = ''
		self.opener = urllib2.build_opener()
		self.opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		self.firstChunk = True

	def stop(self):
		self._stop.set()

	def run(self):
		urlTemplate = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl={lang_from}&tl={lang_to}&dt=t&q={text}'
		for chunk in splitChunks(self.text, self.chunksize):
			# Make sure we don't send requests to google too often.
			# Try to simulate a human.
			if not self.firstChunk:
				sleep(randint(1, 10))
			url = urlTemplate.format(lang_from=self.lang_from, lang_to=self.lang_to, text=urllib2.quote(chunk.encode('utf-8')))
			try:
				response = json.load(self.opener.open(url))
				if self.firstChunk and self.lang_from == "auto" and response["src"] == self.lang_to and self.lang_swap is not None:
					self.lang_to = self.lang_swap
					self.firstChunk = False
					url = urlTemplate.format(lang_from=self.lang_from, lang_to=self.lang_to, text=urllib2.quote(chunk.encode('utf-8')))
					response = json.load(self.opener.open(url))
			except Exception as e:
				log.exception("Instant translate: Can not translate text '%s'" %chunk)
				# We have probably been blocked, so stop trying to translate.
				raise e
			self.translation += "".join(r[0] for r in response[0])
