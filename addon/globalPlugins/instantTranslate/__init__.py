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
import scriptHandler
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
	config ["translation"] = {"from": "auto", "into": lo_lang, "swap": "en"}
	config ["settings"] = {"CopyTranslatedText": "true", "AutoSwap": "true"}
	config ["temporary"] = {"isAutoSwapped": "false"}
	config.write()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		self.opener = urllib2.build_opener()
		self.opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		if globalVars.appArgs.secure:
			return
		self.createMenu()
		self.getUpdatedGlobalVars()

	def getUpdatedGlobalVars(self):
		global lang_from, lang_to, lang_swap, copyTranslation, autoSwap, isAutoSwapped
		config = ConfigObj(config_file)
		# source language
		lang_from = config["translation"]["from"]
		# target language
		lang_to = config["translation"]["into"]
		# language used to swap source and target when source is auto
		lang_swap = config["translation"]["swap"]
		# determine whether to copy translation on clipboard
		copyTranslation = config["settings"]["CopyTranslatedText"]
		# determine whether to swap automatically lang_swap and target language, if source recognized equal to the target
		autoSwap = config["settings"]["AutoSwap"]
		# keep track if there was a swapping from source=auto during previous NVDA session
		isAutoSwapped = config["temporary"]["isAutoSwapped"]

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
			return
		if len(text) < (charslimit): 
			threading.Thread(target=self.translate, args=(text,)).run()
		else:
			# Translators: Message presented when clipboard text (to be translated) is too long (more than a set limit).
			ui.message(_("The clipboard contains a large portion of text. It is %s characters long. The limit is 1500 characters.") % len(text))
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
			if len(info.text) < (charslimit): 
				threading.Thread(target=self.translate, args=(info.text,)).run()
			else:
				# Translators: Message presented when selected text (to be translated) is too long (more than a set limit).
				ui.message(_("The selection contains a large portion of text. It is %s characters long. The limit is 1500 characters.") % len(info.text))
	# Translators: message presented in input help mode, when user presses the shortcut keys for this addon.
	script_translateSelection.__doc__=_("Translates selected text from one language to another using Google Translate.")

	def translate(self, text):
		self.getUpdatedGlobalVars()
		try:
			response = json.load(self.opener.open('http://translate.google.ru/translate_a/t?client=x&text={text}&sl={lang_from}&tl={lang_to}'.format(text=urllib2.quote(text.encode('utf-8')), lang_from=lang_from, lang_to=lang_to)))
			if lang_from == "auto" and response["src"] == lang_to and autoSwap == "true":
				self.swapLanguages(lang_swap, lang_to)
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

	def swapLanguages(self, langFrom, langTo):
		global lang_from, lang_to
		lang_from=langTo
		lang_to=langFrom

	def script_announceOrSwapLanguages(self, gesture):
		self.getUpdatedGlobalVars()
		if scriptHandler.getLastScriptRepeatCount() != 0:
			global isAutoSwapped
			if lang_from == "auto":
				self.swapLanguages(lang_swap, lang_to)
				isAutoSwapped=True
			elif isAutoSwapped and lang_to == lang_swap:
				self.swapLanguages(lang_from, "auto")
				isAutoSwapped=False
			else:
				self.swapLanguages(lang_from, lang_to)
			config = ConfigObj(config_file)
			config["translation"]["from"] = lang_from
			config["translation"]["into"] = lang_to
			config["temporary"]["isAutoSwapped"] = isAutoSwapped
			config.write()
			# Translators: message presented calling the script twice
			ui.message(_("Languages swapped"))
		# Translators: message presented calling the script once or twice
		ui.message(_("Translate: from {lang1} to {lang2}").format(lang1=lang_from, lang2=lang_to))

	__gestures = {
		"kb:NVDA+shift+t": "translateSelection",
		"kb:NVDA+shift+y": "translateClipboardText",
		"kb:NVDA+shift+r": "announceOrSwapLanguages",
	}
