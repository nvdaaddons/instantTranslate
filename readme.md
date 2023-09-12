# Instant Translate #

* Authors: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino and other NVDA contributors.
* Download [stable version][1]
* Download [development version][2]

This add-on is used to translate selected and/or clipboard text from one language to another.
This is done using the Google Translate service.

## Configuring languages ##
To configure source, target and in case swap language, go to: NVDA Menu >> Preferences >> Instant Translate Settings.

There are two comboboxes labeled "Source language" and "Target language", and a checkbox to decide if it must copy the translation to clipboard.

In addition, if you selected auto option (the first choice) from "Source language" combobox, there are also a combobox labeled "Language for swapping" and a checkbox about the auto-swap.

The meaning of two first comboboxes and checkbox for copy is clear, but some words about the rest are necessary. Remember always that the explanations below assume the source language set on the auto option.

The "Language for swapping" combobox is useful when you swap via script (see below) the source and target language; in fact, a target language set on the auto option has no sense, so the addon sets it to value of combobox above.

So, imagine this situation: you usually translate into English (your main language), but sometimes (for example, when you write a document) you need to translate into Italian (your second language, suppose); you can set "Language for swapping" combobox to Italian, so you will translate from English to Italian without accessing directly to the addon settings. Obviously this function has a major or minor utility according to your more frequent needs.

Now, the auto-swap checkbox: it appears if and only if you set the auto option in "Source language" combobox, and is directly connected with "Language for swapping" combobox. If you activate it, then the addon tries to commute automatically from your source and target configuration to a configuration where target becomes the source language, and language selected in "Language for swapping" combobox is the new target language; extremely useful if the source language of the text you want translate is the target language.

A simple example: take again in mind the situation  imagined previously; if you translate a text in a language different from English, there is no problem, you get the correct translation in English. But if you need to translate a text from English, normally you get a translation into English identical to original text, and this is a bit useless. Thanks to auto-swap function, however, assuming that you want to know how your text sounds into Italian, the addon commutes automatically the target language to Italian, so it returns a valid translation.

Anyway, this is a temporary configuration; if this option has no effect (it's experimental), try to commute manually to a stable configuration, using the gesture for swapping described below. It's experimental because in some situations (with short texts, typically), Google does not recognize the real source language correctly, and you have to swap languages manually via script, so to force the source language to be the previous target language (English in our example).

At least, in the speech settings parameters dialog (NVDA Menu >> Preferences >> Speech), you may want to check the "Automatic language switching (when supported)" option. This way, if you are using a multi-lingual synthesizer, the translation will be announced using the target language voice of the synthesizer.

## Using ##
You can use this add-on in three ways:

1. Select some text using selection commands (shift with arrow keys, for example) and press associated key to translate. translation result will be read with synthesizer which you are using.
2. You can also translate text from the Clipboard.
3. Press the dedicated shortcut key to translate the last spoken text.

## Shortcuts ##
All following commands must be pressed after modifier key "NVDA+Shift+t":

* T: Translate selected text,
* Shift+t: translate text from the Clipboard,
* S: swap source and target languages,
* A: announce current configuration,
* C: copy last result to clipboard,
* I: identify the language of selected text,
* L: translate the last spoken text,
* O: open translation settings dialog
* H: announces all available layered commands.

## Changes for 4.4.2 ##
* Restore language detection and auto-swapping (Thanks to Cyrille for fix)
* updated languages for translation (thanks to Cyrille)

## Changes for 4.4 ##
* Instant translate is now compatible with NVDA 2019.3 (Python 3 versions of NVDA)

## Changes for 4.3 ##
* nvda compatibility fix Now instant translate will be compatible with latest nvda builds.
* found a way to use google as a translation service again.

## Changes for 4.2 ##
* Restored working state with newer versions of nvda.
* Restored automatic language detection.

## Changes for 4.1 ##
* InstantTranslate is working again, now with Yandex translator service instead of Google.

## Changes for 4.0 ##
* Translation is automatically performed after swapping.
* Cache bug fixed.

## Changes for 3.0 ##
* Change way how Shortcuts are used, now you can press instantTranslate modifier key "NVDA+Shift+t", and then single letter key to perform some action (see all Commands in the "Shortcuts" section).
* Implemented swapping languages.
* Changed configuration format, now we can change instant translate settings if we are in readonly pane, but remember that this will work before first restart of NVDA.
* Removed limit on amount of text that can be translated.
* Added shortcut t to the Instant Translate Settings menu item
* The auto option is now in first position in source combo, and absent in target combo.
* Added a checkbox for configuring copying translation results.
* Store config file in the root of settings folder.
* Source and target languages syncronized with what Google Translate currently exposes (22 Apr 2015).

## Changes for 2.1 ##
* Now addon can translate text from clipboard when pressing nvda+shift+y. 

## Changes for 2.0 ##
* Added gui configurator where you can choose source and target languages.
* Added addon menu item found under preferences menu.
* Settings now is written in separate config file.
* Translation results now automatically copies into the clipboard for future manipulations.

## Changes for 1.0 ##
* Initial version.

[1]: https://addons.nvda-project.org/legacy?file=instantTranslate

[2]: http://addons.nvda-project.org/files/get.php?file=it-dev
