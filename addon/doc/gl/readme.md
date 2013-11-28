# instantTranslate #

* Authors: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  and other nvda contributors.
* Download [version 3.0-dev][1]

Este complemento utilízase para traducir texto seleccionado e/ou do
portapapeis dunha lingua a outra.  Esto faise utilizando o servizo de Google
Translate.

## Configurando linguas ##
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

## Como utilizar este complemento ##
Hai dúas maneiras de utilizar este complemento:

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
* Engadido un atallo de teclado para o elemento de menú Opcións de Instant
  Translate
* The auto option is now in first position in source combo, and absent in
  target combo.
* Engadida unha casiña de verificación para a configuración do copiado dos
  resultados da traducción.
* Almacenado do ficheiro config na raíz do cartafol de opcións.
* Novas linguas: Alemán, Coreano, Eslovaco, Español, Francés, Finlandés,
  Galego, Húngaro, Italiano, Tamil, Turco.

## Cambios para 2.1 ##
* Agora o complemento pode traducir texto dende o portapapeis ó premer NVDA
  + shift + y.

## Cambios para  2.0 ##
* Engadido un gui para o configurador onde podes escoller linguas fonte e
  destiño.
* Engadido un elemento de menú ó complemento  que se atopa baixo o menú de
  preferencias.
* As opcións agora escríbense nun ficheiro config separado.
* Os resultados da traducción agora cópianse automáticamente no Portapapeis
  para futuras manipulacións.

## Cambios para  1.0 ##
* Versión inicial.

[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=it-dev
