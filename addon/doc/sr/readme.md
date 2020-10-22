# instantTranslate #

* Autori: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  i drugi NVDA saradnici.
* Preuzmi[stabilnu verziju][1]
* Preuzmi[razvojnu verziju][2]

Ovaj dodatak se koristi za prevođenje izabranog teksta ili teksta iz
privremene memorije sa jednog jezika na drugi. Za ovo se koristi servis

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

Uglavnom, ovo je privremeno podešavanje; ako ne radi(eksperimentalna je),
pokušajte ručno da se vratite na ispravna podešavanja, koristeći komandu za
menjanje koja je opisana ispod. Eksperimentalna je zato što u nekim
situacijama(sa kratkim tekstovima, obično), Google ne prepoznaje izvorni
jezik ispravno, i morate zameniti jezike ručno pomoću skripte, kako biste
naterali izvorni jezik da bude prethodni jezik za prevođenje(Engleski u
našem primeru).

## Korišćenje ##
Možete koristiti ovaj dodatak na dva načina:

1. Izaberite tekst koristeći komande za izbor(šift sa strelicama, na primer)
   i koristite komandu za prevod. Prevod će biti pročitan sa sintetizatorom
   kojeg koristite.
2. Takođe možete prevesti tekst iz privremene memorije.

## Prečice ##
Sve komande u nastavku se moraju pritisnuti nakon modifikatorskog
tastera"NVDA+Šift+t":

* T: Prevedi izabran tekst,
* Šift+T: Prevedi tekst privremene memorije,
* S: Zameni izvorni jezik i jezik za prevođenje,
* A: Izgovori trenutna podešavanja,
* C: Kopiraj poslednji rezultat u privremenu memoriju
* I: Prepoznaj jezik izabranog teksta
* H: Izgovara sve dostupne komande

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

[1]: https://addons.nvda-project.org/files/get.php?file=it

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
