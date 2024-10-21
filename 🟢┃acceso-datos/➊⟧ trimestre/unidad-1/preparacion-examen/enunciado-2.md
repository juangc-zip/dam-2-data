Desarrolla una aplicación de gestión de una biblioteca universitaria utilizando Java. La aplicación debe manejar libros, revistas y recursos digitales, almacenados en archivos de acceso aleatorio separados. Además, debe importar y exportar datos en formato XML y JSON. La aplicación debe implementar un sistema de préstamos con fechas de vencimiento y multas por retraso. Utiliza el patrón Modelo-Vista-Controlador (MVC) y aplica programación concurrente para optimizar las operaciones de búsqueda y actualización en los archivos.

Lista de métodos a desarrollar (divididos por niveles de dificultad):
#### Nivel Fácil
1. Crear clases para Libro, Revista y RecursoDigital con atributos comunes y específicos.
2. Implementar métodos para leer objetos de cada tipo desde sus respectivos archivos de acceso aleatorio.
3. Desarrollar una interfaz de usuario básica que permita buscar recursos por título o autor.
4. Crear un método para validar los datos de entrada del usuario.
5. Implementar un método para calcular la fecha de vencimiento de un préstamo.
#### Nivel Medio
1. Desarrollar métodos para escribir, actualizar y eliminar objetos en los archivos de acceso aleatorio.
2. Implementar un sistema de búsqueda que permita filtrar por tipo de recurso, año de publicación, disponibilidad, etc.
3. Crear métodos para exportar e importar datos en formato XML.
4. Desarrollar un Controlador que maneje las interacciones entre la Vista y el Modelo, incluyendo la lógica de préstamos.
5. Implementar un sistema de multas por retraso en la devolución de recursos.
6. Crear un método para generar reportes de recursos más prestados y usuarios con más préstamos activos.
#### Nivel Difícil
1. Implementar programación concurrente para optimizar las operaciones de búsqueda y actualización en los archivos de acceso aleatorio.
2. Desarrollar un sistema de caché para mejorar el rendimiento de las búsquedas frecuentes.
3. Crear métodos para exportar e importar datos en formato JSON, permitiendo la migración entre XML y JSON.
4. Implementar un sistema de recomendaciones basado en el historial de préstamos de los usuarios.
5. Desarrollar un módulo de estadísticas que utilice streams y lambdas para analizar los datos de préstamos y generar insights.
6. Crear un sistema de notificaciones que alerte a los usuarios sobre préstamos próximos a vencer, utilizando programación asíncrona.
7. Implementar pruebas unitarias y de integración para todos los componentes principales, incluyendo pruebas de concurrencia.