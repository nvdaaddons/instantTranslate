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
import sys
import os
impPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(impPath)
import json
import urllib2
del sys.path[-1]
import threading
import api
import textInfos
import globalPluginHandler
from logHandler import log
import queueHandler
import ui
import config
from configobj import *
from locale import getdefaultlocale
import string
import globalVars
from interface import *
import addonHandler
addonHandler.initTranslation()

config_file = os.path.join(globalVars.appArgs.configPath,"instantTranslate.ini")
charslimit=1500
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

	scriptCategory = "InstantTranslate"

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		self.opener = urllib2.build_opener()
		self.opener.addheaders = [('User-agent', 'Mozilla/5.0')]
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
		global lang_from, lang_to, copyTranslation
		try:
			text = api.getClipData()
		except:
			text = None
		if not text or not isinstance(text,basestring) or text.isspace():
			# Translators: message presented when user presses the shortcut key for translating clipboard text but the clipboard is empty.
			ui.message(_("There is no text on the clipboard"))
			return
		if len(text) < (charslimit): 
			config = ConfigObj(config_file)
			lang_from = config["translation"]["from"]
			lang_to = config["translation"]["into"]
			copyTranslation = config["settings"]["CopyTranslatedText"]
			threading.Thread(target=self.translate, args=(text,)).run()
		else:
			# Translators: Message presented when clipboard text (to be translated) is too long (more than a set limit).
			ui.message(_("The clipboard contains a large portion of text. It is %s characters long. The limit is 1500 characters.") % len(text))
	# Translators: message presented in input help mode, when user presses the shortcut keys for this addon.
	script_translateClipboardText.__doc__=_("Translates clipboard text from one language to another using Google Translate.")

	def script_translateSelection(self, gesture):
		global lang_from, lang_to, copyTranslation
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
			if len(info.text) < (charslimit): 
				config = ConfigObj(config_file)
				lang_from = config["translation"]["from"]
				lang_to = config["translation"]["into"]
				copyTranslation = config["settings"]["CopyTranslatedText"]
				threading.Thread(target=self.translate, args=(info.text,)).run()
			else:
				# Translators: Message presented when selected text (to be translated) is too long (more than a set limit).
				ui.message(_("The selection contains a large portion of text. It is %s characters long. The limit is 1500 characters.") % len(info.text))
	# Translators: message presented in input help mode, when user presses the shortcut keys for this addon.
	script_translateSelection.__doc__=_("Translates selected text from one language to another using Google Translate.")

	def script_swapLanguages(script,gesture):
		config = ConfigObj(config_file)
		temp=config["translation"]["from"]
		config["translation"]["from"]=config["translation"]["into"]
		config["translation"]["into"]=temp
		config.write()
		ui.message(_("Languages swapped."))
	script_swapLanguages.__doc__=_("Swaps the languages.")

	def translate(self, text):
		try:
			response = json.load(self.opener.open('http://translate.google.ru/translate_a/t?client=x&text={text}&sl={lang_from}&tl={lang_to}'.format(text=urllib2.quote(text.encode('utf-8')), lang_from=lang_from, lang_to=lang_to)))
		except:
			log.exception("Can not translate text")
			# Translators: Message presented when the given text (from selected or clipboard) cannot be translated.
			queueHandler.queueFunction(queueHandler.eventQueue, ui.message, _('Error translating text. See log for details'))
			return
		translation = "".join(t['trans'] for t in response['sentences'])
		if 'dict' in response:
			translation += " | " + " | ".join((", ".join(w for w in d['terms'])) for d in response['dict'])
		queueHandler.queueFunction(queueHandler.eventQueue, ui.message, translation)
		if copyTranslation == "true":
			api.copyToClip(translation)


		__gestures = {
"kb:NVDA+shift+r": "swapLanguages",
		"kb:NVDA+shift+t": "translateSelection",
"kb:NVDA+shift+y": "translateClipboardText",
	}
