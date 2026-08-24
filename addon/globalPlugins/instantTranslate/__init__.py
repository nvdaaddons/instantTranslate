#__init__.py
# Copyright (C) 2012-2026 Aleksey Sadovoy AKA Lex <lex@progger.ru>,
#ruslan <ru2020slan@yandex.ru>,
#Beka Gozalishvili <beqaprogger@gmail.com>
#This addon was been repacked and optimized for executing without standalone Python by Outsider <outsidepro@rambler.ru>.
#other nvda contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

from collections import OrderedDict, namedtuple
from functools import wraps
from html import escape
from .interface import InstantTranslateSettingsPanel
from .langslist import getLanguageName
from .speechOnDemand import getSpeechOnDemandParameter, executeWithSpeakOnDemand
from locale import getlocale
from tones import beep
from .googleTranslator import GoogleTranslator, languageCache
from .languagePairs import MAX_PAIRS, PAIR_KEYS, parsePairs
import addonHandler
import api
import config
import globalPluginHandler
import globalVars
import gui
import json
import languageHandler
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
import speechViewer
try:
	# For NVDA 2021.1 and above
	from speech import speech
except ImportError:
	# For NVDA 2020.4 and below
	import speech


_curAddon = addonHandler.getCodeAddon()
addonName = _curAddon.name.lower()
_addonSummary = _curAddon.manifest['summary']
addonHandler.initTranslation()

def getLocaleLanguage():
	lang = getlocale()[0] or languageHandler.getLanguage() or "en"
	if lang == "zh_HK":
		return "zh-TW"
	elif lang.startswith("zh"):
		return lang.replace('_', '-')
	else:
		return lang.split("_")[0]

confspec = {
"from": "string(default=auto)",
"into": f"string(default={getLocaleLanguage()})",
"swap": "string(default=en)",
"copytranslatedtext": "boolean(default=true)",
"autoswap": "boolean(default=true)",
"isautoswapped": "boolean(default=false)",
"replaceUnderscores": "boolean(default=false)",
"progressbeeps": "boolean(default=true)",
"pairs": "string_list(default=list())",
}


class ConfigOption:
	def __init__(self, key):
		if key not in confspec:
			raise KeyError("%r is not an Instant Translate configuration key" % (key,))
		self.key = key

	def __get__(self, plugin, pluginType=None):
		if plugin is None:
			return self
		return plugin.addonConf[self.key]

	def __set__(self, plugin, value):
		plugin.addonConf[self.key] = value


# Define speakOnDemand parameter for all scripts needing it
speakOnDemand = getSpeechOnDemandParameter()

TRANSLATION_CACHE_SIZE = 100
TranslationResult = namedtuple("TranslationResult", ("translation", "langTo", "detectedLanguage"))

PROGRESS_BEEP_INTERVAL = 1
PROGRESS_BEEP_PITCH = 500
PROGRESS_BEEP_DURATION = 100

TranslationProgress = namedtuple("TranslationProgress", ("done", "total", "remaining", "percent"))

LayerCommand = namedtuple("LayerCommand", ("keys", "label", "scriptName", "description"))

SCRIPT_PREFIX = "script_"


def layerScript(key, description, label=None, **scriptKwargs):
	keys = (key,) if isinstance(key, str) else tuple(key)
	if not keys:
		raise ValueError("A layer command needs at least one key")

	def decorate(script):
		script = scriptHandler.script(description=description, **scriptKwargs)(script)
		script.layerKeys = keys
		script.layerLabel = label or ", ".join(keys)
		return script

	return decorate


def getLayerCommands(pluginType):
	commands = {}
	for pluginClass in reversed(pluginType.__mro__):
		for name, member in vars(pluginClass).items():
			keys = getattr(member, "layerKeys", None)
			if keys is None or not name.startswith(SCRIPT_PREFIX):
				continue
			commands[name] = LayerCommand(
				keys, member.layerLabel, name[len(SCRIPT_PREFIX):], member.__doc__ or ""
			)
	return list(commands.values())


class ProgressBeeper:
	def __init__(self, interval=PROGRESS_BEEP_INTERVAL):
		self.interval = interval
		self._lock = threading.Lock()
		self._stopEvent = None

	def start(self):
		with self._lock:
			if self._stopEvent is not None:
				return
			stopEvent = self._stopEvent = threading.Event()
		def tick():
			while not stopEvent.wait(self.interval):
				beep(PROGRESS_BEEP_PITCH, PROGRESS_BEEP_DURATION)
		threading.Thread(target=tick, daemon=True, name="InstantTranslateProgressBeeper").start()

	def stop(self):
		with self._lock:
			stopEvent, self._stopEvent = self._stopEvent, None
		if stopEvent is not None:
			stopEvent.set()


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

	lang_from = ConfigOption("from")
	lang_to = ConfigOption("into")
	lang_swap = ConfigOption("swap")
	copyTranslation = ConfigOption("copytranslatedtext")
	autoSwap = ConfigOption("autoswap")
	isAutoSwapped = ConfigOption("isautoswapped")
	replaceUnderscores = ConfigOption("replaceUnderscores")
	progressBeeps = ConfigOption("progressbeeps")
	configuredPairs = ConfigOption("pairs")

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		if globalVars.appArgs.secure:
			return
		config.conf.spec[addonName] = confspec
		self.addonConf = config.conf[addonName]
		self.toggling = False
		self.lastTranslation = None
		self._translationCache = OrderedDict()
		self._translationCacheLock = threading.Lock()
		self._activeTranslators = set()
		self._activeTranslatorsLock = threading.Lock()
		self._beeper = ProgressBeeper()
		InstantTranslateSettingsPanel.addonConf = self.addonConf
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(InstantTranslateSettingsPanel)
		self._speak = speech.speak
		speech.speak = self._localSpeak
		self.lastSpokenText = ''
		self.autoTranslate = False
		languageCache.get()

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
		description=_("Instant Translate layer commands. Then press h to list available commands.")
	)
	def script_ITLayer(self, gesture):
		# A run-time binding will occur from which we can perform various layered translation commands.
		# First, check if a second press of the script was done.
		if self.toggling:
			self.script_error(gesture)
			return
		self.bindGestures(self.getLayerGestures())
		self.toggling = True
		tones.beep(100, 10)

	def getLayerGestures(self):
		return {
			"kb:%s" % key: command.scriptName
			for command in getLayerCommands(type(self))
			for key in command.keys
		}

	def getLayerHelp(self):
		items = "".join(
			"<li><strong>%s</strong>: %s</li>" % (escape(command.label), escape(command.description))
			for command in getLayerCommands(type(self))
		)
		return "<ul>%s</ul>" % items

	def terminate(self):
		self.stopTranslations()
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(InstantTranslateSettingsPanel)
		speech.speak = self._speak

	@layerScript(
		"shift+t",
		# Translators: Description of a layer command, presented in input help mode and in the command list.
		description=_("Translates the clipboard text from one language to another using Google Translate."),
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
			self.translate(text, self.lang_from, self.lang_to)

	def getSelectedText(self):
		obj=api.getCaretObject()
		try:
			info=obj.makeTextInfo(textInfos.POSITION_SELECTION)
			if info or not info.isCollapsed:
				return info.text
		except (RuntimeError, NotImplementedError):
			return None

	@layerScript(
		"t",
		# Translators: Description of a layer command, presented in input help mode and in the command list.
		description=_("Translates the selected text from one language to another using Google Translate."),
		**speakOnDemand,
	)
	def script_translateSelection(self, gesture):
		text = self.getSelectedText()
		if not text:
			# Translators: user has pressed the shortcut key for translating selected text, but no text was actually selected.
			ui.message(_("no selection"))
			return
		self.translate(text, self.lang_from, self.lang_to)

	def translate(self, text, langFrom, langTo):
		if self.replaceUnderscores:
			text = text.replace("_", " ")
		if langFrom == "auto" and self.autoSwap:
			langSwap = self.lang_swap
		else:
			langSwap = None
		key = (text, langFrom, langTo, langSwap)
		cached = self.cacheLookup(key)
		if cached is not None:
			self.announceTranslation(cached)
			return
		# Translators: message presented when a translation has been requested and its result is awaited.
		ui.message(_("Translation started, please wait"))
		self.startTranslator(GoogleTranslator(
			langFrom,
			langTo,
			text,
			langSwap,
			onSuccess=lambda translator: self.translationSucceeded(key, translator),
			onError=self.translationFailed,
		))

	def translationSucceeded(self, key, translator):
		result = TranslationResult(translator.translation, translator.langTo, translator.detectedLanguage)
		self.cacheStore(key, result)
		self.announceTranslation(result)

	def translationFailed(self, translator):
		# Translators: message presented when the translation service could not be reached.
		queueHandler.queueFunction(queueHandler.eventQueue, ui.message, _("Translation failed"))

	def announceTranslation(self, result):
		self.lastTranslation = result.translation
		msgTranslation = {'text': result.translation, 'lang': result.langTo}
		queueHandler.queueFunction(queueHandler.eventQueue, lambda: executeWithSpeakOnDemand(messageWithLangDetection, msgTranslation))
		self.copyResult(result.translation)

	def translateAndCache(self, text, langFrom, langTo, langSwap=None):
		if langFrom != "auto" and langSwap is not None:
			raise RuntimeError("Unexpected arguments: langFrom={}, langTo={}, langSwap={}, text={}".format(langFrom, langTo, langSwap, text))
		# useful for yandex, that doesn't support auto option
#		if langFrom == "auto":
#			langFrom = detect_language(text)
		key = (text, langFrom, langTo, langSwap)
		cached = self.cacheLookup(key)
		if cached is not None:
			return cached
		myTranslator = self.startTranslator(GoogleTranslator(langFrom, langTo, text, langSwap))
		myTranslator.join()
		if myTranslator.shouldStop:
			raise RuntimeError('Translation stopped')
		if myTranslator.error:
			if not self.autoTranslate:
				queueHandler.queueFunction(queueHandler.eventQueue, ui.message, _("Translation failed"))
			raise RuntimeError('Translation failure')
		result = TranslationResult(myTranslator.translation, myTranslator.langTo, myTranslator.detectedLanguage)
		self.cacheStore(key, result)
		return result

	def startTranslator(self, translator):
		translator.onFinished = self._translatorFinished
		with self._activeTranslatorsLock:
			self._activeTranslators.add(translator)
			isFirst = len(self._activeTranslators) == 1
		if isFirst and self.progressBeeps:
			self._beeper.start()
		translator.start()
		return translator

	def _translatorFinished(self, translator):
		with self._activeTranslatorsLock:
			self._activeTranslators.discard(translator)
			wasLast = not self._activeTranslators
		if wasLast:
			self._beeper.stop()

	def translationStatus(self):
		with self._activeTranslatorsLock:
			translators = list(self._activeTranslators)
		if not translators:
			return None
		done = sum(translator.completedChunks for translator in translators)
		total = sum(translator.totalChunks for translator in translators)
		percent = 100 if not total else int(round(done * 100.0 / total))
		return TranslationProgress(done, total, total - done, percent)

	def stopTranslations(self):
		with self._activeTranslatorsLock:
			translators = list(self._activeTranslators)
		for translator in translators:
			translator.stop()
		return len(translators)

	def cacheLookup(self, key):
		with self._translationCacheLock:
			result = self._translationCache.get(key)
			if result is not None:
				self._translationCache.move_to_end(key)
			return result

	def cacheStore(self, key, result):
		with self._translationCacheLock:
			self._translationCache[key] = result
			while len(self._translationCache) > TRANSLATION_CACHE_SIZE:
				self._translationCache.popitem(last=False)

	def clearTranslationCache(self):
		with self._translationCacheLock:
			count = len(self._translationCache)
			self._translationCache.clear()
			return count

	def copyResult(self, translation, ignoreSetting=False):
		if ignoreSetting:
			api.copyToClip(translation)
		elif self.copyTranslation:
			api.copyToClip(translation)

	def swapLanguages(self, langFrom, langTo):
		self.lang_from, self.lang_to = langTo, langFrom

	@layerScript(
		"s",
		# Translators: Description of a layer command, presented in input help mode and in the command list.
		description=_("Swaps the source and target languages."),
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
		self.announceLanguages()
		try:
			# NVDA 2024.1+
			shouldTranslate = speech.getState().speechMode != speech.SpeechMode.onDemand
		except AttributeError:
			# NVDA <= 2023.3
			shouldTranslate = True
		if shouldTranslate:
			self.script_translateSelection(gesture)

	def announceLanguages(self):
		ui.message(
			# Translators: message presented to announce the current source and target languages.
			_("Translate: from {lang1} to {lang2}").format(
				lang1=getLanguageName(self.lang_from, short=True),
				lang2=getLanguageName(self.lang_to, short=True),
			)
		)

	@property
	def languagePairs(self):
		return parsePairs(self.configuredPairs)

	def useLanguagePair(self, slot):
		pairs = self.languagePairs
		if slot >= len(pairs):
			ui.message(
				# Translators: message presented when the user switches to a slot holding no language
				# pair yet. {slot} is the number of that slot, from 1 to 10.
				_("No language pair in slot {slot}").format(slot=slot + 1)
			)
			return
		pair = pairs[slot]
		self.lang_from, self.lang_to = pair.langFrom, pair.langTo
		# The pair sets both languages explicitly, so any pending automatic swap no longer applies.
		self.isAutoSwapped = False
		self.announceLanguages()

	@layerScript(
		"a",
		# Translators: Description of a layer command, presented in input help mode and in the command list.
		description=_("Announces the current source and target languages."),
		**speakOnDemand,
	)
	def script_announceLanguages(self, gesture):
		self.announceLanguages()

	@layerScript(
		"c",
		# Translators: Description of a layer command, presented in input help mode and in the command list.
		description=_("Copies the last translation to the clipboard."),
	)
	def script_copyLastResult(self, gesture):
		if self.lastTranslation:
			self.copyResult(self.lastTranslation, ignoreSetting=True)
			# Translators: message presented to announce a successful copy
			ui.message(_("Last translation copied in clipboard"))
		else:
			# Translators: message presented to announce no previous translation disponibility
			ui.message(_("No stored translation"))

	@layerScript(
		"i",
		# Translators: Description of a layer command, presented in input help mode and in the command list.
		description=_("Identifies the language of the selected text."),
		**speakOnDemand,
	)
	def script_identifyLanguage(self, gesture):
		text = self.getSelectedText()
		if not text:
			# Translators: user has pressed the shortcut key for translating selected text, but no text was actually selected.
			ui.message(_("no selection"))
			return
		ui.message(_("Language is..."))
		self.startTranslator(GoogleTranslator(
			"auto",
			self.lang_to,
			text,
			onSuccess=self.languageIdentified,
			onError=self.translationFailed,
		))

	def languageIdentified(self, translator):
		language = translator.detectedLanguage
		if not language:
			self.translationFailed(translator)
			return
		queueHandler.queueFunction(
			queueHandler.eventQueue, executeWithSpeakOnDemand, ui.message, getLanguageName(language)
		)

	def _localSpeak(self, sequence, *args, **kwargs):
		text_items = [x for x in sequence if isinstance(x, str)]
		self.lastSpokenText = speechViewer.SPEECH_ITEM_SEPARATOR.join(text_items)
		if self.autoTranslate and text_items:
			text_to_translate = self.lastSpokenText
			if self.replaceUnderscores:
				text_to_translate = text_to_translate.replace("_", " ")
			# Perform translation synchronously
			try:
				result = self.translateAndCache(text_to_translate, self.lang_from, self.lang_to)
				translated_text = result.translation
				# Create a new sequence with the translated text
				new_sequence = []
				if config.conf['speech']['autoLanguageSwitching']:
					new_sequence.append(LangChangeCommand(result.langTo))
				new_sequence.append(translated_text)
				self._speak(new_sequence, *args, **kwargs)
				# Optionally, copy the result
				self.copyResult(translated_text)
			except RuntimeError:
				# If translation fails, speak the original sequence
				self._speak(sequence, *args, **kwargs)
		else:
			self._speak(sequence, *args, **kwargs)

	@layerScript(
		"l",
		# Translators: Description of a layer command, presented in input help mode and in the command list.
		description=_("Translates the last spoken text."),
		**speakOnDemand,
	)
	def script_translateLastSpokenText(self, gesture):
		if self.lastSpokenText:
			self.translate(self.lastSpokenText, self.lang_from, self.lang_to)

	@layerScript(
		"p",
		# Translators: Description of a layer command, presented in input help mode and in the command list.
		description=_("Announces how far the translation in progress has got."),
		**speakOnDemand,
	)
	def script_translationStatus(self, gesture):
		progress = self.translationStatus()
		if progress is None:
			# Translators: message presented when the user asks about a translation, but none is running.
			ui.message(_("No translation in progress"))
			return
		ui.message(
			# Translators: message presented to announce how far the translation in progress has got.
			# {done} parts are translated out of {total}, {remaining} are left and {percent} is a percentage.
			_("Translating: {done} of {total} parts done, {remaining} remaining, {percent}%").format(
				done=progress.done,
				total=progress.total,
				remaining=progress.remaining,
				percent=progress.percent,
			)
		)

	@layerScript(
		"x",
		# Translators: Description of a layer command, presented in input help mode and in the command list.
		description=_("Stops the translations in progress."),
		**speakOnDemand,
	)
	def script_stopTranslation(self, gesture):
		if self.stopTranslations():
			# Translators: message presented to announce that the translations in progress were cancelled.
			ui.message(_("Translation stopped"))
		else:
			# Translators: message presented when the user asks to stop translating, but nothing is running.
			ui.message(_("No translation in progress"))

	@layerScript(
		"r",
		# Translators: Description of a layer command, presented in input help mode and in the command list.
		description=_("Clears the cache of recent translations."),
		**speakOnDemand,
	)
	def script_clearTranslationCache(self, gesture):
		self.clearTranslationCache()
		# Translators: message presented to announce that the cache of recent translations has been emptied.
		ui.message(_("Translation cache cleared"))

	@layerScript(
		"h",
		# Translators: Description of a layer command, presented in input help mode and in the command list.
		description=_("Announces all available layer commands."),
		**speakOnDemand,
	)
	def script_displayHelp(self, gesture):
		ui.browseableMessage(
			self.getLayerHelp(),
			# Translators: title of the window listing the commands of the add-on.
			_("Instant Translate commands"),
			isHtml=True,
		)

	@layerScript(
		"o",
		# Translators: Description of a layer command, presented in input help mode and in the command list.
		description=_("Opens the Instant Translate settings dialog."),
	)
	def script_showSettings(self, gesture):
		try:
			# NVDA version >= 2023.2
			popupSettingsDialog = gui.mainFrame.popupSettingsDialog
		except:
			# NVDA version < 2023.2
			popupSettingsDialog = gui.mainFrame._popupSettingsDialog
		wx.CallAfter(popupSettingsDialog, gui.settingsDialogs.NVDASettingsDialog, InstantTranslateSettingsPanel)

	@layerScript(
		"v",
		# Translators: Description of a layer command, presented in input help mode and in the command list.
		description=_("Toggles automatic translation of speech output."),
	)
	def script_toggleAutoTranslate(self, gesture):
		self.autoTranslate = not self.autoTranslate
		if self.autoTranslate:
			# Translators: message presented to announce that automatic translation is enabled.
			ui.message(_("Automatic translation enabled"))
		else:
			# Translators: message presented to announce that automatic translation is disabled.
			ui.message(_("Automatic translation disabled"))

	__gestures = {
		"kb:NVDA+shift+t": "ITLayer",
	}


def makeLanguagePairScript(slot):
	def script(self, gesture):
		self.useLanguagePair(slot)

	script.__name__ = "%suseLanguagePair%d" % (SCRIPT_PREFIX, slot + 1)
	return layerScript(
		PAIR_KEYS[slot],
		# Translators: Description of a layer command, presented in input help mode and in the command
		# list. {number} is the number of the language pair, from 1 to 10.
		description=_("Switches to the language pair {number} configured in the settings.").format(
			number=slot + 1
		),
		**speakOnDemand,
	)(script)


for _slot in range(MAX_PAIRS):
	_pairScript = makeLanguagePairScript(_slot)
	setattr(GlobalPlugin, _pairScript.__name__, _pairScript)
del _slot, _pairScript
