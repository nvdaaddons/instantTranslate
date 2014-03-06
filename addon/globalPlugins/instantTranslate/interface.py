#interface.py
# Copyright (C) 2012-2014 Aleksey Sadovoy AKA Lex <lex@progger.ru>,
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
import _config
import addonHandler

_config.load()
addonHandler.initTranslation()

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
		# Translators: A setting in addon settings dialog.
		self.copyTranslationChk = wx.CheckBox(self, label=_("Copy translation result to clipboard"))
		self.copyTranslationChk.SetValue(_config.instanttranslateConfig['settings']['copytranslatedtext'])
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
		self.autoSwapChk.SetValue(_config.instanttranslateConfig['settings']['autoswap'])
		sizer.Add(self.autoSwapChk)
		iLang_from = self._fromChoice.FindString(self.getDictKey(_config.instanttranslateConfig['translation']['from']))
		iLang_to = self._intoChoice.FindString(self.getDictKey(_config.instanttranslateConfig['translation']['into']))
		iLang_swap = self._swapChoice.FindString(self.getDictKey(_config.instanttranslateConfig['translation']['swap']))
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
		_config.instanttranslateConfig['translation']['from'] = langslist[self._fromChoice.GetStringSelection()]
		_config.instanttranslateConfig['translation']['into'] = langslist[self._intoChoice.GetStringSelection()]
		_config.instanttranslateConfig['translation']['swap'] = langslist[self._swapChoice.GetStringSelection()]
		_config.instanttranslateConfig['settings']['copytranslatedtext'] = self.copyTranslationChk.GetValue()
		_config.instanttranslateConfig['settings']['autoswap'] = self.autoSwapChk.GetValue()
		_config.save()

	def getDictKey (self, currentValue):
		for key, value in langslist.iteritems():
			if value == currentValue:
				return key
