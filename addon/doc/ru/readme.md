# instantTranslate #

* Авторы: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  и другие участники сообщества NVDA.
* Загрузить [стабильную версию][1]
* Загрузить [разрабатываемую версию][2]

Это дополнение используется для перевода выбранного текста и текста из
буфера обмена с одного языка на другой. Это делается с помощью службы Google
Translate.

## Настройка языков ##
Чтобы настроить исходный, целевой и иногда  язык для перемены местами, перейдите: NVDA Меню >> Параметры >> Настройки Instant Translate.

Здесь два комбинированных списка, помеченые "исходный язык" и "Целевой
язык", и флажок для копирования перевода в буфер, если это необходимо.

Кроме того, если вы выбрали автоматическое определение языка (первый выбор)
в комбинированном списке "исходный язык", есть также комбинированный список
с названием "Язык для смены местами" и флажок автоматической перемены.

The meaning of two first comboboxes and checkbox for copy is clear, but some
words about the rest are necessary. Remember always that the explanations
below assume the source language set on the auto option.

The "Language for swapping" combobox is useful when you swap via script (see
below) the source and target language; in fact, a target language set on the
auto option has no sense, so the addon sets it to value of combobox above.

So, imagine this situation: you usually translate into English (your main
language), but sometimes (for example, when you write a document) you need
to translate into Italian (your second language, suppose); you can set
"Language for swapping" combobox to Italian, so you will translate from
English to Italian without accessing directly to the addon
settings. Obviously this function has a major or minor utility according to
your more frequent needs.

Now, the auto-swap checkbox: it appears if and only if you set the auto
option in "Source language" combobox, and is directly connected with
"Language for swapping" combobox. If you activate it, then the addon tries
to commute automatically from your source and target configuration to a
configuration where target becomes the source language, and language
selected in "Language for swapping" combobox is the new target language;
extremely useful if the source language of the text you want translate is
the target language.

A simple example: take again in mind the situation imagined previously; if
you translate a text in a language different from English, there is no
problem, you get the correct translation in English. But if you need to
translate a text from English, normally you get a translation into English
identical to original text, and this is a bit useless. Thanks to auto-swap
function, however, assuming that you want to know how your text sounds into
Italian, the addon commutes automatically the target language to Italian, so
it returns a valid translation.

Anyway, this is a temporary configuration; if this option has no effect
(it's experimental), try to commute manually to a stable configuration,
using the gesture for swapping described below. It's experimental because in
some situations (with short texts, tipically), Google does not recognize the
real source language correctly, and you have to swap languages manually via
script, so to force the source language to be the previous target language
(English in our example).

## Использование ##
Вы можете использовать это дополнение двумя способами:

1. Выделите текст с помощью команд выделения (например, shift со
   стрелками). Затем нажмите связанную с переводом клавишную
   команду. Переведённая строка прочтётся синтезатором, который вы
   используете.
2. Вы также можете перевести текст из буфера обмена.

## Команды ##
Все следующие команды клавиш нужно нажимать после клавишного модификатора
"NVDA+Shift+t":

* T: Перевести выделенный текст,
* Shift+t: перевести текст из буфера обмена,
* S: поменять местами исходный и целевой языки,
* A: объявить текущую конфигурацию,
* C: скопировать последний результат в буфер обмена,
* I: определить язык выделенного текста,
* H: объявляет все доступные пользователю команды.

## Изменения  в версии 3.0 ##
* Изменён способ использования команд, теперь вам нужно нажать
  клавишу-модификатор instantTranslate "NVDA+Shift+t", а затем клавишу одной
  буквы, чтобы выполнить некоторые действия (смотрите все комбинации клавиш
  в разделе "Команды").
* Реализована перемена языков местами.
* Изменен формат конфигурации, теперь можно изменить настройки instant
  translate, находясь в области только для чтения, но помните, что это будет
  работать до первого перезапуска NVDA.
* Убраны ограничение объёма переводимого текста.
* Добавлена клавиша быстрого доступа t к  пункту меню настроек Instant
  Translate
* Опция автоопределения языка теперь находится только в списке выбора
  исходного языка, убрана из списка целевого.
* Добавлен флажок для настройки результата копирования перевода.
* Файл конфигурации хранится в корневой папке пользовательских настроек.
* Исходный и целевой языки синхронизированы с тем, что предоставляет Google
  Translate на текущий момент (22 Apr 2015).


## Изменения  в версии 2.1 ##
* Теперь дополнение переводит текст из буфера обмена при нажатии
  NVDA+Shift+Y.

## Изменения  в версии 2.0 ##
* Добавлен диалог для выбора исходного и целевого языков.
* Добавлен пункт меню дополнения, находящийся в меню параметров.
* Настройки теперь сохраняются в отдельный конфигурационный файл.
* Результат перевода теперь автоматически копируется в буфер обмена для
  последующих манипуляций.

## Изменения в версии 1.0 ##
* Начальная версия.

[1]: http://addons.nvda-project.org/files/get.php?file=it [2]:
http://addons.nvda-project.org/files/get.php?file=it-dev


[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=it

[2]: http://addons.nvda-project.org/files/get.php?file=it-dev
