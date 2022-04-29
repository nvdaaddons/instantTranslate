# Izravno prevođenje (instantTranslate) #

* Autori: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  i drugi NVDA suradnici.
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]

Ovaj se dodatak koristi za prevođenje odabranog teksta ili teksta iz
međuspremnika s jednog jezika na drugi. Za to se koristi usluga Google
Prevoditelj.

## Konfiguriranje jezika ##
Za podešavanje izvornog i ciljanog jezika te jezika zamjene, prijeđi na: NVDA izbornik >> Postavke >> Postavke za izravno prevođenje.

Tu se nalaze dva odabirna okvira s nazivima „Izvorni jezik” i „Jezik za
prevođenje”, kao i odabirno polje za određivanje, treba li prijevod kopirati
u međuspremnik.

Osim toga, ako je odabrana opcija za automatski odabir (prvi izbor) iz
odabirnog okvira „Izvorni jezik”, postoji i odabirni okvir pod nazivom
„Jezik za zamjenu” i odabirni okvir o automatskoj zamjeni.

Značenje prva dva odabirna okvira i odabirnog okvira za kopiranje je jasno,
ali važno je reći nekoliko riječi vezano uz ostalo. Imajte uvijek na umu da
objašnjenja pretpostavljaju izvorni jezik postavljen u opciji automatski.

Odabirni okvir s jezicima za zamjenu je koristan, kad se zamijene izvornog i
ciljnog jezika putem skripte (vidi dolje); u stvari, izvorni jezik koji je
automatski postavljen nema smisla, pa ga dodatak postavlja na vrijednost
gornjeg odabirnog okvira.

Zamislite ovu situaciju, obično prevodite na engleski, vaš glavni jezik, ali
ponekad, na primjer, kad pišete dokument, morate prevesti na talijanski,
pretpostavimo da se radi o vašem drugom jeziku; možete postaviti „Jezik za
zamjenu” na talijanski, pa ćete prevesti s engleskog na talijanski bez
izravnog pristupa postavkama dodatka.

Sada o potvrdnom okviru za automatsku zamjenu: pojavljuje se samo ako
postavite automatsku opciju u kombinaciju „Izvorni jezik” i izravno je
povezan s kombinacijom „Jezik za zamjenu”. Ako ga aktivirate, dodatak
pokušava automatski prebaciti iz vašeg izvora i usmjeriti ga na
konfiguraciju u kojoj cilj postaje izvorni jezik, a jezik odabran u jeziku
„Jezik za zamjenu” kombinira novi ciljni jezik; izuzetno korisno, ako je
izvorni jezik teksta koji želite prevesti novi ciljni jezik.

Jednostavan primjer: uzmite u obzir prethodno zamišljenu situaciju; ako
prevodite tekst na jeziku koji nije engleski, nema problema, dobivate
ispravan prijevod na engleskom. Ali ako trebate prevesti tekst s engleskog
jezika, obično ćete dobiti prijevod na engleski jezik koji je identičan
izvornom tekstu, a to je podosta beskorisno. Međutim, zahvaljujući funkciji
automatske zamjene, pretpostavljajući da želite znati kako vaš tekst zvuči
na talijanskom jeziku, dodatak automatski prebacuje ciljni jezik na
talijanski jezik i vraća valjani prijevod.

U svakom slučaju, to je privremena konfiguracija; ako ova opcija nema
nikakav učinak (to je eksperimentalno), pokušajte ručno prebaciti na
stabilnu konfiguraciju, koristeći gestu za zamjenu, koja je opisana niže
dolje. Eksperimentalno je, jer u nekim situacijama (obično kratkim
tekstovima) Google ne prepoznaje pravi izvorni jezik i morate ručno
mijenjati jezike pomoću skripte, tako da bi izvorni jezik bio prethodni
ciljni jezik (engleski u našem primjeru).

U dijaloškom okviru parametara postavki govora (NVDA izbornik >> Postavke >> Govor) provjeri opciju „Automatsko mijenjanje jezika (kada je podržano)”. Na ovaj način, ako koristiš višejezičnu govornu jedinicu, prijevod će se objavliti korištenjem glasa ciljnog jezika govorne jedinice.

## Primjena ##
Ovaj se dodatak može koristiti na tri načina:

1. Označi tekst koristeći naredbe za označavanje (na primjer šift i tipke sa
   strelicama) i pritisni odgovarajuću tipku za prijevod. Rezultat
   prevođenja će se pročitati pomoću korištene govorne jedinice.
2. Moguće je prevesti i tekst iz međuspremnika.
3. Pritisni tipku prečaca za prevođenje zadnjeg izgovorenog teksta.

## Tipkovni prečaci ##
Sve sljedeće naredbe se moraju pritisnuti nakon modifikacijske tipke
„NVDA+šift+t”:

* T: prevedi označeni tekst,
* Šift+t: prevedi tekst iz međuspremnika,
* S: zamijeni izvorni i ciljni jezik,
* A: najavi trenutačnu konfiguraciju,
* C: kopiraj zadnji rezultat u međuspremnik,
* I: identificiraj jezik odabranog teksta,
* L: prevedi zadnji izgovoreni tekst,
* O: otvori dijaloški okvir s postavkama za prijevod
* H: izgovara sve dostupne slojevne naredbe.

## Promjene u 4.4.2 ##
* Obnovljeno je automatsko otkrivanje jezika i automatsko
  zamijenjivanje. (Hvala Cyrille za ispravak)
* aktualizirani su jezici za prevođenje (hvala Cyrille)

## Promjene u 4.4 ##
* Izravno prevođenje je sada kompatibilno s NVDA 2019.3 (Python 3 verzije
  NVDA čitača)

## Promjene u 4.3 ##
* Popravak NVDA kompatibilnosti: Dodatak „Izravno prevođenje” bit će
  kompatibilan s najnovijim NVDA verzijama.
* pronađen je način za ponovno korištenje googlea kao uslugu za prevođenje.

## Promjene u 4.2 ##
* Obnovljeno je radno stanje s novijim NVDA verzijama.
* Obnovljeno je automatsko otkrivanje jezika.

## Promjene u 4.1 ##
* Izravno prevođenje opet radi, sada s Yandex uslugom za prevođenje, umjesto
  Google usluge.

## Promjene u 4.0 ##
* Prijevod se automatski izvršava nakon zamjene.
* Ispravljena greška s predmemorijom.

## Promjene u 3.0 ##
* Promijenjen je način korištenja tipkovnih prečaca. Za „Izravno prevođenje”
  sada možeš pritisnuti modifikacijsku tipku „NVDA+šift+t”, a nakon toga
  jednu tipku za izvršavanje nekih radnji (vidi sve naredbe u odjeljku
  „Tipkovni prečaci”).
* Uvedena je zamjena jezika.
* Promijenjen je format konfiguracije, sad je moguće promijeniti postavke
  izravnog prevođenja za prikaz koji je samo za čitanje, ali misli na to, da
  će to funkcionirati prije prvog ponovnog pokretanja NVDA čitača.
* Uklonjeno je ograničenje za tekst koji se može prevesti.
* Dodan je tipkovnički prečac „t” u stavku izbornika „Postavke za izravno
  prevođenje”
* Opcija za automatsku stavku se sada nalazi na prvoj mjestu u kombiniranom
  okviru izvora i nema je u kombiniranom okviru cilja.
* Dodan je potvrdni okvir za konfiguraciju kopiranja rezultata prevođenja.
* Spremanje konfiguracijske datoteke u glavnu mapu s postavkama.
* Izvorni i ciljni jezik sinkronizirani su s onim što Google prevoditelj
  trenutnačo pruža (22. travnja 2015.).


## Promjene u 2.1 ##
* Sada dodatak može prevoditi tekst iz međuspremnika kad se pritisnu tipke
  nvda+šift+y.

## Promjene u 2.0 ##
* Konfiguratoru je dadano grafičko sučelje gdje je moguće odabrati izvorni i
  ciljni jezik.
* Dodana je stavka izbornika dodatka koju možete pronaći u izborniku za
  Postavke.
* Postavke se sada zapisuju u posebnu konfiguracijsku datoteku.
* Rezultati prevođenja se sad automatski kopiraju u međuspremnik za buduću
  obradu.

## Promjene u 1.0 ##
* Prva verzija.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=it

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
