# Rýchly prekladač #

* Autori: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  a ďalší.
* Stiahnuť [stabilnú verziu][1]
* Stiahnuť [Vývojovú verziu][2]

pomocou tohto doplnku môžete prekladať vybratý text, alebo text umiestnený v
schránke. Na prekladanie sa používa externá služba.

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

Upozorňujeme, že táto funkcia je experimentálna a nemusí správne
fungovať. Ak narazíte na problémy, otočte jazyky ručne pomocou klávesovej
skratky.

## Použitie ##
Ako prekladať

1. Vyberte nejaký text (napríklad pomocou shift+šípky). Potom stlačte
   príslušné klávesové skratky. NVDA prečíta preložený text.
2. Takisto môžete prekladať text zo schránky.

## Klávesové skratky ##
Pred Každým príkazom najprv stlačte skratku NVDA+SHIFT+t.

* T: Preloží vybratý text,
* shift+t: preloží text v schránke,
* S: Otočí zdrojový a cieľový jazyk,
* A: Oznámi nastavenie jazykov,
* C: Skopíruje preklad do schránky.
* I: Zistí jazyk vybratého textu,
* H: Oznámi dostupné klávesové skratky.

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

[1]: https://addons.nvda-project.org/files/get.php?file=it

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
