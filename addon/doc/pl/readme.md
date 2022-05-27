# Błyskawiczny tłumacz tekstu / instantTranslate #

* Autorzy: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  i inni.
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]

This add-on is used to translate selected and/or clipboard text from one
language to another.  This is done using the Google Translate service.

## konfigurowanie języków ##
Aby skonfigurować język źródłowy, docelowy, oraz ewentualnie język zamiany, idź do: menu NVDA >> Ustawienia >> Ustawienia Instant Translate.

Znajdują się tam dwie listy rozwijane, nazwane "Język źródłowy" and "Język
docelowy", oraz pole wyboru określające czy tłumaczenie ma być kopiowane do
schowka.

Ponadto, jeśli wybrano opcję auto na liście "Język źródłowy",  będzie tam
również lista "Język zamiany" oraz pole wyboru określające automatyczną
zamianę.

Znaczenie pierwszych list rozwijanych i pola wyboru kopiowania jest
oczywiste, ale kilka słów  o pozostałych elementach jest
konieczne. Pamiętaj, że poniższe wyjaśnienia zakładają, że język źródłowy
jest ustawiony na auto.

Lista "Język zamiany"  jest użyteczna, gdy zamieniasz za pomocą skryptu
(więcej poniżej) język źródłowy i docelowy; język docelowy ustawiony na auto
nie ma sensu, więc dodatek ustawia go na wartość powyższej listy.

A zatem wyobraźmy sobie taką sytuację: zwykle tłumaczysz na angielski (twój
podstawowy język), ale czasem (np. podczas tworzenia dokumentu) musisz
przetłumaczyć coś na włoski (przypuśćmy, że jest to drugi język, którym się
posługujesz); możesz ustawić "język zamiany" na Włoski, aby móc tłumaczyć z
angielskiego na włoski bez zmiany ustawień dodatku. Ta funkcja ma różną
użyteczność, zależnie od twoich potrzeb.

Obecnie pole wyboru automatycznej zamiany pojawia się wtedy i tylko wtedy,
gdy "język źródłowy"  jest ustawiony na auto, jest także bezpośrednio
związane z listą "język zamiany". Jeśli aktywowane, dodatek próbuje
automatycznie przełączać z ustawienia języka źródłowego i docelowego, na
konfigurację w której język docelowy staje się źródłowy, a język wybrany na
liście "język zamiany" staje się nowym językiem docelowym; szczególnie
przydatne, gdy język źródłowy tekstu, który chcesz tłumaczyć jest językiem
docelowym.

Prosty przykład: rozważmy sytuację omawianą poprzednio; jeśli tłumaczysz
tekst w języku innym niż angielski, nie stanowi to problemu, otrzymujesz
prawidłowe tłumaczenie po angielsku. Jeśli jednak chcesz przetłumaczyć tekst
z angielskiego, zwykle otrzymasz tłumaczenie angielskie identyczne z
oryginałem, co jest bezużyteczne. Dzięki funkcji automatycznej zamiany,
zakładając, że chcesz wiedzieć jak twój tekst będzie brzmieć po Włosku,
dodatek automatycznie ustawia język docelowy na Włoski i zwraca prawidłowe
tłumaczenie.

Anyway, this is a temporary configuration; if this option has no effect
(it's experimental), try to commute manually to a stable configuration,
using the gesture for swapping described below. It's experimental because in
some situations (with short texts, typically), Google does not recognize the
real source language correctly, and you have to swap languages manually via
script, so to force the source language to be the previous target language
(English in our example).

At least, in the speech settings parameters dialog (NVDA Menu >> Preferences >> Speech), you may want to check the "Automatic language switching (when supported)" option. This way, if you are using a multi-lingual synthesizer, the translation will be announced using the target language voice of the synthesizer.

## Użycie ##
You can use this add-on in three ways:

1. Select some text using selection commands (shift with arrow keys, for
   example) and press associated key to translate. translation result will
   be read with synthesizer which you are using.
2. Możesz również przetłumaczyć tekst ze schowka.
3. Press the dedicated shortcut key to translate the last spoken text.

## Skróty ##
Wszystkie poniższe polecenia muszą być wywołane po klawiszu modyfikatora
"NVDA+Shift+t":

* T: tłumaczy zaznaczony tekst, 
* Shift+t: tłumaczy tekst w schowku, 
* S: zamienia język źródłowy i docelowy, 
* A: oznajmia aktualną konfigurację, 
* C: kopiuje ostatni wynik do schowka, 
* I: identyfikuje język zaznaczonego tekstu,
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

## Zmiany dla wersji 4.1 ##
* Wtyczka Instant translate działa poprawnie, ale teraz zamiast Google
  translate, używa yandexa.

## zmiany dla wersji 4.0 ##
* wyniki tłumaczenia automatycznie kopiowane są do schowka po zamiany
  języka.
* Poprawiony błąd z cache.

## zmiany dla wersji 3.0 ##
* Zmieniono sposób użycia klawiszy skrótu, obecnie możesz nacisnąć klawisz
  modyfikatora instantTranslate "NVDA+Shift+t",  a następnie pojedynczą
  literę dla wykonania określonej akcji {wszystkie polecenia w sekcji
  "Klawisze skrótu"}.
* Zaimplementowana zamiana języków.
* Zmieniony format konfiguracji, teraz możemy zmieniać ustawienia dodatku w
  panelu tylko do odczytu, ale proszę pamiętać, że będzie to działać przed
  pierwszym restartem nvda.
* Usunięty limit ilości tekstu, która może zostać przetłumaczona.
* skrut i pozwala szybko dostać się do ustawień wtyczki z menu nvda.
* Opcja Auto jest na pierwszej pozycji listy języka źródłowego, a nie ma jej
  na liście języka docelowego.
* Dodane pole wyboru ustawiające kopiowanie do schowka wyniku tłumaczenia.
* plik konfiguracyjny trzymany jest teraz w głównym katalogu ustawień nvda.
* Języki źródłowe i docelowe zsynchronizowane z listą obsługiwanych przez
  Google Translate (22 Kwi 2015).


## Zmiany dla wersji 2.1 ##
* Skrót klawiszowy NVDA+shift+y tłumaczy tekst w schowku.

## zmiany dla wersji 2.0 ##
* dodano okienko, w którym możemy wybrać źródłowy i docelowy język.
* dodano pozycję dla wtyczki w menu NVDA Ustawienia.
* ustawienia zapisywane są w oddzielnym pliku konfiguracyjnym.
* wyniki tłumaczenia automatycznie kopiowane są do schowka.

## zmiany dla wersji 1.0 ##
* Wstępne wydanie.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=it

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
