##   CONCEPTOS | PROGRAMACION MULTIMEDIA
—————————————————————————————————————————
###  CONCEPTOS BASICOS | 1
- **Null Var Acceptor:** para poder hacer que un variable admita nulos debemos determinarlo de la siguente manera:
```kotlin
var nombre: String?
nombre = null
```
- **Null Var Assign:** para poder asignar a una variable el valor de una variable que puede ser nulo, lo debemos hacer en modo seguro, y especificarlo utilizando _?_. la asignacion seria la siguiente:
```kotlin
var nombre: String? = null

var longitud: Int? = nombre?.length
println("longitud: ${longitud}") // longitud: null
```
- **If Null Value, Reassign:** si sabemos que el valor de una variable puede ser nulo, podemos sustituir el valor nulo por el que queramos. de tal manera que el valor nulo podria ser uno por defecto. un ejemplo seria el nombre:
```kotlin
var nombre: String? = null

var longitud: Int = nombre?.length ?: 0
println("longitud: ${longitud}") // longitud: 0 (valor reasignado)
```
- **Tipos de Variables y su Alcance:**
	- ***Variables Locales:*** se declaran en algun bloque del programa y unicamente perduran en ese bloque. _solo se pueden usar dentro de su bloque_.
	- ***Variables Globales:*** se declaran a nivel de clase, al inicio del programa _(ejemplo: constantes)_ y perduran durante toda su ejecucion.
```kotlin
class Hola {
	var prueba: String // declaracion variable global

	fun mensaje () {
		var abc: String // declaracion variable local

		abc = "hola"
		println(abc)
	}
}
```
- **Tipos de Constantes:**
	- ***Constantes (Java Type):*** constantes (tipo java) se asigna el valor una unica vez, y no se podra volver a reasignar.
	- ***Constantes (Kotlin Type):*** constantes (tipo kotlin) funcionamiento igual que java pero la nomenclatura es diferente.
```kotlin
 // declaracion | constante | kotlin type
val NUMERO_PAGINAS: Int = 10 // declaracion & asignacion
	// variable sin nueva asignacion

 // declaracion | constante | java type
 const val WEBSITE_NAME = "maestrecalatrava"
	 // constate fija, fuera de la funcion
```
- **Lectura y Escritura en Consola:**
	- ***Lectura por Consola:*** le datos directamente del teclado, debemos usar la funcion `readLine()`. la funcion devuelve un objeto `String?` ya que podemos asignar un valor nulo.
	- ***Escritura en Consola:*** los datos que querramos escribir por consola deberan ser usado con la funcion `println()` con salto de linea, y `print()` sin salto de linea.
```kotlin
 // lectura de datos por consola
println("introduce tu nombre: ")
val nombre = readLine()

 // escritura de datos por consola
var edad: Int = 12
print("la edad del usuario es ${edad}")
```
- **Lectura por Consola Modificaciones:** al ser un flujo de datos si quieramos determinar que la variable a la que se asignaran los datos deberemos añadirles al final un modificador indicando al tipo de dato que se convertira el flujo. un ejemplo seria:
```kotlin
println("indica la edad que tienes: ")
val edad = readLine().toInt()  // el tipo de dato pasa a ser integer
```
—————————————————————————————————————————
###  CONCEPTOS BASCICOS | BUCLES Y CONDICIONES
- **Estructuras de Control:**
	- ***Condicional Simple: If*** condicion simple de comparacion de 2 expresiones y complejas (utilizando operadores logicos).
	- ***Condicional Compleja: When*** es una version mejorada de _switch_ en java. compara un valor con una lista de entradas, podemos usarlo para expresiones, comprobaciones de rango o comprobaciones de tipo.
```kotlin
 // condicional simple + variantes
var numero: Int = 2

if ( (numero % 2) == 0 ) {
	print("el numero es par")
} else if (numero == 0) {
	print("operacion no valida")
} else {
	print("el numero no es par")
}
//—————————————————————————————
 // condicional compleja + usos
	 // comprobacion de variable
var numero: Int = 2
when (numero) {
	1 -> print ("el numero es 1")
	2 -> print ("el numero es 2")
	else -> {
	print ("el numero no es 1 ni 2")}
}
	 // comprobacion de rango
var mes: Int = 3
fun getMes (mes : Int) {
	when (mes) {
		in 1 <= .. <= 6 -> print("primer semestre")
		in 7 <= .. <= 12 -> print("segundo semestre")
		!in 1 <= .. <= 12 -> print("no es un semestre")
	}
}
	 // comprobacion de tipos
var tipoVar: Int
fun evaluarTipos (value: Any) {
	when (value) {
		is Int -> print(value + 1)
		is String -> print ("el texto es $value")
		is Boolean -> if (value) print ("es verdadero") else print ("es falso")
	}
}
```
- **Estructuras de Repeticion:** permiten ejecutar de forma repetitivas bloques de codigo, podemos meter expresiones dentro como condicion para que el bucle se detenga.
	- ***Bucle While:*** los bucles se repiten mientras que se cumpla una condicion determinada.
	- ***Bucle Do While:*** igual que el bucle while, pero la condicion se evalua despues de cada vuelta.
	- ***Bucle For:*** sirve para recorrer colecciones de objetos desde el principio hasta el final.
```kotlin

var i = 0
while (i < 100) {
	print(i)
	i++
}
//—————————————————————————————
 // estructura repetitiva | do while
var num: Int
do {
	print("teclea numero mayor que 0: ")
	num = readIn().toInt()
} while (num <= 0)
//—————————————————————————————
 // estructura repetitiva | for
for (i in 1..5) {
	println("contando $i")
}
```
- **Estructura Repetitiva: For** el bucle for al recoger un rango tiene modificadores para poder ahorrarnos codigo, esto se declara dentro de la expresion. Tambien podemos recorrer cadenas de caracteres de una manera mas sencilla.
```kotlin
 // estructura repetitiva | for
	// iteraccion regular
for (char in 'a' <= .. <= 'd') print (char) // abcd
//—————————————————————————————
	// iteraccion con avance de 2 (2++)
for (char in 'a' <= .. <= 'd' step 2) print (char) // ac
//—————————————————————————————
	// iteraccion inversa
for (char in 'd' >= downTo >= 'a') print (char) // dcba
//—————————————————————————————
	// iteraccion excluyendo el limite superior
for (char in 'a' <= until < 'f') print (char)

//————————————————————————————————————————
 // estructura repetitiva | for
	// recorrer una cadena
for (c in "ejemplo") {
	print (c)
}
```
—————————————————————————————————————————
###  CONCEPTOS BASICOS | FUNCIONES & CLASES
——————————————————————————————————
####   FUNCIONES | BASICAS, PARAMETROS & VALORES
- **Declaracion de Funciones:** las funciones se declaran utilizando la palabra `fun` seguida del nombre que queremos poner en la funcion.
```kotlin
fun main() {
	print("hola mundo!")
}
```
- **Funciones con Parametros y Devolucion de Valores:** las funciones pueden tener parametros o devolver valores. la declaracion de cada una se hace de diferente forma a la de java.
```kotlin
 // funciones | parametros y valores
	// funcion con parametros
fun mostrarInformacion (nombre: String, apellidos: String) {
	println("Me llamo $nombre con apellidos $apellidos")
}

//————————————————————————————————————————
	// funcion devolucion valores
fun suma (firstNumber: Int, secondNumber: Int): Int {
	return firstNumber + secondNumber 
}
```
——————————————————————————————————
####   CLASES | BASICAS & MODIFICADORES
- **Clases en Kotlin:** las clases se deben declaran con la primera letra en Mayuscula, y dentro podemos almacenar funciones, constantes, variables, ...
```kotlin
class Complejo {
	var re: Int = 0
	var im: Int = 0

	fun suma (v: Complejo) {
		re = re + v.re
		im = im + v.im
	}
}
```
- **Moficiadores de Visibilidad:** los modificadores de visibilidad se deben usar siempre, ya que sirven para modificar el acceso de las clases. los modificadores se pueden usar en clases, inferfaces, constructores y funciones y las propiedades.
```kotlin
 // modificadore | tipos y usos
	// public | publico - mayor claridad
public class ClasePublica {
	public val atributo = 1
}

//————————————————————————————————————————
	// private | privado - solo propia clase
class ClasePrivada {
	private val atributo = 2
}

//————————————————————————————————————————
	// protected | protegida - atributos y clases heredadas visibles - no otras clases
class ClaseProtegida {
	protected val atributo = 3
}

//————————————————————————————————————————
	// internal | interno - solo disponible en el mismo modulo
class ClaseInterna {
	internal val atributo = 4
}
```
—————————————————————————————————————————
###  CONCEPTOS BASICOS | OBJETOS, MIEMBROS & REFERENCIA
- **Creacion y Declaracion de Objetos:** los objetos son instacias de una clase, la clase es la definicion general y el objeto es la materializacion.
```kotlin
 // objetos | creacion y declaracion
	// creacion de un objeto Punto
class Punto {
	var x: Int = 0
	var y: Int = 0
}

//————————————————————————————————————————
	// declaracion de un objeto Punto
var p: Punto
var p = Punto()

//————————————————————————————————————————
	// utilizacion de atributos del objeto
var p = Punto()
p.x = 1;
p.y = 3;
```
- **Metodos Accesores (Getters & Setters):** los setters permiten modificar los atributos de una clase, mientras que los getters permiten leer los valores de los atributos
```kotlin
class Person {
	var name: String = "noname"
		// getters >
		get () {
			return field
		}
		// setters >
		set (value) {
			field = value
		}
}

//————————————————————————————————————————
 // dentro de los getter y los setters se utiliza la variable field para evitar la recursividad ya que si pusieramos this.name llamaria al metodo get/set
```
- **Creacion de Objetos y Uitlizacion de Getters/Setters:** un ejemplo de como funcionaria el objeto anterior podemos observar este codigo:
```kotlin
 // explicacion getters/setters con objetos
	// creacion de objeto Person
val p = Person()
   // internamente se llama al metodo set() | field = value
p.name = "juan"

   // internamente se llama al metodo get() | field = value
print("${p.name}")
```
- **Sobreescribir Getters/Setters:** ya sabemos que los getters y setters van anclados a un atributo, de tal manera que podemos sobreescribir estos metodos.
```kotlin
class Person {
	var name: String = "noname"
	  // name | getters/setters
		get () {
			return field
		}
		
		set(value) {
			field = value
		}

	var age: Int = 0
	  // age | getters/setters
		get() {
			return field
		}

		set (value) {
			if (value < 18) field = 18
			else if (value >= 18 && value <= 30) {
				field = value
			} else field = value-3
		}
}
```
—————————————————————————————————————————
###  CONCEPTOS AVANZADOS | CLASES - CONSTRUCTORES
——————————————————————————————————
####   CONSTRUCTORES | NO-ARGS - SOBRECARGA
- **Informacion Constructores:** es un metodo especial dentro de la inicializacion, el nombre debe ser "constructor", puede recibit cualquier tipo de argumentos y no devuelve ningun valor.
```kotlin
class Punto {
	var x: Int = 0
	var y: Int = 0
	
	constructor (a: Int, b: Int) {
		x: a
		y: b
	}
}
```
- **Constructor No-Args:** es un constructor que no recibe ningun valor simplemente se denomina el constructor vacio. ***en el momento que ya hay un constructor normal no se puede declarar uno no-args***.
```kotlin
class Punto {
	var x: Int = 0
	var y: Int = 0
	
	constructor () {
		x = 0
		y = 0
	}
}
```
- **Sobrecarga de Constructores:** podemos tener dentro de nuestro objeto varios constructores, pero deben de distinguuirse en los argumentos que necesita, ya sea en el numero o en el tipo. la sobrecarga es aplicable a otros metodos.
```kotlin
class Punto {
	var x: Int = 0
	var y: Int = 0
	
	constructor a: Int, b: Int() {
		x = a
		y = b
	}
	
	constructor () {
		x = 0
		y = 0
	}
}
```
- **Delegacion de Constructores:** los constructores a su vez pueden llamar a otros constructores usando la palabra _this_ aunque ademas si tenemos dentro de un constructor un parametro que se llama igual que un atributo del metodo tambien podemos usar _this_ para referirnos al atributo.
```kotlin
Class Punto {
	var x: Int = 0
	var y: Int = 0

	constructor (x: Int, y: Int) {
		this.x = x
		this.y = y
	}
	
	constructor(): this(0, 0)
}
```
——————————————————————————————————
####   CONSTRUCTORES | PRIMAR. & SECUND. - BLOQ. INICIALIZACION
- **Constructor Primario:** constructor principal de un clase, se define dentro de la declaracion de la clase. puede tener parametros y usarlos como atributos.
```kotlin
class Person (var name: String, var age: Int) {
	var name: String
	var age: Int
}
```
- **Constructor Secundario:** son constructores que pueden tener diferentes parametros y se usan para crear instancias de diferentes maneras. si existe un constructor primario cada constructor secundario debe llamar al primario usando _this_.
```kotlin
 // constructor primario
class Person (var name: String, var age: Int) {
	var name: String
	var age: Int

	constructor (name: String) : this(name, 0) {
		// secundario
	}
}
```
- **Bloques de Inicializacion:** se utiliza con la funcion _init_ y se usa para inicializar los atributos antes de los constructores en el caso que necesitemos tener una valores por defecto.
```kotlin
class Person (name: String) {
	var name: String
	var age: Int
	
	  // bloque de inicializacion
	init {
		this.name = name
		this.age = 0
	}
	
	  // constructor secundario
	constructor (name: String, age:Int) : this(name) {
		this.age = age
	}
}
```
—————————————————————————————————————————
###  CONCEPTOS AVANZADOS | PROPIEDADES KOTLIN
pag. 57
—————————————————————————————————————————