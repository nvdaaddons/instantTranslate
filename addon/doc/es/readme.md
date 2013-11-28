# instantTranslate #

* Authors: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  and other nvda contributors.
* Download [version 3.0-dev][1]

Este complemento se utiliza para traducir texto seleccionado y/o del
portapapeles de un idioma a otro.  Esto se hace utilizando el servicio
Google Translate.

## Configurando idiomas ##
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

## Cómo utilizar este complemento ##
Hay dos modos de utilizar este complemento:

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
* Añadido un atajo de teclado al elemento de menú Opciones de Instant
  Translate
* The auto option is now in first position in source combo, and absent in
  target combo.
* Añadida una casilla de verificación para configurar el copiado de los
  resultados de la traducción.
* Almacenar el fichero config en la raíz de la carpeta de configuraciones.
* Nuevos idiomas: Alemán, Coreano, Eslovaco, Español, Francés, Finlandés,
  Gallego, Húngaro, Italiano, Tamil, Turco.

## Cambios para 2.1 ##
* Ahora el complemento puede traducir texto desde el portapapeles cuando se
  presione NVDA+shift+y.

## Cambios para 2.0 ##
* Añadida una GUI para el configurador donde  puedes elegir los idiomas
  fuente y destino.
* Añadido un elemento de menú al complemento que se encuentra bajo el menú
  preferencias.
* Las configuraciones ahora se escriben en un fichero config separado.
* Los resultados de la traducción se copian ahora automáticamente en el
  portapapeles para manipulaciones futuras.

## Cambios para 1.0 ##
* Versión Inicial.

[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=it-dev
