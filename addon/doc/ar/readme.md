# instantTranslate #
[[!meta title="instantTranslate"]]

* Authors: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  and other nvda contributors.
* Download [version 3.0-dev][1]

تقوم هذه الإضافة بترجمة النص المظلل أو الموجود بحافظة الويندوز من لغة إلى
أخرى مستخدمة في ذلك خدمة الترجمة من قوقل.

## إعداد اللغات ##
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

## كيفية استخدام الإضافة ##
توجد طريقتان لاستخدام هذه الإضافة:

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
* إضافة حرف الوصول السريع T إلى قائمة إعدادات instant translate
* The auto option is now in first position in source combo, and absent in
  target combo.
* إضافة مربع تحديد لإعداد نسخ نتائج الترجمة.
* تخزين ملف الإعدادات داخل مجلد الإعدادات.
* ترجمة الإضافة إلى: الأرجانيزية, والعربية, والبرازيلية البرتغالية,
  والهولندية,  والكرواتية, والفنلندية, الفرنسية, الغالية, الألمانية,
  المجرية, الإيطالية, الكورية, السلوفاكية, الإسبانية, ولغة تاميل, والتوركية.

## مستجدات الإصدار 2.1 ##
* من الآن يمكن للإضافة ترجمة النص المخزن بحافظة الويندوز عن طريق الضغط على
  nvda+shift+y.

## مستجدات الإصدار 2.0 ##
* إضافة عنصر لواجهة المستخدم يمكن من خلاله تحديد لغة المصدر ولغة الهدف.
* إضافة عنصر قائمة للتحكم في إعدادات الإضافة بقائمة التفضيلات.
* من الآن سيتم كتابة الإعدادات في ملف منفصل.
* من الآن سيتم نسخ نتائج الترجمة إلى حافظة الويندوز للرجوع إليها وقت الحاجة.

## مستجدات الإصدار 2.0 ##
* إصدار أولي

[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=it-dev
