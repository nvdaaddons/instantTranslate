# Rýchly prekladač #

* Autori: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  a ďalší.
* Stiahnuť [stabilnú verziu][1]
* Stiahnuť [Vývojovú verziu][2]

This add-on is used to translate selected and/or clipboard text from one
language to another.  This is done using the Google Translate service.

## nastavenie jazykov ##
Zdrojový a cieľový jazyk a otáčanie jazykov nastavíte v menu nvda > nastavenia > Rýchly prekladač.

Sú tu dva zoznamy označené ako "zdrojový jazyk", "Cieľový jazyk" a
začiarkávacie políčko, ktoré určuje, či sa bude preložený text automaticky
kopírovať do schránky.

Ak zvolíte ako zdrojový jazyk možnosť automaticky, pribudne v dialógu
možnosť nastaviť jazyk pre automatické otáčanie a začiarkávacie políčko,
ktorého začiarknutím zaistíte automatické otáčanie.

Nastavenie zdrojového a cieľového jazyka je jasné. Preto si vysvetlíme
ostatné nastavenia. Budeme predpokladať, že sme ako zdrojový jazyk zvolili
možnosť automaticky.

Jazyk, ktorý zvolíte v zozname "Sekundárny jazyk" sa použije, ak otočíte
jazyky pomocou klávesovej skratky (popíšeme neskôr). Ak dáte preložiť text z
rovnakého jazyka, ako je zdrojový jazyk, doplnok bude predpokladať, že ako
zdrojový jazyk má použiť práve tento sekundárny jazyk.

Predpokladajme, že zvyčajne prekladáte do angličtiny. Niekedy ale chcete
preložiť anglický text do taliančiny. Preto si nastavíte "sekundárny jazyk"
na taliančinu.

Ak ste ako zdrojový jazyk vybrali možnosť automatická detekcia, môžete stále
začiarknuť možnosť automatické otáčanie: ak ju začiarknete, doplnok sa
pokúsi zistiť z akého do akého jazyka má prekladať, pričom bude vychádzať z
jazyka, ktorý nastavíte v zozname "sekundárny jazyk". Toto je užitočné, ak
prekladáte do nejakého jazyka a niekedy naopak potrebujete prekladať z tohto
jazyka do iného jazyka.

Ak napríklad prekladáte text z iného ako anglického jazyka, dostanete
preklad do angličtiny. Ak ale zadáte na preloženie text v angličtine,
doplnok rozpozná jazyk a automaticky bude prekladať do taliančiny.

Anyway, this is a temporary configuration; if this option has no effect
(it's experimental), try to commute manually to a stable configuration,
using the gesture for swapping described below. It's experimental because in
some situations (with short texts, typically), Google does not recognize the
real source language correctly, and you have to swap languages manually via
script, so to force the source language to be the previous target language
(English in our example).

At least, in the speech settings parameters dialog (NVDA Menu >> Preferences >> Speech), you may want to check the "Automatic language switching (when supported)" option. This way, if you are using a multi-lingual synthesizer, the translation will be announced using the target language voice of the synthesizer.

## Použitie ##
You can use this add-on in three ways:

1. Select some text using selection commands (shift with arrow keys, for
   example) and press associated key to translate. translation result will
   be read with synthesizer which you are using.
2. Takisto môžete prekladať text zo schránky.
3. Press the dedicated shortcut key to translate the last spoken text.

## Klávesové skratky ##
Pred Každým príkazom najprv stlačte skratku NVDA+SHIFT+t.

* T: Preloží vybratý text,
* shift+t: preloží text v schránke,
* S: Otočí zdrojový a cieľový jazyk,
* A: Oznámi nastavenie jazykov,
* C: Skopíruje preklad do schránky.
* I: Zistí jazyk vybratého textu,
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

## Zmeny vo verzii 4.1 ##
* Namiesto Google sa teraz na preklad používa služba Yandex.

## Zmeny vo verzii 4.0 ##
* Text bude automaticky preložený po výmene jazykov.
* Opravené problémy s pamäťou.

## Zmeny vo verzii 3.0 ##
* Prerobené klávesovéskratky. Všetky príkazy odteraz začínajú skratkou
  NVDA+Shift+t. Zoznam skratiek nájdete v časti klávesové skratky.
* Implementované otáčanie jazykov.
* Zmenil sa formát ukladania konfigurácie. Nastavenia sa dajú meniť aj v
  prípade, že je médium Iba na čítanie, nastavenia platia len po najbližší
  reštart NVDA.
* odstránený limit, P
* pridaná skratka pre nastavenia Instant translate do názvu položky v menu
* Možnosť automaticky detegovať jazyk je ako prvá v zozname zdrojový jazyk a
  bola odstránená zo zoznamu do jazyka
* pridané začiarkavacie políčko na nastavenie kopírovania prekladu.
* Konfiguračný súbor je v hlavnom adresáry s nastaveniami.
* Pridané všetky podporované jazyky Google (sta k 22. 4. 2015).


## Zmeny vo verzii 2.1 ##
* NVDA+shift+y preloží text v schránke.

## Zmeny vo verzii 2.0 ##
* Pridané okno kde sa dá nastaviť cieľový a koncový jazyk.
* Dialóg sa dá otvoriť z menu možnosti.
* nastavenia sa ukladajú do samostatného súboru.
* Výsledok prekladu sa automaticky skopíruje do schránky.

## Zmeny vo verzii 1.0 ##
* Prvé vydanie.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=instantTranslate

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
