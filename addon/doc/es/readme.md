# instantTranslate #

* autores: Alexy Sadovoy, ruslan, Beqa Gozalishvili y otros colaboradores de
  nvda.
* Descargar: [versión 2.2beta2][1]

Este complemento se utiliza para traducir texto seleccionado y/o del
portapapeles de un idioma a otro.  Esto se hace utilizando el servicio
Google Translate.

## Configurando idiomas ##

Para configurar el idioma fuente y el de destino, desde el menú NVDA, ve a
Preferencias, luego ve a Opciones de Instant Translate.  Hay dos cuadros
combinados etiquetados como "Idioma original" e "Idioma de la traducción".
Haz tu selección de idioma y pulsa INTRO sobre el botón Aceptar.

## Cómo utilizar este complemento ##

Hay dos modos de utilizar este complemento:

1. Selecciona algún texto utilizando las órdenes de selección (shift con
   teclas de cursor, por ejemplo). luego pulsa Shift+NVDA+T para traducir el
   texto seleccionado. Entonces la cadena traducida se leerá, siempre que el
   sintetizador utilizado soporte el idioma de destino.
2. Copia algún texto al portapapeles. entonces pulsa Shift+NVDA+Y para
   traducir el texto del portapapeles al idioma de destino.

## Cambios para  2.2 ##
* Aumentado el número de caracteres a 1500.
* Añadido un atajo de teclado al elemento de menú Opciones de Instant
  Translate
* Añadida una casilla de verificación para configurar el copiado de los
  resultados de la traducción.
* Almacenar el fichero config en la raíz de la carpeta de configuraciones.
* Nuevos idiomas: Alemán, Coreano, Eslovaco, Español, Francés, Finlandés,
  Gallego, Húngaro, Italiano, Tamil, Turco.

## Cambios para 2.1 ##
* Ahora el complemento puede traducir texto desde el portapapeles cuando se
  presione NVDA+shift+y.

## Cambios para 2.0 ##
* Añadida una GUI para el configurador donde  puedes elegir los idiomas
  fuente y destino.
* Añadido un elemento de menú al complemento que se encuentra bajo el menú
  preferencias.
* Las configuraciones ahora se escriben en un fichero config separado.
* Los resultados de la traducción se copian ahora automáticamente en el
  portapapeles para manipulaciones futuras.

## Cambios para 1.0 ##
* Versión Inicial.

[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=it
