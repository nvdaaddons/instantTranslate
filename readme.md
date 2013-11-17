# Instant Translate #

* Authors: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino and other nvda contributors.
* Download [version 2.2beta2][1]
* Download [version 3.0-dev][2]

This add-on is used to translate selected and/or clipboard text from one language to another.
This is done using the Google Translate service.

## Configuring languages ##
To configure source, target and in case swap language, from NVDA menu, go to Preferences, then go to Instant Translate Settings.
There are three combo boxes labeled "translate from", "translate into" and "Language for swapping" (if you selected auto option from source languages).

If you selected the auto option from source languages, there is also a checkbox about the auto-swap: if you activate it, then the addon tries to commute automatically from your source and target configuration to a configuration where target becomes the source language, and language selected in "Language for swapping" combo is the new target language; extremely useful if the source language of the text you want translate is the target language.

However, this is a temporary configuration, if this option has no effect (it's experimental), try to commute manually to a stable configuration, using the gesture for swapping described below.

## How to use this add-on ##
There are two ways of using this add-on:

1. Select some text using selection commands (shift with arrow keys, for example). Then press Shift+NVDA+T to translate the selected text. Then the translated string will be read, providing that the synthesizer you are using supports the target language.
2. Copy some text to clipboard. Then press Shift+NVDA+Y to translate the text in the clipboard to the target language.

## Other useful commands ##
* NVDA+shift+r: pressed once, announce current configuration; pressed twice, swap source and target languages.

## Changes for 3.0 ##
* Implemented swapping languages.
* Changed configuration format, for code style reasons.
* Removed limit on amount of text that can be translated.
* Added shortcut t to the Instant Translate Settings menu item
* The auto option is now in first position in source combo, and absent in target combo.
* Added a checkbox for configuring copying translation results.
* Store config file in the root of settings folder.
* New languages: Aragonese, Arabic, Brazilian Portuguese, Croatian, Dutch, Finnish, French, Galician, German, Hungarian, Italian, Japanese, Korean, Nepali, Polish, Slovak, Slovenian, Spanish, Tamil, Turkish.

## Changes for 2.1 ##
* Now addon can translate text from clipboard when pressing nvda+shift+y. 

## Changes for 2.0 ##
* Added gui configurator where you can choose source and target languages.
* Added addon menu item found under preferences menu.
* Settings now is written in separate config file.
* Translation results now automatically copies into the clipboard for future manipulations.

## Changes for 1.0 ##
* Initial version.

[1]: http://addons.nvda-project.org/files/get.php?file=it
[2]: http://addons.nvda-project.org/files/get.php?file=it-dev
