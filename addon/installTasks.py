# -*- coding: UTF-8 -*-

import addonHandler
import gui
import wx
import os
import globalVars

addonHandler.initTranslation()

def onInstall():
	for addon in addonHandler.getAvailableAddons():
		if addon.manifest['name'] == "Instant-Translate":
			askToRemove(addon)
			break
		elif addon.manifest['name'] == "instantTranslate" and addon.manifest['version'] == "3.0-dev":
			if os.path.isfile(os.path.join(globalVars.appArgs.configPath, "instantTranslate.ini")):
				os.remove(os.path.join(globalVars.appArgs.configPath, "instantTranslate.ini"))
			askToRemove(addon)
			break

def askToRemove(addon):
	if gui.messageBox(
		# Translators: the label of a message box dialog.
		_("You have installed an old and incompatible version of this addon. Do you want to uninstall the old version?"),
		# Translators: the title of a message box dialog.
		_("Uninstall incompatible add-on"),
		wx.YES|wx.NO|wx.ICON_WARNING) == wx.YES:
			addon.requestRemove()
