# Błyskawiczny tłumacz tekstu / instantTranslate #

* Autorzy: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  i inni.
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]

Ta wtyczka tłumaczy tekst ze schowka lub zaznaczenia z jednego języka na
drugi. W tym celu używany jest tłumacz google.

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

Jest to tymczasowe ustawienie; jeśli ta opcja nie przyniesie rezultatu (jest
eksperymentalna), try przełącz się ręcznie na stabilną konfigurację,
używając zdarzenia wejścia zamiany, opisanego poniżej. Ta funkcja jest
eksperymentalna, ponieważ w niektórych sytuacjach (np. krótkich tekstów),
Google nie rozpozna prawidłowo rzeczywistego języka źródłowego i musisz
ręcznie zamienić języki aby przestawić język źródłowy na poprzedni język
docelowy (angielski w naszym przykładzie).

## Użycie ##
Można użyć tego dodatku na dwa sposoby:

1. Zaznacz jakiś tekst używając poleceń zaznaczania (np. shift z klawiszami
   strzałek). Następnie naciśnij kombinację klawiszy tłumaczenia, aby
   przetłumaczyć zaznaczony tekst. Przetłumaczony tekst zostanie odczytany
   przy pomocy używanego syntezatora.
2. Możesz również przetłumaczyć tekst ze schowka.

## Skróty ##
Wszystkie poniższe polecenia muszą być wywołane po klawiszu modyfikatora
"NVDA+Shift+t":

* T: tłumaczy zaznaczony tekst, 
* Shift+t: tłumaczy tekst w schowku, 
* S: zamienia język źródłowy i docelowy, 
* A: oznajmia aktualną konfigurację, 
* C: kopiuje ostatni wynik do schowka, 
* I: identyfikuje język zaznaczonego tekstu,
* H: przedstawia użytkownikowi wszystkie dostępne polecenia.

## zmiany dla wersji 3.0 ##
* Change way how Shortcuts are used, now you can press instantTranslate
  modifier key "NVDA+Shift+t", and then single letter key to perform some
  action (see all Commands in the "Shortcuts" section).
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

[1]: http://addons.nvda-project.org/files/get.php?file=it [2]:
http://addons.nvda-project.org/files/get.php?file=it-dev


[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=it

[2]: http://addons.nvda-project.org/files/get.php?file=it-dev
