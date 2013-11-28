# instantTranslate #

* Authors: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  and other nvda contributors.
* Download [version 3.0-dev][1]

Este complemento serve para traduzir um texto selecionado e/ou da área de
transferência dum idioma para outro.  Isso é feito por meio do serviço
Google Translate.

## Configurando idiomas ##
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

## Como usar este complemento ##
Há duas formas de usar o complemento:

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
* Adicionada a tecla de atalho t para o item de menu Opções do Tradutor
  Instantâneo
* The auto option is now in first position in source combo, and absent in
  target combo.
* Adicionada uma caixa de seleção para configurar a cópia de resultados de
  traduções.
* Armazena arquivo de configuração na raiz da pasta de opções.
* Novos idiomas: Alemão, Árabe, Aragonês, Coreano, Croata, Eslovaco,
  Esloveno, Espanhol, Finlandês, Francês, Galego, Holandês, Húngaro,
  Italiano, Japonês, Nepalês, Polonês, Português do Brasil, Tâmil, Turco.

## Mudanças na 2.1 ##
* Agora o complemento pode traduzir o texto da área de transferência ao
  pressionar NVDA+SHIFT+y.

## Mudanças na 2.0 ##
* Adicionado configurador gráfico onde pode escolher os idiomas fonte e
  destino.
* Adicionado item de menu do complemento, encontrado no menu Preferências.
* As configurações agora são escritas num arquivo de configuração separado.
* Agora os resultados de traduções são colocados automaticamente na área de
  transferência para futuras manipulações.

## Mudanças na 1.0 ##
* Versão inicial.

[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=it-dev
