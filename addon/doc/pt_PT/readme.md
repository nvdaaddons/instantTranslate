# tradutorInstantâneo #

* Autores: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  e outros colaboradores do NVDA.
* Baixar [versão estável][1]
* Baixar [versão de desenvolvimento][2]

This add-on is used to translate selected and/or clipboard text from one
language to another.  This is done using the Google Translate service.

## Configurar idiomas ##
Para configurar os idiomas de origem, de destino e, em alguns casos, de alternância, vá para: Menu do NVDA >> Preferências >> configurações << tradutor instantânio.

Nas configurações, pode encontrar duas caixas de combinação denominadas
"Idioma de origem" e "Idioma de destino", e uma caixa de selecção para
indicar se deve ser copiada a tradução para a área de transferência.

Além disso, caso tenha seleccionado a opção "auto" (como escolha na caixa de
combinação "Idioma de origem", haverá também uma caixa de combinação chamada
"Idioma para alternância" e uma caixa de selecção para alternância
automática.

O significado das duas primeiras caixas e da caixa de selecção de "copiar
para a área de transferência" é claro, mas tornam-se necessárias algumas
palavras sobre o restante. Lembre-se, sempre, que a explicação abaixo
pressupõe que o idioma de origem está configurado para a opção "auto".

A caixa de combinação "Idioma para alternância" é útil, quando faz a troca,
por script (ver abaixo) dos idiomas de origem e de destino; com efeito, um
idioma de destino configurado na opção "auto" não faz sentido, portanto o
extra configura-o para o valor da caixa de combinação de alternância.

Assim, imagine a seguinte situação: geralmente, traduz para Inglês (que é o
seu idioma principal), mas às vezes (por exemplo quando escreve um
documento) necessita traduzi-lo para Italiano (digamos que seria o seu
segundo idioma); você pode colocar a caixa de combinação "Idioma para
alternância" para Italiano, de modo que traduzirá de Inglês para Italiano,
sem aceder directamente as configurações do extra. Obviamente, essa função
será mais ou menos útil, conforme as suas necessidades deste artifício.

Nesse caso, surge a caixa de seleção "alternância automática": ela aparece
somente se se seleciona a opção "auto", na caixa de combinação "Idioma de
origem" e está directamente conectada à caixa de combinação "Idioma de
alternância". Caso a active, o extra tenta comutar automaticamente da atual
configuração de origem e destino para uma configuração na qual o idioma de
destino se torna o de origem e o idioma escolhido na caixa de combinação
"Idioma  de alternância" é o novo idioma de destino; isto é útil se o idioma
de origem do texto que quer traduzir é o idioma de destino.

Um exemplo simples: Parta da situação imaginada antes; se traduz um texto
num idioma diferente do Inglês, não há problemas, pois obtém a tradução
correcta em Inglês. Agora se precisar de traduzir um texto do Inglês,
normalmente obtém uma tradução para Inglês idêntica ao texto original e isso
é inútil. Graças a opção de "alternância automática", porém, supondo que
você queira saber como o texto fica em Italiano, o extra comuta
automaticamente o idioma de destino para Italiano e portanto devolve uma
tradução válida.

Anyway, this is a temporary configuration; if this option has no effect
(it's experimental), try to commute manually to a stable configuration,
using the gesture for swapping described below. It's experimental because in
some situations (with short texts, typically), Google does not recognize the
real source language correctly, and you have to swap languages manually via
script, so to force the source language to be the previous target language
(English in our example).

At least, in the speech settings parameters dialog (NVDA Menu >> Preferences >> Speech), you may want to check the "Automatic language switching (when supported)" option. This way, if you are using a multi-lingual synthesizer, the translation will be announced using the target language voice of the synthesizer.

## Como Usar ##
You can use this add-on in three ways:

1. Select some text using selection commands (shift with arrow keys, for
   example) and press associated key to translate. translation result will
   be read with synthesizer which you are using.
2. Também pode traduzir o texto da área de transferência.
3. Press the dedicated shortcut key to translate the last spoken text.

## Teclas de atalho: ##
Estes comandos só são válidos após ter sido pressionada a tecla modificadora
"NVDA+Shift+t":

* T: Traduz o texto seleccionado,
* Shift+t: Traduz o texto da área de transferência,
* S: Alterna os idiomas de origem e destino,
* A: indica a configuração atual,
* C: Copia o último resultado para a área de transferência,
* I: identifica o idioma do texto seleccionado,
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

## Mudanças para a 4.1 ##
* O Tradutor Instantâneo está novamente a funcionar, agora com o serviço
  Yandex translator em vez do Google.

## Mudanças para a 4.0 ##
* A tradução é executada automaticamente após a alternância.
* Problema de cache corrigido.

## Mudanças para a 3.0 ##
* Foi modificado o modo como as teclas de atalho são usadas, agora pode
  pressionar a tecla modificadora do InstantTranslate "NVDA+Shift+t" e então
  uma tecla única para executar uma acção (veja todos os comandos na secção
  "atalhos").
* Implementado "idiomas de alternância".
* Foi modificado o formato das configurações; agora podem alterar-se as
  opções do Tradutor Instantâneo estando no painel somente leitura, mas
  lembre que as mesmas terão efeito antes da primeira reinicialização do
  NVDA.
* Foi removido o limite da quantidade de texto que se pode traduzir.
* Adicionada a tecla de atalho "t" para o item de menu do Tradutor
  Instantâneo
* A opção "automático", agora, encontra-se em primeiro lugar na caixa de
  combinação origem e desapareceu da caixa de combinação destino.
* Adicionada uma caixa de selecção para configurar a cópia dos resultados de
  traduções.
* Passou a armazenar o ficheiro de configuração na raíz da pasta de opções.
* Idiomas de origem e destino sincronizados com o que o Google Translate
  expõe atualmente (22 de abril de 2015).


## Mudanças para a 2.1 ##
* Agora, o extra pode traduzir o texto da área de transferência, ao
  pressionar NVDA+SHIFT+y.

## Mudanças para a 2.0 ##
* Adicionado configurador gráfico onde se podem escolher os idiomas de
  origem e de destino.
* Adicionado item de menu do extra, no menu Preferências.
* As configurações agora são registadas num ficheiro de configuração
  separado.
* Agora, os resultados das traduções são colocados automaticamente na área
  de transferência para futuras manipulações.

## Mudanças para a 1.0 ##
* Versão inicial.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=it

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
