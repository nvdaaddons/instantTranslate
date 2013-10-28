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
import globalPluginHandler
from logHandler import log
import queueHandler
import ui
import config
from configobj import *
from locale import getdefaultlocale
import globalVars
from interface import *
from translator import Translator
from tones import beep
from time import sleep
import addonHandler
addonHandler.initTranslation()

config_file = os.path.join(globalVars.appArgs.configPath,"instantTranslate.ini")
lo_lang = getdefaultlocale () # get a language of the OS localization.
s = lo_lang[0] # get the first element of the tuplet.
lo_lang = s[0:s.find("_")] # get the default language which is translated into.

if not os.path.isfile(config_file):
	config = ConfigObj()
	config.filename = config_file
	config ["translation"] = {"from": "auto", "into": lo_lang}
	config ["settings"] = {"CopyTranslatedText": "true"}
	config.write()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		if globalVars.appArgs.secure:
			return
		self.createMenu()

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

	def script_translateClipboardText(self,gesture):
		try:
			text = api.getClipData()
		except:
			text = None
		if not text or not isinstance(text,basestring) or text.isspace():
			# Translators: message presented when user presses the shortcut key for translating clipboard text but the clipboard is empty.
			ui.message(_("There is no text on the clipboard"))
		else:
			self.translate(text)
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
			self.translate(info.text)
	# Translators: message presented in input help mode, when user presses the shortcut keys for this addon.
	script_translateSelection.__doc__=_("Translates selected text from one language to another using Google Translate.")

	def translate(self, text):
		config = ConfigObj(config_file)
		lang_from = config["translation"]["from"]
		lang_to = config["translation"]["into"]
		copyTranslation = config["settings"]["CopyTranslatedText"]
		myTranslator = Translator(lang_from, lang_to, text)
		myTranslator.start()
		while  myTranslator.isAlive():
			sleep(0.5)
			beep(500, 100)
		myTranslator.join()
		queueHandler.queueFunction(queueHandler.eventQueue, ui.message, myTranslator.translation)
		if copyTranslation == "true":
			api.copyToClip(myTranslator.translation)

	__gestures = {
		"kb:NVDA+shift+t": "translateSelection",
"kb:NVDA+shift+y": "translateClipboardText",
	}
