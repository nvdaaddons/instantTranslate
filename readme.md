[[!meta title="instantTranslate"]]

* authors: Alexy Sadovoy, ruslan, Beqa Gozalishvili and other nvda contributors.
* download [version 2.2beta2][1]

This add-on is used to translate selected and/or clipboard text from one language to another.
This is done using the Google Translate service.

## Configuring languages ##

To configure source and target language, from NVDA menu, go to Preferences, then go to Instant Translate Settings.
There are two combo boxes labeled "translate from" and "translate into".
Make your language selection and press ENTER on the OK button.

## How to use this add-on ##

There are two ways of using this add-on:

1. Select some text using selection commands (shift with arrow keys, for example). Then press Shift+NvDA+T to translate the selected text. Then the translated string will be read, providing that the synthesizer you are using supports the target language.
2. Copy some text to clipboard. Then press Shift+NvDA+Y to translate the text in the clipboard to the target language.

## Changes for 2.2 ##
* Increased number of characters to 1500.
* Added shortcut t to the Instant Translate Settings menu item
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
