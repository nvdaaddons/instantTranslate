# Tradutor Instantâneo (instantTranslate) #

* Autores: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  e outros colaboradores do NVDA.
* Baixe a [versão estável][1]
* Baixe a [versão em desenvolvimento][2]

Este complemento é usado para traduzir o texto selecionado e/ou da área de
transferência de um idioma para outro. Isso é feito usando o serviço Google
Tradutor.

## Configurar idiomas ##
Para configurar os idiomas de origem, de destino e nalguns casos de permuta, vá para: Menu do NVDA >> Preferências >> Configurações do Tradutor Instantâneo.

Existem duas caixas de combinação rotuladas "Idioma de origem" e "Idioma de
destino", e uma caixa de seleção para decidir se deve ser copiada a tradução
para a área de transferência.

Além disso, caso tenha selecionado a opção automático (a primeira escolha na
caixa de combinação "Idioma de origem", haverá também uma caixa de
combinação rotulada "Idioma de permuta" e uma caixa de seleção para permuta
automática.

O significado das duas primeiras caixas de combinação e da caixa de seleção
para cópia é claro, mas algumas palavras acerca do restante se fazem
necessárias.Lembre sempre que a explicação abaixo pressupõe que o idioma de
origem está configurado na opção automática.

A caixa de combinação "Idioma de permuta" é útil quando você alterna por
script (ver abaixo) os idiomas de origem e de destino; com efeito, um idioma
de destino configurado na opção automática não faz sentido, portanto o
complemento o configura para o valor da caixa de combinação acima.

Assim, imagine a situação: você geralmente taduz para Português (seu idioma
principal), mas às vezes (por exemplo quando escreve um documento) necessita
traduzir para Italiano (digamos seu segundo idioma); você pode colocar a
caixa de combinação "Idioma de permuta" para Italiano, de modo que traduzirá
de Português para Italiano sem acessar diretamente as configurações do
complemento. Obviamente, essa função tem maior ou menor utilidade, conforme
sua necessidade mais freqüente.

Agora, vem a caixa de seleção permuta automática: ela aparece se e somente
se você seleciona a opção automático na caixa de combinação "Idioma de
origem" e está diretamente conectada à caixa de combinação "Idioma de
permuta". Caso você a ative, o complemento tenta comutar automaticamente da
atual configuração de origem e destino para uma configuração na qual o
idioma de destino torna-se o de origem e o idioma escolhido na caixa de
combinação "Idioma de permuta" é o novo idioma de destino; extremamente útil
se o idioma de origem do texto que você quer traduzir é o idioma destino.

Um exemplo simple: tenha de novo em mente a situação imaginada antes; se
você traduz um texto num idioma diferente de Português, não há problemas,
você obtém a tradução correta em Português. Agora se você precisa traduzir
um texto do Português, normalmente você obtém uma tradução para Português
idêntica ao texto original e isso é pouco útil. Graças a opção de permuta
automática, porém, supondo que você queira saber como o texto soa em
Italiano, o complemento comuta automaticamente o idioma de destino para
Italiano e portanto devolve uma tradução válida.

Em todo caso, isso é uma configuração temporária; se a opção não tiver
efeito (a mesma é experimental), tente comutar manualmente para uma
configuração estável usando o gesto de alternância descrito abaixo. Ela é
experimental porque, em certas situações (geralmente com textos curtos), o
Google não reconhece corretamente o verdadeiro idioma de origem e é preciso
alternar os idiomas manualmente via script, de modo a forçar o idioma de
origem a ser o anterior idioma de destino (Português em nosso exemplo).

Pelo menos, no diálogo dos parâmetros de configuração de fala (Menu NVDA >> Preferências >> Fala), você pode querer marcar a opção "Alternância automática de idioma (quando suportado)". Desta forma, se você estiver usando um sintetizador multilíngue, a tradução será anunciada usando a voz do idioma de destino do sintetizador.

## Usando ##
Você pode usar este complemento de três maneiras:

1. Selecione algum texto usando comandos de seleção (shift com as teclas de
   seta, por exemplo) e pressione a tecla associada para traduzir; o
   resultado da tradução será lido com o sintetizador que você está usando.
2. Pode também traduzir o texto da área de transferência.
3. Pressione a tecla de atalho dedicada para traduzir o último texto falado.

## Atalhos ##
Todos os seguintes comandos devem ser pressionados após a tecla modificadora
"NVDA+Shift+t":

* T: Traduz o texto selecionado,
* Shift+t: traduz o texto da área de transferência,
* S: permuta os idiomas de origem e destino,
* A: anuncia a configuração atual,
* C: copia o último resultado para a área de transferência,
* I: identifica o idioma do texto selecionado,
* L: traduz o último texto falado,
* O: abrir diálogo de configurações de tradução
* H: anuncia ao usuário todos os comandos disponíveis de camada.

## Changes for 4.4.3 ##
* Added the ability to replace underscores with spaces, may provide better
  translation results depending on context (thanks to Beka Gozalishvili)
* Added compatibility for NVDA 2022.1

## Mudanças na 4.4.2 ##
* Restaura detecção de idioma e permuta automática (agradecimentos a Cyrille
  pela correção)
* idiomas atualizados para tradução (graças ao Cyrille)

## Mudanças na 4.4 ##
* Tradutor instantâneo agora é compatível com NVDA 2019.3 (versões Python 3
  do NVDA)

## Mudanças na 4.3 ##
* correção de compatibilidade com nvda Agora o tradutor instantâneo será
  compatível com as compilações do nvda mais recentes.
* descobri uma maneira de usar o google como serviço de tradução novamente.

## Mudanças na 4.2 ##
* Estado de trabalho restaurado com versões mais recentes do nvda.
* Detecção automática de idioma restaurada.

## Mudanças na 4.1 ##
* O Tradutor Instantâneo funciona novamente, agora com o serviço Yandex
  translator ao invés do Google.

## Mudanças na 4.0 ##
* Tradução é executada automaticamente após alternância.
* Falha de cache corrigida.

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
* Idiomas de origem e destino sincronizados com o que o Google Tradutor
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

[1]: https://addons.nvda-project.org/files/get.php?file=instantTranslate

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
