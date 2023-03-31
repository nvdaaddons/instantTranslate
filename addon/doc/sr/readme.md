# instantTranslate #

* Autori: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  i drugi NVDA saradnici.
* Preuzmi[stabilnu verziju][1]
* Preuzmi[razvojnu verziju][2]

This add-on is used to translate selected and/or clipboard text from one
language to another.  This is done using the Google Translate service.

## Podešavanje jezika ##
Da podesite izvorni, jezik za prevođenje i za zamenu, uđite u: NVDA meni>> podešavanja>> Instant Translate podešavanja.

Tu ćete pronaći dva izborna okvira sa nazivima"Izvorni jezik" i"Jezik za
prevođenje", kao i izborno polje koje odlučuje da li prevod treba kopirati u
privremenu memoriju.

Takođe, ako ste izabrali automatsku opciju(prvi izbor) iz"izvorni jezik"
izbornog polja, takođe ćete pronaći izborni okvir "jezik za zamenu" i
izborno polje o automatskoj zameni.

Značenja prva dva okvira i izbornog polja za kopiranje su jasna, ali
objašnjenje za ostatak je potrebno. Zapamtite da ovo objašnjenje zahteva da
je izvorni jezik podešen na automatski.

"Jezik za zamenu" je koristan kada menjate uz pomoć skripte(pogledajte
ispod) izvorni i jezik za prevođenje; Zapravo, Jezik za prevođenje podešen
na automatski nema smisla, tako da ga dodatak podešava na opciju koja je
podešena u ovom izbornom okviru.

Tako da, zamislite ovu situaciju: Obično prevodite na Engleski(vaš jezik),
ali ponekad(na primer, kada pišete dokument) morate prevoditi na
Italijanski(vaš drugi jezik, ); Možete podesiti"jezik za zamenu" na
Italijanski, kako biste mogli da prevodite sa Engleskog na Italijanski bez
pristupa dijalogu za podešavanje dodatka. Naravno ova funkcija može biti
više ili manje bitna u zavisnosti od vašeg korišćenja.

Sada, izborno polje za automatsku zamenu: Pojavljuje se ako i samo ako
podesite opciju"izvorni jezik" na automatski, i povezana je sa opcijom"Jezik
za zamenu". Ako je aktivirate, dodatak automatski pokušava da jezik koji
otkrije učini jezikom na koji prevodite, i jezik koji je izabran u
opciji"jezik za zamenu" je novi jezik za prevođenje; Veoma korisno ako je
jezik teksta koji prevodite jezik za prevođenje.

Jednostavan primer: Ponovo zamislite prethodnu situaciju; Ako prevodite
tekst na jezik koji nije Engleski, nema problema, dobijate tačan prevod na
Engleskom. Ali ako morate da prevodite tekst sa Engleskog, obično dobijate
prevod koji je isti kao i originalan tekst, i ovo je
beskorisno. Zahvaljujući opciji automatske zamene, međutim, ukoliko želite
da znate kako vaš tekst zvuči na Italijanskom, dodatak automatski prebacuje
jezik za prevođenje na Italijanski, pa daje ispravan prevod.

Anyway, this is a temporary configuration; if this option has no effect
(it's experimental), try to commute manually to a stable configuration,
using the gesture for swapping described below. It's experimental because in
some situations (with short texts, typically), Google does not recognize the
real source language correctly, and you have to swap languages manually via
script, so to force the source language to be the previous target language
(English in our example).

At least, in the speech settings parameters dialog (NVDA Menu >> Preferences >> Speech), you may want to check the "Automatic language switching (when supported)" option. This way, if you are using a multi-lingual synthesizer, the translation will be announced using the target language voice of the synthesizer.

## Korišćenje ##
You can use this add-on in three ways:

1. Select some text using selection commands (shift with arrow keys, for
   example) and press associated key to translate. translation result will
   be read with synthesizer which you are using.
2. Takođe možete prevesti tekst iz privremene memorije.
3. Press the dedicated shortcut key to translate the last spoken text.

## Prečice ##
Sve komande u nastavku se moraju pritisnuti nakon modifikatorskog
tastera"NVDA+Šift+t":

* T: Prevedi izabran tekst,
* Šift+T: Prevedi tekst privremene memorije,
* S: Zameni izvorni jezik i jezik za prevođenje,
* A: Izgovori trenutna podešavanja,
* C: Kopiraj poslednji rezultat u privremenu memoriju
* I: Prepoznaj jezik izabranog teksta
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

## Promene u 4.1 ##
* Instant translate radi ponovo, sada koristi Yandex translate umesto Google
  prevodioca kao servis

## Promene u 4.0 ##
* Prevod se automatski izvršava nakon promene
* Popravljena greška sa kešom

## Promene u 3.0 ##
* Promenjen način na koji se prečice koriste, sada možete pritisnuti instant
  translate modifikatorski taster"NVDA+Šift+t", a zatim slova za određene
  radnje(pogledajte sve komandeu delu"prečice").
* Dodata zamena jezika
* Promenjen format podešavanja, sada se mogu menjati u sistemu samo za
  čitanje, ali ovo će raditi pre prvog ponovnog pokretanja programa NVDA
* Uklonjen limit teksta koji može da se prevede
* Dodata prečica t za stavku instant translate podešavanja
* Automatska opcija je sada prva opcija, i nije dostupna u jeziku za
  prevođenje
* Dodato izborno polje za podešavanje kopiranja prevoda
* Čuvanje datoteke sa podešavanjima u config folderu
* Izvorni i jezik za prevođenje nude isto što i Google prevodioc(22 Apr
  2015).


## Promene u 2.1 ##
* Sada dodatak može da prevodi tekst privremene memorije kada pritisnete
  nvda+šift+y.

## Promene u 2.0 ##
* Dodat interfejs podešavanja gde možete menjati izvorni i jezik za
  prevođenje.
* Dodata stavka menija za podešavanja dodatka
* Podešavanja su sada u posebnoj datoteci
* Rezultati prevoda se sada kopiraju automatski

## Promene u 1.0 ##
* Prva verzija


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=instantTranslate

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
