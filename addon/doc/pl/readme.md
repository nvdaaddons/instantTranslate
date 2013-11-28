# Błyskawiczny tłumacz tekstu / instantTranslate #

* Authors: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  and other nvda contributors.
* Download [version 3.0-dev][1]

Ta wtyczka tłumaczy tekst ze schowka lub zaznaczenia z jednego języka na
drugi. W tym celu używany jest tłumacz google.

## konfigurowanie języków ##
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

## jak użyć tego dodatku? ##
Są na to dwa sposoby

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
* skrut i pozwala szybko dostać się do ustawień wtyczki z menu nvda.
* The auto option is now in first position in source combo, and absent in
  target combo.
* Dodane pole wyboru ustawiające kopiowanie do schowka wyniku tłumaczenia.
* plik konfiguracyjny trzymany jest teraz w głównym katalogu ustawień nvda.
* Nowe języki: aragoński, arabski, brazylijski portugalski, chorwacki,
  holenderski, fiński, francuski, galicyjski, niemiecki, węgierski, włoski,
  japoński, koreański, nepalski, polski, słowacki, słoweński, hiszpański,
  tamilski, turecki.

## Zmiany dla wersji 2.1 ##
* Skrót klawiszowy NVDA+shift+y tłumaczy tekst w schowku.

## zmiany dla wersji 2.0 ##
* dodano okienko, w którym możemy wybrać źródłowy i docelowy język.
* dodano pozycję dla wtyczki w menu NVDA Ustawienia.
* ustawienia zapisywane są w oddzielnym pliku konfiguracyjnym.
* wyniki tłumaczenia automatycznie kopiowane są do schowka.

## zmiany dla wersji 1.0 ##
* Wstępne wydanie.

[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=it-dev
