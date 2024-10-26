##  DI | UNIDAD 2 | EXPRESIONES LAMBDA
###   EXPRESIONES LAMBDA
las expresiones lambda son funciones anonimas que permiten definir operaciones de manera concisa. tienen la siguiente sintaxis `parametros => expresion`. son utiles para escribir funciones cortas y directas. Un ejemplo seria:
   `x => x * x` / una funcion toma un valor x y devuelve su cuadrado.
###   LINQ (LANGUAGE INTEGRATED QUERY)
es una herramienta que permite realizar consultas a colecciones (lista, arrays, colecciones o bases de datos) de manera similar a SQL, pero en codigo. utiliza metodos como Where, Select, OrderBy. se suelen combinar con expresiones lambda. Un ejemplo seria:
   `var pares = numeros.Where(n => n % 2 == 0)` / filtra una lista de numeros seleccionando solo los pares.

la relacion entre expresiones lambda y LINQ son claves para definir filtros y transformaciones de manera flexible y concisa.
###   EJEMPLOS EN CODIGO
####    1. ACTUALIZAR PROPIEDADES DE UNA LISTA
la siguiente expresion lambda es pare de una consulta LINQ que trabaja sobre una lista de objetos Persona.
```c#
listPersonas.Where(p => p.Nombre == txtNombre.Text && p.Apellidos == txtApellidos.Text).ToList().ForEach(p => {
	p.Nombre = txtNombre.Text;
	p.Apellidos = txtApellidos.Text;
	p.Edad = int.Parse(txtEdad.Text);
});
```

se filtra la listPersonas usando el metodo Where, este aplica una condicion de filtrado a cada elemento de la lisa.
- la experesion `p => p.Nombre == txtNombre.Text && p.Apellidos == txtApellidos.Text`  / indica que solo se seleccionaran las personas cuyo nombre y apellidos coincidan con los valores introducidos en los campos Nombre y Apellidos.
- el metodo `.ToList()` / crea una lista con cada objeto Persona valido despues de pasar por el filtro, ya que el metodo Where devuelve un objeto de tipo Enumerable.
- el metodo `.ForEach(p => {...})` / aplica a cada objeto Persona una accion, en este caso actualizar las propiedades Nombre, Apellidos y Edad.
####    2. COMPROBAR SI ALGUN REGISTRO CUMPLE LA CONDICION
la siguiente expresion lambda es parte de una condicion que trabaja con una lista de objetos Persona.
```c#
if (listPersonas.Where(p => p.Nombre == txtNombre.Text && p.Apellidos == txtApellidos.Text).toList().Any() == false) {} //sino existe
```

se filtra la listPersonas usando el metodo Where, este aplica una condicion de filtrado a cada elemento de la lista,
- la expresion `p => p.Nombre == txtNombre.Text && p.Apellidos == txtApellidos.Text` / filtra la lista listPersonas para encontrar personas cuyo nombre y apellidos coincidan en nombre y apellidos.
- el metodo `.ToList()` / convierte el resultado filtrado en una lista.
- el metodo `.Any()` verifica si existe al mentos un elemento en la lista filtrada, devuelve tru si hay coincidencias y false si no hay.

