#__init__.py
# Copyright (C) 2012-2013 Aleksey Sadovoy AKA Lex <lex@progger.ru>,
#ruslan <ru2020slan@yandex.ru>,
#beqa <beqaprogger@gmail.com>
#This addon was been repacked and optimized for executing without standalone Python by Outsider <outsidepro@rambler.ru>.
#other nvda contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import gui
import wx
import api
import textInfos
import tones
import scriptHandler
import globalPluginHandler
from logHandler import log
from functools import wraps
import queueHandler
import ui
import config
from locale import getdefaultlocale
import globalVars
from interface import *
from translator import Translator
from tones import beep
from time import sleep
import threading
import _config
import addonHandler

_config.load()
_addonDir = os.path.join(os.path.dirname(__file__), "..", "..").decode("mbcs")
_curAddon = addonHandler.Addon(_addonDir)
_addonSummary = _curAddon.manifest['summary']
addonHandler.initTranslation()

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

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = unicode(_addonSummary)

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		if globalVars.appArgs.secure:
			return
		self.createMenu()
		self.getUpdatedGlobalVars()
		self.toggling = False

	def getUpdatedGlobalVars(self):
		global lang_from, lang_to, lang_swap, copyTranslation, autoSwap, isAutoSwapped
		# source language
		lang_from = _config.instanttranslateConfig['translation']['from']
		# target language
		lang_to = _config.instanttranslateConfig['translation']['into']
		# language used to swap source and target when source is auto
		lang_swap = _config.instanttranslateConfig['translation']['swap']
		# determine whether to copy translation on clipboard
		copyTranslation = _config.instanttranslateConfig['settings']['copytranslatedtext']
		# determine whether to swap automatically lang_swap and target language, if source recognized equal to the target
		autoSwap = _config.instanttranslateConfig['settings']['autoswap']
		# keep track if there was a swapping from source=auto during previous NVDA session
		isAutoSwapped = _config.instanttranslateConfig['temporary']['isautoswapped']

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
	script_ITLayer.__doc__=_("Instant Translate layer commands. Press C to translate clipboard text, t to translate selction or s to swap languages.")

	def createMenu(self):
		self.prefsMenu = gui.mainFrame.sysTrayIcon.menu.GetMenuItems()[0].GetSubMenu()
		self.instantTranslateSettingsItem = self.prefsMenu.Append(wx.ID_ANY,
			# Translators: name of the option in the menu.
			_("Instant &Translate Settings..."),
			# Translators: tooltip text for the menu item.
			_("Select languages to be used for translation."))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU , lambda e : gui.mainFrame._popupSettingsDialog(InstantTranslateSettingsDialog), self.instantTranslateSettingsItem)

	def terminate(self):
		try:
			self.prefsMenu.RemoveItem(self.instantTranslateSettingsItem)
		except wx.PyDeadObjectError:
			pass

	def script_translateClipboardText(self, gesture):
		try:
			text = api.getClipData()
		except:
			text = None
		if not text or not isinstance(text,basestring) or text.isspace():
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
		myTranslator = None
		if not autoSwap:
			myTranslator = Translator(lang_from, lang_to, text)
		else:
			myTranslator = Translator(lang_from, lang_to, text, lang_swap)
		ui.message(_("Translating..."))
		myTranslator.start()
		i=0
		while  myTranslator.isAlive():
			sleep(0.1)
			i+=1
			if i == 10:
				beep(500, 100)
				i = 0
		myTranslator.join()
		queueHandler.queueFunction(queueHandler.eventQueue, ui.message, myTranslator.translation)
		if copyTranslation:
			api.copyToClip(myTranslator.translation)

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
		_config.instanttranslateConfig['translation']['from'] = lang_from
		_config.instanttranslateConfig['translation']['into'] = lang_to
		_config.instanttranslateConfig['temporary']['isautoswapped'] = isAutoSwapped
		_config.save()
		# Translators: message presented to announce that the source and target languages have been swapped.
		ui.message(_("Languages swapped"))
		# Translators: message presented to announce the current source and target languages.
		ui.message(_("Translate: from {lang1} to {lang2}").format(lang1=lang_from, lang2=lang_to))
	# Translators: Presented in input help mode.
	script_swapLanguages.__doc__ = _("It swaps source and target languages.")

	def script_announceLanguages(self, gesture):
		self.getUpdatedGlobalVars()
		# Translators: message presented to announce the current source and target languages.
		ui.message(_("Translate: from {lang1} to {lang2}").format(lang1=lang_from, lang2=lang_to))
	# Translators: Presented in input help mode.
	script_announceLanguages.__doc__ = _("It announces the current source and target languages.")

	__ITGestures={
		"kb:t":"translateSelection",
		"kb:shift+t":"translateClipboardText",
		"kb:s":"swapLanguages",
		"kb:a":"announceLanguages"
	}

	__gestures = {
		"kb:NVDA+shift+t": "ITLayer",
	}
