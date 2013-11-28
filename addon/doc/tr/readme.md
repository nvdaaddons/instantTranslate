# instantTranslate #

* Authors: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  and other nvda contributors.
* Download [version 3.0-dev][1]

Bu eklenti seçilen ya da panoya kopyalanmış olan metnin tercümesi için
kullanılır. Google Translate servisi kullanılmaktadır.

## Dillerin ayarlanması ##
To configure source, target and in case swap language, from NVDA menu, go to
Preferences, then go to Instant Translate Settings.  There are three combo
boxes labeled "translate from", "translate into" and "Language for swapping"
(if you selected auto option from source languages).

If you selected the auto option from source languages, there is also a
checkbox about the auto-swap: if you activate it, then the addon tries to
commute automatically from your source and target configuration to a
configuration where target becomes the source language, and language
selected in "Language for swapping" combo is the new target language;
extremely useful if the source language of the text you want translate is
the target language.

However, this is a temporary configuration, if this option has no effect
(it's experimental), try to commute manually to a stable configuration,
using the gesture for swapping described below.

## Eklentinin kullanımı ##
Eklenti iki yolla kullanılabilir :

1. Select some text using selection commands (shift with arrow keys, for
   example). Then press Shift+NVDA+T to translate the selected text. Then
   the translated string will be read, providing that the synthesizer you
   are using supports the target language.
2. Copy some text to clipboard. Then press Shift+NVDA+Y to translate the
   text in the clipboard to the target language.

## Other useful commands ##
* NVDA+shift+r: pressed once, announce current configuration; pressed twice,
  swap source and target languages.

## Changes for 3.0 ##
* Implemented swapping languages.
* Changed configuration format, now we can change instant translate settings
  if we are in readonly pane, but remember that this will work before first
  restart of nvda.
* Removed limit on amount of text that can be translated.
* Anında Çeviri Ayarlar menü öğesi eklendi kısayol t
* The auto option is now in first position in source combo, and absent in
  target combo.
* Çeviri sonuçlarının kopyalanmasıyla ilgili bir onay kutusu eklendi.
* Yapılandırma dosyasını konfigürasyon dizininin kökünde bulundur
* Yeni diller: Aragonese, Arapça, Brezilya Portekizcesi, İspanyolca,
  Slovence, Slovakça, Lehçe, Nepal, Korece, Japonca, İtalyanca, Macarca,
  Almanca, Galiçyaca, Fransızca, Fince Hırvatça, Hollandaca, Tamil, Türkçe.

## 2.1 için değişiklikler ##
* NVDA + shift + y basılınca Şimdi eklenti panodaki metni çevirebilir.

## 2.0 için değişiklikler ##
* kaynak ve hedef dil seçebileceğiniz gui yapılandırıcı eklendi.
* Tercihler menüsü altına eklenti menü öğesi eklendi.
* Ayarlar şimdi ayrı bir yapılandırma dosyasına yazılıyor.
* Çeviri sonuçları artık otomatik olarak gelecek kullanımlar için panoya
  kopyalanır.

## 1.0 için değişiklikler ##
* İlk sürümü.

[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=it-dev
