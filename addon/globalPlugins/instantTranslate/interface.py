#interface.py
# Copyright (C) 2012-2016 Aleksey Sadovoy AKA Lex <lex@progger.ru>,
#ruslan <ru2020slan@yandex.ru>,
#beqa <beqaprogger@gmail.com>
#other nvda contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import os.path
import sys
import wx
import gui
from .langslist import langslist
from . import langslist as lngModule
import globalVars
import config
import addonHandler
from copy import deepcopy
from locale import strxfrm

addonHandler.initTranslation()

class InstantTranslateSettingsPanel(gui.SettingsPanel):
	# Translators: name of the dialog.
	title = _("Instant Translate")

	def __init__(self, parent):
		super(InstantTranslateSettingsPanel, self).__init__(parent)

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
		temp = self.prepareChoices()
		# zh-TW is not present in sources, on site
		temp1 = deepcopy(temp)
		temp1.remove(lngModule.g("zh-TW"))
		self._fromChoice = wx.Choice(self, choices=temp1)
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
		self.copyTranslationChk.SetValue(config.conf['instanttranslate']['copytranslatedtext'])
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
		self.autoSwapChk.SetValue(config.conf['instanttranslate']['autoswap'])
		sizer.Add(self.autoSwapChk)
		iLang_from = self._fromChoice.FindString(self.getDictKey(config.conf['instanttranslate']['from']))
		iLang_to = self._intoChoice.FindString(self.getDictKey(config.conf['instanttranslate']['into']))
		iLang_swap = self._swapChoice.FindString(self.getDictKey(config.conf['instanttranslate']['swap']))
		self._fromChoice.Select(iLang_from)
		self._intoChoice.Select(iLang_to)
		self._swapChoice.Select(iLang_swap)
		if iLang_from != 0:
			sizer.Hide(self.swapSizer)
			sizer.Hide(self.autoSwapChk)

	def postInit(self):
		self._fromChoice.SetFocus()

	def prepareChoices(self):
		keys=list(langslist.keys())
		auto=lngModule.g("auto")
		keys.remove(auto)
		if sys.version_info[0] >= 3:
			keys.sort(key=strxfrm)
		else:
			# Python 2: strxfrm does not seem to work correctly, so do not use locale rules for sorting.
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

	def onSave(self):
		# Update Configuration
		config.conf['instanttranslate']['from'] = langslist[self._fromChoice.GetStringSelection()]
		config.conf['instanttranslate']['into'] = langslist[self._intoChoice.GetStringSelection()]
		config.conf['instanttranslate']['swap'] = langslist[self._swapChoice.GetStringSelection()]
		config.conf['instanttranslate']['copytranslatedtext'] = self.copyTranslationChk.GetValue()
		config.conf['instanttranslate']['autoswap'] = self.autoSwapChk.GetValue()

	def getDictKey(self, currentValue):
		for key, value in langslist.items():
			if value == currentValue:
				return key
		# set English if search fails
		return lngModule.g("en")
