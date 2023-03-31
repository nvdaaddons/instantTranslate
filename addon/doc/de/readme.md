# Sofortübersetzung #

* Autoren: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  und andere NVDA-Entwickler.
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]

Diese Erweiterung wird verwendet, um ausgewählten Text und/oder Text aus der
Zwischenablage von einer Sprache in eine andere zu übersetzen. Dies
geschieht über den Google-Dienst für Übersetzungen.

## Sprachen einstellen ##
Um die Quell-, Ziel- und ggf. Tauschsprache zu konfigurieren, gehen Sie zu: NVDA-Menü >> Einstellungen >> Einstellungen für die Sofortübersetzung.

Es gibt zwei Ausklapplisten mit den Bezeichnungen"Quellsprache"
und"Zielsprache" und ein Kontrollkästchen, um zu entscheiden, ob die
Übersetzung in die Zwischenablage kopiert werden soll.

Zusätzlich, wenn Sie die Auto-Option (die erste Wahl) aus der
"Quellsprache"-Ausklappliste ausgewählt haben, gibt es auch eine
Ausklappliste mit der Bezeichnung"Sprachentausch" und ein Kontrollkästchen
Automatischer Tausch.

Die Bedeutung der beiden ersten Ausklapplisten und des Kontrollfeldes für
die Kopie ist klar, aber einige Worte über den Rest sind notwendig. Denken
Sie immer daran, dass die folgenden Erklärungen die Quellsprache mit
Auto-Option voraussetzen.

Die Ausklappliste "Sprachentausch" ist nützlich, wenn Sie per Skript (siehe
unten) die Quell- und Zielsprache austauschen. Tatsächlich hat eine
Zielsprache, die auf der Auto-Option eingestellt ist, keinen Sinn, also
setzt die Erweiterung sie auf den Wert der obigen Ausklappliste.

Stellen Sie sich diese Situation vor: Sie übersetzen normalerweise ins
Englische (Ihre Hauptsprache). Manchmal (zum Beispiel, wenn Sie ein Dokument
schreiben) müssen Sie ins Italienische übersetzen (Ihre zweite
Sprache). Nehmen Sie an Sie könnten die "Sprachentausch"-Ausklappliste auf
Italienisch einstellen, so dass Sie aus dem Englischen ins Italienische
übersetzen ohne direkt auf die Erweiterungseinstellungen
zuzugreifen. Offensichtlich hat diese Funktion einen höheren oder geringeren
Nutzen, je nach Ihren individuellen Bedürfnissen.

Das Auto-Tausch-Kontrollkästchen erscheint ausschließlich wenn Sie die
Auto-Option in der Ausklappliste "Quellsprache" eingestellt haben. Das
Kontrollkästchen ist direkt mit der Ausklappliste "Sprachentausch"
verbunden. Wenn Sie es aktivieren, dann versucht die Erweiterung automatisch
von Ihrer Quell- und Zielkonfiguration in eine Konfiguration umzuwandeln,
bei der die Ziel- zur Quellsprache wird und die Sprache, die in der
"Sprachentausch"-Ausklappliste ausgewählt wurde, Zielsprache wird. Dies ist
äußerst nützlich, wenn die Quellsprache des zu übersetzenden Textes die
Zielsprache ist.

Ein einfaches Beispiel: Denken Sie noch einmal an die Situation, die Sie
sich vorher vorgestellt haben. Wenn Sie einen Text aus einer anderen Sprache
als Englisch übersetzen, gibt es kein Problem. Sie erhalten die richtige
Übersetzung ins Englische. Aber wenn Sie einen Text aus dem Englischen
übersetzen müssen, erhalten Sie normalerweise eine Übersetzung ins
Englische, die mit dem Originaltext identisch ist. Das ist ein Wenig
nutzlos. Durch die Auto-Swap-Funktion geht die Erweiterung davon aus, dass
Sie wissen wollen wie Ihr Text ins Italienische klingt. Die Funktion
schaltet automatisch die Zielsprache ins Italienische um, so dass eine
gültige Übersetzung ausgegeben wird.

Wie auch immer, dies ist eine temporäre Konfiguration; Wenn diese Option
keine Wirkung hat (sie ist experimentell), versuchen Sie, manuell zu einer
stabilen Konfiguration zu wechseln, indem Sie die unten beschriebene
Tastenkombination zum Wechseln verwenden. Es ist experimentell, da Google in
einigen Situationen (in der Regel bei kurzen Texten) die echte
Ausgangssprache nicht richtig erkennt und Sie die Sprachen manuell per
Skript austauschen müssen, um die Ausgangssprache als vorherige Zielsprache
zu erzwingen (Englisch in unserem Beispiel).

Zumindest im Dialogfeld mit den Sprach-Einstellungen (NVDA-Menü -> Einstellungen -> Sprache) möchten Sie vielleicht die Option "Automatische Sprachumschaltung (wenn unterstützt)" aktivieren. Wenn Sie einen mehrsprachigen Synthesizer verwenden, wird die Übersetzung auf diese Weise mit der zielsprachlichen Stimme der Sprachausgabe angesagt.

## Verwendung ##
Sie können diese Erweiterung auf drei Arten verwenden:

1. Wählen Sie Text mit Tastenkombinationen zur Auswahl aus (z. B. Umschalten
   mit den Pfeiltasten) und drücken Sie zum Übersetzen die entsprechende
   Taste. Das Übersetzungsergebnis wird von der verwendeten Sprachausgabe
   mitgeteilt.
2. Sie können auch den Text der Zwischenablage übersetzen lassen.
3. Drücken Sie die entsprechende Tastenkombination, um den zuletzt
   gesprochenen Text zu übersetzen.

## Tastenkürzel ##
Alle folgenden Befehle müssen nach der zuvor gedrückten Modifikationstaste
"NVDA+Shift+t" gedrückt werden:

* T: Markierten Text übersetzen,
* Umschalt+t: Text aus der Zwischenablage übersetzen,
* S: tausche Ausgangs- und Zielsprache,
* A: aktuelle Konfiguration ansagen,
* C: kopiere letztes Ergebnis in die Zwischenablage,
* I: die Sprache des markierten Texts ermitteln,
* L: Den zuletzt vorgelesenen Text übersetzen,
* O: Einstellungen für die Übersetzungen öffnen
* H: Nennt alle verfügbaren Tastenbefehle.

## Änderungen in 4.4.3 ##
* Es wurde die Möglichkeit hinzugefügt, Unterstriche durch Leerzeichen zu
  ersetzen, was je nach Kontext zu besseren Übersetzungsergebnissen führen
  kann (Dank an Beka Gozalishvili)
* Kompatibilität für NVDA 2022.1 hinzugefügt

## Änderungen in 4.4.2 ##
* Stellt die Spracherkennung und den automatischen Austausch wieder her
  (Danke an Cyrille für die Korrektur)
* aktualisierte Sprachen für die Übersetzung (Dank an Cyrille)

## Änderungen in 4.4 ##
* Instant Translate ist jetzt mit neueren NVDA (Python 3) kompatibel.

## Änderungen in 4.3 ##
* Instant Translate ist mit den neuesten NVDA-Builds kompatibel.
* einen Weg gefunden, Google wieder als Übersetzungsdienst zu nutzen.

## Änderungen in 4.2 ##
* Betriebszustand mit neueren Versionen von NVDA wiederhergestellt.
* Automatische Spracherkennung wiederhergestellt.

## Änderungen in 4.1 ##
* Sofortübersetzung funktioniert wieder, jetzt jedoch mit Yandex-Übersetzer
  statt mit Google.

## Änderungen in 4.0 ##
* Übersetzungsergebnisse  werden nun automatisch in die Zwischenablage
  kopiert, um diese weiter verwenden zu können.
* Cache-Problem behoben.

## Änderungen in 3.0 ##
* Ändert die Art und Weise, wie Shortcuts verwendet werden. Jetzt können Sie
  die Änderungstasten der Sofortübersetzung (NVDA+Shift+t) drücken und dann
  einen Buchstaben, um eine Aktion auszuführen (siehe alle Befehle im
  Abschnitt"Tastenbefehle").
* Sprachen vertauschen implementiert.
* Geändertes Einstellungsformat, jetzt können Sie die Einstellungen für die
  Sofortübersetzung ändern, wenn Sie sich im Nur-Lesen-Fenster
  befinden. Dies wird nur vor dem ersten Neustart von NVDA funktionieren.
* Die Begrenzung der Textmenge, die übersetzt werden kann, wurde entfernt.
* Tastenkürzel T zum Menüpunkt für die Einstellungen von Sofortübersetzung
  hinzugefügt
* Die Auto-Option befindet sich jetzt an erster Stelle in der
  Quellkombination und fehlt in der Zielkombination.
* Option hinzugefügt, um festzulegen, ob das Resultat der Übersetzung
  kopiert werden soll.
* Konfigurationsdatei wird im Einstellungsverzeichnis gespeichert.
* Ausgangs- und Zielsprache mit Google-Translate-Vorschlägen synchronisiert
  ( 22. April 2015 ).


## Änderungen in 2.1 ##
* Die Erweiterung übersetzt nun den Text aus der Zwischenablage mittels
  NVDA+Y.

## Änderungen in 2.0 ##
* Einstellungsdialog zur Wahl der Ein- und Ausgabesprache hinzugefügt.
* Menü für die Erweiterung im Einstellungen-Menü hinzugefügt.
* Einstellungen werden in eine separate Datei geschrieben.
* Übersetzungsergebnisse  werden nun automatisch in die Zwischenablage
  kopiert, um diese weiter verwenden zu können.

## Änderungen in 1.0 ##
* Erste Version.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=instantTranslate

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
