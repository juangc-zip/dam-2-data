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

—————————————————————————————————————————