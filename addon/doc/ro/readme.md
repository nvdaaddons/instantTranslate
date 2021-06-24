# instantTranslate #

* Autori: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  și alți contribuitori NVDA.
* Descărcați [versiunea stabilă][1]
* Descărcați [versiunea în dezvoltare][2]

Acest supliment este folosit pentru a traduce un text selectat dintr-o limbă
în alta.  Acesta utilizează un serviciu extern.

## Configurarea limbilor ##
Pentru a configura limba sursă, cea aleasă și cea pentru schimbare, mergeți la: Meniul NVDA, Preferințe, Setări Instant Translate.

Acolo sunt două casete combinate etichetate „limba sursă” și „limba aleasă”
și o casetă de bifat pentru a decide dacă traducerea trebuie să fie copiată
pe planșetă.

În plus, dacă ați selectat opțiunea automată (prima alegere) din caseta
combinată "Limba sursă", există, de asemenea, o casetă combinată etichetată
"Limba de schimbare" și o casetă de bifat cu privire la auto-schimbare.

Semnificația primelor două casete combinate și caseta pentru copiere este
clară, dar unele cuvinte despre restul sunt necesare. Amintiți-vă
întotdeauna că explicațiile de mai jos își asumă limba sursă setată pe
opțiunea automată.

Caseta combinată „limba de schimbare” atunci când o modificați prin script
(vedeți mai jos) limba sursă și cea aleasă; de fapt, limba aleasă setată la
opțiunea auto nu are nici un sens, deci add-on-ul o setează la valoarea
casetei combinate de mai sus.

Așadar, imaginați-vă această situație: De obicei, traduceți în Engleză
(limba dumneavoastră principală), dar câteodată (de exemplu, când scrieți un
document) aveți nevoie să-l traduceți în italiană (limba dumneavoastră
secundară; puteți seta caseta combinată „limba pentru schimbare” la
italiană, deci veți traduce din engleză în italiană fără a accesa în mod
direct setările add-on-ului. Evident că această funcție are o utilitate
minoră sau majoră în funcție de nevoile dumneavoastră mai frecvente.

Acum, caseta de bifat auto-schimbare: Apare dacă și numai dacă setați
opțiunea auto în caseta combinată „limba sursă” și este conectată în mod
direct cu combobox-ul „limba pentru schimbare”. Dacă o activați, add-onul
încearcă să comute automat de la configurația sursă și cea aleasă la o
configurație unde limba aleasă devine limbă sursă și limba selectată în
combobox-ul „limba pentru schimbare” este noua limbă aleasă; în mod extrem,
este utilă dacă limba sursă a textului pe care vreți să-l traduceți este
limba aleasă.

Un exemplu simplu: Luați din nou în considerare situația imaginată mai
devreme; dacă traduceți un text în altă limbă decât engleza, nu există o
problemă, obțineți traducerea corectă în engleză, dar dacă aveți nevoie să
traduceți un text din engleză, în mod normal veți obține o traducere în
engleză, identică cu textul original, acest lucru este un pic
inutil. Mulțumiri funcției auto-schimbare! Totuși,presupunând că vreți să
știți cum sună textul în italiană, add-on-ul comută automat limba aleasă la
italiană, așa că returnează o traducere validă.

Oricum, aceasta este o configurație temporară; dacă această opțiune nu are
efect (este experimentală), încercațisă comutați manual la o configurație
stabilă, folosind gestul pentru schimbarea descrisă mai jos. Este
experimentală, deoarece în unele situații (cu texte scurte, Google nu
recunoaște limba sursă reală corect, iar dumneavoastră trebuie să schimbați
limbile manual prin script.

## Utilizare ##
Puteți folosi acest add-on în două moduri:

1. Selectații un text folosind comenzi de selectare (de exemplu, shift cu
   săgețile) și apăsați tasta asociată pentru a traduce. Rezultatul
   traducerii va fi citit cu sintetizatorul pe care îl folosiți.
2. De asemenea, puteți traduce un text de pe planșetă.

## Scurtături ##
Toate comenzile afișate mai jos trebuiesc apăsate după tasta de modificare
"NVDA+Shift+t":

* T: Traduce textul selectat,
* Shift+t: Traduce textul de pe planșetă,
* S: Schimbă limba sursă și cea aleasă,
* A: Anunță configurația curentă,
* C: Copiază ultimul rezultat pe planșetă,
* I: Identifică limba textului selectat,
* H: Anunță toate comenzile disponibile pentru utilizator.

## Modificări în 4.1 ##
* InstantTranslate funcționează din nou, acum cu serviciul Yandex translator
  în loc de Google.

## Modificări în 4.0 ##
* Traducerea este efectuată automat după schimbare.
* O eroare a fost reparată.

## Modificări în 3.0 ##
* A fost schimbat modul în care sunt folosite scurtăturile, acum puteți
  apăsa tasta de modificare instantTranslate "NVDA+Shift+t", apoi o singură
  literă pentru a efectua o acțiune (vedeți toate comenzile în secțiunea
  „Scurtături”.
* A fost implementată schimbarea limbilor.
* A fost schimbat formatul configurației, acum putem modifica setările de
  traducere dacă suntem în panoul doar citire, dar amintiți-vă că aceasta va
  funcționa înainte de prima repornire a NVDA-ului.
* A fost eliminată de cantitate a textului bare poate fi tradus.
* A fost adăugată o scurtătură t pentru elementul Setări Instant Translate.
* Opțiunea auto este acum în prima poziție în caseta sursă și absentă în
  caseta limbii alese.
* A fost adăugată o casetă de bifat pentru configurarea copierii
  rezultatelor traducerilor.
* Fișierul de configurare se păstrează în rădăcina dosarului  cu setări.
* Limba sursă și cea aleasă sunt sincronizate cu ceea ce expune Google
  Translate în prezent.


## Modificări în 2.1 ##
* Acum add-on-ul poate traduce textul de pe planșetă la apăsarea
  nvda+shift+y.

## Modificări în 2.0 ##
* A fost adăugat configuratorul gui de unde puteți alege limba sursă și
  limba aleasă.
* A fost adăugată opțiunea add-on-ului găsită în meniul Preferințe.
* Setările sunt acum scrise într-un fișier separat de configurare.
* Rezultatele traducerilor sunt copiate automat pe planșetă pentru
  manipulările viitoare.

## Modificări în 1.0 ##
* Versiunea inițială.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=it

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
