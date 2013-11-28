# instantTranslate #

* Authors: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  and other nvda contributors.
* Download [version 3.0-dev][1]

Это дополнение используется для перевода выбранного текста и текста из
буфера обмена с одного языка на другой. Это делается с помощью службы Google
Translate.

## Настройка языков ##
To configure source, target and in case swap language, from NVDA menu, go to
Preferences, then go to Instant Translate Settings.  There are three combo
boxes labeled "translate from", "translate into" and "Language for swapping"
(if you selected auto option from source languages).

If you selected the auto option from source languages, there is also a
checkbox about the auto-swap: if you activate it, then the addon tries to
commute automatically from your source and target configuration to a
configuration where target becomes the source language, and language
selected in "Language for swapping" combo is the new target language;
extremely useful if the source language of the text you want translate is
the target language.

However, this is a temporary configuration, if this option has no effect
(it's experimental), try to commute manually to a stable configuration,
using the gesture for swapping described below.

## Как использовать это дополнение ##
Есть два способа использования этого дополнения:

1. Select some text using selection commands (shift with arrow keys, for
   example). Then press Shift+NVDA+T to translate the selected text. Then
   the translated string will be read, providing that the synthesizer you
   are using supports the target language.
2. Copy some text to clipboard. Then press Shift+NVDA+Y to translate the
   text in the clipboard to the target language.

## Other useful commands ##
* NVDA+shift+r: pressed once, announce current configuration; pressed twice,
  swap source and target languages.

## Changes for 3.0 ##
* Implemented swapping languages.
* Changed configuration format, now we can change instant translate settings
  if we are in readonly pane, but remember that this will work before first
  restart of nvda.
* Removed limit on amount of text that can be translated.
* Добавлена клавиша быстрого доступа t к  пункту меню настроек Instant
  Translate
* The auto option is now in first position in source combo, and absent in
  target combo.
* Добавлен флажок для настройки результата копирования перевода.
* Файл конфигурации хранится в корневой папке пользовательских настроек.
* Новые языки: арагонский, арабский, бразильский португальский, хорватский,
  голландский, финский, французский, галисийский, немецкий, венгерский,
  итальянский, японский, корейский, непальский, польский, словацкий,
  словенский, испанский, тамильский, турецкий.

## Изменения  в версии 2.1 ##
* Теперь дополнение переводит текст из буфера обмена при нажатии
  NVDA+Shift+Y.

## Изменения  в версии 2.0 ##
* Добавлен диалог для выбора исходного и целевого языков.
* Добавлен пункт меню дополнения, находящийся в меню параметров.
* Настройки теперь сохраняются в отдельный конфигурационный файл.
* Результат перевода теперь автоматически копируется в буфер обмена для
  последующих манипуляций.

## Изменения в версии 1.0 ##
* Начальная версия.

[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=it-dev
