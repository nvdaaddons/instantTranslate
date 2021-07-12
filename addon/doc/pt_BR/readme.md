# instantTranslate #

* Autores: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  e outros colaboradores do NVDA.
* Baixe a [versão estável][1]
* Baixe a [versão de desenvolvimento][2]

This add-on is used to translate selected and/or clipboard text from one
language to another.  This is done using the Google Translate service.

## Configurar idiomas ##
Para configurar os idiomas de origem, de destino e nalguns casos de alternância, vá para: Menu do NVDA >> Preferências >> Opções do tradutor instantânio.

Existem duas caixas de combinação rotuladas "Idioma de origem" e "Idioma de
destino", e uma caixa de seleção para decidir se deve ser copiada a tradução
para a área de transferência.

Além disso, caso tenha selecionado a opção auto (a primeira escolha na caixa
de combinação "Idioma de origem", haverá também uma caixa de combinação
rotulada "Idioma para alternância" e uma caixa de seleção para alternância
automática.

O significado das duas primeiras caixas de combinação e da caixa de seleção
de copiar é claro, mas algumas palavras acerca do restante se fazem
necessárias.Lembre sempre que a explicação abaixo pressupõe que o idioma de
origem está configurado na opção auto.

A caixa de combinação "Idioma para alternância" é útil quando você alterna
por script (ver abaixo) os idiomas de origem e de destino; com efeito, um
idioma de destino configurado na opção auto não faz sentido, portanto o
complemento o configura para o valor da caixa de combinação acima.

Assim, imagine a situação: você geralmente taduz para Inglês (seu idioma
principal), mas às vezes (por exemplo quando escreve um documento) necessita
traduzir para Italiano (digamos seu segundo idioma); você pode colocar a
caixa de combinação "Idioma para alternância" para Italiano, de modo que
traduzirá de Inglês para Italianosem acessar diretamente as opções de
complemento. Obviamente, essa função tem maior ou menor utilidade, conforme
sua necessidade mais freqüente.

Aí vem a caixa de seleção alternância automática: ela aparece se e somente
se você seleciona a opção auto na caixa de combinação "Idioma de origem" e
está diretamente conectada à caixa de combinação "Idioma com o qual
alternar". Caso você a ative, o complemento tenta comutar automaticamente da
atual configuração de origem e destino para uma configuração na qual o
idioma de destino torna-se o de origem e o idioma escolhido na caixa de
combinação "Idioma com o qual alternar" é o novo idioma de destino;
extremamente útil se o idioma de origem do texto que você quer traduzir é o
idioma destino.

Um exemplo simple: tenha de novo em mente a situação imaginada antes; se
você traduz um texto num idioma diferente de Inglês, não há problemas, você
obtém a tradução correta em Inglês. Agora se você precisa traduzir um texto
do Inglês, normalmente você obtém uma tradução para Inglês idêntica ao texto
original e isso é pouco útil. Graças a opção de alternância automática,
porém, supondo que você queira saber como o texto soa em Italiano, o
complemento comuta automaticamente o idioma de destino para Italiano e
portanto devolve uma tradução válida.

Anyway, this is a temporary configuration; if this option has no effect
(it's experimental), try to commute manually to a stable configuration,
using the gesture for swapping described below. It's experimental because in
some situations (with short texts, typically), Google does not recognize the
real source language correctly, and you have to swap languages manually via
script, so to force the source language to be the previous target language
(English in our example).

At least, in the speech settings parameters dialog (NVDA Menu >> Preferences >> Speech), you may want to check the "Automatic language switching (when supported)" option. This way, if you are using a multi-lingual synthesizer, the translation will be announced using the target language voice of the synthesizer.

## Usando ##
You can use this add-on in three ways:

1. Select some text using selection commands (shift with arrow keys, for
   example) and press associated key to translate. translation result will
   be read with synthesizer which you are using.
2. Pode também traduzir o texto da área de transferência.
3. Press the dedicated shortcut key to translate the last spoken text.

## Atalhos ##
Todos os seguintes comandos devem ser pressionados após a tecla modificadora
"NVDA+Shift+t":

* T: Traduz o texto selecionado,
* Shift+t: Traduz o texto da área de transferência,
* S: Alterna os idiomas de origem e destino,
* A: Anuncia a configuração atual,
* C: Copia o último resultado para a área de transferência,
* I: identifica o idioma do texto selecionado,
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

## Mudanças na 4.1 ##
* O Tradutor Instantâneo funciona novamente, agora com o serviço Yandex
  translator ao invés do Google.

## Mudanças na 4.0 ##
* Tradução é executada automaticamente após alternância.
* Bug de cache corrigido.

## Mudanças na 3.0 ##
* Alterado o modo como os atalhos são usados, agora pode pressionar a tecla
  modificadora do InstantTranslate "NVDA+Shift+t" e então uma tecla única
  para executar uma ação (veja todos os comandos na seção "atalhos").
* Implementado idiomas de permuta.
* Alterado formato das configurações; agora pode-se alterar as opções do
  Tradutor Instantâneo estando no painel somente leitura, mas lembre que as
  mesmas terão efeito antes da primeira reinicialização do NVDA.
* Removido limite na quantidade de texto que se pode traduzir.
* Adicionada a tecla de atalho t para o item de menu Opções do Tradutor
  Instantâneo
* A opção automático agora encontra-se em primeiro lugar na caixa de
  combinação origem e está ausente na caixa de combinação destino.
* Adicionada uma caixa de seleção para configurar a cópia de resultados de
  traduções.
* Armazena arquivo de configuração na raiz da pasta de opções.
* Idiomas de origem e destino sincronizados com o que o Google Translate
  expõe atualmente (22 de abril de 2015).


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


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=it

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
