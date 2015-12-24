# Gyorsfordító #

* Készítők: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto
  Buffolino, és további NVDA közreműködők.
* Letöltés [Stabil verzió][1]
* Letöltés [Fejlesztői verzió][2]

A kiegészítő használatával egy kijelölt és/vagy vágólapra másolt szöveget
fordíthat le egyik nyelvről a másikra, a Google fordító segítségével.

## Nyelvek beállítása ##
A forrás, célnyelv, és nyelvek felcserélésére szolgáló lehetőségeket az NVDA menü->beállítások->Gyorsfordító beállításai menüpontban érheti el.

A megnyíló ablakban két kombinált listamező található a forrásnyelv és
célnyelv beállítására, ill. egy jelölőnégyzet, mellyel a fordítás vágólapra
másolását lehet szabályozni.

Amennyiben a forrásnyelvnél az automatikus nyelvfelismerését választotta ki
(a listában az első elem), megjelenik egy "Felcserélés nyelve" megnevezésű
lista amellyel a nyelv felcserélését lehet konfigurálni, és egy az
automatikus felcserélés beállítására való jelölőnégyzet is.

Az első két kombinált listamező és a másolást szabályzó jelölőnégyzet
működése egyértelmű, viszont a többi beállítás bővebb magyarázatra
szorul. Fontos, hogy az alábbiak csak akkor érvényesek, ha a forrás nyelve
automatikusra van állítva.

A "Felcserélés nyelve" funkció abban az esetben hasznos, ha a forrás és cél
nyelv váltását automatikusan szeretné megoldani. Mivel az automatikus
felismerésnek a cél nyelv esetén nincs értelme, így ez ebben a listában nem
jelenik meg.

Képzelje el a következő szituációt: Minden szöveget magyar nyelvre szeretne
lefordítani, de olykor a magyarul begépelt szövegnek szeretné megnézni az
angol fordítását is. Amennyiben a felcserélés nyelvét angolra állítja, úgy a
két nyelv közötti fordítás automatikusan megtörténik, anélkül hogy megnyitná
a kiegészítő párbeszédablakát.

Ha a forrás nyelvnél az automatikus felismerés van kiválasztva, megjelenik
egy jelölőnégyzet az automatikus forrás és célnyelv felcseréléséről. Ha
aktiválja ezt, a kiegészítő megpróbálja automatikusan váltogatni a forrás és
a célnyelvet. Ekkor a forrás nyelv lesz a célnyelv, és a "Felcserélés
nyelve" az új forrás nyelv. Ez a lehetőség akkor nagyon hasznos, hogyha a
beállított célnyelvről szeretnénk egy szöveget lefordíttatni.

A fenti példából  kiindulva, ha bármilyen szöveget lefordít magyarra, az
eredmény magyar nyelvű lesz. A felcserélés nyelve funkció használata nélkül
ha egy magyar szöveget ad meg a programnak, ugyanazt a szöveget kapja
vissza, aminek nincs túl sok értelme. Az automatikus felcserélésnek
köszönhetően a kiegészítő felismeri, hogy az éppen kijelölt szöveget milyen
nyelvre kell lefordítania, ha a szöveg nyelve nem egyezik meg a
célnyelvével, akkor automatikusan a célnyelven adja vissza.

Ez egy kísérleti funkció, így főképp rövid szövegeknél a Google nem ismeri
fel a megadott forrás nyelvét, ekkor a fentebb taglalt funkció nem működik
megfelelően.

## Használat ##
Kétféle módon is használható ez a kiegészítő:

1. Jelölje ki a lefordítandó szöveget a kijelölési parancsokkal
   (pl. Shift+nyilak), majd nyomja meg a fordításhoz szükséges
   billentyűparancsot. A lefordított szöveg egy kis idő elteltével elhangzik
   a cél nyelven (feltéve ha a használatban lévő beszédszintetizátor
   támogatja azt).
2. A kiegészítő képes a vágólapon lévő szöveg lefordítására is.

## Billentyűparancsok ##
Az alábbi parancsok az "NVDA+Shift+t" módosító billentyűparancs lenyomása
után használhatók:

* T: Lefordítja a kijelölt szöveget,
* Shift+t: Lefordítja a vágólapon található szöveget,
* S: Felcseréli a forrás- és a célnyelvet.
* A: Bemondja az aktuális beállításokat,
* C: Az utolsó fordítás eredményét a vágólapra másolja,
* I: Felismeri a kijelölt szöveg nyelvét,
* H: Bemondja az összes rendelkezésre álló felhasználói parancsot.

## A 3.0 verzió változásai ##
* Megváltoztatásra került a billentyűparancsok felépítése, az NVDA+shift+t
  megnyomása után az egykarakteres gyorsbillentyűt lenyomva aktiválható a
  kiválasztott funkció. Bővebb információk a {"Billentyűparancsok"
  fejezetben} olvashatók.
* Beépítették a nyelvek felcserélése funkciót.
* A beállítás módjának megváltoztatása, így módosíthatóak a Gyorsfordító
  beállításai egy csak olvasható eszközön is, de ezek csak az NVDA
  újraindításáig maradnak életben.
* A lefordítható szöveg mennyisége korlátozásának megszüntetése.
* Gyorsbillentyű hozzáadása a Gyorsfordító menüjének eléréséhez.
* Az automatikus felismerés a legelső a forrásnyelv listában, a célnyelvéből
  pedig hiányzik.
* Egy jelölőnégyzet hozzáadása a fordítás eredményének konfigurálásához.
* A konfigurációs fájl a beállítások főmappájában található.
* A forrás és célnyelv már a Google-nek megfelelő formátumban kerül
  elküldésre (2015 április22)


## A 2.1 verzió változásai ##
* Mostantól a kiegészítő képes a vágólapon lévő szöveg lefordítására is az
  nvda+shift+y billentyűparanccsal.

## A 2.0 verzió változásai ##
* Grafikus ablak hozzáadása, ahol kiválasztható a forrás és a célnyelv.
* A kiegészítő menüjének hozzáadása a beállítások menühöz.
* A beállítások mostantól egy elkülönített konfigurációs fájlba íródnak.
* A fordítás eredménye automatikusan a vágólapra kerül, így később ez
  könnyen használható.

## Az 1.0 verzió változásai ##
* Első változat


[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=it

[2]: http://addons.nvda-project.org/files/get.php?file=it-dev
