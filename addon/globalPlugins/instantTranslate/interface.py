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
import langslist as lngModule
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
		# Translators: A setting in addon settings dialog.
		fromLabel = wx.StaticText(self, label=_("Source language:"))
		fromSizer.Add(fromLabel)
		# list of choices, in alphabetical order but with auto in first position
		temp=self.prepareChoices()
		self._fromChoice = wx.Choice(self, choices=temp)
		fromSizer.Add(self._fromChoice)
		intoSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: A setting in addon settings dialog.
		intoLabel = wx.StaticText(self, label=_("Target language:"))
		intoSizer.Add(intoLabel)
		# auto has no sense in target
		temp.remove(lngModule.g("auto"))
		self._intoChoice = wx.Choice(self, choices=temp)
		intoSizer.Add(self._intoChoice)
		sizer.Add(fromSizer)
		sizer.Add(intoSizer)
		config = ConfigObj(config_file)
		CopyStateValue=AutoSwapStateValue=0
		if config["settings"]["CopyTranslatedText"] == "True":
			CopyStateValue = 1
		if config["settings"]["AutoSwap"] == "True":
			AutoSwapStateValue = 1
		# Translators: A setting in addon settings dialog.
		self.copyTranslationChk = wx.CheckBox(self, label=_("Copy translation result to clipboard"))
		self.copyTranslationChk.SetValue(CopyStateValue)
		sizer.Add(self.copyTranslationChk)
		self.swapSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: A setting in addon settings dialog, shown if source language is on auto.
		swapLabel = wx.StaticText(self, label=_("Language for swapping:"))
		self.swapSizer.Add(swapLabel)
		self._swapChoice = wx.Choice(self, choices=temp)
		self._fromChoice.Bind(wx.EVT_CHOICE, lambda event, sizer=sizer: self.onFromSelect(event, sizer))
		self.swapSizer.Add(self._swapChoice)
		sizer.Add(self.swapSizer)
		# Translators: A setting in addon settings dialog, shown if source language is on auto.
		self.autoSwapChk = wx.CheckBox(self, label=_("Activate the auto-swap if recognized source is equal to the target (experimental)"))
		self.autoSwapChk.SetValue(AutoSwapStateValue)
		sizer.Add(self.autoSwapChk)
		iLang_from = self._fromChoice.FindString(self.getDictKey(config["translation"]["from"]))
		iLang_to = self._intoChoice.FindString(self.getDictKey(config["translation"]["into"]))
		iLang_swap = self._swapChoice.FindString(self.getDictKey(config["translation"]["swap"]))
		self._fromChoice.Select(iLang_from)
		self._intoChoice.Select(iLang_to)
		self._swapChoice.Select(iLang_swap)
		if iLang_from != 0:
			sizer.Hide(self.swapSizer)
			sizer.Hide(self.autoSwapChk)

	def postInit(self):
		self._fromChoice.SetFocus()

	def prepareChoices(self):
		keys=langslist.keys()
		auto=lngModule.g("auto")
		keys.remove(auto)
		keys.sort()
		choices=[]
		choices.append(auto)
		choices.extend(keys)
		return choices

	def onFromSelect(self, event, sizer):
		if event.GetString() == lngModule.g("auto"):
			sizer.Show(self.swapSizer)
			sizer.Show(self.autoSwapChk)
		else:
			sizer.Hide(self.swapSizer)
			sizer.Hide(self.autoSwapChk)

	def onOk(self, event):
		super(InstantTranslateSettingsDialog, self).onOk(event)
		# Update Configuration
		config = ConfigObj(config_file)
		config["translation"]["from"] = langslist[self._fromChoice.GetStringSelection()]
		config["translation"]["into"] = langslist[self._intoChoice.GetStringSelection()]
		config["translation"]["swap"] = langslist[self._swapChoice.GetStringSelection()]
		if self.copyTranslationChk.GetValue() == 1:
			config["settings"]["CopyTranslatedText"] = "True"
		else:
			config["settings"]["CopyTranslatedText"] = "False"
		if self.autoSwapChk.GetValue() == 1:
			config["settings"]["AutoSwap"] = "True"
		else:
			config["settings"]["AutoSwap"] = "False"
		config.write()

	def getDictKey (self, currentValue):
		for key, value in langslist.iteritems():
			if value == currentValue:
				return key
