# instantTranslate #

* Authors: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  and other nvda contributors.
* Download [version 3.0-dev][1]

Ce module complémentaire permet de traduire le texte sélectionné et ou le
texte copié dans le presse-papiers d'une langue à une autre.  Il utilise le
service Google Traduction.

## Configurer les langues ##
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

## Comment utiliser ce module complémentaire ##
Il y a deux façons d'utiliser ce module complémentaire :

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
* Ajout du raccourci t à l'élément de menu paramètres de Instant Translate
* The auto option is now in first position in source combo, and absent in
  target combo.
* Ajout d'une case à cocher pour configurer la copie du résultat de la
  traduction.
* Sauvegarde du fichier de configuration à la racine du dossier paramètres.
* Nouvelles langues : Aragonais, Arab, Portugais Brésilien, Croate,
  Néherlandais, Finnois, Français, Galicien, Allemand, Hongrois, Italien,
  Japonais, Coréen, Népalais, Polonais, Slovaque, Slovénien, Espagnol,
  Tamoul, Turque.

## Changements pour la version 2.1 ##
* Maintenant le module peut traduire du texte depuis le presse-papier en
  pressant NVDA+maj+y.

## Changements pour la version 2.0 ##
* Ajout d'un dialogue de configuration permettant de choisir la langue
  source et la langue cible.
* Ajout d'un élément de menu pour ce module dans le menu préférences.
* Les paramètres sont maintenant stockés dans un fichier de configuration
  séparé.
* Les résultats de traduction sont maintenant automatiquement copiés dans le
  presse-papier pour des manipulations ultérieures.

## Changements pour la version 1.0 ##
* Version initiale.

[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=it-dev
