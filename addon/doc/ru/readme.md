# instantTranslate #

* Авторы: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  и другие участники сообщества NVDA.
* Загрузить [стабильную версию][1]
* Загрузить [разрабатываемую версию][2]

Это дополнение используется для перевода выделенного текста и/или текста из
буфера обмена с одного языка на другой.  Это делается с помощью сервиса
Google Translate.

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
some situations (with short texts, typically), Google does not recognize the
real source language correctly, and you have to swap languages manually via
script, so to force the source language to be the previous target language
(English in our example).

По крайней мере, в диалоге параметров настройки речи (меню NVDA >> Параметры >> Речь) вы можете захотеть установить флажок "Автоматическое переключение языка (если поддерживается)". Таким образом, если вы используете многоязычный синтезатор, перевод будет озвучен голосом синтезатора на целевом языке.

## Использование ##
Вы можете использовать это дополнение тремя способами:

1. Выделите текст с помощью команд выделения (например, shift с помощью
   клавиш со стрелками) и нажмите соответствующую клавишу для
   перевода. результат перевода будет прочитан с помощью синтезатора,
   который вы используете.
2. Вы также можете перевести текст из буфера обмена.
3. Нажмите специальную комбинацию клавиш, чтобы перевести последний
   произнесенный текст.

## Команды ##
Все следующие команды клавиш нужно нажимать после клавишного модификатора
"NVDA+Shift+t":

* T: Перевести выделенный текст,
* Shift+t: перевести текст из буфера обмена,
* S: поменять местами исходный и целевой языки,
* A: объявить текущую конфигурацию,
* C: скопировать последний результат в буфер обмена,
* I: определить язык выделенного текста,
* L: перевести последний произнесённый текст,
* O: открыть диалог настроек перевода
* H: объявляет все доступные многоуровневые команды.

## Изменения  в версии 4.4.3 ##
* Added the ability to replace underscores with spaces, may provide better
  translation results depending on context (thanks to Beka Gozalishvili)
* Added compatibility for NVDA 2022.1

## Изменения  в версии 4.4.2 ##
* Restore language detection and auto-swapping (Thanks to Cyrille for fix)
* updated languages for translation (thanks to Cyrille)

## Изменения  в версии 4.4 ##
* Instant translate is now compatible with NVDA 2019.3 (Python 3 versions of
  NVDA)

## Изменения  в версии 4.3 ##
* nvda compatibility fix Now instant translate will be compatible with
  latest nvda builds.
* снова найден способ использовать Google в качестве сервиса переводов.

## Изменения  в версии 4.2 ##
* Restored working state with newer versions of nvda.
* Восстановлено автоматическое определение языка.

## Изменения  в версии 4.1 ##
* InstantTranslate снова работает со службой переводчика Яндекс вместо
  Google.

## Изменения  в версии 4.0 ##
* Результат перевода теперь автоматически выполняется при смене языков
  местами.
* Исправлена ошибка кэша.

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


[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=instantTranslate

[2]: https://www.nvaccess.org/addonStore/legacy?file=it-dev
