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
from speech import speak
try:
	from speech.commands import LangChangeCommand
except:
	from speech import LangChangeCommand
import braille
import wx
import speech
import speechViewer
from versionInfo import version_year

_curAddon = addonHandler.getCodeAddon()
addonName = _curAddon.name.lower()
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

speechModule = speech.speech if version_year>=2021 else speech

confspec = {
"from": "string(default=auto)",
"into": f"string(default={lo_lang})",
"swap": "string(default=en)",
"copytranslatedtext": "boolean(default=true)",
"autoswap": "boolean(default=true)",
"isautoswapped": "boolean(default=false)",
"replaceUnderscores": "boolean(default=false)",
}

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
	scriptCategory = _addonSummary

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		if globalVars.appArgs.secure:
			return
		config.conf.spec[addonName] = confspec
		self.addonConf = config.conf[addonName]
		self.toggling = False
		self.maxCachedResults = 5
		self.cachedResults = []
		InstantTranslateSettingsPanel.addonConf = self.addonConf
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(InstantTranslateSettingsPanel)
		self._speak = speechModule.speak
		speechModule.speak = self._localSpeak
		self.lastSpokenText = ''

	@property
	def lang_from(self):
		return self.addonConf['from']

	@lang_from.setter
	def lang_from(self, lang):
		self.addonConf['from'] = lang

	@property
	def lang_to(self):
		return self.addonConf['into']

	@lang_to.setter
	def lang_to(self, lang):
		self.addonConf['into'] = lang

	@property
	def lang_swap(self):
		return self.addonConf['swap']

	@lang_swap.setter
	def lang_swap(self, lang):
		self.addonConf['swap'] = lang

	@property
	def copyTranslation(self):
		return self.addonConf['copytranslatedtext']

	@copyTranslation.setter
	def copyTranslation(self, enable):
		self.addonConf['copytranslatedtext'] = enable

	@property
	def autoSwap(self):
		return self.addonConf['autoswap']

	@autoSwap.setter
	def autoSwap(self, enable):
		self.addonConf['autoswap'] = enable

	@property
	def isAutoSwapped(self):
		return self.addonConf['isautoswapped']

	@isAutoSwapped.setter
	def isAutoSwapped(self, enable):
		self.addonConf['isautoswapped'] = enable

	@property
	def replaceUnderscores(self):
		return self.addonConf['replaceUnderscores']

	@replaceUnderscores.setter
	def replaceUnderscores(self, enable):
		self.addonConf['replaceUnderscores'] = enable

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
	script_ITLayer.__doc__=_("Instant Translate layer commands. t translates selected text, shift+t translates clipboard text, a announces current swap configuration, s swaps source and target languages, c copies last result to clipboard, i identify the language of selected text, l translates last spoken text, o opens translation setting dialog.")

	def terminate(self):
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(InstantTranslateSettingsPanel)

	def script_translateClipboardText(self, gesture):
		try:
			text = api.getClipData()
		except:
			text = None
		if not text or not isinstance(text, str) or text.isspace():
			# Translators: message presented when user presses the shortcut key for translating clipboard text but the clipboard is empty.
			ui.message(_("There is no text on the clipboard"))
		else:
			threading.Thread(target=self.translate, args=(text,)).start()
	# Translators: message presented in input help mode, when user presses the shortcut keys for this addon.
	script_translateClipboardText.__doc__=_("Translates clipboard text from one language to another using Google Translate.")

	def getSelectedText(self):
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
			return
		else:
			return info.text

	def script_translateSelection(self, gesture):
		text = self.getSelectedText()
		threading.Thread(target=self.translate, args=(text,)).start()
	# Translators: message presented in input help mode, when user presses the shortcut keys for this addon.
	script_translateSelection.__doc__=_("Translates selected text from one language to another using Google Translate.")

	def translate(self, text):
		if self.replaceUnderscores:
			text = text.replace("_", " ")
		# useful for yandex, that doesn't support auto option
#		if self.lang_from == "auto":
#			self.lang_from = detect_language(text)
		translation = None
		if (text, self.lang_to, self.lang_from) in [(x[0],x[1],x[2]) for x in self.cachedResults]:
			translation,lang = [f for f in self.cachedResults if f[0] == text and f[1] == self.lang_to and f[2] == self.lang_from][0][3:5]
			index = [(te,lt,lf,tr) for te, lt, lf, tr, lg in self.cachedResults].index((text, self.lang_to, self.lang_from, translation))
			self.addResultToCache(text, translation, lang, removeIndex=index)
		else:
			myTranslator = None
			if not self.autoSwap:
				myTranslator = Translator(self.lang_from, self.lang_to, text)
			else:
				myTranslator = Translator(self.lang_from, self.lang_to, text, self.lang_swap)
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
		self.cachedResults.append((text, self.lang_to, self.lang_from, translation, lang))

	def copyResult(self, translation, ignoreSetting=False):
		if ignoreSetting:
			api.copyToClip(translation)
		elif self.copyTranslation:
			api.copyToClip(translation)

	def swapLanguages(self, langFrom, langTo):
		self.lang_from, self.lang_to = langTo, langFrom

	def script_swapLanguages(self, gesture):
		if self.lang_from == "auto":
			self.swapLanguages(self.lang_swap, self.lang_to)
			self.isAutoSwapped = True
		elif self.isAutoSwapped and self.lang_to == self.lang_swap:
			self.swapLanguages(self.lang_from, "auto")
			self.isAutoSwapped = False
		else:
			self.swapLanguages(self.lang_from, self.lang_to)
		# Translators: message presented to announce that the source and target languages have been swapped.
		ui.message(_("Languages swapped"))
		# Translators: message presented to announce the current source and target languages.
		ui.message(_("Translate: from {lang1} to {lang2}").format(lang1=self.lang_from, lang2=self.lang_to))
		self.script_translateSelection(gesture)
	# Translators: Presented in input help mode.
	script_swapLanguages.__doc__ = _("It swaps source and target languages.")

	def script_announceLanguages(self, gesture):
		# Translators: message presented to announce the current source and target languages.
		ui.message(_("Translate: from {lang1} to {lang2}").format(lang1=self.lang_from, lang2=self.lang_to))
	# Translators: Presented in input help mode.
	script_announceLanguages.__doc__ = _("It announces the current source and target languages.")

	def script_copyLastResult(self, gesture):
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
		text = self.getSelectedText()
		myTranslator = Translator("auto", self.lang_to, text)
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
	# Translators: Presented in input help mode.
	script_translateLastSpokenText.__doc__ = _("It translates the last spoken text")

	def script_displayHelp(self, gesture):
		ui.message(_("t translates selected text, shift+t translates clipboard text, a announces current swap configuration, s swaps source and target languages, c copies last result to clipboard, i identify the language of selected text, l translates last spoken text, o open translation settings dialog, h displays this message."))
	# Translators: Presented in input help mode.
	script_displayHelp.__doc__ = _("Announces all available layered commands")

	def script_showSettings(self, gesture):
		wx.CallAfter(gui.mainFrame._popupSettingsDialog, gui.settingsDialogs.NVDASettingsDialog, InstantTranslateSettingsPanel)
	# Translators: Presented in input help mode.
	script_showSettings.__doc__ = _("Opens Instant Translate settings dialog.")

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
