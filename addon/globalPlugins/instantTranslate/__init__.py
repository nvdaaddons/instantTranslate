#__init__.py
# Copyright (C) 2012-2016 Aleksey Sadovoy AKA Lex <lex@progger.ru>,
#ruslan <ru2020slan@yandex.ru>,
#beqa <beqaprogger@gmail.com>
#This addon was been repacked and optimized for executing without standalone Python by Outsider <outsidepro@rambler.ru>.
#other nvda contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

from functools import wraps, lru_cache
from .interface import InstantTranslateSettingsPanel
from .langslist import g
from .speechOnDemand import getSpeechOnDemandParameter, executeWithSpeakOnDemand
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

# Define speakOnDemand parameter for all scripts needing it
speakOnDemand = getSpeechOnDemandParameter()

# Below toggle code came from Tyler Spivey's code, with enhancements by Joseph Lee.

def finally_(func, final):
	"""Calls final after func, even if it fails."""
	@wraps(func)
	def new(*args, **kwargs):
		try:
			func(*args, **kwargs)
		finally:
			final()
	return new

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
		self.lastTranslation = None
		InstantTranslateSettingsPanel.addonConf = self.addonConf
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(InstantTranslateSettingsPanel)
		self._speak = speechModule.speak
		speechModule.speak = self._localSpeak
		self.lastSpokenText = ''
		self.settings = {"lang_from": "from", "lang_to": "into", "lang_swap": "swap", "copyTranslation": "copytranslatedtext", "autoSwap": "autoswap", "isAutoSwapped": "isautoswapped", "replaceUnderscores": "replaceUnderscores"}
		[setattr(self.__class__, propertyMethod, property(lambda self, propertyName=propertyName: self.addonConf[propertyName], lambda self, value, propertyName=propertyName: self.addonConf.__setitem__(propertyName, value))) for propertyMethod, propertyName in self.settings.items()]

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

	@scriptHandler.script(
		description=_("Instant Translate layer commands. t translates selected text, shift+t translates clipboard text, a announces current swap configuration, s swaps source and target languages, c copies last result to clipboard, i identify the language of selected text, l translates last spoken text, o opens translation setting dialog.")
	)
	def script_ITLayer(self, gesture):
		# A run-time binding will occur from which we can perform various layered translation commands.
		# First, check if a second press of the script was done.
		if self.toggling:
			self.script_error(gesture)
			return
		self.bindGestures(self.__ITGestures)
		self.toggling = True
		tones.beep(100, 10)

	def terminate(self):
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(InstantTranslateSettingsPanel)

	@scriptHandler.script(
		# Translators: message presented in input help mode, when user presses the shortcut keys for this addon.
		description=_("Translates clipboard text from one language to another using Google Translate."),
		**speakOnDemand,
	)
	def script_translateClipboardText(self, gesture):
		try:
			text = api.getClipData()
		except:
			text = None
		if not text or not isinstance(text, str) or text.isspace():
			# Translators: message presented when user presses the shortcut key for translating clipboard text but the clipboard is empty.
			ui.message(_("There is no text on the clipboard"))
		else:
			threading.Thread(target=self.translate, args=(text,self.lang_from, self.lang_to,)).start()

	def getSelectedText(self):
		obj=api.getCaretObject()
		try:
			info=obj.makeTextInfo(textInfos.POSITION_SELECTION)
			if info or not info.isCollapsed:
				return info.text
		except (RuntimeError, NotImplementedError):
			return None

	@scriptHandler.script(
		# Translators: message presented in input help mode, when user presses the shortcut keys for this addon.
		description=_("Translates selected text from one language to another using Google Translate."),
		**speakOnDemand,
	)
	def script_translateSelection(self, gesture):
		text = self.getSelectedText()
		if not text:
			# Translators: user has pressed the shortcut key for translating selected text, but no text was actually selected.
			ui.message(_("no selection"))
			return
		threading.Thread(target=self.translate, args=(text,self.lang_from,self.lang_to,)).start()

	def translate(self, text, langFrom, langTo):
		if self.replaceUnderscores:
			text = text.replace("_", " ")
		if langFrom == "auto" and self.autoSwap:
			langSwap = self.lang_swap
		else:
			langSwap = None
		try:
			result = self.translateAndCache(text, langFrom, langTo, langSwap)
		except RuntimeError:
			return
		self.lastTranslation = result.translation
		msgTranslation = {'text': result.translation, 'lang': result.lang_to}
		queueHandler.queueFunction(queueHandler.eventQueue, lambda: executeWithSpeakOnDemand(messageWithLangDetection, msgTranslation))
		self.copyResult(result.translation)

	@lru_cache()
	def translateAndCache(self, text, langFrom, langTo, langSwap=None):
		"""Translates a text and caches the result:
		@param text: text to translate
		@param langFrom: language of the text to be translated.
			"auto" triggers auto-detection of the language of this text.
		@param langTo: language to which the text should be translated.
		@param langSwap: if langFrom is set to "auto" and the text is detected to be from langTo language,
			translates the text to langSwap instead.
		"""
		if langFrom != "auto" and langSwap is not None:
			raise RuntimeError("Unexpected arguments: langFrom={}, langTo={}, langSwap={}, {}".format(text, langFrom, langTo, langSwap))
		# useful for yandex, that doesn't support auto option
#		if langFrom == "auto":
#			langFrom = detect_language(text)
		translation = None
		myTranslator = Translator(langFrom, langTo, text, langSwap)
		myTranslator.start()
		i=0
		while myTranslator.is_alive():
			sleep(0.1)
			i+=1
			if i == 10:
				beep(500, 100)
				i = 0
		myTranslator.join()
		if myTranslator.error:
			queueHandler.queueFunction(queueHandler.eventQueue, ui.message, _("Translation failed"))
			raise RuntimeError('Translation failure')
		return myTranslator

	def copyResult(self, translation, ignoreSetting=False):
		if ignoreSetting:
			api.copyToClip(translation)
		elif self.copyTranslation:
			api.copyToClip(translation)

	def swapLanguages(self, langFrom, langTo):
		self.lang_from, self.lang_to = langTo, langFrom

	@scriptHandler.script(
		# Translators: Presented in input help mode.
		description=_("It swaps source and target languages."),
	)
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
		try:
			# NVDA 2024.1+
			shouldTranslate = speech.getState().speechMode != speech.SpeechMode.onDemand
		except AttributeError:
			# NVDA <= 2023.3
			shouldTranslate = True
		if shouldTranslate:
			self.script_translateSelection(gesture)

	@scriptHandler.script(
		# Translators: Presented in input help mode.
		description=_("It announces the current source and target languages."),
		**speakOnDemand,
	)
	def script_announceLanguages(self, gesture):
		# Translators: message presented to announce the current source and target languages.
		ui.message(_("Translate: from {lang1} to {lang2}").format(lang1=self.lang_from, lang2=self.lang_to))

	@scriptHandler.script(
	)
	def script_copyLastResult(self, gesture):
		if self.lastTranslation:
			self.copyResult(self.lastTranslation, ignoreSetting=True)
			# Translators: message presented to announce a successful copy
			ui.message(_("Last translation copied in clipboard"))
		else:
			# Translators: message presented to announce no previous translation disponibility
			ui.message(_("No stored translation"))
	# Translators: Presented in input help mode.
	description=_("It copies the last translation to clipboard"),

	@scriptHandler.script(
		# Translators: Presented in input help mode.
		description=_("It identifies the language of selected text"),
		**speakOnDemand,
	)
	def script_identifyLanguage(self, gesture):
		text = self.getSelectedText()
		if not text:
			# Translators: user has pressed the shortcut key for translating selected text, but no text was actually selected.
			ui.message(_("no selection"))
			return
		myTranslator = Translator("auto", self.lang_to, text)
		ui.message(_("Language is..."))
		myTranslator.start()
		i=0
		while  myTranslator.is_alive():
			sleep(0.1)
			i+=1
			if i == 10:
				beep(500, 100)
				i = 0
		myTranslator.join()
		language = myTranslator.lang_detected
		queueHandler.queueFunction(queueHandler.eventQueue, ui.message, g(language))

	def _localSpeak(self, sequence, *args, **kwargs):
		self._speak(sequence, *args, **kwargs)
		self.lastSpokenText = speechViewer.SPEECH_ITEM_SEPARATOR.join([x for x in sequence if isinstance(x, str)])

	@scriptHandler.script(
		# Translators: Presented in input help mode.
		description=_("It translates the last spoken text"),
		**speakOnDemand,
	)
	def script_translateLastSpokenText(self, gesture):
		self.lastSpokenText and threading.Thread(target=self.translate, args=(self.lastSpokenText, self.lang_from, self.lang_to)).start()

	@scriptHandler.script(
		# Translators: Presented in input help mode.
		description=_("Announces all available layered commands"),
		**speakOnDemand,
	)
	def script_displayHelp(self, gesture):
		ui.message(_("t translates selected text, shift+t translates clipboard text, a announces current swap configuration, s swaps source and target languages, c copies last result to clipboard, i identify the language of selected text, l translates last spoken text, o open translation settings dialog, h displays this message."))

	@scriptHandler.script(
		# Translators: Presented in input help mode.
		description=_("Opens Instant Translate settings dialog."),
	)
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
