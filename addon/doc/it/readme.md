# instantTranslate #

* Autori: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  e altri collaboratori per NVDA.
* Download [versione stabile][1]
* Download [versione in sviluppo][2]

Questo componente aggiuntivo viene utilizzato per tradurre del testo
selezionato oppure presente negli appunti da una lingua ad un'altra. il
servizio è reso possibile utilizzando la piattaforma di  Google Translate.

## Configurazione delle lingue ##
Per configurare la lingua di origine, di destinazione e, nel caso, di scambio, andare in: menu di NVDA >> Preferenze >> Instant Translate - Impostazioni.

Ci sono due caselle combinate chiamate "Lingua di origine" e "Lingua di
destinazione", e una casella di controllo per decidere se copiare la
traduzione negli appunti.

Inoltre, se si è selezionata l'opzione automatica (la prima scelta) dalla
casella combinata "Lingua di origine", ci sono anche una casella di
controllo chiamata "Lingua di scambio" e un'altra sullo scambio automatico.

Il significato delle prime due caselle combinate e di quella di controllo
per la copia è chiaro, ma qualche parola sul resto è necessaria. Ricordarsi
sempre che le spiegazioni seguenti assumono la lingua di origine impostata
su automatica.

La casella combinata "Lingua di scambio" è utile quando si scambiano la
lingua di origine e di destinazione via script (vedere sotto); infatti, una
lingua di destinazione impostata sull'opzione automatica non ha senso,
perciò l'addon la imposta col valore della casella combinata suddetta.

Si immagini questa situazione: you usually translate into English (your main
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

## Utilizzo ##
Questo componente aggiuntivo può essere usato in due modi:

1. Selezionare una parte di testo utilizzando i comandi di selezione (ad
   esempio Tasto Shift con i tasti freccia) e premere il relativo tasto per
   tradurre. Il risultato della traduzione verrà letto con il sintetizzatore
   che si sta utilizzando.
2. Si può anche tradurre testo dagli appunti.

## Combinazioni di tasti ##
Tutti i comandi seguenti devono essere premuti dopo il tasto modificatore
"NVDA+Shift+t":

* T: traduce il testo selezionato,
* Shift+t: traduce il testo dagli appunti,
* S: scambia la lingua di origine e di destinazione,
* A: annuncia l'attuale configurazione,
* C: copia l'ultimo risultato negli appunti,
* I: identifica la lingua del testo selezionato,
* H: annuncia tutti i comandi disponibili all'utente.

## Modifiche nella versione 3.0 ##
* Cambiato l'uso delle combinazioni di tasti, ora si può premere il tasto
  Instant Translate "NVDA+Shift+t", e poi lettere singole per eseguire una
  azione (vedere tutti i comandi nella sezione "Combinazioni di tasti").
* Implementato lo scambio lingue
* Cambiato il formato di configurazione, ora è possibile cambiare le
  impostazioni di InstantTranslate se ci si trova in un pannello in sola
  lettura, ma ricordarsi che questo funzionerà prima del primo riavvio di
  NVDA.
* Rimossi i limiti sulla quantità di testo che si poteva tradurre.
* Aggiunto il tasto rapido t al menu impostazioni per Instant Translate.
* L'opzione auto è ora in prima posizione nella casella combinata lingua
  d'origine, e assente in quella di destinazione.
* Aggiunta una casella di controllo per configurare la copia dei risultati
  di traduzione.
* Salvataggio del file di configurazione nella cartella radice delle
  impostazioni.
* Source and target languages syncronized with what Google Translate
  currently exposes (22 Apr 2015).


## Modifiche nella versione 2.1 ##
* Ora il componente aggiuntivo può tradurre il testo dagli appunti mediante
  la pressione della combinazione NVDA+shift+y.

## Modifiche nella versione 2.0 ##
* Aggiunta un'interfaccia grafica di configurazione da dove poter
  selezionare la lingua di origine e la lingua di destinazione.
* Aggiunto il menu del componente aggiuntivo sotto al menu preferenze.
* Le impostazioni ora vengono salvate in un file separato di configurazione.
* I risultati di traduzione ora vengono copiati automaticamente negli
  appunti per manipolazioni future.

## Modifiche nella versione 1.0 ##
* Versione Iniziale.

[1]: http://addons.nvda-project.org/files/get.php?file=it [2]:
http://addons.nvda-project.org/files/get.php?file=it-dev


[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=it

[2]: http://addons.nvda-project.org/files/get.php?file=it-dev
