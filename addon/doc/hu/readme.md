# Gyorsfordító #

* Authors: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  and other nvda contributors.
* Download [version 3.0-dev][1]

A kiegészítő segítségével egy kijelölt/vágólapra másolt szöveget fordíthat
le egyik nyelvről a másikra, a Google fordító segítségével.

## Nyelvek beállítása ##
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

## Hogyan használható ez a kiegészítő? ##
Kétféle módon használhatja ezt a bővítményt:

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
* Gyorsbillentyű hozzáadása a Gyorsfordító menüjének eléréséhez.
* The auto option is now in first position in source combo, and absent in
  target combo.
* Egy jelölőnégyzet hozzáadása a fordítás eredményének konfigurálásához.
* A konfig fájl a beállítások főmappájában található.
* Új nyelvek: Finn, Német, Francia, Galíciai, Kóreai, Magyar, Német, Olasz,
  Spanyoll, Szlovák, Tamil, Török.

## A 2.1 verzió változásai ##
* Mostantól a kiegészítő képes a vágólapon lévő szöveg lefordítására is az
  nvda+shift+y billentyűparanccsal.

## A 2.0 verzió változásai ##
* Grafikus ablak hozzáadása, ahol kiválasztható a forrás és a célnyelv.
* A kiegészítő menüjének hozzáadása a beállítások menühöz.
* A beállítások mostantól egy elkülönített konfig fájlba írodnak.
* A fordítás eredménye automatikusan a vágólapra kerül, így később ez
  könnyen használható.

## Az 1.0 verzió változásai ##
* Első változat

[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=it-dev
