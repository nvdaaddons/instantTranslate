# instantTranslate #

* Autori: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  e altri collaboratori per NVDA.
* Download [versione stabile][1]
* Download [versione in sviluppo][2]

Questo add-on viene utilizzato per tradurre del testo selezionato oppure
presente negli appunti da una lingua ad un'altra. Il tutto viene realizzato
grazie all'utilizzo del servizio di  Google Translate.

## Configurazione delle lingue ##
Per configurare la lingua di origine, di destinazione e, nel caso, di scambio, andare in: menu di NVDA >> Preferenze >> Instant Translate - Impostazioni.

Ci sono due caselle combinate chiamate "Lingua di origine" e "Lingua di
destinazione", e una casella di controllo per decidere se copiare la
traduzione negli appunti.

Inoltre, se avete selezionato l'opzione automatica (la prima scelta) dalla
casella combinata "Lingua di origine", ci saranno anche una casella di
controllo chiamata "Lingua di scambio" e un'altra sullo scambio automatico.

Il significato delle prime due caselle combinate e di quella di controllo
per la copia è chiaro, ma qualche parola sul resto è necessaria. Ricordatevi
sempre che le seguenti spiegazioni assumono la lingua di origine impostata
su automatica.

La casella combinata "Lingua di scambio" è utile quando si scambiano la
lingua di origine e di destinazione via script (vedere sotto); infatti, una
lingua di destinazione impostata sull'opzione automatica non ha senso,
perciò l'add-on la imposta col valore della casella combinata suddetta.

Immaginate questa situazione: siete soliti tradurre in italiano (la vostra
lingua principale), ma a volte (scrivendo un documento, ad esempio) avete
bisogno di tradurre in inglese (la vostra seconda lingua, supponiamo);
potete impostare la "Lingua di scambio" su inglese, così tradurrete da
italiano a inglese senza accedere direttamente alle impostazioni
dell'add-on. Ovviamente questa funzionalità ha una maggiore o minore utilità
a seconda delle vostre necessità più frequenti.

Ora, la casella di controllo per l'auto-scambio: questa appare se e solo se
si è impostata l'opzione automatica nella casella combinata "Lingua di
origine", ed è direttamente collegata alla casella combinata "Lingua di
scambio". Se si attiva, allora l'add-on prova a commutare automaticamente
dalla configurazione d'origine e destinazione a una configurazione dove la
lingua di destinazione diventa quella d'origine, e la lingua selezionata in
"Lingua di scambio" è la nuova lingua di destinazione; estremamente utile se
la lingua d'origine del testo che si vuole tradurre è la lingua di
destinazione.

Un semplice esempio: tenete di nuovo a mente la situazione immaginata in
precedenza; se traducete un testo in una lingua diversa dall'italiano, non
ci sono problemi, ottenete la corretta traduzione in italiano. Ma se avete
bisogno di tradurre un testo dall'italiano, normalmente otterrete una
traduzione in italiano identica al testo originale, il che è abbastanza
inutile. Grazie alla funzione di auto-scambio, invece, assumendo vogliate
sapere come suona un testo in inglese, il componente aggiuntivo commuta
automaticamente la lingua di destinazione a inglese, così da restituire una
traduzione valida.

Comunque, questa è una configurazione temporanea; se quest'opzione non ha
effetto (è sperimentale), provate a commutare manualmente a una
configurazione stabile, usando la combinazione di tasti per lo scambio
descritta in seguito. E' sperimentale perché in alcune situazioni (con testi
brevi, tipicamente), Google non riconosce correttamente la reale lingua di
origine, e bisogna scambiare manualmente le lingue via script, così da
forzare la lingua di origine a essere la precedente lingua di destinazione
(italiano, nel nostro esempio).

## Utilizzo ##
Potete usare questo add-on in due modi:

1. Selezionate una parte di testo utilizzando i comandi di selezione (ad
   esempio Tasto Shift con i tasti freccia) e premete il relativo tasto per
   tradurre. Il risultato della traduzione verrà letto con il sintetizzatore
   che state utilizzando.
2. Potete anche tradurre testo dagli appunti.

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
* Lingue di origine e destinazione sincronizzate con quelle messe a
  disposizione attualmente da Google Translate (22 Apr 2015).


## Modifiche nella versione 2.1 ##
* Ora l'add-on può tradurre il testo dagli appunti mediante la pressione
  della combinazione NVDA+shift+y.

## Modifiche nella versione 2.0 ##
* Aggiunta un'interfaccia grafica di configurazione da dove poter
  selezionare la lingua di origine e la lingua di destinazione.
* Aggiunto il menu dell'add-on sotto al menu preferenze.
* Le impostazioni ora vengono salvate in un file separato di configurazione.
* I risultati di traduzione ora vengono copiati automaticamente negli
  appunti per manipolazioni future.

## Modifiche nella versione 1.0 ##
* Versione Iniziale.


[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=it

[2]: http://addons.nvda-project.org/files/get.php?file=it-dev
