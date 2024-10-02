##  PMDM | UNIDAD 1 | ANALISIS TECNOLOGICO PARA DISPOSITIVOS MOVILES
———————————————————————————————————————————————————————————————————————————————————————————
###   1. DISPOSITIVOS MOVILES: TIPOS, HISTORIA Y EVOLUCION
La revolucion de los smartphones, llego con la introduccion de los mismo a finales de los 90 y principios de los 2000. Estos dispositivos combinan la capacidad de hacer llamadas con otras mas actualizadas (acceso a Internet, correo electronico y aplicaciones). BlackBerry: primero smartphones existosos (movil y mensajeria).

La era tactil, llego con el Iphone en 2007, la pantalla tactil capacitiva (introducio apple) permite realizar gestos intuitivos como pellizcar o deslizar.
Hacia el futuro, la evolucion no desacelera, en 2020 llego la tecnologia 5G la cual permite velocidades de Internet aun mas rapidas y con una mayor cantidad de transmision de datos. Ademas de avances como la Realidad Aumentada (RA) o la Realidad Virtual (RV).

Los sistemas operativos de dispositivos moviles estan coronado con un 71,28% por parte de Android y un 28,02% por parte de IOS.
—————————————————————————————————————————————————————————————————————————————
###   2. CARACTERÍSTICAS Y LIMITACIONES EN EL DESARROLLO DE APLICACIONES PARA DISPOSITIVOS MÓVILES
La aplicaciones moviles no son aplicaciones de escritorio adaptadas para dispositivos con pantallas moviles. Es necesario que sean aplicaciones diferentes por:
- Se debe evitar la sobrecarga de elementos multimedia.
- El tamaño de las pantallas y su iluminacion.
- Generar menus poco sobrecargados, facilitando la introduccion de informacion mediante desplegables.
- Distribucion de elemenos en pantalla de forma intuitiva y natural, agrupando los componentes por funcionalidades.
- Durante el envio y la recepcion de datos avisar al usuario del proceso.
- Las conexiones pueden fallar por la falta de cobertura en los dispositivos.
—————————————————————————————————————————————————————————————————————————————
###   3. TIPOLOGÍAS DE LAS APLICACIONES MÓVILES
Podemos encontrar distintos enfoques para desarrollar aplicaciones moviles: aplicaciones nativas, aplicaciones web, aplicaciones hibridas, aplicaciones progresivas (pwa), aplicaciones de compilacion cruzada y apicaciones interpretadas o de Scripting en vivo.
####    APLICACIONES NATIVAS
Estas aplicaciones se crean especificamente para cada plataforma haciendo uso del lenguaje o lenguajes que usa de forma nativa la plataforma. Las ventajas son:
- Se obtiene un acceso total al hardware del dispositivo.
- Maximo rendimiento y fluidez en las aplicaciones.
Pero tambien contienen incovenientes:
- Nuevo desarrollo para cada plataforma.
- Mayor tiempo de desarrollo y mayor coste final.
———————————————————————————————————————————————————————————
####    APLICACIONES HIBRIDAS
Las aplicaciones hibridas (o multiplataforma) combinan elementos ed las aplicaciones nativas y las aplicaciones web. Se desarrollan utilizando tecnologias web como HTML, CSS y JavaScript, sin embargo se empaquetan en un formato que pueden ser instalados en un dispositivo movil como cualquier aplicacion nativa.

Se pretende obetener las ventajas de las aplicaciones nativas y las aplicaciones web. Una aplicacion hibrida utiliza el morot del navegador del dispositivo y sincroniza el contenido HTML, CSS y JavaScript en contenedores web nativos como WebView (Android) o WKWebView (IOS).
———————————————————————————————————————————————————————————
####    APLICACIONES WEB
Estas aplicacones tienen como caracteristica principal su ciclo de vida, en el contexto de un navegador web. Las ventajas que poseen las aplicaciones web son:
- Desarrollo mas versatil, no se depende de un SSOO concreto.
- Mayor rango de difusion al abarcar todas las stores.
Pero tambien poseen incovenientes tales como:
- Especial cuidado con la compatibilidad entre navegadores.
- Acceso muy limitado al hardware del dispositivo.
—————————————————————————————————————————————————————————————————————————————
###   4. ARQUITECTURA ANDROID
Android esta construido sobre un nucleo Linux, pero modificado drasticamente para adaptarse a los dipositivos moviles. Esta eleccion esta basada en la excelente portabilidad, flexibilidad y seguridad que posee Linux. Android esta bajo licencia GPL ya que hereda el Kernel de Linux.

- Capas de librerias nativas, en esta capa se encuentran partes como la HAL, librerias nativas, demonios, las herramientas de consola y manejadores de tiempo de ejecucion. Pero que es la HAL (Capa de Abstraccion de Hardware).
	- Capa de Abstraccion de Hardware (HAL): es el componente que permite la independencia del hardware. esto quiere decir que android esta construido para poder ejecutarse en cualquier dispositivo movil, sin importar la arquitectura fisica. Actua como una arquitectura generica que representa a todos los posibles tipo de hardware que puda haber en el mercado.

- Android Runtime, recordemos que las aplicaciones Android estan escritas en Java o Kotlin estas son traducidas a bytecode e interpretadas por la Maquina Virtual llamada ART, esta herramienta fue diseñada para ser flexible ante el diseño de hardware de un dispositivo movil. Ademas JVM no es de licencia GPL, asi que Google decidio generar su propia herramienta que ha conseguido reducir el tiempo de ejecucion en un 33%.

- Framework para aplicaciones, es la capa que nos interesa, ya que podemos encotrar todas las librerias necesarias para programar nuestras aplicaciones. los paquetes con mas preponderacia son los "android.* " ya que alojan todas las caracteristcas necesarias de una aplicacion Android. Tambien podemos encontrar manejadores, servicios y proveedores de contenido que soportan comunicacion con nuestra aplicacion con Android.

- Capa de aplicaciones, es la ultima instancia/capa del funcionamiento de Android. Esta centrada en la ejecucion, comunicacion y estabilidad de las aplicaciones preinstaladas por el fabricante o las que vamos a construir. A ella acceden los usuarios Android debido a su alto nivel de comprension y simplicidad.
—————————————————————————————————————————————————————————————————————————————
###   5. ARQUITECTURA IOS
IOS se divide en 4 capas o instancias del sistemas operativo, desde la capa mas importante para el desarrollador hasta la mas importante para el hardware o los componentes. Las capas que podemos encontrar en IOS son Cocoa Touch, Media Services, Core Services y Core OS.

- Cocoa Touch, es la capa superior y la mas importante para el desarrollo de aplicaciones en IOS. Es la que los usuarios utlizan para interactuar con las aplicaciones, esta fundamentalmente utilizada por 2 Frameworks: UIKit, clases para el desarrollo de una interfaz de usuario y Foundation Framework, acceso y manejo de objetos y servicios del S.O.

- Media Services, provee los servicios de audio, graficos y multimedia a la capa superior.
- Core Services, proporciona los servicios imprescindibles para el sistemas para poder ser utilizados por todas las apps.
- Core OS, es el nucle del sistema con las caracteristcas de bajo nivel, manejo de memoria, seguridad, drivers...
—————————————————————————————————————————————————————————————————————————————
