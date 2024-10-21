Desarrolla una aplicación de gestión de inventario para una tienda de electrónica utilizando Java. La aplicación debe manejar productos electrónicos (como smartphones, laptops y tablets) almacenados en un archivo de acceso aleatorio. Además, debe importar y exportar datos de productos en formato XML. Implementa la aplicación siguiendo el patrón Modelo-Vista-Controlador (MVC).

Lista de métodos a desarrollar (divididos por niveles de dificultad):
#### Nivel Fácil
1. **Crear una clase Producto** con atributos como id, nombre, precio y stock.
2. **Desarrollar un método para leer objetos Producto** desde el archivo de acceso aleatorio.
3. **Implementar un método para buscar un Producto por su id** en el archivo de acceso aleatorio.
4. **Crear una interfaz de usuario (Vista)** que permita al usuario realizar operaciones básicas (Crear, Leer).
5. **Desarrollar un método para validar los datos de entrada del usuario** antes de realizar operaciones en el Modelo.
#### Nivel Medio
1. **Implementar un método para escribir objetos Producto** en un archivo de acceso aleatorio.
2. **Implementar un método para actualizar la información de un Producto** en el archivo de acceso aleatorio.
3. **Desarrollar un método para eliminar un Producto** del archivo de acceso aleatorio.
4. **Crear un Controlador que maneje las interacciones** entre la Vista y el Modelo.
5. **Implementar manejo de excepciones** para operaciones de archivo.
#### Nivel Difícil
1. **Desarrollar un método para exportar todos los Productos a un archivo XML.**
2. **Implementar un método para importar Productos desde un archivo XML.**
3. **Desarrollar un método para generar reportes de inventario**, mostrando productos con bajo stock.
4. **Crear pruebas unitarias para los métodos principales del Modelo y el Controlador.**
5. **Implementar un sistema de logging** para registrar todas las operaciones realizadas en la aplicación.

