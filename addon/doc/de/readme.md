# Sofortübersetzung #

* Autoren: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  und andere NVDA-Entwickler.
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]

Diese Erweiterung wird verwendet, um über einen externen Dienst markierten
Text bzw. Text der Zwischenablage in eine andere Sprache zu übersetzen.

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

Wenn diese Option keine Wirkung hat (sie ist experimentell), versuchen Sie,
manuell zu einer stabilen Konfiguration zu wechseln, indem Sie die unten
beschriebene Geste verwenden. Sie ist noch nicht ausgereift, weil Google
typischerweise in manchen Situationen die eigentliche Quellsprache in kurzen
Texten nicht richtig erkennt. Sie müssen die Sprachen manuell per Skript
wechseln, um die Quellsprache als vorherige Zielsprache zu erzwingen (in
unserem Beispiel Englisch).

## Verwendung ##
Sie können diese Erweiterung auf zwei Arten verwenden:

1. Markieren Sie einen Text mit Hilfe von Auswahlbefehlen(z.B. Shift +
   Pfeiltasten) und drücken Sie die zugehörige Taste, um ihn zu
   übersetzen. Das Übersetzungsergebnis wird mit der Sprachausgabe, die Sie
   verwenden, vorgelesen.
2. Sie können auch den Text der Zwischenablage übersetzen lassen.

## Tastenkürzel ##
Alle folgenden Befehle müssen nach der zuvor gedrückten Modifikationstaste
"NVDA+Shift+t" gedrückt werden:

* T: Markierten Text übersetzen,
* Umschalt+t: Text aus der Zwischenablage übersetzen,
* S: tausche Ausgangs- und Zielsprache,
* A: aktuelle Konfiguration ansagen,
* C: kopiere letztes Ergebnis in die Zwischenablage,
* I: die Sprache des markierten Texts ermitteln,
* H: gibt alle verfügbaren Befehle aus.

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

[1]: https://addons.nvda-project.org/files/get.php?file=it

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
