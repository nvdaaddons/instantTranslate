# instantTranslate #

* Autores: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  y otros colaboradores de NVDA.
* Descargar [Versión estable][1]
* Descargar [versión de desarrollo][2]

Este complemento se utiliza para traducir texto seleccionado y/o del
portapapeles de un idioma a otro.  Esto se hace utilizando el servicio
Traductor de Google.

## Configurando idiomas ##
Para configurar el idioma origen, el destino y, en su caso, el intercambio, ve a: NVDA Menú >> Preferenciass >> Opciones de Instant Translate.

Hay dos cuadros combinados etiquetados "idioma de origen" y "idioma
destino", y una casilla de verificación para decidir si debe copiar la
traducción al portapapeles.

Además, si seleccionaste la opción auto (la primera elección) desde el
cuadro combinado "Idioma Origen", también hay un cuadro combinado etiquetado
"Idioma para intercambiar" y una casilla de verificación acerca del auto
intercambiado.

El significado de los dos primeros cuadros combinados y de la casilla de
verificación para copiar es claro, pero son necesarias algunas palabras
acerca del resto. Recuerda siempre que las explicaciones de más abajo asumen
el idioma origen ajustado a la opción auto.

El cuadro combinado "Idioma para Intercambiar" es útil cuando intercambias a
través de un script (Mira más abajo) el idioma origen y el destino; de
hecho, un idioma destino ajustado a la opción auto no tiene sentido, así el
complemento lo ajusta al valor del cuadro combinado anterior.

Así, imagina esta situación: normalmente traduces al inglés (tu idioma
principal), pero a veces(por ejemplo, cuando escribes un documento)
necesitas traducir al italiano (tu segundo idioma, suponiendo tal); puedes
ajustar el cuadro combinado "Idioma para intercambiar" a Italiano, así
traducirás desde el inglés al Italiano sin acceder directamente a las
opciones del complemento. Obviamente esta función tiene una mayor o menor
utilidad dependiendo de tus necesidades más frecuentes.

Ahora, la casilla de verificación auto intercambiar: aparece si, y sólo si
ajustas la opción auto en el cuadro combinado "Idioma de origen", y está
conectada directamente con el cuadro combinado "Idioma para
intercambiar". Si la activas, entonces el complemento intenta conmutar
automáticamente desde tu configuración origen y destino a una configuración
donde el destino viene a ser el idioma origen , y el idioma seleccionado en
el cuadro combinado "Idioma para Intercambiar" es el nuevo idioma destino;
extremadamente útil si el idioma origen del texto que quieres traducir es el
idioma destino.

Un ejemplo simple: ten nuevamente en cuenta la situación imaginada
previamente; si traduces un texto en un idioma diferente del inglés, no hay
problemas, obtienes la traducción correcta en inglés. Pero si necesitas
traducir un texto del inglés, normalmente obtienes una traducción al inglés
idéntica al texto original, y esto es un poco inútil. Gracias a la función
de auto-intercambiar, sin embargo, asumiendo que quieres saber cómo suena tu
texto en Italiano, el complemento conmuta automáticamente el idioma destino
a Italiano, tal que devuelve una traducción válida.

De todos modos, esto es una configuración temporal; si esta opción no tiene
efecto (es experimental), intenta conmutar manualmente a una configuración
estable, utilizando el gesto para intercambio descrito más abajo. Es
experimental porque en algunas situaciones (con textos cortos, típicamente),
Google no reconoze el idioma origen real correctamente, y tienes que
intercambiar idiomas manualmente a través de script, así fuerzas al idioma
origen a ser el  idioma destino anterior (inglés en nuestro ejemplo).

Al menos, en el diálogo de configuración de parámetros de voz (menú NVDA >> Preferencias >> Voz), puedes querer marcar la opción "Cambio automático de idioma (cuando esté soportado)". De este modo, si usas un sintetizador multiidioma, se anunciará la traducción usando la voz del sintetizador del idioma de destino.

## Utilizando ##
Puedes utilizar este complemento de tres maneras:

1. Selecciona texto usando las órdenes de selección(shift con teclas de
   flecha, por ejemplo) y pulsa la tecla asociada para traducir. A
   continuación, el resultado de la traducción se leerá con el sintetizador
   que estés utilizando.
2. También puedes traducir texto desde el portapapeles.
3. Pulsa la tecla de atajo asociada para traducir el último texto
   verbalizado.

## Atajos de teclado ##
Todas las órdenes que siguen deben pulsarse después de la tecla modificadora
"NVDA+Shift+t":

* T: Traduce el texto seleccionado,
* Shift+t: traduce el texto desde el portapapeles,
* S: intercambia idiomas origen y destino,
* A: anuncia la configuración actual,
* C: copia el último resultado al portapapeles,
* I: identifica el idioma del texto seleccionado,
* L: traduce el último texto verbalizado,
* O: abre el diálogo de opciones de traducción
* H: anuncia todas las órdenes disponibles de capa.

## Cambios para 4.4.3 ##
* Añadida la posibilidad de reemplazar subrayados con espacios, puede
  proporcionar mejores resultados de traducción según el contexto (gracias a
  Beka Gozalishvili)
* Añadida compatibilidad con NVDA 2022.1

## Cambios para 4.4.2 ##
* Se restaura la detección de idiomas y el intercambio automático (gracias a
  Cyrille por la corrección)
* se han actualizado los idiomas para traducir (gracias a Cyrille)

## Cambios para 4.4 ##
* Instant Translate ahora es compatible con NVDA 2019.3 (versiones de NVDA
  basadas en Python 3)

## Cambios para 4.3 ##
* corrección de compatibilidad con NVDA. Ahora, Instant Translate es
  compatible con las compilaciones de NVDA más recientes.
* se ha encontrado una forma de usar Google como servicio de traducción otra
  vez.

## Cambios para 4.2 ##
* Se restaura el funcionamiento con versiones más recientes de NVDA.
* Se restaura la detección automática de idiomas.

## Cambios para 4.1 ##
* InstantTranslate está funcionando otra vez, ahora usa el servicio de
  traducción de Yandex en vez de Google.

## Cambios para 4.0 ##
* La traducción se realiza automáticamente después del intercambio.
* Corregido el error en la memoria caché.

## Cambios para 3.0 ##
* Cambia la forma de cómo se utilizan los atajos de teclado, ahora puedes
  pulsar la tecla modificadora de instantTranslate "NVDA+Shift+t", y luego
  letras solas para llevar a cabo alguna acción (Mira todas las órdenes en
  la sección "Atajos de teclado").
* Implementado el intercambio de idiomas.
* Formato de configuración cambiado, ahora podemos cambiar las opciones de
  instant translate si estamos en un panel de sólo lectura, pero recuerda
  que esto funcionará antes del primer reinicio de NVDA.
* Eliminado el límite de cantidad de texto que puede ser traducido.
* Añadido un atajo de teclado al elemento de menú Opciones de Instant
  Translate
* La opción auto se encuentra ahora en la primera posición en el cuadro
  combinado de origen, y ausente en el cuadro combinado de destino.
* Añadida una casilla de verificación para configurar el copiado de los
  resultados de la traducción.
* Almacenar el fichero config en la raíz de la carpeta de configuraciones.
* Los idiomas fuente y destino se sincronizaron con lo que actualmente
  expone Google Translate (22 Apr 2015).


## Cambios para 2.1 ##
* Ahora el complemento puede traducir texto desde el portapapeles cuando se
  presione NVDA+shift+y.

## Cambios para 2.0 ##
* Añadida una Interface Gráfica de Usuario para el configurador donde
  puedes elegir los idiomas de origen y de destino.
* Añadido un elemento de menú al complemento que se encuentra en el menú
  preferencias.
* Las configuraciones ahora se escriben en un fichero config separado.
* Los resultados de la traducción se copian ahora automáticamente en el
  portapapeles para manipulaciones futuras.

## Cambios para 1.0 ##
* Versión Inicial.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=instantTranslate

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
