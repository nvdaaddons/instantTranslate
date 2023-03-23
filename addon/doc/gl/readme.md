# instantTranslate #

* Autores: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  e outros colaboradores do NVDA.
* Descargar [Versión estable][1]
* Descargar [versión de desenvolvemento][2]

Este complemento utilízase para traducir texto seleccionado e/ou do
portapapeis dunha lingua a outra.  Isto faise utilizando o servizo Google
Translate.

## Configurando linguas ##
Para configurar a lingua orixe, o destiño e, no seu caso, o intercambio, vai ó: Menú NVDA >> Preferenciass >> Opcións de Instant Translate.

Hai dúas caixas combinadas etiquetadas "Lingua de orixe" e "Lingua destiño",
e unha caixa de verificación para decidir se debe copiar a traducción ó
portapapeis.

Ademáis, se seleccioaches a opción auto (l primeira elección) dende a caixa
combinada "Lingua de Orixe", tamén hai unha caixa combinada etiquetada
"Lingua para intercambiar" e unha caixa de verificación acerca do auto
intercambiado.

O sentido das dúas primeiras caixas combinadas e da caixa de verificación
para copiar é craro, pero son necesarias algunhas palabras acerca do
resto. Lembra sempre que as explicacións de máis abaixo asumen a lingua
orixe axustada á opción auto.

A caixa combinada "Lingua para Intercambiar" é útil cando intercambias a
través dun script (consulta máis abaixo) a lingua orixe e a destiño; de
feito, unha lingua destiño axustada á opción auto non ten sentido, así o
complemento axústao ó valor da caixa combinada anterior.

Así, imaxina esta situación: normalmente traduces ó inglés (a túa lingua
principal), pero ás veces(por exemplo, cando escribes un documento)
necesitas traducir ó italiano (a túa segunda lingua, supoñendo tal); podes
axustar a caixa combinada "Lingua para intercambiar" a Italiano, así
traducirás dende o inglés ó Italiano sen acceder directamente ás opcións do
complemento. Obviamente esta función ten unha maior ou menor utilidade
dependendo das túas necesidades máis frecuentes.

Agora, a caixa de verificación auto intercambiar: aparece se, e só se
axustas a opción auto na caixa combinada "Lingua de orixe", e está conectada
directamente ca caixa combinada "Lingua para intercambiar". Se a activas,
entón o complemento intenta conmutar automáticamente dende a túa
configuración orixe e destiño a unha configuración onde o destiño ven ser a
lingua orixe, e a lingua seleccioada na caixa combinada "Lingua para
Intercambiar" é a nova lingua destiño; extremadamente útil se a lingua orixe
do texto que queres traducir é a lingua destiño.

Un exemplo sinxelo: ten novamente en conta a situación imaxinada
previamente; se traduces un texto nunha lingua diferente do inglés, non hai
problemas, obtés a traducción correcta en inglés. Pero se necesitas traducir
un texto do inglés, normalmente obtés unha traducción ó inglés idéntica ó
texto orixinal, e esto é un pouco inútil. Gracias á función de
auto-intercambiar, sen embargo, asumindo que queres saber cómo soa o teu
texto en Italiano, o complemento conmuta automáticamente a lingua destiño ó
Italiano, tal que devolve unha traducción válida.

De todos os xeitos, ésta é unha configuración temporal; se esta opción non
ten efecto (é experimental), tenta conmutar manualmente a unha configuración
estable, utilizando o xesto para intercambio descrito máis abaixo. É
experimental porque nalgunhas situacións (con textos curtos, tipicamente),
Google non recoñece a lingua orixe real correctamente, e tes que
intercambiar linguas manualmente a través de script, así forzas á lingua
orixe a ser a lingua destino anterior (inglés no noso exemplo).

Cando menos, no diálogo de opcións de parámetros de voz (Menú NVDA >> Preferencias >> Voz), poderías querer marcar a opción "Cambio automático de lingua (cando se soporte)". Deste xeito, se utilizas un sintetizador multilingüe, a tradución anunciarase utilizando a voz do sintetizador no idioma de destino.

## Utilizando ##
Podes utilizar este complemento de tres xeitos:

1. Selecciona texto usando as ordes de selección(shift con teclas de frecha,
   por exemplo) e preme a tecla asociada para traducir. A continuación, a
   traducción da cadea será lida co sintetizador que esteas utilizando.
2. Tamén podes traducir texto dende o portapapeis.
3. Preme a tecla de orde adicada para traducir o último texto falado.

## Atallos de teclado ##
Todas as ordes que siguen deben premerse despois da tecla modificadora
"NVDA+Shift+t":

* T: Traduce o texto seleccioado,
* Shift+t: traduce o texto dende o portapapeis,
* S: intercambia idiomas orixe e destiño,
* A: anuncia a configuración actual,
* C: copia o derradeiro resultado ó portapapeis,
* I: identifica a lingua do texto seleccioado,
* L: traducir o último texto falado,
* O: abrir o diálogo de opcións do complemento
* H: anuncia todas as ordes en capa dispoñibles.

## Trocos para 4.4.3 ##
* Engadida a posibilidade de reemprazar guión con espazos, podería
  proporcionar mellores resultados de tradución dependendo do contexto
  (grazas a Beka Gozalishvili)
* Engadida compatibilidade con NVDA 2022.1.

## Trocos para 4.4.2 ##
* Restaurada a detección de idioma e o intercambio automático (grazas a
  Cyrille polo arranxo)
* actualizadas linguas de tradución (grazas a Cyrille)

## Cambios para 4.4 ##
* Instant Translate é agora compatible con NVDA 2019.3 (versións Python 3 de
  NVDA)

## Trocos para 4.3 ##
* arranxo de compatibilidade con nvda Agora Instant Translate será
  compatible coas últimas versións de NVDA.
* atopado un xeito para utilizar google como un servizo de tradución de
  novo.

## Trocos para 4.2 ##
* Restaurado o estado de traballo con versións máis recentes de NVDA.
* Restaurada a detección automática de lingua.

## Cambios para 4.1 ##
* InstantTranslate funciona de novo, agora co servizo de tradución Yandex en
  lugar de Google.

## Cambios para 4.0 ##
* Realízase automáticamente a tradución despois de intercambiar.
* Correxido o fallo do Caché.

## Cambios para 3.0 ##
* Cambia o xeito de cómo se usan os atallos de teclado, agora podes premer a
  tecla modificadora do instantTranslate "NVDA+Shift+t", e entón letras soas
  para realizar algunha acción (Mira todas as ordes na sección "Atallos de
  teclado").
* Implementado o intercambio de linguas.
* Formato de configuración cambiado, agora podemos cambiar as opcións do
  instant translate se estamos nun panel de só lectura, pero lembra que esto
  funcionará antes do primeiro reinicio do NVDA.
* Eliminado o límite da cantidade de texto que pode ser traducido.
* Engadido un atallo de teclado ó elemento de menú Opcións do Instant
  Translate
* A opción auto atópase agora na primeira posición na caixa combinada de
  orixe, e ausente na caixa combinada de destiño.
* Engadida unha caixa de verificación para configurar o copiado dos
  resultados da traducción.
* Almacenar o ficheiro config na raíz da carpeta de configuracións.
* As linguas orixe e destiño sincronizáronse co que actualmente expón Google
  Translate (22 Apr 2015).


## Cambios para 2.1 ##
* Agora o complemento pode traducir texto dende o portapapeis cando se prema
  NVDA+shift+y.

## Cambios para 2.0 ##
* Engadida unha Interface Gráfica de Usuario para o configurador onde  podes
  escoller as linguas de orixe e de destiño.
* Engadido un elemento de menú ó complemento que se atopa no menú
  preferencias.
* As configuracións agora escríbense nun ficheiro config separado.
* Os resultados da traducción cópianse agora automáticamente no portapapeis
  para manipulacións futuras.

## Cambios para 1.0 ##
* Versión Inicial.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=it

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
