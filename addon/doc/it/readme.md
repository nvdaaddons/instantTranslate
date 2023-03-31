# instantTranslate #

* Autori: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  e altri collaboratori per NVDA.
* Download [versione stabile][1]
* Download [versione in sviluppo][2]

This add-on is used to translate selected and/or clipboard text from one
language to another.  This is done using the Google Translate service.

## Configurazione delle lingue ##
Per configurare la lingua di origine, di destinazione e, nel caso, di scambio, andare in: menu di NVDA >> Preferenze >> Impostazioni di Instant Translate.

Ci sono due caselle combinate chiamate "Lingua di origine" e "Lingua di
destinazione", e una casella di controllo per decidere se copiare la
traduzione negli appunti.

Inoltre, se avete selezionato l'opzione "automatica" (la prima scelta) dalla
casella combinata "Lingua di origine", ci saranno anche una casella di
controllo chiamata "Lingua di scambio" e un'altra sullo scambio automatico.

Il significato delle prime due caselle combinate e di quella di controllo
per la copia è chiaro, ma qualche parola sul resto è necessaria. Ricordatevi
sempre che le seguenti spiegazioni assumono che la lingua di origine sia
impostata su automatica.

La casella combinata "Lingua di scambio" è utile quando si scambiano la
lingua di origine e di destinazione via script (vedere sotto); infatti, una
lingua di destinazione impostata sull'opzione "automatica" non ha senso,
perciò l'add-on la imposta col valore della casella combinata suddetta.

Immaginate questa situazione: siete soliti tradurre in italiano (la vostra
lingua principale), ma a volte (scrivendo un documento, ad esempio) avete
bisogno di tradurre in inglese (la vostra seconda lingua, supponiamo);
potete impostare la "Lingua di scambio" su inglese, così tradurrete da
italiano a inglese senza accedere direttamente alle impostazioni
dell'add-on. Ovviamente questa funzionalità ha una maggiore o minore utilità
a seconda delle vostre necessità più frequenti.

Ora, la casella di controllo per l'auto-scambio: questa appare se e solo se
si imposta l'opzione "automatica" nella casella combinata "Lingua di
origine", ed è direttamente collegata alla casella combinata "Lingua di
scambio". Se si attiva, allora l'add-on prova a commutare automaticamente
dalla configurazione d'origine e destinazione a una configurazione dove la
lingua di destinazione diventa quella d'origine, e la lingua selezionata in
"Lingua di scambio" è la nuova lingua di destinazione; estremamente utile se
la lingua d'origine del testo che si vuole tradurre è la lingua di
destinazione.

Un semplice esempio: tenete di nuovo a mente la situazione immaginata in
precedenza; se traducete un testo in una lingua diversa dall'italiano, non
ci sono problemi: ottenete la corretta traduzione in italiano. Ma se avete
bisogno di tradurre un testo dall'italiano, normalmente otterrete una
traduzione in italiano identica al testo originale, il che è abbastanza
inutile. Grazie alla funzione di auto-scambio, invece, assumendo vogliate
sapere come suona un testo in inglese, il componente aggiuntivo commuta
automaticamente la lingua di destinazione a inglese, così da restituire una
traduzione valida.

Anyway, this is a temporary configuration; if this option has no effect
(it's experimental), try to commute manually to a stable configuration,
using the gesture for swapping described below. It's experimental because in
some situations (with short texts, typically), Google does not recognize the
real source language correctly, and you have to swap languages manually via
script, so to force the source language to be the previous target language
(English in our example).

At least, in the speech settings parameters dialog (NVDA Menu >> Preferences >> Speech), you may want to check the "Automatic language switching (when supported)" option. This way, if you are using a multi-lingual synthesizer, the translation will be announced using the target language voice of the synthesizer.

## Utilizzo ##
You can use this add-on in three ways:

1. Select some text using selection commands (shift with arrow keys, for
   example) and press associated key to translate. translation result will
   be read with synthesizer which you are using.
2. Potete anche tradurre testo dagli appunti.
3. Press the dedicated shortcut key to translate the last spoken text.

## Combinazioni di tasti ##
Tutti i comandi seguenti devono essere premuti dopo il tasto modificatore
"NVDA+Shift+t":

* T: traduce il testo selezionato,
* Shift+t: traduce il testo dagli appunti,
* S: scambia la lingua di origine e di destinazione,
* A: annuncia l'attuale configurazione,
* C: copia l'ultimo risultato negli appunti,
* I: identifica la lingua del testo selezionato,
* L: translate the last spoken text,
* O: open translation settings dialog
* H: announces all available layered commands.

## Changes for 4.4.3 ##
* Added the ability to replace underscores with spaces, may provide better
  translation results depending on context (thanks to Beka Gozalishvili)
* Added compatibility for NVDA 2022.1

## Changes for 4.4.2 ##
* Restore language detection and auto-swapping (Thanks to Cyrille for fix)
* updated languages for translation (thanks to Cyrille)

## Changes for 4.4 ##
* Instant translate is now compatible with NVDA 2019.3 (Python 3 versions of
  NVDA)

## Changes for 4.3 ##
* nvda compatibility fix Now instant translate will be compatible with
  latest nvda builds.
* found a way to use google as a translation service again.

## Changes for 4.2 ##
* Restored working state with newer versions of nvda.
* Restored automatic language detection.

## Novità nella versione 4.1 ##
* Instant Translate funziona di nuovo, ora con il servizio fornito da Yandex
  invece di Google.

## Novità nella versione 4.0 ##
* Le traduzioni vengono effettuate automaticamente dopo lo scambio lingue.
* Risolto un bug sulla cache.

## Novità nella versione 3.0 ##
* Cambiato l'uso delle combinazioni di tasti; ora si può premere il tasto
  Instant Translate "NVDA+Shift+t", e poi lettere singole per eseguire una
  azione (vedere tutti i comandi nella sezione "Combinazioni di tasti").
* Implementato lo scambio lingue.
* Cambiato il formato di configurazione; ora è possibile cambiare le
  impostazioni di Instant Translate se ci si trova in un pannello in sola
  lettura, ma ricordarsi che questo funzionerà prima del primo riavvio di
  NVDA.
* Rimossi i limiti sulla quantità di testo che si poteva tradurre.
* Aggiunto il tasto rapido t alla voce impostazioni del menu di Instant
  Translate
* L'opzione auto è ora in prima posizione nella casella combinata lingua
  d'origine, e assente in quella di destinazione.
* Aggiunta una casella di controllo per configurare la copia dei risultati
  di traduzione.
* Salvataggio del file di configurazione nella cartella radice delle
  impostazioni.
* Lingue di origine e destinazione sincronizzate con quelle messe a
  disposizione attualmente da Google Translate (22 Apr 2015).


## Novità nella versione 2.1 ##
* Ora l'add-on può tradurre il testo dagli appunti quando si preme
  NVDA+shift+y.

## Novità nella versione 2.0 ##
* Aggiunta un'interfaccia grafica di configurazione da dove poter
  selezionare la lingua di origine e la lingua di destinazione.
* Aggiunto il menu dell'add-on sotto al menu preferenze.
* Le impostazioni ora vengono salvate in un file separato di configurazione.
* I risultati di traduzione ora vengono copiati automaticamente negli
  appunti per manipolazioni future.

## Novità nella versione 1.0 ##
* Versione Iniziale.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=instantTranslate

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
