# Sofortübersetzung #

* Autoren: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  und andere NVDA-Entwickler.
* [stabile version][1] herunterladen
* [Testversion][2] herunterladen

This add-on is used to translate selected and/or clipboard text from one
language to another.  This is done using an external service.

## Sprachen einstellen ##
To configure source, target and in case swap language, go to: NVDA Menu >> Preferences >> Instant Translate Settings.

There are two comboboxes labeled "Source language" and "Target language",
and a checkbox to decide if it must copy the translation to clipboard.

In addition, if you selected auto option (the first choice) from "Source
language" combobox, there are also a combobox labeled "Language for
swapping" and a checkbox about the auto-swap.

The meaning of two first comboboxes and checkbox for copy is clear, but some
words about the rest are necessary. Remember always that the explanations
below assume the source language set on the auto option.

The "Language for swapping" combobox is useful when you swap via script (see
below) the source and target language; in fact, a target language set on the
auto option has no sense, so the addon sets it to value of combobox above.

So, imagine this situation: you usually translate into English (your main
language), but sometimes (for example, when you write a document) you need
to translate into Italian (your second language, suppose); you can set
"Language for swapping" combobox to Italian, so you will translate from
English to Italian without accessing directly to the addon
settings. Obviously this function has a major or minor utility according to
your more frequent needs.

Now, the auto-swap checkbox: it appears if and only if you set the auto
option in "Source language" combobox, and is directly connected with
"Language for swapping" combobox. If you activate it, then the addon tries
to commute automatically from your source and target configuration to a
configuration where target becomes the source language, and language
selected in "Language for swapping" combobox is the new target language;
extremely useful if the source language of the text you want translate is
the target language.

A simple example: take again in mind the situation imagined previously; if
you translate a text in a language different from English, there is no
problem, you get the correct translation in English. But if you need to
translate a text from English, normally you get a translation into English
identical to original text, and this is a bit useless. Thanks to auto-swap
function, however, assuming that you want to know how your text sounds into
Italian, the addon commutes automatically the target language to Italian, so
it returns a valid translation.

Anyway, this is a temporary configuration; if this option has no effect
(it's experimental), try to commute manually to a stable configuration,
using the gesture for swapping described below. It's experimental because in
some situations (with short texts, tipically), Google does not recognize the
real source language correctly, and you have to swap languages manually via
script, so to force the source language to be the previous target language
(English in our example).

## verwende ##
Sie können diese Erweiterung auf zwei Arten verwenden:

1. Select some text using selection commands (shift with arrow keys, for
   example) and press associated key to translate. translation result willbe
   read with synthesizer which you are using.
2. Sie können auch den Text, welcher sich in der Zwischenablage befindet
   übersetzen lassen.

## Tastenkürzel ##
All following commands must be pressed after modifier key "NVDA+Shift+t":

* T: Markierten Text übersetzen,
* Umschalt+t: Text aus der Zwischenablage übersetzen,
* S: tausche Ausgangs- und Zielsprache,
* A: aktuelle Konfiguration ansagen,
* C: kopiere letztes Ergebnis in die Zwischenablage,
* I: die Sprache des markierten Texts ermitteln,
* H: gibt alle verfügbaren Befehle aus.

## Änderungen für 3.0 ##
* Change way how Shortcuts are used, now you can press instantTranslate
  modifier key "NVDA+Shift+t", and then single letter key to perform some
  action (see all Commands in the "Shortcuts" section).
* Sprachen vertauschen implementiert.
* Changed configuration format, now we can change instant translate settings
  if we are in readonly pane, but remember that this will work before first
  restart of NVDA.
* Removed limit on amount of text that can be translated.
* l
* The auto option is now in first position in source combo, and absent in
  target combo.
* Option hinzugefügt, um festzulegen, ob das Resultat der Übersetzung
  kopiert werden soll.
* Konfigurationsdatei wird im Einstellungsverzeichnis gespeichert.
* Ausgangs- und Zielsprache mit dem, was Google Translate derzeit vorschlägt
  synchronisiert ( 22. April 2015 ).


## Änderungen für 2.1 ##
* Die Erweiterung übersetzt nun den Text aus der Zwischenablage mittels
  nvda+y

## Änderungen für 2.0 ##
* Einstellungsdialog zur Wahl der Ein- und Ausgabesprache hinzugefügt.
* Menü für die Erweiterung im Einstellungen-Menü hinzugefügt.
* Einstellungen werden in eine separate Datei geschrieben.
* Übersetzungsergebnisse  werden nun automatisch in die Zwischenablage
  kopiert, um diese weiter verwenden zu können.

## Änderungen für 1.0 ##
* Erstveröffentlichung


[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=it

[2]: http://addons.nvda-project.org/files/get.php?file=it-dev
