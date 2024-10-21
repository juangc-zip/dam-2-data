### Ejercicio 1: Analizador de Logs Distribuido
Desarrolla un programa que analice archivos de log de manera distribuida utilizando múltiples procesos. El programa principal debe:
1. Recibir como argumentos el directorio que contiene los archivos de log y un patrón de búsqueda.
2. Crear un proceso hijo por cada archivo de log en el directorio.
3. Cada proceso hijo debe buscar el patrón en su archivo asignado y contar las ocurrencias.
4. Los resultados de cada proceso hijo se deben escribir en un archivo temporal.
5. El proceso padre debe esperar a que todos los hijos terminen, leer los archivos temporales, sumar los resultados y mostrar el total de ocurrencias.
6. Implementa manejo de errores para casos como archivos no encontrados o permisos insuficientes.
Asegúrate de que el programa principal pueda manejar un número variable de archivos de log y que los procesos hijos se ejecuten en paralelo.
### Ejercicio 2: Simulador de Sistema de Compilación
Crea un programa que simule un sistema de compilación distribuida. El programa debe:
1. Recibir como entrada un archivo de "proyecto" que liste varios archivos fuente ficticios.
2. Por cada archivo fuente, crear un proceso hijo que simule la compilación:
    - Leer el contenido del archivo (si existe).
    - Esperar un tiempo aleatorio entre 1 y 3 segundos para simular el proceso de compilación.
    - Generar un archivo ".o" ficticio con un tamaño aleatorio.
3. El proceso padre debe monitorear el progreso de los hijos, mostrando actualizaciones en tiempo real.
4. Una vez que todos los procesos hijos hayan terminado, el padre debe "enlazar" los archivos .o, simulando este proceso con una espera adicional.
5. Finalmente, mostrar un resumen del proceso de compilación, incluyendo tiempos y tamaños de archivos generados.
Implementa un manejo adecuado de errores y asegúrate de que el programa pueda manejar proyectos de diferentes tamaños.
### Ejercicio 3: Procesador de Imágenes Multiprocess
Desarrolla un programa que procese un conjunto de imágenes utilizando múltiples procesos. El programa debe:
1. Recibir como argumentos un directorio de entrada con imágenes, un directorio de salida y una operación a realizar (por ejemplo, "resize", "grayscale", "blur").
2. Crear un proceso hijo por cada imagen en el directorio de entrada.
3. Cada proceso hijo debe:
    - Cargar la imagen asignada.
    - Aplicar la operación especificada.
    - Guardar la imagen procesada en el directorio de salida.
    - Escribir en un archivo de log información sobre el procesamiento (tiempo, tamaño original y final).
4. El proceso padre debe monitorear el progreso, mostrando actualizaciones en tiempo real.
5. Una vez que todos los hijos hayan terminado, el padre debe generar un informe resumen con estadísticas del procesamiento.