##  PROYECTO PINOCHO | OBJETO TABLERO
###   INFORMACION NECESARIA | BASE
####    CONSTANTES & ATRIBUTOS NECESARIOS
#####     CONSTANTES NECESARIAS
casilla_pirana: daño que realiza la casilla pirana | -1 vida
casilla_agua: no pasa nada si el jugador cae | nada
casilla_piedra: el jugador pierde un pez | -1 pez
casilla_pez: el jugador pesca un pez | +1 pez

value_pirana: int del valor de la casilla_pirana | 0
value_agua: int del valor de la casilla_agua | 1
value_piedra: int del valor de la casilla_piedra | 2
value_pez: int del valor de la casilla_pez | 3

num_defecto_filas: int del valor por defecto de las filas | 12
num_defecto_columnas: int del valor por defecto de las columnas | 12
valor_defecto_salida: string del caracter por defecto de la salida | "»"
——————————————————————————————————————————————————————————————————————————————————————————————
#####     ATRIBUTOS DEL TABLERO
numFilas: int del numero de filas del tablero
numColumnas: int del numero de columnas del tablero
tableroGeneral: string[,] matriz principal del programa

filaSalida: int del valor de la fila maxima
columnaSalida: int del valor de la columna maxima
valorSalida: string del caracter que indica la salida

——————————————————————————————————————————————————————————————————————————————————————————————————————————
####    CONSTRUCTORES DEL TABLERO
#####     CONSTRUCTOR MAS ESPECIFICO Y MODICABLE
```c#
public Tablero (int inputFilas, int inputColumnas, int inputFilaSalida, int inputColumnaSalida, string inputExitChar) {
	this.numFilas = inputFilas;
	this.numColumnas = inputColumnas;
	this.valorSalida = inputExitChar;

	this.filaSalida = inputFilaSalida;
	this.columnaSalida = inputColumnaSalida;

	this.tableroGeneral = new string[this.numFilas, this.numColumnas];
}
```
——————————————————————————————————————————————————————————————————————————————————————————————
#####     CONSTRUCTOR MEDIO Y PREDETERMINADO
```c#
public Tablero (int inputFilas, int inputColumnas, string inputExitChar) {
	this.numFilas = inputFilas;
	this.numColumnas = inputColumnas;
	this.valorSalida = inputExitChar;

	this.filaSalida = this.numFilas;
	this.columnaSalida = this.numColumnas;

	this.tableroGeneral = new string[this.numFilas, this.numColumnas];
}
```
——————————————————————————————————————————————————————————————————————————————————————————————
#####     CONSTRUCTOR MAS GENERAL Y BASICO
```c#
public Tablero () {
	this.numFilas = NUM_DEFECTO_FILAS;
	this.numColumnas = NUM_DEFECTO_COLUMNAS;
	this.valorSalida = VALOR_DEFECTO_SALIDA;

	this.filaSalida = this.numFilas;
	this.columnaSalida = this.numColumnas;

	this.tableroGeneral = new string[this.numFilas, this.numColumnas];
}
```
——————————————————————————————————————————————————————————————————————————————————————————————————————————
####    METODOS PRIVADOS ESPECIFICOS
——————————————————————————————————————————————————————————————————————————————————————————————————————————
####    METODOS PUBLICOS GENERALES
——————————————————————————————————————————————————————————————————————————————————————————————————————————
####    GETTERS & SETTERS ATRIBUTOS
#####     NUMERO DE FILAS
getter: debe devolver el numero de filas del tablero
setter: debe cambiar el numero de filas del tablero 
——————————————————————————————————————————————————————————————————————————————————————————————
#####     NUMERO DE COLUMNAS
getter: debe devolver el numero de columnas del tablero
setter: debe cambiar el numero de columnas del tablero
——————————————————————————————————————————————————————————————————————————————————————————————
#####     MATRIZ-TABLERO GENERAL
getter: debe devolver la matriz/tablero utilizado
setter: debe cambiar la matriz/tablero utilizado
——————————————————————————————————————————————————————————————————————————————————————————————
#####     NUMERO FILA MAXIMA
getter: debe devolver el numero de la fila maxima
setter: debe cambiar el numero de la fila maxima
——————————————————————————————————————————————————————————————————————————————————————————————
#####     NUMERO COLUMNA MAXIMA
getter: debe devolver el numero de la columna maxima
setter: debe cambiar el numero de la columna maxima
——————————————————————————————————————————————————————————————————————————————————————————————
#####     STRING CARACTER SALIDA
getter: debe devolver el caracter utilizado para indicar la salida
setter: debe cambiar el caracter utilizado para indicar la salida
——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————