# instantTranslate #

* autori: Alexy Sadovoy, ruslan, Beqa Gozalishvili e altri collaboratori di
  NVDA.
* download [version 2.2beta2][1]

Questo componente aggiuntivo viene utilizzato per tradurre del testo
selezionato oppure presente negli appunti da una lingua ad un'altra. il
servizio è reso possibile utilizzando la piattaforma di  Google Translate.

## Configurazione delle lingue ##

Per configurare la lingua di origine e di destinazione, dal menu di NVDA,
andare in Preferenze, poi su Impostazioni Instant Translate. Ci sono due
caselle combinate etichettate lingua di origine e lingua di
destinazione. Effettuare la selezione desiderata dopodichè premere invio sul
pulsante OK.

## Come utilizzare questo componente aggiuntivo. ##

Vi sono due modi per utilizzare questo componente aggiuntivo:

1. Selezionare una parte di testo utilizzando i comandi di selezione (ad
   esempio Tasto Shift con i tasti freccia). Quindi, premere Shift + NVDA +
   T per tradurre il testo selezionato. La stringa tradotta verrà letta, a
   condizione che il sintetizzatore utilizzato supporti la lingua di
   destinazione.
2. Copiare del testo negli appunti. Quindi, premere Shift + NVDA + Y per
   tradurre il testo appena copiato nella lingua di destinazione.

## Modifiche nella versione 2.2 ##
* Increased number of characters to 1500.
* Added shortcut t to the Instant Translate Settings menu item
* Added a checkbox for configuring copying translation results.
* Store config file in the root of settings folder.
* New languages: Aragonese, Arabic, Brazilian Portuguese, Croatian, Dutch,
  Finnish, French, Galician, German, Hungarian, Italian, Japanese, Korean,
  Nepali, Polish, Slovak, Slovenian, Spanish, Tamil, Turkish.

## Changes for 2.1 ##
* Now addon can translate text from clipboard when pressing nvda+shift+y.

## Changes for 2.0 ##
* Added gui configurator where you can choose source and target languages.
* Added addon menu item found under preferences menu.
* Settings now is written in separate config file.
* Translation results now automatically copies into the clipboard for future
  manipulations.

## Changes for 1.0 ##
* Initial version.

[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=it
