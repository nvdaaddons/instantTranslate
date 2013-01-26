#interface.py
# Copyright (C) 2012-2013 Aleksey Sadovoy AKA Lex <lex@progger.ru>,
#ruslan <ru2020slan@yandex.ru>,
#beqa <beqaprogger@gmail.com>
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import os.path
import wx
import gui
from langslist import langslist
import config
from configobj import *

config_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instantTranslate.ini')

class InstantTranslateSettingsDialog(gui.SettingsDialog):
	title = _("Instant Translate Settings")

	def __init__(self, parent):
		super(InstantTranslateSettingsDialog, self).__init__(parent)

	def makeSettings(self, sizer):
		helpLabel = wx.StaticText(self, label=_("Select language from which you want to translate text and into and press ok to save."))
		helpLabel.Wrap(self.GetSize()[0])
		sizer.Add(helpLabel)
		fromSizer = wx.BoxSizer(wx.HORIZONTAL)
		fromLabel = wx.StaticText(self, label=_("Language From:"))
		fromSizer.Add(fromLabel)
		self._fromChoice = wx.Choice(self, style=wx.CB_SORT, choices=langslist.keys())
		fromSizer.Add(self._fromChoice)
		intoSizer = wx.BoxSizer(wx.HORIZONTAL)
		intoLabel = wx.StaticText(self, label=_("Language Into:"))
		intoSizer.Add(intoLabel)
		self._intoChoice = wx.Choice(self, style=wx.CB_SORT, choices=langslist.keys())
		intoSizer.Add(self._intoChoice)
		sizer.Add(fromSizer)
		sizer.Add(intoSizer)

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
		config.write()

	def getDictKey (self, currentValue):
		for key, value in langslist.iteritems():
			if value == currentValue:
				return key
