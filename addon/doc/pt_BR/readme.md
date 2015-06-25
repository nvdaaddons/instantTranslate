# instantTranslate #

* Autores: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  e outros colaboradores do NVDA.
* Baixe a [versão estável][1]
* Baixe a [versão de desenvolvimento][2]

Este complemento serve para traduzir um texto selecionado e/ou da área de
transferência dum idioma para outro.  Isso é feito por meio do serviço
Google Translate.

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

Em todo caso, isso é uma configuração temporária; se a opção não tiver
efeito (a mesma é experimental), tente comutar manualmente para uma
configuração estável usando o gesto de alternância descrito abaixo. Ela é
experimental porque, em certas situações (geralmente com textos curtos), o
Google não reconhece corretamente o verdadeiro idioma de origem e é preciso
alternar os idiomas manualmente via script, de modo a forçar o idioma de
origem a ser o anterior idioma de destino (Inglês em nosso exemplo).

## Usando ##
Você pode usar este complemento de duas maneiras:

1. Selecione um texto usando comandos de seleção (shift com setas, por
   exemplo). Aí pressione a tecla atribuída para traduzir o texto
   selecionado. A tradução resultante será lida com o sintetizador que está
   a usar.
2. Pode também traduzir o texto da área de transferência.

## Atalhos ##
Todos os seguintes comandos devem ser pressionados após a tecla modificadora
"NVDA+Shift+t":

* T: Traduz o texto selecionado,
* Shift+t: Traduz o texto da área de transferência,
* S: Alterna os idiomas de origem e destino,
* A: Anuncia a configuração atual,
* C: Copia o último resultado para a área de transferência,
* I: identifica o idioma do texto selecionado,
* H: Anuncia ao usuário todos os comandos disponíveis.

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

[1]: http://addons.nvda-project.org/files/get.php?file=it

[2]: http://addons.nvda-project.org/files/get.php?file=it-dev
