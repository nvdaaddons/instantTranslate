# encoding: utf-8
#
# Copyright (C) 2013 Mesar Hameed <mhameed@src.gnome.org>
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

import os
import re
import sys
import threading
from time import sleep
from random import randint
from logHandler import log

impPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(impPath)
import urllib2
del sys.path[-1]

# Each group has to be a class of possible breaking points for the writing script.
# Usually this is the major syntax marks, such as:
# full stop, comma, exclaim, question, etc.
arabicBreaks = u'[،؛؟]'
# Thanks to Talori in the NVDA irc room:
# U+3000 to U+303F, U+FE10 to U+FE1F, U+FE30 to U+FE6F, U+FF01 to U+FF60
chineseBreaks = u'[　-〿︐-︟︰-﹯！-｠]'
latinBreaks = r'[.,!?;:\n]'
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

	def __init__(self, lang_from, lang_to, text, lang_swap=None, chunksize=350, *args, **kwargs):
		super(Translator, self).__init__(*args, **kwargs)
		self._stop = threading.Event()
		self.text = text
		self.chunksize = chunksize
		self.lang_to = lang_to
		self.lang_from = lang_from
		self.lang_swap = lang_swap
		self.translation = ''
		self.lang_translated = ''
		self.firstChunk = True

	def stop(self):
		self._stop.set()

	def run(self):
		for chunk in splitChunks(self.text, self.chunksize):
			# Make sure we don't send requests to google too often.
			# Try to simulate a human.
			if not self.firstChunk:
				sleep(randint(1, 10))
			req = self.buildRequest(chunk.encode('utf-8'), self.lang_from, self.lang_to)
			try:
				response = urllib2.urlopen(req)
				translation, lang_translated = self.parseData(response)
				if self.firstChunk and self.lang_from == "auto" and  lang_translated == self.lang_to and self.lang_swap is not None:
					self.lang_to = self.lang_swap
					self.firstChunk = False
					req = self.buildRequest(chunk.encode('utf-8'), self.lang_from, self.lang_to)
					response = urllib2.urlopen(req)
					translation, lang_translated = self.parseData(response)
			except Exception as e:
				log.exception("Instant translate: Can not translate text '%s'" %chunk)
				# We have probably been blocked, so stop trying to translate.
				raise e
			self.translation += translation
		# some adjustment, better to do on full text
		self.translation = self.fixNewlines(self.translation)
		self.lang_translated = lang_translated

	def buildRequest(self, text, lang_from, lang_to):
		"""Build POST request which will be sent to Google."""
		urlTemplate = 'http://translate.google.com/translate_a/single?client=t&sl={lang_from}&tl={lang_to}&ie=utf-8&oe=utf-8&dt=t&dt=bd&tk='
		url = urlTemplate.format(lang_from=lang_from, lang_to=lang_to)
		header = {'User-agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'}
		data = 'text=%s' %urllib2.quote(text)
		req = urllib2.Request(url, data, header)
		return req

	def parseData(self, response):
		"""Parse unstructured response."""
		data = response.readlines()[0]
		# get segments with couples ["translation","original text"]
		l1, l2 = data.split(']],', 1)
		translation = l1[3:]
		if l2.startswith('[[\"'):
			# get list of synonyms
			syn = l2[l2.find(',[')+1:l2.find(']')].split(',')
			temp = ', '.join([x.replace('\"', '') for x in syn])
		else:
			# get a list with each couple as item
			sentences = translation.split('],[')
			temp = ''
			# get translation, removing first char (quote symbol)
			for item in sentences:
				item = item.split('\",\"', 1)[0][1:]
				# join all translations
				temp = ' '.join([temp, item])
		translation = temp.decode('string-escape').decode('utf-8')
		translation = self.fixPunctuation(translation)
		# get the language of original text
		tempLang = data.partition(']],,\"')[2]
		lang = tempLang[:tempLang.find('\"')]
		if lang == '':
			lang = _("unavailable")
		return translation, lang

	def fixPunctuation(self, translation):
		"""Clean text from space before punctuation symbol."""
		# list of potentially positions of spaces to remove
		spacePos = []
		for puncMark in splitReg.finditer(translation):
			spacePos.append(puncMark.start()-1)
		if len(spacePos) == 0:
			return translation
		fixedTranslation = ''
		for n in xrange(0,len(translation)):
			temp = translation[n]
			if n in spacePos and temp == ' ':
				continue
			else:
				fixedTranslation += temp
		return fixedTranslation

	def fixNewlines(self, translation):
		"""Adjust newlines and (subsequent or double) spaces."""
		fixes = [('\r\n ', '\r\n'), ('\n ', '\r\n'), ('  ', ' ')]
		for fix in fixes:
			translation = translation.replace(fix[0], fix[1])
		# first char is a space, so...
		return translation[1:]
