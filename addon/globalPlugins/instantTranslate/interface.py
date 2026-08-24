#interface.py
# Copyright (C) 2012-2026 Aleksey Sadovoy AKA Lex <lex@progger.ru>,
#ruslan <ru2020slan@yandex.ru>,
#Beka Gozalishvili <beqaprogger@gmail.com>
#other nvda contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import wx
import gui
import gui.guiHelper
from gui.settingsDialogs import SettingsPanel
from .langslist import g, getLanguages
from .languagePairs import MAX_PAIRS, LanguagePair, formatPairs, parsePairs, slotLabel
import addonHandler

addonHandler.initTranslation()


def sourceChoices(sourceLangs):
	auto = g("auto")
	return [auto] + [name for name in sourceLangs if name != auto]


def getName(languages, code):
	for name, languageCode in languages.items():
		if languageCode == code:
			return name
	return g("en")


class InstantTranslateSettingsPanel(SettingsPanel):
	# Translators: name of the dialog.
	title = _("Instant Translate")

	def makeSettings(self, sizer):
		helper = gui.guiHelper.BoxSizerHelper(self, sizer=sizer)
		self.sourceLangs = getLanguages("source")
		self.targetLangs = getLanguages("target")
		self.languagePairs = parsePairs(self.addonConf['pairs'])

		# Translators: Help message for a dialog.
		helpLabel = wx.StaticText(self, label=_("Select translation source and target language:"))
		sizer.Add(helpLabel)

		# Translators: A setting in addon settings dialog.
		fromLabelText = _("Source language:")
		# list of choices, in alphabetical order but with auto in first position
		self._fromChoice = helper.addLabeledControl(fromLabelText, wx.Choice, choices=sourceChoices(self.sourceLangs))

		# Translators: A setting in addon settings dialog.
		intoLabelText = _("Target language:")
		self._intoChoice = helper.addLabeledControl(intoLabelText, wx.Choice, choices=list(self.targetLangs))

		# Translators: A setting in addon settings dialog, shown if source language is on auto.
		swapLabelText = _("Language for swapping:")
		self._swapChoice = helper.addLabeledControl(swapLabelText, wx.Choice, choices=list(self.targetLangs))
		self._fromChoice.Bind(wx.EVT_CHOICE, self.onFromSelect)

		# Translators: A setting in addon settings dialog, shown if source language is on auto.
		self.autoSwapChk = helper.addItem(wx.CheckBox(self, label=_("Activate the auto-swap if recognized source is equal to the target (experimental)")))
		self.autoSwapChk.SetValue(self.addonConf['autoswap'])

		# Translators: A setting in addon settings dialog.
		self.copyTranslationChk = helper.addItem(wx.CheckBox(self, label=_("Copy translation result to clipboard")))
		self.copyTranslationChk.SetValue(self.addonConf['copytranslatedtext'])

		# Translators: A setting in addon settings dialog.
		self.replaceUnderscores = helper.addItem(wx.CheckBox(self, label=_("Replace underscores with spaces (May provide better translation results depending on context)")))
		self.replaceUnderscores.SetValue(self.addonConf['replaceUnderscores'])

		# Translators: A setting in addon settings dialog.
		self.progressBeepsChk = helper.addItem(wx.CheckBox(self, label=_("Beep while a translation is in progress")))
		self.progressBeepsChk.SetValue(self.addonConf['progressbeeps'])

		# Translators: A button in addon settings dialog, opening the language pairs dialog.
		self.pairsBtn = helper.addItem(wx.Button(self, label=_("Language &pairs...")))
		self.pairsBtn.Bind(wx.EVT_BUTTON, self.onLanguagePairs)

		# Translators: A setting in addon settings dialog.
		self.donateBtn = helper.addItem(wx.Button(self, label=_("Support an author...")))
		self.donateBtn.Bind(wx.EVT_BUTTON, self.onDonate)

		iLang_from = self._fromChoice.FindString(getName(self.sourceLangs, self.addonConf['from']))
		iLang_to = self._intoChoice.FindString(getName(self.targetLangs, self.addonConf['into']))
		iLang_swap = self._swapChoice.FindString(getName(self.targetLangs, self.addonConf['swap']))
		self._fromChoice.Select(iLang_from)
		self._intoChoice.Select(iLang_to)
		self._swapChoice.Select(iLang_swap)
		if iLang_from != 0:
			self._swapChoice.Disable()
			self.autoSwapChk.Disable()

	def postInit(self):
		self._fromChoice.SetFocus()

	def onDonate(self, evt):
		from .donate_dialog import requestDonations
		requestDonations(self)

	def onLanguagePairs(self, evt):
		dialog = LanguagePairsDialog(self, self.languagePairs, self.sourceLangs, self.targetLangs)
		try:
			if dialog.ShowModal() == wx.ID_OK:
				self.languagePairs = dialog.pairs
		finally:
			dialog.Destroy()
		self.pairsBtn.SetFocus()

	def onFromSelect(self, event):
		if event.GetString() == g("auto"):
			self._swapChoice.Enable()
			self.autoSwapChk.Enable()
		else:
			self._swapChoice.Disable()
			self.autoSwapChk.Disable()

	def onSave(self):
		self.addonConf['from'] = self.sourceLangs[self._fromChoice.GetStringSelection()]
		self.addonConf['into'] = self.targetLangs[self._intoChoice.GetStringSelection()]
		self.addonConf['swap'] = self.targetLangs[self._swapChoice.GetStringSelection()]
		self.addonConf['copytranslatedtext'] = self.copyTranslationChk.GetValue()
		self.addonConf['autoswap'] = self.autoSwapChk.GetValue()
		self.addonConf['replaceUnderscores'] = self.replaceUnderscores.GetValue()
		self.addonConf['progressbeeps'] = self.progressBeepsChk.GetValue()
		self.addonConf['pairs'] = formatPairs(self.languagePairs)

	def getName(self, languages, code):
		return getName(languages, code)


class LanguagePairsDialog(wx.Dialog):
	def __init__(self, parent, pairs, sourceLangs, targetLangs):
		# Translators: title of the dialog managing the language pairs.
		super().__init__(parent, title=_("Language pairs"))
		self.pairs = list(pairs)
		self.sourceLangs = sourceLangs
		self.targetLangs = targetLangs

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		helper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: label of the list of language pairs, in the language pairs dialog.
		listLabel = _("Language &pairs, activated by the keys 1 to 0 of the Instant Translate layer:")
		self.pairsList = helper.addLabeledControl(listLabel, wx.ListBox, choices=[], style=wx.LB_SINGLE)
		self.pairsList.Bind(wx.EVT_LISTBOX, self.onSelect)
		self.pairsList.Bind(wx.EVT_LISTBOX_DCLICK, self.onEdit)

		buttonHelper = gui.guiHelper.ButtonHelper(wx.HORIZONTAL)
		# Translators: a button of the language pairs dialog.
		self.addBtn = buttonHelper.addButton(self, label=_("&Add"))
		# Translators: a button of the language pairs dialog.
		self.editBtn = buttonHelper.addButton(self, label=_("&Edit"))
		# Translators: a button of the language pairs dialog.
		self.removeBtn = buttonHelper.addButton(self, label=_("&Remove"))
		# Translators: a button of the language pairs dialog, moving a pair one slot up.
		self.upBtn = buttonHelper.addButton(self, label=_("Move &up"))
		# Translators: a button of the language pairs dialog, moving a pair one slot down.
		self.downBtn = buttonHelper.addButton(self, label=_("Move &down"))
		self.addBtn.Bind(wx.EVT_BUTTON, self.onAdd)
		self.editBtn.Bind(wx.EVT_BUTTON, self.onEdit)
		self.removeBtn.Bind(wx.EVT_BUTTON, self.onRemove)
		self.upBtn.Bind(wx.EVT_BUTTON, self.onMoveUp)
		self.downBtn.Bind(wx.EVT_BUTTON, self.onMoveDown)
		helper.addItem(buttonHelper)

		helper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		mainSizer.Add(helper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.refresh(0 if self.pairs else wx.NOT_FOUND)
		self.CentreOnScreen()
		self.pairsList.SetFocus()

	def refresh(self, selection):
		self.pairsList.Set([slotLabel(index, pair) for index, pair in enumerate(self.pairs)])
		if self.pairs:
			self.pairsList.SetSelection(max(0, min(selection, len(self.pairs) - 1)))
		else:
			self.pairsList.SetSelection(wx.NOT_FOUND)
		self.updateButtons()

	def updateButtons(self):
		index = self.pairsList.GetSelection()
		hasSelection = index != wx.NOT_FOUND
		self.addBtn.Enable(len(self.pairs) < MAX_PAIRS)
		self.editBtn.Enable(hasSelection)
		self.removeBtn.Enable(hasSelection)
		self.upBtn.Enable(hasSelection and index > 0)
		self.downBtn.Enable(hasSelection and index < len(self.pairs) - 1)

	def onSelect(self, evt):
		self.updateButtons()

	def editPair(self, pair=None):
		dialog = LanguagePairDialog(self, self.sourceLangs, self.targetLangs, pair)
		try:
			return dialog.pair if dialog.ShowModal() == wx.ID_OK else None
		finally:
			dialog.Destroy()

	def onAdd(self, evt):
		if len(self.pairs) >= MAX_PAIRS:
			return
		pair = self.editPair()
		if pair is not None:
			self.pairs.append(pair)
			self.refresh(len(self.pairs) - 1)
		self.pairsList.SetFocus()

	def onEdit(self, evt):
		index = self.pairsList.GetSelection()
		if index == wx.NOT_FOUND:
			return
		pair = self.editPair(self.pairs[index])
		if pair is not None:
			self.pairs[index] = pair
			self.refresh(index)
		self.pairsList.SetFocus()

	def onRemove(self, evt):
		index = self.pairsList.GetSelection()
		if index == wx.NOT_FOUND:
			return
		del self.pairs[index]
		self.refresh(index)
		self.pairsList.SetFocus()

	def onMoveUp(self, evt):
		self.move(-1)

	def onMoveDown(self, evt):
		self.move(1)

	def move(self, offset):
		index = self.pairsList.GetSelection()
		target = index + offset
		if index == wx.NOT_FOUND or not 0 <= target < len(self.pairs):
			return
		self.pairs[index], self.pairs[target] = self.pairs[target], self.pairs[index]
		self.refresh(target)
		self.pairsList.SetFocus()


class LanguagePairDialog(wx.Dialog):
	def __init__(self, parent, sourceLangs, targetLangs, pair=None):
		# Translators: title of the dialog adding or editing one language pair.
		super().__init__(parent, title=_("Language pair"))
		self.sourceLangs = sourceLangs
		self.targetLangs = targetLangs

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		helper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		# Translators: A setting in addon settings dialog.
		self._fromChoice = helper.addLabeledControl(_("Source language:"), wx.Choice, choices=sourceChoices(sourceLangs))
		# Translators: A setting in addon settings dialog.
		self._intoChoice = helper.addLabeledControl(_("Target language:"), wx.Choice, choices=list(targetLangs))
		helper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		mainSizer.Add(helper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)

		self._fromChoice.Select(max(0, self._fromChoice.FindString(getName(sourceLangs, pair.langFrom))) if pair else 0)
		self._intoChoice.Select(max(0, self._intoChoice.FindString(getName(targetLangs, pair.langTo))) if pair else 0)
		self.CentreOnScreen()
		self._fromChoice.SetFocus()

	@property
	def pair(self):
		return LanguagePair(
			self.sourceLangs[self._fromChoice.GetStringSelection()],
			self.targetLangs[self._intoChoice.GetStringSelection()],
		)
