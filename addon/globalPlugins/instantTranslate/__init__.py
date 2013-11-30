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
		self.__toggle_gestures = {}
		for c in "tcs":
			self.__toggle_gestures["KB:%s" % c] = "toggleX"

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

	def script_toggleX(self, gesture):
		char = gesture.identifiers[-1][-1]
		if char == 't':
			self.translateSelection()
		elif char == 'c':
			self.translateClipboardText()
		elif char == 's':
			self.announceOrSwapLanguages()

	def script_toggle(self, gesture):
		#If already toggling, send it on and clean up
		if self.toggling:
			gesture.send()
			return
		#alert the user of a gesture map error, rather than making the machine unusable
		try:
			self.bindGestures(self.__toggle_gestures)
		except:
			ui.message("Error binding toggle gestures")
			raise
		self.toggling = True
		tones.beep(100, 10)

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

	def translateClipboardText(self):
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
	translateClipboardText.__doc__=_("Translates clipboard text from one language to another using Google Translate.")

	def translateSelection(self):
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
	translateSelection.__doc__=_("Translates selected text from one language to another using Google Translate.")

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

	def announceOrSwapLanguages(self):
		self.getUpdatedGlobalVars()
		if scriptHandler.getLastScriptRepeatCount() != 0:
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
	announceOrSwapLanguages.__doc__ = _("When pressed once, announces the current source and target languages. Pressed twice will swap source and target.")

	__gestures = {
		"kb:NVDA+shift+t": "toggle",
	}
