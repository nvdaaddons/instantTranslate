#donate_dialog.py
# Copyright (C) 2022-2023 Beqa Gozalishvili <beqaprogger@gmail.com>
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import addonHandler
import gui
import webbrowser
import wx

addonHandler.initTranslation()


class DonationDialog(gui.nvdaControls.MessageDialog):
    YOOMONEY_URL = "https://yoomoney.ru/to/4100117727255296"
    PAYPAL_URL = "https://paypal.me/gozaltech"

    def __init__(self, parent, title, message):
        super().__init__(parent, title, message, dialogType=gui.nvdaControls.MessageDialog.DIALOG_TYPE_WARNING)

    def _addButtons(self, buttonHelper):
        paypalBtn = buttonHelper.addButton(self, label=_("Donate via Paypal"), name="PAYPAL_URL")
        yoomoneyBtn = buttonHelper.addButton(self, label=_("Donate via Yoomoney"), name="YOOMONEY_URL")
        paypalBtn.Bind(wx.EVT_BUTTON, self.onDonate)
        yoomoneyBtn.Bind(wx.EVT_BUTTON, self.onDonate)
        cancelBtn = buttonHelper.addButton(self, id=wx.ID_CANCEL)
        cancelBtn.Bind(wx.EVT_BUTTON, lambda evt: self.EndModal(wx.CANCEL))

    def onDonate(self, evt):
        donateBtn = evt.GetEventObject()
        donateUrl = getattr(self, donateBtn.Name)
        webbrowser.open(donateUrl)
        self.EndModal(wx.OK)

def requestDonations(parentWindow):
    addon = addonHandler.getCodeAddon()
    addonName = addon.name
    title = _("Request for contributions to {name}").format(name=addonName)
    message = _("{name} is a free add-on for NVDA.\n"
    "You can make a donation to its author to support further development of this and other free projects.\n"
    "Do you want to donate now? Choose one of the available payment methods. You will be redirected to the corresponding website to complete a donation").format(name=addonName)
    return DonationDialog(parentWindow, title, message).ShowModal()
