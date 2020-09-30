#__init__.py
# Copyright (C) 2012-2016 Aleksey Sadovoy AKA Lex <lex@progger.ru>,
#ruslan <ru2020slan@yandex.ru>,
#beqa <beqaprogger@gmail.com>
#This addon was been repacked and optimized for executing without standalone Python by Outsider <outsidepro@rambler.ru>.
#other nvda contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

from functools import wraps
from .interface import InstantTranslateSettingsPanel
from .langslist import g
from locale import getdefaultlocale
from time import sleep
from tones import beep
from .translator import Translator
import addonHandler
import api
import config
import globalPluginHandler
import globalVars
import gui
import json
import os
import queueHandler
import scriptHandler
import textInfos
import threading
import tones
import ui
from speech import LangChangeCommand, speak
import braille
import wx
import six
import speech
import speechViewer

_addonDir = os.path.join(os.path.dirname(__file__), "..", "..")
if isinstance(_addonDir, bytes):
	_addonDir = _addonDir.decode("mbcs")
_curAddon = addonHandler.Addon(_addonDir)
_addonSummary = _curAddon.manifest['summary']
addonHandler.initTranslation()

lo_lang = getdefaultlocale()
s = lo_lang[0]
if s == "zh_HK":
	lo_lang = "zh-TW"
elif s.startswith("zh"):
	lo_lang = s.replace('_', '-')
else:
	lo_lang = s[0:s.find("_")]

confspec = {
"from": "string(default=auto)",
"into": "string(default={lo_lang})",
"swap": "string(default=en)",
"copytranslatedtext": "boolean(default=true)",
"autoswap": "boolean(default=true)",
"isautoswapped": "boolean(default=false)",
}
config.conf.spec["instanttranslate"] = confspec

# Below toggle code came from Tyler Spivey's code, with enhancements by Joseph Lee.

def finally_(func, final):
	"""Calls final after func, even if it fails."""
	def wrap(f):
		@wraps(f)
		def new(*args, **kwargs):
			try:
				func(*args, **kwargs)
			finally:
				final()
		return new
	return wrap(final)

#def detect_language(text):
#	response=urllib.urlopen("https://translate.yandex.net/api/v1.5/tr.json/detect?key=trnsl.1.1.20150410T053856Z.1c57628dc3007498.d36b0117d8315e9cab26f8e0302f6055af8132d7&"+urllib.urlencode({"text":text.encode('utf-8')})).read()
#	response=json.loads(response)
#	return response['lang']

def messageWithLangDetection(msg):
	autoLanguageSwitching=config.conf['speech']['autoLanguageSwitching']
	if autoLanguageSwitching:
		speechSequence=[]
		speechSequence.append(LangChangeCommand(msg['lang']))
		speechSequence.append(msg['text'])
		speak(speechSequence)
		braille.handler.message(msg['text'])
	else:
		ui.message(msg['text'])


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = six.text_type(_addonSummary)

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		if globalVars.appArgs.secure:
			return
		self.getUpdatedGlobalVars()
		self.toggling = False
		self.maxCachedResults = 5
		self.cachedResults = []
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(InstantTranslateSettingsPanel)
		self._speak = speech.speak
		speech.speak = self._localSpeak
		self.lastSpokenText = ''

	def getUpdatedGlobalVars(self):
		global lang_from, lang_to, lang_swap, copyTranslation, autoSwap, isAutoSwapped
		# source language
		lang_from = config.conf['instanttranslate']['from']
		# target language
		lang_to = config.conf['instanttranslate']['into']
		# language used to swap source and target when source is auto
		lang_swap = config.conf['instanttranslate']['swap']
		# determine whether to copy translation on clipboard
		copyTranslation = config.conf['instanttranslate']['copytranslatedtext']
		# determine whether to swap automatically lang_swap and target language, if source recognized equal to the target
		autoSwap = config.conf['instanttranslate']['autoswap']
		# keep track if there was a swapping from source=auto during previous NVDA session
		isAutoSwapped = config.conf['instanttranslate']['isautoswapped']

	def getScript(self, gesture):
		if not self.toggling:
			return globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		script = globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		if not script:
			script = finally_(self.script_error, self.finish)
		return finally_(script, self.finish)

	def finish(self):
		self.toggling = False
		self.clearGestureBindings()
		self.bindGestures(self.__gestures)

	def script_error(self, gesture):
		tones.beep(120, 100)

	def script_ITLayer(self, gesture):
		# A run-time binding will occur from which we can perform various layered translation commands.
		# First, check if a second press of the script was done.
		if self.toggling:
			self.script_error(gesture)
			return
		self.bindGestures(self.__ITGestures)
		self.toggling = True
		tones.beep(100, 10)
	script_ITLayer.__doc__=_("Instant Translate layer commands. t translates selected text, shift+t translates clipboard text, a announces current swap configuration, s swaps source and target languages, c copies last result to clipboard, i identify the language of selected text.")

	def terminate(self):
		speech.speak = self._speak
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(InstantTranslateSettingsPanel)

	def script_translateClipboardText(self, gesture):
		try:
			text = api.getClipData()
		except:
			text = None
		if not text or not isinstance(text,six.string_types) or text.isspace():
			# Translators: message presented when user presses the shortcut key for translating clipboard text but the clipboard is empty.
			ui.message(_("There is no text on the clipboard"))
		else:
			threading.Thread(target=self.translate, args=(text,)).start()
	# Translators: message presented in input help mode, when user presses the shortcut keys for this addon.
	script_translateClipboardText.__doc__=_("Translates clipboard text from one language to another using Google Translate.")

	def script_translateSelection(self, gesture):
		obj=api.getFocusObject()
		treeInterceptor=obj.treeInterceptor
		if hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough:
			obj=treeInterceptor
		try:
			info=obj.makeTextInfo(textInfos.POSITION_SELECTION)
		except (RuntimeError, NotImplementedError):
			info=None
		if not info or info.isCollapsed:
			# Translators: user has pressed the shortcut key for translating selected text, but no text was actually selected.
			ui.message(_("no selection"))
		else:
			threading.Thread(target=self.translate, args=(info.text,)).start()
	# Translators: message presented in input help mode, when user presses the shortcut keys for this addon.
	script_translateSelection.__doc__=_("Translates selected text from one language to another using Google Translate.")

	def translate(self, text):
		self.getUpdatedGlobalVars()
		global lang_from
		# useful for yandex, that doesn't support auto option
#		if lang_from == "auto":
#			lang_from = detect_language(text)
		translation = None
		if (text, lang_to, lang_from) in [(x[0],x[1],x[2]) for x in self.cachedResults]:
			translation,lang = [f for f in self.cachedResults if f[0] == text and f[1] == lang_to and f[2] == lang_from][0][3:5]
			index = [(te,lt,lf,tr) for te, lt, lf, tr, lg in self.cachedResults].index((text, lang_to, lang_from, translation))
			self.addResultToCache(text, translation, lang, removeIndex=index)
		else:
			myTranslator = None
			if not autoSwap:
				myTranslator = Translator(lang_from, lang_to, text)
			else:
				myTranslator = Translator(lang_from, lang_to, text, lang_swap)
			myTranslator.start()
			i=0
			while myTranslator.is_alive():
				sleep(0.1)
				i+=1
				if i == 10:
					beep(500, 100)
					i = 0
			myTranslator.join()
			translation = myTranslator.translation
			lang = myTranslator.lang_to
			if translation != '':
				self.addResultToCache(text, translation, lang)
		msgTranslation = {'text': translation, 'lang': lang}
		queueHandler.queueFunction(queueHandler.eventQueue, messageWithLangDetection, msgTranslation)
		self.copyResult(translation)

	def addResultToCache(self, text, translation, lang, removeIndex=0):
		if removeIndex:
			del self.cachedResults[removeIndex]
		elif len(self.cachedResults) == self.maxCachedResults:
			del self.cachedResults[0]
		self.cachedResults.append((text, lang_to, lang_from, translation, lang))

	def copyResult(self, translation, ignoreSetting=False):
		if ignoreSetting:
			api.copyToClip(translation)
		elif copyTranslation:
			api.copyToClip(translation)

	def swapLanguages(self, langFrom, langTo):
		global lang_from, lang_to
		lang_from=langTo
		lang_to=langFrom

	def script_swapLanguages(self, gesture):
		self.getUpdatedGlobalVars()
		global isAutoSwapped
		if lang_from == "auto":
			self.swapLanguages(lang_swap, lang_to)
			isAutoSwapped = True
		elif isAutoSwapped and lang_to == lang_swap:
			self.swapLanguages(lang_from, "auto")
			isAutoSwapped = False
		else:
			self.swapLanguages(lang_from, lang_to)
		config.conf['instanttranslate']['from'] = lang_from
		config.conf['instanttranslate']['into'] = lang_to
		config.conf['instanttranslate']['isautoswapped'] = isAutoSwapped
		# Translators: message presented to announce that the source and target languages have been swapped.
		ui.message(_("Languages swapped"))
		# Translators: message presented to announce the current source and target languages.
		ui.message(_("Translate: from {lang1} to {lang2}").format(lang1=lang_from, lang2=lang_to))
		self.script_translateSelection(gesture)
	# Translators: Presented in input help mode.
	script_swapLanguages.__doc__ = _("It swaps source and target languages.")

	def script_announceLanguages(self, gesture):
		self.getUpdatedGlobalVars()
		# Translators: message presented to announce the current source and target languages.
		ui.message(_("Translate: from {lang1} to {lang2}").format(lang1=lang_from, lang2=lang_to))
	# Translators: Presented in input help mode.
	script_announceLanguages.__doc__ = _("It announces the current source and target languages.")

	def script_copyLastResult(self, gesture):
		self.getUpdatedGlobalVars()
		if len(self.cachedResults) > 0:
			translation = self.cachedResults[len(self.cachedResults)-1][3]
			self.copyResult(translation, ignoreSetting=True)
			# Translators: message presented to announce a successful copy
			ui.message(_("Last translation copied in clipboard"))
		else:
			# Translators: message presented to announce no previous translation disponibility
			ui.message(_("No stored translation"))
	# Translators: Presented in input help mode.
	script_copyLastResult.__doc__ = _("It copies the last translation to clipboard")

	def script_identifyLanguage(self, gesture):
		obj=api.getFocusObject()
		treeInterceptor=obj.treeInterceptor
		if hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough:
			obj=treeInterceptor
		try:
			info=obj.makeTextInfo(textInfos.POSITION_SELECTION)
		except (RuntimeError, NotImplementedError):
			info=None
		if not info or info.isCollapsed:
			# Translators: user has pressed the shortcut key for identifying the language of selected text, but no text was actually selected.
			ui.message(_("no selection"))
		else:
			self.getUpdatedGlobalVars()
			myTranslator = Translator("auto", lang_to, info.text)
			ui.message(_("Language is..."))
			myTranslator.start()
			i=0
			while  myTranslator.isAlive():
				sleep(0.1)
				i+=1
				if i == 10:
					beep(500, 100)
					i = 0
			myTranslator.join()
			language = myTranslator.lang_detected
			queueHandler.queueFunction(queueHandler.eventQueue, ui.message, g(language))
	# Translators: Presented in input help mode.
	script_identifyLanguage.__doc__ = _("It identifies the language of selected text")

	def _localSpeak(self, sequence, *args, **kwargs):
		self._speak(sequence, *args, **kwargs)
		self.lastSpokenText = speechViewer.SPEECH_ITEM_SEPARATOR.join([x for x in sequence if isinstance(x, str)])

	def script_translateLastSpokenText(self, gesture):
		self.lastSpokenText and threading.Thread(target=self.translate, args=(self.lastSpokenText,)).start()
	script_translateLastSpokenText.__doc__ = _("It translates the last spoken text")

	def script_displayHelp(self, gesture):
		ui.message(_("t translates selected text, shift+t translates clipboard text, a announces current swap configuration, s swaps source and target languages, c copies last result to clipboard, i identify the language of selected text, o open translation settings dialog, h displays this message."))

	def script_showSettings(self, gesture):
		wx.CallAfter(gui.mainFrame._popupSettingsDialog, gui.settingsDialogs.NVDASettingsDialog, InstantTranslateSettingsPanel)

	__ITGestures={
		"kb:t":"translateSelection",
		"kb:shift+t":"translateClipboardText",
		"kb:s":"swapLanguages",
		"kb:a":"announceLanguages",
		"kb:c":"copyLastResult",
		"kb:i":"identifyLanguage",
		"kb:l":"translateLastSpokenText",
		"kb:o":"showSettings",
		"kb:h":"displayHelp",
	}

	__gestures = {
		"kb:NVDA+shift+t": "ITLayer",
	}
