#interface.py
# Copyright (C) 2012-2013 Aleksey Sadovoy AKA Lex <lex@progger.ru>,
#ruslan <ru2020slan@yandex.ru>,
#beqa <beqaprogger@gmail.com>
#other nvda contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import os.path
import wx
import gui
from langslist import langslist
import globalVars
import config
from configobj import *
import addonHandler
addonHandler.initTranslation()

config_file = os.path.join(globalVars.appArgs.configPath,"instantTranslate.ini")

class InstantTranslateSettingsDialog(gui.SettingsDialog):
	# Translators: name of the dialog.
	title = _("Instant Translate Settings")

	def __init__(self, parent):
		super(InstantTranslateSettingsDialog, self).__init__(parent)

	def makeSettings(self, sizer):
		# Translators: Help message for a dialog.
		helpLabel = wx.StaticText(self, label=_("Select translation source and target language:"))
		helpLabel.Wrap(self.GetSize()[0])
		sizer.Add(helpLabel)
		fromSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: A setting in instant translate settings dialog.
		fromLabel = wx.StaticText(self, label=_("Source language:"))
		fromSizer.Add(fromLabel)
		self._fromChoice = wx.Choice(self, style=wx.CB_SORT, choices=langslist.keys())
		fromSizer.Add(self._fromChoice)
		intoSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: A setting in instant translate settings dialog.
		intoLabel = wx.StaticText(self, label=_("Target language:"))
		intoSizer.Add(intoLabel)
		self._intoChoice = wx.Choice(self, style=wx.CB_SORT, choices=langslist.keys())
		intoSizer.Add(self._intoChoice)
		sizer.Add(fromSizer)
		sizer.Add(intoSizer)
		config = ConfigObj(config_file)
		CopyStateValue = 0
		if config["settings"]["CopyTranslatedText"] == "true":
			CopyStateValue = 1
		else:
			CopyStateValue = 0
		self.copyTranslationChk = wx.CheckBox(self, label=_("Copy translation result to clipboard"))
		self.copyTranslationChk.SetValue(CopyStateValue)
		sizer.Add(self.copyTranslationChk)

	def postInit(self):
		config = ConfigObj(config_file)
		iLang_from = self._fromChoice.FindString(self.getDictKey(config["translation"]["from"]))
		iLang_to = self._intoChoice.FindString(self.getDictKey(config["translation"]["into"]))

		self._fromChoice.Select(iLang_from)
		self._intoChoice.Select(iLang_to)
		self._fromChoice.SetFocus()


	def onOk(self, event):
		super(InstantTranslateSettingsDialog, self).onOk(event)
		# Update Configuration
		config = ConfigObj(config_file)
		config["translation"]["from"] = langslist[self._fromChoice.GetStringSelection()]
		config["translation"]["into"] = langslist[self._intoChoice.GetStringSelection()]
		if self.copyTranslationChk.GetValue() == 1:
			config["settings"]["CopyTranslatedText"] = "true"
		else:
			config["settings"]["CopyTranslatedText"] = "false"
		config.write()

	def getDictKey (self, currentValue):
		for key, value in langslist.iteritems():
			if value == currentValue:
				return key
