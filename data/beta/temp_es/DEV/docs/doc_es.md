#Manual TCA-Media Downloader 3

TCA-Media Downloader 3 es una aplicación escrita en Python 3 la cual es totalmente accesible 
con lectores de pantalla.

Está basada en la librería YT-DLP, la cual nos permite descargar contenido multimedia de 
cientos de sitios. [Aquí puede consultar los sitios que soporta oficialmente](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md):

Además, TCA-Media Downloader 3 usa FFMPEG, librería  la cual, combinada con YT-DLP nos 
permite convertir nuestras descargas a distintos formatos.

Principalmente TCA-Media Downloader 3 esta enfocado a YouTube, pero como se comenta es 
compatible con más sitios añadiendo compatibilidad con algunos no oficiales. Esto último 
dependerá si YT-DLP puede obtener la información necesaria para poder descargar, si detecta 
multimedia de la página que proporcionemos.

Este manual, pretende describir la interface de TCA-Media Downloader 3 en su primera 
versión. Las novedades que en las distintas actualizaciones se agreguen estarán reflejadas en el 
apartado [Registro de cambios](#registrodecambios), en dicho apartado se pondrá las nuevas opciones y su 
descripción por lo que el manual principal será solo detallando la primera versión.

Igualmente cuando recibamos una actualización, se intentará proporcionar una descripción 
detallada de las novedades que se incluyen en dicha actualización.

TCA-Media Downloader 3 viene con un actualizador incorporado, que nos brindará las 
actualizaciones del programa. Dichas actualizaciones estarán divididas en 3 secciones, Librería, 
Funciones y Completa.

1. Actualizaciones en la rama Librería: Esta rama recibirá actualizaciones menores de librerías y corrección de errores.
2. Actualizaciones en la rama Funciones: Esta rama recibirá actualizaciones de nuevas funciones agregadas a la aplicación. Aquellas ampliaciones o mejoras de funciones ya implementadas estarán en Librería; en esta rama solo las funciones nuevas.
3. Actualizaciones en la rama Completa: En esta rama se recibirán actualizaciones completas de la aplicación. Esta rama actualizará por completo todos los componentes de la aplicación y será usada para actualizar con nuevas funciones, corrección de errores mayores o librerías críticas.

Al buscar actualizaciones, en la descripción, se especificará a que rama pertenece la actualización y siempre podremos saber con la nomenclatura de la versión que se actualizó.

TCA-Media Downloader en su primera versión será 3.0.0.0, el primer 0 pertenece a la rama 
Completa, el segundo a la rama Función y el último a la rama Librería.

Este manual describirá lo principal de la aplicación dejando al usuario su exploración y que descubra por sí, todo el potencial que se a intentado dotar a TCA-Media Downloader 3 para 
nuestro disfrute.

Como adelanto decir que TCA-Media Downloader en esta versión incorpora nuevos formatos de descarga, más opciones de descarga, nuevas posibilidades de personalizar la misma y, algo 
que pocos tienen, por no decir ninguno.

Podremos buscar vídeos, como en las versiones anteriores, pero además ahora podremos buscar PlayList y Canales de una manera rápida y sencilla y poder interactuar con dichos 
resultados.

Asimismo, en esta versión es posible tener múltiples descargas a la vez con la capacidad de poder reproducir simultáneamente, mientras seguimos usando la aplicación.

Se pretende agregar muchas opciones nuevas que ya están en desarrollo y, algunas pensadas.

En esta primera versión se a intentado dar lo que TCA-Media Downloader 2 tenía, pero vitaminado y con nuevas características Con el fin de dar lo más estable posible la versión final.

Una vez se Compruebe que la versión final esta estabilizada se empezarán a incorporar nuevas funciones que creo serán del agrado de todos.

##Descripción de la interface

En esta primera versión podemos decir que la aplicación esta dividida en 3 secciones:

1. Pestañas.
2. Reproductor.
3. Controles.

###Pestañas

En esta primera versión tenemos 3 pestañas, URL (Alt+1), Búsqueda (Alt+2) y Descargas (Alt+3).

Podremos movernos entre ellas rápidamente con las teclas Alt+1, alt+2 y alt+3, así como con Ctrl + Tab 
para ir a la siguiente pestaña o Ctrl + Shift + Tab para ir a la pestaña anterior.

Podremos saber en cualquier momento en que pestaña estamos pulsando la combinación Ctrl+Espacio.
####URL (Alt+1)

En esta pestaña, cuando sea enfocada, nos dejará en el campo para introducir una URL.

Solo funcionará si detecta que lo que introdujimos fue una dirección de internet, de lo contrario, no hará nada.

Como e mencionado, esta aplicación principalmente esta enfocada a YouTube, por lo que si ponemos una URL de YouTube, nos detectará que clase de URL es.

#####vídeo, PlayList o Canal.

En caso de que no sea una URL de YouTube y sea de otra página web compatible o, que deseemos probar si podemos descargar multimedia de ella, nos dará Otras posibilidades de descarga.

Bien, una vez pongamos una URL, si pulsamos intro se nos desplegará un menú contextual, con opciones relacionadas con dicha URL, las opciones cambian dependiendo de la clase de URL introducida.

En una URL de YouTube de vídeo tendremos las siguientes opciones:

* Descarga normal: Esta opción nos permitirá descargar el vídeo con las opciones que hayamos elegido (descritas más adelante), nos agregará la descarga con la propiedad vídeo y con 
formato (explicado más adelante), la descarga podremos verla en la pestaña Descargas (Alt+3).
* Descarga personalizada: Esta opción nos abrirá un diálogo donde nos dará la posibilidad de elegir un formato y ver sus propiedades, esto es para usuarios avanzados que conozcan los códex de audio y vídeo.
* Información del Vídeo: Esto nos abrirá un diálogo donde podremos ver información de éste y opciones para dicho vídeo como copiar información diversa al portapapeles, descargar y 
consultar información.
* Reproducir: Nos permitirá reproducir el vídeo en el reproductor incorporado en TCA-Media Downloader 3 (explicado más adelante).

En una URL de YouTube de playlist tendremos las siguientes opciones:

* Descarga toda la PlayList: Nos agregará la playlist con todos sus vídeos a descargar, con las opciones establecidas.
* Elegir vídeos para descargar: Abrirá un diálogo donde poder marcar aquellos vídeos que deseamos descargar, descartando aquellos que no estén marcados.

En este diálogo disponemos también de las siguientes teclas en la lista de vídeos:

* Espacio: Marca o desmarca el ítem seleccionado.
* Ctrl +R: Reproducirá imediatamente ese vídeo.
* Ctrl +D: Descargará imediatamente ese vídeo con las opciones que tengamos asignadas.
* Ctrl +I: Nos dará información de la posición en la que nos encontramos en la playlist.
* Ctrl +F: Nos abrirá un diálogo para escribir una posición y movernos rápidamente en la lista a esa posición. (Esto va bien para aquellas playlist que tienen muchos vídeos.)
* Información de la PlayList: Nos abrirá un diálogo donde podremos visualizar información sobre la playlist, tendremos un área donde nos mostrará los vídeos que contiene dicha playlist 
y tendremos opciones para dicha playlist.

En este diálogo en vídeos de la PlayList, podremos pulsar intro en cada vídeo y obtendremos un menú contextual con las opciones correspondientes a vídeos. Igualmente tenemos varias 
teclas en cada ítem de esa lista:

* Ctrl +R: Reproducirá imediatamente ese vídeo.
* Ctrl +D: Descargará imediatamente ese vídeo con las opciones que tengamos asignadas.
* Ctrl +I: Nos dará información de la posición en la que nos encontramos en la playlist.
* Ctrl +F: Nos abrirá un diálogo para poner una posición y movernos rápidamente en la lista a 
esa posición, esto va bien para aquellas playlist que tienen muchos vídeos.

En una URL de YouTube de canal tendremos las siguientes opciones:

* Descarga todo el Canal: Esto agregará a descargas todos los vídeos que contenga el canal con las opciones que hayamos elegido.
* Elegir vídeos para descargar: Se abrirá un diálogo donde podremos elegir los vídeos que deseamos descargar marcándolos e igualmente descartar aquellos que no deseemos, al abrirse este diálogo puede que nos informe que no hay vídeos en la playlist, esto puede ocurrir por que el 
canal tenga los vídeos protegidos con derechos de autor, tenga los vídeos ocultos, bloqueados por YouTube, bloqueados con contraseña o dichos vídeos del canal estén en playlist en vez de 
la parte principal del canal.

En este diálogo tenemos también la posibilidad de usar varias teclas en la lista de vídeos:

* Espacio: Marca o desmarca el ítem seleccionado.
* Ctrl +R: Reproducirá imediatamente ese vídeo.
* Ctrl +D: Descargará imediatamente ese vídeo con las opciones que tengamos asignadas.
* Ctrl +I: Nos dará información de la posición en la que nos encontramos en la playlist principal del canal.
* Ctrl +F: Nos abrirá un diálogo para escribir una posición y movernos rápidamente en la lista a 
esa posición. (Esto va bien para aquellas playlist que tienen muchos vídeos.)
* Información del Canal: Nos abrirá un diálogo con información sobre el canal y un área con dos pestañas, vídeos y Playlist. Donde poder ver, que vídeos contiene y ver las playlist que 
dicho canal contiene.

En cualquiera de estas dos áreas podemos pulsar la tecla intro en un ítem y nos dará las opciones correspondientes a vídeos o playlist. También podremos usar en el área vídeos Ctrl+r para reproducir, Ctrl+d para descargar, Ctrl+i para saber en qué posición estamos y Ctrl+f para movernos rápidamente al ítem que deseemos.

También en este diálogo dispondremos de distintos botones para poder copiar al portapapeles 
o descargar el canal.

Si ponemos una URL que no pertenece a YouTube, al pulsar intro la aplicación intentará encontrar contenido multimedia.

Si encuentra contenido multimedia para descargar en la URL introducida nos dará dos opciones: Intentar descargar con formato, que nos intentará guardar el archivo con las opciones que tengamos establecidas e Intentar descargar original, que intentará descargar el archivo multimedia en formato original.

En caso de no encontrar contenido multimedia, nos informará con un mensaje.

El cuadro de URL puede ser enfocado rápidamente si estamos en la pestaña URL con (Alt + I).
ígualmente puede ser borrado el campo de la URL siempre que tenga el foco con Ctrl +B.

Las siguientes opciones de esta pestaña son las que quedarán establecidas para las descargas futuras que hagamos tanto de URL como de búsquedas (explicado más adelante).

Si seguimos tabulando en la pestaña URL caeremos en un cuadro combinado llamado Elija Formato: (Alt + F).

En dicho cuadro combinado podremos elegir los distintos formatos soportados por la aplicación tanto de vídeo como de audio. Además, la última opción del cuadro es Avanzado que nos permitirá nuevas opciones de descarga para lo que elijamos descargar.

Si volvemos a tabular tendremos el cuadro combinado Elija calidad del audio: (Alt + C) o Elija 
una opción avanzada de formato personal: (Alt +C)en caso que en el cuadro combinado de 
formato tengamos elegido avanzado.

En la calidad de audio podremos elegir el Bitrate que deseamos para el audio de la descarga, esto siempre es dependiendo si lo que intentamos descargar lo permite, de lo contrario si hemos puesto un bitrate alto siempre nos intentará descargar la mejor calidad de audio.

Si en formato tenemos avanzado este cuadro nos ofrecerá 412 opciones, las cuales no todas funcionan en todos los vídeos o audios que deseemos descargar, esto es ir probando y sobre todo esta sección es para usuarios avanzados. Se recomienda al usuario normal no entrar a esta 
sección.

Cada opción tiene una descripción de lo que se intentará al descargar.

En este cuadro combinado tenemos 2 teclas rápidas:

* Ctrl + I: Que nos informará de la posición en el cuadro combinado en la que nos encontramos.
* Ctrl +F: Que nos abrirá un diálogo para poder movernos rápidamente a una opción de toda la lista.

Si seguimos tabulando caeremos en un cuadro combinado llamado Elija la composición del 
nombre de salida: (Alt + N). Aquí podremos elegir el nombre de los archivos resultantes 
teniendo por el momento la posibilidad además de que se cree un subdirectorio, poder numerar, o no, los vídeos o audios descargados.

Si volvemos a tabular caeremos en una casilla de verificación donde podremos elegir el directorio donde deseamos guardar las descargas (Alt + U).

Esta casilla por defecto viene desactivada y nos guardará las descargas en el subdirectorio por defecto de TCAMediaDownloader dentro del directorio música, creando este directorio en caso de que no exista.
Podemos marcar la casilla y se nos abrirá una ventana donde poder elegir la ubicación personalizada donde deseamos guardar nuestras descargas. Si cuando está marcada la casilla, la 
Desmarcamos, volverá a descargar en la carpeta por defecto.

Hasta aquí pertenece el área URL.

####Búsqueda (Alt+2)

Esta pestaña tiene solo dos componentes:

Introduzca una búsqueda (Alt +B): Aquí podremos poner cualquier texto y pulsar intro para obtener opciones.

Si pulsamos intro con el campo vacío nos dará una única opción: Elegir cantidad de resultados a 
Mostrar, que es un submenú donde podremos elegir la cantidad de resultados que deseamos obtener, nos deja elegir entre 10 y 500 resultados. Esta opción se queda guardada hasta que la volvamos a modificar.

Si introducimos un texto y pulsamos intro nos dará opciones para buscar vídeos, playlist o canales, al igual que nos mostrará la opción anterior para cambiar la cantidad de resultados que 
deseamos. Esto se nos mostrará en un menú contextual.

Si elegimos cualquiera de las 3 primeras opciones nos buscará sobre el término que hayamos 
introducido en el cuadro de búsqueda.

Este cuadro de búsqueda puede ser borrado rápidamente con (Ctrl +B), lo cual limpiará el campo de búsqueda y los resultados. También podemos borrar con retroceso el campo 
búsqueda y dar a intro, entonces nos saldrá un menú con Limpiar búsqueda el cual limpiará el campo de búsqueda y resultados y también nos dará la posibilidad de modificar la cantidad de resultados.

Los menús son dinámicos depende de la acción que hagamos.

Bien si tabulamos caeremos en una lista llamada Resultados de la búsqueda (Alt + R): En dicha lista podremos pulsar intro en cualquiera de los resultados y nos dará las mismas opciones que 
ya han sido descritas en la pestaña URL para cada búsqueda.

Hay algunas opciones añadidas si la búsqueda se trata de vídeo.

Podremos usar Ctrl + R para reproducir rápidamente un vídeo, Ctrl + D para descargarlo y además cuando pulsemos intro sobre dicho vídeo tendremos la siguiente opción nueva en el menú:

Descargador múltiple para la búsqueda: Esta opción nos abrirá un diálogo donde se mostrarán todos los resultados de la búsqueda, dejándonos elegir aquellos vídeos que deseamos descargar.

Este diálogo es ideal para seleccionar de una vez todo lo que deseamos y no tener que ir descargando, uno a uno.

En la lista de este diálogo de los vídeos podremos usar las teclas, espacio para marcar o 
desmarcar, Ctrl +R para reproducir, Ctrl + D para descargar el ítem que esté enfocado. Además, si damos intro, nos dará las opciones en un menú para los vídeos, ya explicado más arriba.

Si tabulamos caeremos en un cuadro de edición donde tendremos que introducir el nombre para la descarga múltiple, este nombre aparte de identificar la descarga lo que hará es crear un subdirectorio con lo que hayamos puesto en nuestro directorio de descargas y en dicho 
subdirectorio se hará la descarga múltiple de todo lo que elijamos en este diálogo.

Hasta aquí la pestaña Búsqueda.

####Descargas (Alt+3)

Esta pestaña es también sencilla con dos controles.

Una lista donde tendremos las descargas, a la cual podemos acceder rápidamente con (Alt+ L) y, si tabulamos, un campo de solo lectura llamado estado (Alt + E). También hay una barra 
de progreso que nos indicará el estado de la descarga que tengamos elegida en la lista.

En la lista de descargas, nos dirá a que clase pertenece la descarga. Si Vídeo, PlayList, Canal 
u otros y, además nos pondrá el formato. El formato dependerá de lo que tengamos elegido en la pestaña URL. También el nombre de la descarga.

Si pulsamos intro en una descarga nos dará un menú con opciones, este menú es dinámico 
dependiendo de las descargas y su estado.

Si la descarga esta en curso nos permitirá:

* Reproducir (solo en descargas de vídeo)
* Abrir enlace de la descarga en la web
* Copiar el enlace de la descarga al portapapeles

Si la descarga a terminado también nos ofrecerá:

* Abrir carpeta de la descarga
* Además, nos permitirá en un submenú llamado acciones generales si hay descargas terminadas:
* Limpiar descargas terminadas

* Si se produce un error y tenemos elegida la descarga del error nos permitirá una nueva opción 
que es ver el error donde nos dará un diálogo con el error que se produjo y la posibilidad de copiar dicho error al portapapeles.

También en el submenú acciones generales nos saldrá una opción para limpiar las descargas 
erróneas en caso de haberlas.

Si tabulamos caeremos en el cuadro de solo lectura donde se nos dará una pequeña información sobre el estado de la descarga y lo que se está haciendo.

Hasta aquí la pestaña descargas.

###Reproductor

En este apartado si tabulamos y no hay nada reproduciéndose se saltará a la siguiente sección 
(Controles), ya que esta sección solo contiene los botones de reproducción, cuando está activa.

Los botones son:

* Atrasar (F1)
* Reproducir (F2) o Pausar (F2) dependiendo del estado
* Adelantar (F3)
* Detener (F4)

Tanto en el botón Atrasar (F1) como en el botón Adelantar (F3)podemos pulsar la tecla aplicaciones, Shift F10 o Ctrl + M, para obtener un menú, el cual nos permitirá elegir el tiempo de 
retroceso o adelanto, de la pista que estemos reproduciendo.

La opción que elijamos en dicho menú será la definida hasta que vuelva a ser cambiada.

El reproductor puede ser manejado con las teclas de atajo citadas  más arriba, desde cualquier parte o diálogo de la aplicación exceptuando el diálogo de Ajustes y de 
Actualizaciones.

En estos dos diálogos, donde no se puede manejar el reproductor, cuando sean abiertos, pausará la reproducción hasta que los diálogos se cierren.

Hay que tener en cuenta que si alguna de las acciones de dichos diálogos necesitan reiniciar la aplicación, la reproducción se detendrá y, si lo 
Deseamos, tendremos que volverla a reanudar  nosotros.

###Controles

En esta sección tendremos:

####Volumen: (F5 / F6):
Con dichas teclas bajaremos o subiremos el volumen al igual que si pulsamos (Alt + V) y el control está enfocado, con flecha izquierda o derecha o flecha abajo o arriba, bajaremos o subiremos respectivamente el volumen.
####Velocidad: (F7 / F8):
Podemos también pulsar para enfocar este control (Alt + V), esta combinación alternará entre volumen y velocidad dependiendo que control tenga el foco. 
* con F6 y F7 o flecha izquierda o derecha o abajo o arriba, disminuiremos o aumentaremos la velocidad de reproducción. Tenemos que tener cuidado por que si ponemos mucha velocidad puede que el buffer de reproducción se quede sin datos y puede dar error, esto no pasa en todos los vídeos y depende también mucho de la conexión a internet de la que dispongamos.
####Salida de audio:
Este cuadro Combinado podemos enfocarlo rápidamente con (Alt + S) pero dicho control solo estará disponible si la reproducción esta activa ya sea reproduciendo o pausada. 
Podremos elegir por que dispositivo deseamos que se reproduzca  el sonido.
Aclarar que cuando la reproducción se detenga, el dispositivo vuelve a ser el predeterminado, por lo que si en la siguiente reproducción deseamos otro dispositivo tendremos que volver a elegirlo. Esta opción no puede ser guardada por motivos técnicos, en la actualidad.
Si en un  futuro se encuentra una solución, se permitirá elegir al usuario, por qué dispositivo desea que el sonido se reproduzca.
####Pantalla de vídeo (F11):
Podemos también, si la reproducción esta activa, ya sea reproduciendo o en pausa, acceder al control rápidamente con (Alt + P). El control es una casilla de verificación que si la verificamos con espacio nos mostrará una pantalla completa con el vídeo pudiendo ver su contenido. Por defecto el vídeo viene desactivado reproduciendo solo el audio, pero en cualquier momento y desde cualquier diálogo podemos activar la pantalla de vídeo con F11 exceptuando en los diálogos de Ajustes y Actualizaciones. La pantalla de vídeo también admite F1 para atrasar, F2 para reproducir / pausar, F3 para adelantar, F4 para detener y la pantalla se cerrará, F5 y F6 para bajar y subir volumen, F7 y F8  para aumentar la velocidad de reproducción y teclas explicadas más adelante. Decir que esta pantalla se puede cerrar continuando la reproducción con escape o perdiendo el foco se cierra automáticamente. Esto último quiere decir que si estamos en la pantalla de vídeo y pulsamos Alt + Tab, al perder el foco la ventana se cerrará.

###Botón Menú (Alt + M):
Este menú contendrá herramientas y distintas opciones y acciones generales. En esta primera versión contiene lo siguiente:

####Buscar actualizaciones:
Nos buscará actualizaciones, si no encuentra nos informará y, si encuentra, abrirá un diálogo dándonos información y dando la posibilidad de actualizar. Decir que esta opción solo puede ser llamada si no tenemos descargas activas.
####Opciones:
Nos abrirá un diálogo con opciones de la aplicación (explicado en la siguiente sección)
####Manual:
Nos abrirá en nuestro navegador esta documentación.
####Entra a nuestro sitio web:
Abrirá la página principal del blog.
####Acerca de...:
Nos dará información de la versión del programa, versión de librerías, y versión de Python con la que fue compilada la aplicación.
####Salir:
Saldrá de la aplicación comprobando antes si tenemos descargas activas, en dicho caso se nos informará con un diálogo donde deberemos elegir si deseamos realmente salir. También podemos salir con Alt + F4 desde la interface principal.

###Diálogo de opciones

Este diálogo en esta primera versión tiene distintas áreas.

Cuando lo abramos, el foco quedará en una lista donde están las distintas áreas, pudiendo movernos con flecha arriba y abajo.

Se agregarán en este diálogo nuevas secciones y opciones conforme el programa vaya incluyendo nuevas funciones.

Cuando estemos encima del área que deseamos si tabulamos caeremos en las opciones de dicha área y podemos movernos con tabulación por ellas.

En esta primera versión nos ofrece las siguientes secciones:

####General:
Esta área contiene opciones de carácter general, cuyas opciones son:

#####Cambiar idioma de la aplicación:
Al pulsar este botón nos dará un menú con los idiomas que la aplicación admite. Actualmente admite 85 idiomas de los cuales en esta primera versión oficial solo es el español y el resto de idiomas, son generados automáticamente por un traductor. En una siguiente sección de este documento se explica el funcionamiento y como, quien lo desee, puede agregar un idioma y hacer que su idioma sea oficial para la aplicación. Más adelante hablaré de los idiomas y daré más información técnica para traductores.
#####Elija la pestaña de inicio de la aplicación:
Podremos en este cuadro combinado elegir que pestaña será la que cargue al iniciar la aplicación.
#####Minimizar a la bandeja de sistema cuando se minimice la ventana principal:
Si activamos esta casilla y minimizamos la ventana, en vez de quedar minimizada, se esconderá a la bandeja de sistema, apareciendo un nuevo icono con el nombre TCA-Media Downloader y su versión. Si pulsamos en el icono directamente se abrirá la ventana de TCA-Media Downloader, si pulsamos botón izquierdo nos dará un menú para abrir o cerrar la aplicación y, si pulsamos doble clic se abrirá la aplicación. Esto a futuro tendrá nuevas opciones, el icono solo aparecerá cuando se esconda la aplicación en caso de estar restaurada, el icono desaparecerá de la bandeja de sistema.
####Descargas:
Aquí iré agregando aquellas opciones que sean referida a las descargas.

Actualmente tenemos:

#####Continuar descargas no terminadas (experimental):
Si marcamos esta casilla nos aparecerá un diálogo explicando su funcionamiento pero resumiendo, lo que intentará es que si cerramos la 
aplicación y quedaron descargas activas si volvemos a poner la misma URL o búsqueda y volvemos a descargar si detecta rastros de que esa descarga ya estuvo, en vez de empezar desde el principio, intentará continuar la descarga por donde se interrumpió.

Decir que esta opción esta en modo experimental y que no es seguro que funcione en todos los casos.

####Reproductor:
Aquí pondré lo referido al reproductor.

Actualmente trae lo siguiente:

#####Reproducir la mejor calidad (no mostrará el menú para elegir calidad al pulsar reproducir):
Por defecto esta casilla esta marcada por lo que cuando reproduzcamos un vídeo, siempre nos dará la mejor calidad que encuentre de dicho vídeo. Si desmarcamos esta casilla al dar a 
reproducir en un vídeo nos dará un menú donde podremos elegir la calidad de reproducción, baja, media o alta siempre y cuando esté disponible. En algunos vídeos puede por ejemplo 
darnos solo calidad baja y media o baja y alta o media y alta. Todo depende de que calidad encuentre.

Esto queda a gusto del usuario su configuración, fue puesta para aquellos usuarios con conexiones limitadas, puedan tener la posibilidad de elegir si desmarcan la casilla por 
ejemplo calidad baja para ahorrar datos de conexión.
#####Mostrar pantalla de vídeo al reproducir:
Por defecto esta casilla esta desmarcada.

Si la marcamos, cuando empiece la reproducción de un vídeo se abrirá automáticamente la pantalla de vídeo.

En dicha pantalla podremos emplear las teclas de reproducción desde F1 A F12.

Decir que la pantalla de vídeo si pierde el foco se cierra y tendremos que volver a abrirla para seguir viendo el contenido de manera visual.
####Sonido:
Aquí podremos personalizar que sonidos deseamos que se reproduzcan y cuales no.

Actualmente podemos activar o desactivar los siguientes:

* Reproducir sonido inicio (sonará en las cargas de la aplicación al iniciar lentas)
* Reproducir sonido de espera (sonará en los diálogos de espera)
* Reproducir sonido de nueva descarga (sonará al añadir una descarga nueva)
* Reproducir sonido al terminar una descarga exitosa
* Reproducir sonido al terminar una descarga errónea
* Mandar mensajes de información de acciones al lector de pantallas

Las anteriores casillas podemos seleccionar para que suenen o no. Por defecto vienen todas activadas.


Decir algo sobre Mandar mensajes de información de acciones al lector de pantallas, esta opción nos dará información sobre distintas acciones que se realizan en la aplicación, por ejemplo cuando pulsamos Ctrl + B en el campo de URL nos dirá campo de url borrado, esto 
será el lector de pantallas quien nos informe.

También en las teclas de reproductor, subir volumen o bajar, o en la velocidad nos dirá por ejemplo subiendo volumen 95%, o reproduciendo, pausando, adelantando 30 segundos, etc. 
Estos son mensajes enviados al lector de pantallas si la casilla está activada, en caso de no estar activada, dichos mensajes no saldrán.

Hay tres combinaciones de teclas que, aunque tengamos desactivada la casilla, serán enviadas al lector. Son las siguientes:

* F9: Nos dirá el tiempo transcurrido y total de la pista que este activa en el reproductor, en caso de no haber ninguna, nos dirá sin nada en reproducción.
* F10: Nos dirá el titulo de la pista que esté en reproducción, en caso de no haber nada, nos informará.
* Ctrl + O: Esta combinación nos dará información rápida de las opciones de descarga que tengamos establecidas en la pestaña URL.
* Ctrl + S: Esta combinación nos dará información de las descargas activas, terminadas y erróneas.

Estas teclas pueden ser llamadas y usadas en cualquier parte de la aplicación excepto en 
Ajustes y Actualizaciones.

También después de las casillas para los sonidos tenemos el siguiente cuadro combinado:

#####Muestra de sonidos (seleccione un sonido y pulse ctrl+r para reproducirlo):
en este cuadro, si pulsamos Ctrl + R, nos dará la muestra del sonido, así podremos identificar los sonidos de la aplicación.

Y para finalizar, este diálogo de opciones, dispone de los botones Aceptar y cancelar.

Si aceptamos, guardará los cambios y, si cancelamos, no guardará nada de lo que hayamos cambiado.

Advertir que el cambio de idioma requiere que la aplicación sea reiniciada y que solo dejará cambiar de idioma si no hay descargas activas.

##Resumen de teclas importantes

###Para el reproductor:

* F1: Atrasar
* F2: Reproducir / Pausar
* F3: Adelantar
* F4: Detener
* F5: Bajar volumen
* F6: Subir volumen
* F7: Bajar velocidad
* F8: Subir velocidad
* F9: Tiempo transcurrido / tiempo total
* F10: Título de la reproducción en curso
* F11: Activar o desactivar pantalla de vídeo
* F12: Activar o desactivar mensajes hablados por el lector de pantalla
* Ctrl + M: Muestra el menú para elegir tiempo de adelantar y atrasar solo en dichos botones del reproductor

###En las listas de vídeo:

* Ctrl + R: Reproducir
* Ctrl + D: Descargar
* Ctrl + I: Posición en la lista
* Ctrl + F: Diálogo para moverse a una posición en la lista
* Intro: Acción sobre el ítem enfocado y otras opciones dependiendo donde nos encontremos
* Espacio: Solo en las listas que sean de selección tendrá efecto marcando o desmarcando el ítem enfocado

###En el resto de las listas que no son de vídeo y campos de texto:

* Ctrl + B: Borra los campos de texto
* Intro: Nos brinda el menú con las opciones correspondientes a donde nos encontremos

###Cuadro combinado de Elija una opción avanzada de formato personal::

* Ctrl + I: Informa de la posición en el cuadro combinado
* Ctrl + F: Muestra el diálogo para elegir a que posición queremos dirigirnos del cuadro combinado

###Diálogo de espera:

En el diálogo de espera que aparece cada vez que ejecuta una acción hay una combinación de teclas especial de pánico.

Dicha combinación es:

Shift + Ctrl + Alt + K

Esta combinación es experimental y solo tiene que usarse en caso que el diálogo de espera se demore en exceso y la aplicación no realice la acción que hemos solicitado.

Solo usar en casos puntuales y cuando sea un tiempo excesivo que dicho cuadro permanezca.

###Otras:

* Ctrl + O: Nos dará la información de formato, calidad, nombre y ubicación en un mensaje hablado.

Estas opciones son las que tengamos definidas en la pestaña de URL y son las que se establecen para las descargas.

* Ctrl + S: Información del estado de las descargas

Nos informará con un mensaje en nuestro lector si hay o no descargas.

Si hay nos dirá el número de descargas activas, terminadas y erróneas.

Esta tecla funciona en cualquier parte de la aplicación excepto en el diálogo de actualizaciones, ajustes, espera y diálogo de elegir posición.

##Información sobre los idiomas de la aplicación

Como mencioné con anterioridad, en esta versión primera, solo el idioma español es oficial, siendo los otros 84 generados automáticamente por un traductor.

Si alguien desea contribuir con un idioma oficial tiene que seguir los pasos a continuación.

En el directorio DATA/LOCALE están todos los idiomas. Solo tiene que ir al suyo y modificar el archivo base.po.

Puede borrar la traducción automática y hacer la suya propia o corregir la traducción automática, luego guardar los cambios y generar el archivo .po. Con eso su idioma la próxima 
vez que reinicie ya reflejara sus cambios.

Si desea hacerlo oficial háganos llegar el base.po a través de los medios de contacto que hay en 
el blog de Tecnoconocimiento Accesible.

Si su idioma no se encuentra entre los incluidos todavía puede añadirlo.

En la carpeta DATA/LOCALE hay un archivo llamado main.pot, puede abrir el archivo y generar 
una plantilla po para su idioma.

Luego solo tiene que seguir la misma estructura de directorios que hay para agregar su idioma 
y guardar el base.po con su traducción en el directorio del nuevo idioma que desea agregar.

La próxima vez que se inicie la aplicación ya podrá elegir su idioma.

Puede mandar igualmente el base.po con el nuevo idioma a los contactos del blog y se 
agregará el nuevo idioma de manera oficial.

Advertir que en aquellas actualizaciones que en la descripción se ponga que se 
actualizarán idiomas, si hemos hecho alguna modificación por nuestra cuenta, dicha 
modificación se sobrescribirá por la de la actualización por lo que recomiendo se guarde antes 
cualquier cambio que hayamos echo y luego lo copiemos a mano de nuevo.

De lo contrario la actualización como digo borrara cualquier modificación que no sea oficial.

Si la modificación es oficial los cambios no se perderán.

Decir igualmente que solo se da soporte a las traducciones oficiales no asegurando que las 
traducciones automáticas funcionen correctamente ni su traducción sea perfecta, al el contrario, 
seguro que tienen muchos fallos pero en la mayoría de casos puede servir para que el usuario 
que no conoce otro idioma pueda usar medianamente en su lenguaje la aplicación.

## Observaciones técnicas

La aplicación en el directorio DATA/LOGS guardará archivos de depuración.

Dichos archivos contienen información de errores que se pueden producir, por lo que se pide 
encarecidamente que si se reporta un error se adjunten dichos archivos.

Cuando se produce un error intentar ver exactamente a la hora que se a producido ya que en 
los archivos de log se guarda la hora y, así si el archivo tiene más de un error, con esos archivos y 
la hora a la que se produjo el error, es más fácil de detectar.

Se a intentado que la aplicación tenga protecciones para que nunca quede congelada ni quede 
inutilizable y se a intentado contemplar la mayoría de los errores que pueden surgir.

Pero entender que es imposible contemplar absolutamente todos, por lo que con las distintas 
actualizaciones que se vayan haciendo se intentará que la aplicación cada vez sea más robusta.

También advertir del abuso de agregar descargas, cada descarga que agreguemos requiere recursos por lo que si ponemos muchas descargas y nuestro equipo no tiene suficientes recursos podemos llegar a bloquear el equipo.

Usar con responsabilidad y teniendo en cuenta que cada descarga requiere de memoria RAM y de ancho de banda de internet.

##Observaciones
En ocasiones, podemos encontrar un canal que, al parecer no contenga vídeos.
En este caso procederemos de la siguiente manera:

1. Para volver a los resultados de búsqueda pulsaremos escape
2. Sobre el resultado del canal, pulsamos enter y accedemos a su información
3. Una vez allí, nos movemos a la pestaña (listas del canal) con ctrl + Tab
4. Aquí podremos encontrar los canales, si los tiene y, elegir vídeos para descargar de dicho canal.

#Agradecimientos

Quiero dar un agradecimiento especial a los probadores en la fase beta, Gera, Gustavo, Peter, Pepe, Rosa, Romina, Rayo, Óscar, Simone y alguno que seguro me olvido. Disculpar.

Igualmente, a los traductores oficiales:

* Italiano: Simone Dal Maso
* Turco: Umut Korkmaz
* Inglés: slanovani
* Ucraniano: Iván Shtefuryak, Volodímir Pyrig
* Ruso: Valentin Kupriyanov
* Árabe: Moataz Geba

#Registro de cambios.<a name="registrodecambios"></a>

Recordar que en esta sección se agregarán las nuevas funciones no modificando el documento 
principal siendo una orientación conforme vayan saliendo actualizaciones.

Por lo tanto una vez ya estemos familiarizados con la aplicación en su primera versión es 
recomendable visitar esta sección para ver las novedades ya que aquí se pondrán las nuevas 
funciones, su descripción y sus atajos de tecla.

Solo se agregarán las versiones de actualización que pertenezcan a las ramas de Funciones y 
Completa.

La rama Librería serán actualizaciones de corrección de errores y de librerías internas, no cambiando nada del manejo de la aplicación.

El usuario es el responsable de revisar esta sección para estar informado de los cambios.

## Versión 3.0.2.0.

* Agregado el poder cambiar de rama de desarrollo de TCA-Media Downloader.

En opciones / general tendremos un botón llamado Alternar rama de desarrollo.

Si pulsamos dicho botón nos permitirá cambiar entre la rama final que es la estable y la beta que es la que recibe las novedades antes pero puede contener errores.

* Solucionado la extracción de información de canales con nombre

Ahora los canales que tengan nombre en vez de id se mostrarán correctamente.

* Se a agregado la posibilidad también de añadir a la base de datos desde los resultados de la búsqueda.

Ahora podremos dar intro en un resultado ya sea de videos, playlist o canales y la ultima opción del menú contextual nos permitirá interactuar con la base de datos de favoritos.

Tendremos las mismas opciones que desde los diálogos de información de video, playlist o canales.

* Agregado Ctrl + R y Ctrl + D en el campo de URL.

Ahora en la pestaña URL si ponemos una URL de un video de YouTube podremos pulsar dichas combinaciones ya sea para reproducir o descargar sin necesidad de desplegar el menú contextual.

* Solucionado problemas con canales que no mostraban PlayList.

* Agregado contemplación de URLs de shorts de YouTube.

Ahora cuando introduzcamos una URL en la pestaña URLs y que dicha URL coincida con
una de tipo shorts se ofrecerán las opciones iguales que si fuese un video de YouTube y
así poder interactuar con dichas URL como si fuese un video.

* Agregado contemplación de URLs de clips de YouTube.

Ahora si ponemos una URL de un clip de YouTube en la pestaña URLS nos dará la posibilidad de descargar con formato o original.

También nos permitirá obtener información del clip mezclado con la ficha original del video donde se extrajo el clip.

Los clips no pueden ser reproducidos con la combinación Ctrl + R ni ser reproducidos.

Los clips tampoco pueden ser añadidos a la pestaña favoritos.

* Agregado en DATA un directorio DEV.

En este directorio se incluye la documentación para que los traductores trabajen en ella, los lenguajes oficiales con las cadenas incluidas y que faltan por traducir y el main.pot para nuevas plantillas de idioma.

A partir de ahora los idiomas vendrán con traducción automática en los idiomas oficiales hasta recibir las traducciones que se encuentran en este directorio.

Solo se traducirán las cadenas que se hayan agregado de una versión a otra de manera automática. De esta manera siempre el programa estará traducido y el traductor oficial puede ir con más tranquilidad en sus traducciones.

En este directorio esta el trabajo del traductor oficial junto a las cadenas que faltan por traducir.

* Agregada la posibilidad de elegir la rama de la librería YT-DLP.

Ahora en opciones en la categoría General podremos elegir la rama a usar de la librería YT-DLP.

Podremos entre Stable y Nightly.

La versión Stable es la versión final de la librería y la Nightly es una versión que va incorporando las novedades pero que no esta tan probada como la Stable.

* Se agrego la comprobación si existen actualizaciones de YT-DLP.

Ahora si buscamos actualizaciones también comprobara aparte de si hay de la aplicación si hay de la librería YT-DLP.

En caso de que haya nos informara. Decir que por defecto siempre primero comprueba si hay actualización de la aplicación y si hay ya no comprobara de YT-DLP por que en las actualizaciones siempre se actualiza YT-DLP con la versión más reciente de la rama Stable.

En caso de no encontrar actualización de aplicación continuara comprobando si hay de YT-DLP y nos informara.

Si actualizamos la aplicación y tenemos seleccionada la rama Nightly de YT-DLP tendremos que buscar nuevamente actualización después de instalar la aplicación para descargar la rama correspondiente.

Esto ultimo es por que las actualizaciones de aplicación solo llevan la rama Stable.

* Se agrega a las notificaciones de actualización también notificaciones de actualización para YT-DLP.

Si tenemos activadas las notificaciones de actualización ahora también buscara de la librería YT-DLP y si encuentra nos dará el número de versión.

Sucede igual que si buscamos actualización en el menú si encuentra actualización de aplicación ya no buscara de YT-DLP hasta que no actualicemos la aplicación.

* Agregada la posibilidad de elegir el inicio en la pestaña favoritos en opciones.

* Arreglado compartir con MASTODON.

* Actualizada la librería YT-DLP a la versión 2023.07.06.

* Se han actualizado librerías internas para un mejor funcionamiento de la aplicación.

* Solucionados errores internos.

* Actualizadas traducciones.

## Versión 3.0.1.0.

* Nueva pestaña llamada Favoritos (Alt + 4).

Ahora podremos guardar aquellos vídeos, playlist o canales que deseemos en esta pestaña para poder ser consultados de una manera rápida.

Cuando caemos en esta pestaña tendremos 3 partes:

Alt + F: Nos dejara en el árbol donde podremos interactuar con las ramas.

El árbol tiene la base llamada favoritos en la cual si pulsamos intro podremos borrar la base de datos por completo, o hacer y restaurar una copia de seguridad de la base de datos.

Tiene una rama llamada Vídeos, en la cual si pulsamos intro podremos crear listas de vídeos, si pulsamos dicha opción se abrirá una ventana para introducir el nombre de la lista.

Cuando tengamos listas de vídeos agregadas podremos desplegar la rama y tendremos subramas con las cuales si pulsamos intro nos aparecerá la posibilidad de editar, borrar o vaciar dicha lista de vídeos.

También tenemos dos ramas en el árbol llamadas PlayList y Canales, si alguna de estas ramas tiene contenido podremos pulsar intro en ellas y borrar su contenido.

Alt + C: Nos deja en la zona de contenido, en esta zona se mostrará el contenido de la lista de vídeos que tengamos seleccionada, de PlayList o Canales.

En esta zona, si pulsamos intro en algún item, se nos mostrará un menú correspondiente a la categoría vídeos, playlist o canales pudiendo interactuar con ellos.

Alt + B: Nos llevara a un cuadro donde podremos hacer búsquedas en la rama que estemos, en este cuadro podremos poner indiferentemente en minúsculas o mayúsculas lo que estemos buscando y pulsar intro para que nos dé el resultado en la zona de consultas, podremos interactuar con el resultado pulsando intro en él.

El campo de búsqueda permite introducir un texto sin necesidad de que sea completo, por ejemplo, si buscamos TCA nos devolverá todos los vídeos si es en la rama que estamos que contengan dichas letras.

Podemos volver la búsqueda a valores originales y restaurar la zona de contenido rápidamente pulsando en el cuadro de búsqueda Ctrl + B o borrando el texto que tengamos escrito y pulsando intro, también desde el área de contenido si hay una búsqueda echa si pulsamos Ctrl + B nos volverá a valores originales.

Para agregar contenido a la base de datos, se hace desde la información de cada rama. Por ejemplo si deseamos agregar un vídeo a una lista que tengamos creada desde la pestaña búsqueda, cuando tengamos resultados de la búsqueda en el item que estemos pulsamos intro y damos a información del vídeo, en la ventana que se abre ahora tendremos un botón llamado Añadir a una lista de vídeos el cual si lo pulsamos nos desplegará un menú con todas las listas de vídeo que tenemos creadas en la base de datos y si elegimos una el vídeo se abrá guardado en dicha lista.

Podemos agregar el mismo vídeo a varias listas pero solo se puede agregar una vez por lista.

En cuanto a las playlist y canales, es similar, yendo al diálogo de información y nos aparecerá un botón llamado Añadir a favoritos. Si lo pulsamos se agregará a la rama de la base de datos que corresponda, el botón entonces pasará a llamarse Quitar de favoritos y mientras no borremos desde la pestaña favoritos o desde el diálogo de información dicha playlist o canal estarán en la base de datos.

Las ramas playlist y canales solo guardarán un mismo item, pudiendo guardar varios con el mismo nombre mientras la url sea distinta.

En el área de consulta podremos pulsar Ctrl + I para saber en que posición estamos y Ctrl + F para movernos rápidamente al item que deseemos.

Se a agregado la posibilidad también de añadir a la base de datos desde los resultados de la búsqueda.

Ahora podremos dar intro en un resultado ya sea de vídeos, playlist o canales y la última opción del menú contextual nos permitirá interactuar con la base de datos de favoritos.

Tendremos las mismas opciones que desde los diálogos de información de vídeo, playlist o canales.

* Agregado Ctrl + R y Ctrl + D en el campo de URL.

Ahora en la pestaña URL si ponemos una URL de un vídeo de YouTube podremos pulsar dichas combinaciones ya sea para reproducir o descargar sin necesidad de desplegar el menú contextual.

* Se a agregado en el cuadro combinado calidad 64 Kbps.

Tendremos una nueva calidad para ahorrar en datos de descarga. Tener en cuenta que la calidad del audio también se reduce.

* Agregada la posibilidad de ver comentarios en un vídeo (experimental).

Ahora cuando abramos el diálogo de información del vídeo aparecerá un botón si dicho vídeo tiene comentarios.

El botón se llama Ver o guardar comentarios y si lo pulsamos nos dejara ver o guardar los comentarios.

Estas opciones son experimentales y se a detectado que en ocasiones puede cerrar la aplicación por lo que si hay descargas en marcha se le avisara al usuario que puede perder la información que se esté descargando.

Si elegimos ver comentarios aparecerá una ventana de extracción de comentarios en la cual nos avisará con un porcentaje de lo que lleva extraído, podemos cancelar la extracción dando al botón cancelar de la ventana.

Una vez termina la extracción se abrirá una ventana con todos los comentarios, en la ventana aparecerán los comentarios en un control de árbol.

Podemos desplegar el árbol y navegar por los comentarios, si el comentario tiene respuestas igualmente podemos desplegarlo para ver sus respuestas.

Aquellos comentarios muy largos, aparecerán con un ** al final ya que no cabe todo el comentario.

Para ello existe una combinación de teclas para que nuestro lector lo lea y es Ctrl + T.

Igualmente, si tabulamos caeremos en un cuadro de solo lectura donde tendremos el comentario íntegro junto con el nombre de quien publicó, la fecha y la cantidad de  me gusta.

En esta ventana hay un botón llamado guardar que lo que hace es lo mismo que en la ventana de información del vídeo en el menú contextual y es guardar los comentarios en un html accesible.

La estructura del html es la siguiente:

Nivel de encabezado 1 para el titulo del vídeo.

Nivel de encabezado 2 para el comentario principal.

Nivel de encabezado 3 para las respuestas al comentario.

Toda la ventana tiene atajos para movernos rápidamente por ella:

Alt + L: Nos deja en el árbol de comentarios.
Alt + D: Nos lleva rápidamente a los detalles del comentario que esté enfocado.
Alt + G: Guarda un html con los comentarios.
Alt + C, Alt + F4 o Escape: Cierra la ventana.

* Nuevas funciones en los menús contextuales y mejoras.

Se han corregido los menús contextuales en la zona de descarga, no saliendo ahora el reproducir en aquellos ítems que no sean vídeos.

Se a corregido que si solo hay un resultado de vídeos no salga el menú para descarga múltiple, tampoco si solo hay un vídeo en la base de datos no saldrá.

Se a agregado a aquellos menús que se adecúan al contexto nuevas opciones como:

Abrir en la WEB, que nos abrirá en nuestro navegador el vídeo, playlist o canal que tengamos seleccionado llevándonos a YouTube.

Copiar enlace del video al portapapeles, de la PlayList o Canal: Copia el enlace al portapapeles.

Se agrego un submenú llamado Compartir.

Dicho menú nos permitirá compartir la url con Twitter, Facebook, Telegram, WhatsApp, Mastodon o por código QR con nuestro móvil.

Si elegimos Genera código QR para abrir con el móvil se abrirá una ventana en el centro de la pantalla que contendrá un código QR, si con el lector de nuestro móvil apuntamos a ella una vez lo detecte se abrirá en nuestro dispositivo dicha URL ya sea de vídeo, playlist o canal.

Comentar que en Facebook solo deja compartir la URL, por lo que no podremos añadir automáticamente texto, en la pantalla a la que nos dirige, sí podremos añadir información a mano.

En Mastodon nos pedirá nuestra URL de la instancia en la que estamos, podremos guardarla o modificarla, si lo deseamos. Si la guardamos quedará ya predefinida y no tendremos que agregarla cada vez que queramos compartir con Mastodon.

Advertir que para compartir por cualquiera de las redes sociales, antes tenemos que estar con la sesión iniciada en nuestro navegador, al igual que será más fácil compartir si tenemos las aplicaciones instaladas tanto de WhatsApp como Unigram.

* Agregadas nuevas opciones en el diálogo ajustes.

En la categoría general se ha agregado:

Comprobar si existen actualizaciones y notificar: En este cuadro combinado podemos elegir si queremos que busque actualizaciones y nos notifique con una notificación de Windows.

Podremos elegir o tener desactivada esta opción o que busque si hay actualizaciones en cualquiera de los tiempos que hay en el cuadro combinado.

Cuando encuentre una actualización, se avisará por una notificación de Windows informando que encontró una actualización y su versión.

Esta opción no descarga actualizaciones, solo comprueba cada x tiempo, que hayamos seleccionado, si existen actualizaciones, por lo que tendremos que ir a buscar actualizaciones para descargarla.

Las notificaciones se nos mostrarán cada x tiempo seleccionado hasta que actualicemos.

En la categoría descargas se ha agregado:

Tiempo para extraer información (transcurrido el tiempo dará error si no se obtuvo toda la información, válido para grandes PlayList o Canales): En este cuadro combinado podremos aumentar el tiempo que tardará en decir que no se a podido obtener la información.

Por defecto son 2 minutos en los cuales se intenta obtener la información, ya que es un tiempo prudencial y más que suficiente para la mayoría de PlayList y Canales.

En caso de necesitar más tiempo, porque las Playlist o canales tengan más de 5000 vídeos, podremos aumentar el tiempo de obtención de datos.

* Añadida protección contra la descarga de transmisiones en directo en todos los diálogos.

Se a agregado una protección en la cual se detectara que si la URL que deseamos descargar es una transmisión en vivo no nos dejará.

Esto daba problemas y en próximas versiones se dará una solución alternativa.

* Se han actualizado librerías internas para un mejor funcionamiento de la aplicación.

* Solucionados errores internos.

* Actualizadas traducciones.

## Versión 3.0.0.0.

* Versión inicial.
