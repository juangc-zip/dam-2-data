### Ejercicio 1: Simulador de Biblioteca
Desarrolla un programa que simule el funcionamiento de una biblioteca utilizando hilos. La biblioteca tiene un número limitado de libros (por ejemplo, 5) y varios lectores (por ejemplo, 8) que quieren leerlos.
- Crea una clase `Libro` que tenga un título y un estado (disponible o prestado).
- Implementa una clase `Lector` que extienda `Thread`. Cada lector intentará tomar un libro aleatorio, leerlo durante un tiempo aleatorio (entre 2 y 5 segundos) y luego devolverlo.
- Desarrolla una clase `Biblioteca` que gestione los libros y tenga métodos sincronizados para prestar y devolver libros.
- En el método `main`, crea la biblioteca, los libros y los lectores. Inicia todos los hilos de lectores y espera a que terminen.
- Asegúrate de que no haya condiciones de carrera al acceder a los libros y que los lectores esperen si no hay libros disponibles.
### Ejercicio 2: Productor-Consumidor de Tareas
Implementa un sistema de productor-consumidor utilizando un buffer limitado para tareas.
- Crea una clase `Tarea` con un identificador y una duración en milisegundos.
- Implementa una clase `Buffer` con capacidad para 10 tareas, con métodos sincronizados para añadir y retirar tareas.
- Desarrolla una clase `Productor` que extienda `Thread` y genere tareas con ID y duración aleatoria (entre 100 y 1000 ms) cada 500 ms.
- Crea una clase `Consumidor` que extienda `Thread` y procese las tareas del buffer, simulando su ejecución con `Thread.sleep()`.
- En la clase principal, crea 2 productores y 3 consumidores. Inicia todos los hilos y déjalos correr durante 20 segundos antes de detenerlos.
- Utiliza `wait()` y `notifyAll()` para la sincronización entre productores y consumidores.
### Ejercicio 3: Simulador de Carrera de Relevos con Obstáculos
Crea un programa que simule una carrera de relevos con obstáculos utilizando hilos.
- Implementa una clase `Corredor` que extienda `Thread`. Cada corredor debe completar una vuelta que consiste en correr y superar un obstáculo.
- Crea una clase `Equipo` que contenga 4 corredores y un testigo.
- Desarrolla una clase `Pista` que tenga un método sincronizado para superar el obstáculo (simula un tiempo aleatorio entre 1 y 3 segundos).
- En el método `run()` de `Corredor`, simula la carrera (tiempo aleatorio entre 3 y 5 segundos) y luego llama al método para superar el obstáculo.
- Implementa la lógica para pasar el testigo al siguiente corredor del equipo utilizando `wait()` y `notify()`.
- En la clase principal, crea 3 equipos, inicia la carrera y muestra por consola el progreso y el equipo ganador.
- Utiliza `CountDownLatch` para sincronizar el inicio de la carrera para todos los equipos.