##  PROYECTO PINOCHO | OBJETO JUGADOR
###   INFORMACION NECESARIA | BASE
####    CONSTANTES & ATRIBUTOS NECESARIOS
#####     CONSTANTES NECESARIAS
min_vidas: numero minimo de vidas del jugador | 3
peces_iniciales: peces con los que empieza el jugador | 0
min_peces: peces minimos para ganar el juego | 5
max_saltos: numero maxmimo de saltos que puede realizar el jugador | 18
——————————————————————————————————————————————————————————————————————————————————————————————
#####     ATRIBUTOS DEL JUGADOR
inicialNombre: string de un caracter para la ficha del jugador
numVidas: int del numero de vidas que tiene el jugador (actualizable)
numPeces: int del numero de peces que tiene el jugador (actualizable)
minPeces: int del numero minimo de peces que necesita el jugador para ganar
numSaltos: int del numero de saltos que tiene el jugador (actualizable)
maxSaltos: int del numero de saltos maximos que puede realizar el jugador.
——————————————————————————————————————————————————————————————————————————————————————————————————————————
####    CONSTRUCTORES DEL JUGADOR
#####     CONSTRUCTOR MAS ESPECIFICO Y MODICABLE
```c#
public Jugador (string inputNombre, int inputVidas, int inputMinPeces, int inputMaxSaltos) {
	this.inicial = inputNombre;
	this.vidas = inputVidas;
	this.minPeces = inputMinPeces;
	this.maxSaltos = inputMaxSaltos;

	this.peces = 0;
}
```
——————————————————————————————————————————————————————————————————————————————————————————————
#####     CONSTRUCTOR MEDIO Y PREDETERMINADO
```c#
public Jugador (string inputNombre, int inputVidas, int inputMaxSaltos) {
	this.inicial = inputNombre;
	this.vidas = inputVidas;
	this.maxSaltos = inputMaxSaltos;

	this.minPeces = MIN_PECES;
	this.peces = 0;
}
```
——————————————————————————————————————————————————————————————————————————————————————————————
#####     CONSTRUCTOR MAS GENERAL Y BASICO
```c#
public Jugador (string inputNombre) {
	this.inicial = inputNombre;
	this.vidas = MIN_VIDAS;
	this.minPeces = MIN_PECES;
	this.maxSaltos = MAX_SALTOS;
	this.peces = PECES_INICIALES;
}
```
——————————————————————————————————————————————————————————————————————————————————————————————————————————
####    METODOS PRIVADOS ESPECIFICOS
——————————————————————————————————————————————————————————————————————————————————————————————————————————
####    METODOS PUBLICOS GENERALES
#####     METODO | TIENE MIN PECES
metodo "tieneMinPeces" | devuelve true si el jugador tiene el minimo de peces
```c#
public static bool tieneMinPeces (Jugador inputJugador) {
	bool _tieneMinPeces = false;
	if (inputJugador._numPeces == inputJugador._minPeces) {
		_tieneMinPeces = true;
	}
	
	return _tieneMinPeces;
}
```
——————————————————————————————————————————————————————————————————————————————————————————————
#####     METODO | NO QUEDAN SALTOS
metodo "noQuedanSaltos" | devuelve true si el jugador no tiene mas saltos
```c#
public static bool noQuedanSaltos (Jugador inputJugador) {
	bool _noQuedanSaltos = false;
	if (inputJugador._maxSaltos <= 0) {
		_noQuedanSaltos = true;
	}
	
	return _noQuedanSaltos;
}
```
——————————————————————————————————————————————————————————————————————————————————————————————
#####     METODO | NO QUEDAN VIDAS
metodo "noQuedanVidas" | devuelve true si el jugador no tiene mas vidas
```c#
public static bool noQuedanVidas (Jugador inputJugador) {
	bool _noQuedanVidas = false;
	if (inputJugador._numVidas <= 0) {
		_noQuedanVidas = true;
	}
	
	return _noQuedanVidas;
}
```
——————————————————————————————————————————————————————————————————————————————————————————————————————————
####    GETTERS & SETTERS ATRIBUTOS
#####     CARACTER-NOMBRE JUGADOR
getter: debe devolver el caracter usado por el jugador
setter: debe cambiar el caracter usado por el jugador
——————————————————————————————————————————————————————————————————————————————————————————————
#####     NUMERO ACTUAL DE VIDAS
getter: debe devolver el numero de vidas actual del jugador
setter: debe cambiar el numero de vidas actual del jugador
——————————————————————————————————————————————————————————————————————————————————————————————
#####     NUMERO MINIMO DE PECES
getter: debe devolver el numero minimo de peces necesarios
setter: debe cambiar el numero minimo de peces necesarios
——————————————————————————————————————————————————————————————————————————————————————————————
#####     NUMERO ACTUAL DE PECES
getter: debe devolver el numero de peces actual del jugador
setter: debe cambiar el numero de peces actual del jugador
——————————————————————————————————————————————————————————————————————————————————————————————
#####     NUMERO MAXIMO DE SALTOS
getter: debe devolver el numero maximo de saltos permitidos
setter: debe cambiar el numero maximo de saltos permitidos
——————————————————————————————————————————————————————————————————————————————————————————————
#####     NUMERO ACTUAL DE SALTOS
getter: debe devolver el numero de saltos actual del jugador
setter: debe cambiar el numero de saltos actual del jugador
——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
