# Gyorsfordító #

* Készítők: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto
  Buffolino, és további NVDA közreműködők.
* Letöltés [Stabil verzió][1]
* Letöltés [Fejlesztői verzió][2]

This add-on is used to translate selected and/or clipboard text from one
language to another.  This is done using the Google Translate service.

## Nyelvek beállítása ##
A forrás, célnyelv, és nyelvek felcserélésére szolgáló lehetőségeket az NVDA menü->beállítások->Gyorsfordító beállításai menüpontban érheti el.

A megnyíló ablakban két kombinált listamező található a forrásnyelv és
célnyelv beállítására, ill. egy jelölőnégyzet, mellyel a fordítás vágólapra
másolását lehet elrendelni vagy tiltani.

Amennyiben a forrásnyelvnél az automatikus nyelvfelismerését választotta ki
(a listában az első elem), megjelenik egy "Felcserélés nyelve" megnevezésű
lista, amellyel a nyelv felcserélését lehet konfigurálni, és egy az
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
két nyelv közötti fordítás automatikusan megtörténik, anélkül, hogy
megnyitná a kiegészítő párbeszédablakát.

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

Anyway, this is a temporary configuration; if this option has no effect
(it's experimental), try to commute manually to a stable configuration,
using the gesture for swapping described below. It's experimental because in
some situations (with short texts, typically), Google does not recognize the
real source language correctly, and you have to swap languages manually via
script, so to force the source language to be the previous target language
(English in our example).

At least, in the speech settings parameters dialog (NVDA Menu >> Preferences >> Speech), you may want to check the "Automatic language switching (when supported)" option. This way, if you are using a multi-lingual synthesizer, the translation will be announced using the target language voice of the synthesizer.

## Használat ##
You can use this add-on in three ways:

1. Select some text using selection commands (shift with arrow keys, for
   example) and press associated key to translate. translation result will
   be read with synthesizer which you are using.
2. A kiegészítő képes a vágólapon lévő szöveg lefordítására is.
3. Press the dedicated shortcut key to translate the last spoken text.

## Billentyűparancsok ##
Az alábbi parancsok az "NVDA+Shift+t" módosító billentyűparancs lenyomása
után használhatók:

* T: Lefordítja a kijelölt szöveget,
* Shift+t: Lefordítja a vágólapon található szöveget,
* S: Felcseréli a forrás- és a célnyelvet.
* A: Bemondja az aktuális beállításokat,
* C: Az utolsó fordítás eredményét a vágólapra másolja,
* I: Felismeri a kijelölt szöveg nyelvét,
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

## A 4.1 verzió változásai ##
* A gyorsfordító újra működik, a Google szolgáltatása helyett Yandex fordító
  szolgáltatásával.

## A 4.0 verzió változásai ##
* A fordítás eredménye automatikusan a vágólapra kerül a nyelv  felcserélést
  követöen.
* A gyorsítótárazási hibát javították.

## A 3.0 verzió változásai ##
* Megváltoztatták a billentyűparancsok felépítését, az NVDA+shift+t
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


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=instantTranslate

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
