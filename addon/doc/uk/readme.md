# instantTranslate #

* Автори: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  та інші розробники NVDA.
* Завантажити [стабільну версію][1]
* Завантажити [версію в розробці][2]

This add-on is used to translate selected and/or clipboard text from one
language to another.  This is done using the Google Translate service.

## Конфігурування мов ##
Щоб налаштувати мову оригіналу і перекладу, а також випадки зміни мов, перейдіть до меню NVDA >> «Налаштування» >> «Налаштування Instant Translate».

Є два комбіновані списки з назвами «Мова оригіналу» і «Мова перекладу», і
прапорець, щоб вирішити, чи потрібно копіювати переклад у буфер обміну.

Крім того, якщо ви оберете параметр «автоматично» (перший варіант) в
комбінованому списку «Мова оригіналу», ви також знайдете комбінований список
«Мова для зміни» і прапорець, який відповідає за автоматичну зміну мови.

Значення двох перших комбінованих списків та прапорця для копіювання чітке,
але решту параметрів потребують додаткових пояснень. Завжди пам’ятайте, що
наведені нижче пояснення передбачають мову оригіналу, встановлену для
параметра «автоматично».

Комбінований список «Мова для зміни» корисний у разі заміни мови оригіналу й
перекладу за сценарієм (дивіться нижче); насправді, параметр «автоматично»
для мови перекладу не має сенсу, тому додаток встановлює для неї значення з
комбінованого списку вище.

Отже, уявімо таку ситуацію: ви зазвичай перекладаєте на англійську (вашу
основну мову), але іноді (наприклад, коли пишете документ) потрібно
перекласти на італійську (припустимо, вашу другу мову); ви можете встановити
у комбінованому списку «Мова для зміни» італійську, щоб перекладати з
англійської на італійську, не переходячи безпосередньо до налаштувань
додатка. Очевидно, що ця функція має основну чи другорядну користь
відповідно до ваших частіших потреб.

Тепер про прапорець автоматичної зміни: він з’являється тоді і лише тоді,
коли ви встановили параметр «автоматично» в списку «Мова оригіналу» і
безпосередньо пов’язаний зі списком «Мова для зміни». Якщо ви активуєте
його, тоді додаток намагатиметься автоматично переходити  з конфігурації мов
оригіналу  та перекладу  до конфігурації, де мова перекладу стає мовою
оригіналу, а мова, вибрана у списку «Мова для зміни», стає новою мовою
перекладу; надзвичайно корисно, якщо оригінальною мовою тексту, який ви
хочете перекласти, є мова перекладу.

Простий приклад: знову візьмемо до уваги ситуацію, яку розглядали раніше;
якщо ви перекладаєте текст мовою, відмінною від англійської, немає проблем,
ви отримуєте правильний переклад англійською мовою. Але якщо вам потрібно
перекласти текст з англійської, зазвичай ви отримуєте переклад англійською
мовою, ідентичний оригінальному, і це даремна трата часу. Однак завдяки
функції автоматичної заміни, припускаючи, що ви хочете знати, як ваш текст
звучить італійською, додаток автоматично замінює мову перекладу на
італійську, тому він повертає дійсний переклад.

Anyway, this is a temporary configuration; if this option has no effect
(it's experimental), try to commute manually to a stable configuration,
using the gesture for swapping described below. It's experimental because in
some situations (with short texts, typically), Google does not recognize the
real source language correctly, and you have to swap languages manually via
script, so to force the source language to be the previous target language
(English in our example).

At least, in the speech settings parameters dialog (NVDA Menu >> Preferences >> Speech), you may want to check the "Automatic language switching (when supported)" option. This way, if you are using a multi-lingual synthesizer, the translation will be announced using the target language voice of the synthesizer.

## Як користуватися ##
You can use this add-on in three ways:

1. Select some text using selection commands (shift with arrow keys, for
   example) and press associated key to translate. translation result will
   be read with synthesizer which you are using.
2. Ви також можете перекласти текст з буфера обміну.
3. Press the dedicated shortcut key to translate the last spoken text.

## Гарячі клавіші ##
Усі нижченаведені команди необхідно натискати після комбінації
«NVDA+Shift+t»:

* T: перекладає виділений текст,
* Shift+t: перекладає текст з буфера обміну,
* S: міняє місцями мови оригіналу і перекладу,
* A: промовляє поточну конфігурацію,
* C: копіює останній результат в буфер обміну,
* I: визначає мову виділеного тексту,
* L: translate the last spoken text,
* O: open translation settings dialog
* H: announces all available layered commands.

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

## Зміни у версії 4.1 ##
* Додаток InstantTranslate знову працює, але замість Google Translate
  використовує сервіс перекладу від Yandex.

## Зміни у версії 4.0 ##
* Після того, як ви поміняєте мови місцями, переклад виконається
  автоматично.
* Виправлено помилку з кешуванням.

## Зміни у версії 3.0 ##
* Змінено спосіб використання команд, тепер вам потрібно натискати
  «NVDA+Shift+t», а потім літеру для виконання низки дій (усі команди
  дивіться у розділі «Команди»).
* Додано можливість міняти мови місцями.
* Змінено формат конфігурації, тепер можна змінити налаштування миттєвого
  перекладу, перебуваючи в області лише для читання, але пам’ятайте, що це
  спрацює перед першим перезапуском NVDA.
* Видалено ліміт на обсяг тексту, який можна перекласти.
* Додано клавіатурне скорочення t для елемента меню «Налаштування Instant
  Translate»
* Параметр «автоматично» тепер розташований першим у списку мов оригіналу і
  вилучений зі списку мов перекладу.
* Додано прапорець для налаштування копіювання результатів перекладу.
* Файл конфігурації зберігається в корені папки з налаштуваннями.
* Мови оригіналу й перекладу синхронізовані з тими, які наразі надає
  перекладач Google (22 квіт 2015).


## Зміни у версії 2.1 ##
* Додаток може перекладати текст з буфера обміну, коли ви натиснете
  nvda+shift+y.

## Зміни у версії 2.0 ##
* Додано діалог вибору мов оригіналу й перекладу.
* У меню «Параметри» додано елемент меню додатка.
* Зараз налаштування прописуються в окремому конфігураційному файлі.
* Результати перекладу автоматично копіюються в буфер обміну для подальших
  дій з ними.

## Зміни у версії 1.0 ##
* Перший реліз.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=it

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
