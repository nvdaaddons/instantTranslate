# Błyskawiczny tłumacz tekstu / instantTranslate #

* Autorzy: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  i inni.
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]

Ten dodatek służy do tłumaczenia zaznaczonego i/lub schowka tekstu z jednego
języka na drugi.  Odbywa się to za pomocą usługi Tłumacz Google.

## Konfigurowanie języków ##
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

W każdym razie jest to konfiguracja tymczasowa; Jeśli ta opcja nie ma wpływu
(jest eksperymentalna), spróbuj ręcznie dojeżdżać do stabilnej konfiguracji,
używając gestu do zamiany opisanego poniżej. Jest to eksperymentalne,
ponieważ w niektórych sytuacjach (zazwyczaj z krótkimi tekstami) Google nie
rozpoznaje poprawnie prawdziwego języka źródłowego i musisz ręcznie zamienić
języki za pomocą skryptu, aby wymusić język źródłowy jako poprzedni język
docelowy (angielski w naszym przykładzie).

Przynajmniej w oknie dialogowym parametrów ustawień mowy (Menu NVDA >> Preferencje >> Mowa) możesz zaznaczyć opcję "Automatyczne przełączanie języka (jeśli jest obsługiwane)". W ten sposób, jeśli używasz syntezatora wielojęzycznego, tłumaczenie zostanie ogłoszone przy użyciu głosu języka docelowego syntezatora.

## Użycie ##
Możesz użyć tego dodatku na trzy sposoby:

1. Zaznacz tekst za pomocą poleceń zaznaczania (na przykład Shift za pomocą
   strzałek) i naciśnij powiązany, aby przetłumaczyć. wynik tłumaczenia
   zostanie odczytany za pomocą syntezatora, którego używasz.
2. Możesz również przetłumaczyć tekst ze schowka.
3. Naciśnij dedykowany skrótu, aby przetłumaczyć ostatni tekst mówiony.

## Skróty ##
Wszystkie poniższe polecenia muszą być wywołane po klawiszu modyfikatora
"NVDA+Shift+t":

* T: Tłumaczenie zaznaczonego tekstu,
* Shift+t: tłumaczenie tekstu ze Schowka,
* S: zamiana języków źródłowych i docelowych,
* Odp .: ogłosić bieżącą konfigurację,
* C: skopiuj ostatni wynik do schowka,
* I: identyfikuje język zaznaczonego tekstu,
* L: przetłumaczyć ostatni tekst mówiony,
* O: otwórz okno dialogowe ustawień tłumaczenia
* H: ogłasza wszystkie dostępne polecenia warstwowe.

## Zmiany w wersji 4.4.3 ##
* Dodano możliwość zastępowania podkreśleń spacjami, może zapewnić lepsze
  wyniki tłumaczenia w zależności od kontekstu (dzięki Beka Gozalishvili)
* Dodano kompatybilność z NVDA 2022.1

## Zmiany w wersji 4.4.2 ##
* Przywróć wykrywanie języka i automatyczne zamienianie (podziękowania dla
  Cyrille'a za poprawkę)
* zaktualizowane języki do tłumaczenia (podziękowania dla Cyrille)

## Zmiany dla wersji 4.4 ##
* Natychmiastowe tłumaczenie jest teraz kompatybilne z NVDA 2019.3 (wersje
  NVDA w języku Python 3)

## Zmiany w wersji 4.3 ##
* Poprawka kompatybilności nvda Teraz natychmiastowy tłumacz będzie
  kompatybilny z najnowszymi kompilacjami nvda.
* znalazł sposób na ponowne wykorzystanie Google jako usługi tłumaczeniowej.

## Zmiany w wersji 4.2 ##
* Przywrócono stan roboczy z nowszymi wersjami nvda.
* Przywrócono automatyczne wykrywanie języka.

## Zmiany dla wersji 4.1 ##
* Wtyczka Instant translate działa poprawnie, ale teraz zamiast Google
  translate, używa yandexa.

## Zmiany dla wersji 4.0 ##
* Tłumaczenie jest wykonywane automatycznie po zamianie.
* Poprawiony błąd z cache.

## Zmiany dla wersji 3.0 ##
* Zmieniono sposób użycia klawiszy skrótu, obecnie możesz nacisnąć klawisz
  modyfikatora instantTranslate "NVDA+Shift+t",  a następnie pojedynczą
  literę dla wykonania określonej akcji {wszystkie polecenia w sekcji
  "Klawisze skrótu"}.
* Zaimplementowana zamiana języków.
* Zmieniony format konfiguracji, teraz możemy zmieniać ustawienia dodatku w
  panelu tylko do odczytu, ale proszę pamiętać, że będzie to działać przed
  pierwszym restartem nvda.
* Usunięty limit ilości tekstu, która może zostać przetłumaczona.
* Dodano skrót t do pozycji menu Ustawienia błyskawicznego tłumaczenia
* Opcja Auto jest na pierwszej pozycji listy języka źródłowego, a nie ma jej
  na liście języka docelowego.
* Dodane pole wyboru ustawiające kopiowanie do schowka wyniku tłumaczenia.
* Przechowuj plik konfiguracyjny w katalogu głównym folderu ustawień.
* Języki źródłowe i docelowe zsynchronizowane z listą obsługiwanych przez
  Google Translate (22 Kwi 2015).


## Zmiany dla wersji 2.1 ##
* Skrót klawiszowy NVDA+shift+y tłumaczy tekst w schowku.

## Zmiany dla wersji 2.0 ##
* Dodano konfigurator gui, w którym można wybrać język źródłowy i docelowy.
* Dodano element menu dodatku znajdujący się w menu preferencji.
* Ustawienia są teraz zapisane w osobnym pliku konfiguracyjnym.
* Wyniki tłumaczenia są teraz automatycznie kopiowane do schowka w celu
  przyszłych manipulacji.

## Zmiany dla wersji 1.0 ##
* Wstępne wydanie.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=it

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
