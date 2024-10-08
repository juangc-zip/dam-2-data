##  DI | UNIDAD 1 | PROYECTO PINOCHO
###   INFORMACION GENERAL
####    OBJETOS / COMPONENTES NECESARIOS
__Componentes Graficos:__
- Tablero: Tamaño Modificable
- Jugador 1: Pinocho
- Jugador 2: Pepito Grillo

—————————————————————————————————————————————————————————————————————————————————————————
__Componente | Tablero:__
- Tamaño: introducido en el constructor
- Contenido: valores generados 0-3
	- _Valor 0:_ Piraña = -1 vida
	- _Valor 1:_  Agua = nada
	- _Valor 2:_ Piedra = -pez
	- _Valor 3:_  Pez = +pez

- Caracteres: caracteres internos
	- _Caracter 1:_ Pinocho = `caracter jugador 1`
	- _Caracter 2:_ Pepito = `caracter jugador 2`
	- _Caracter 3:_ Pinocho + Pepito = `caracter misma casilla | jugador 1 & 2`

- Constructores: constructores tablero
```c#
public tableroRio (int inputFilas, int inputColumnas) {
	this.filas = inputFilas;
	this.columnas = inputColumas;
}
```

- Metodos Privados: metodos internos de Tablero
	- _Metodo "fillMatrix" | rellena el tablero con valores aleatorios_
	- _Metodo "printMatrix" | imprime el tablero de manera normal_
	- _Metodo "savePlayerPos" | guarda la posicion del jugador_
	- _Metodos "savePlayerPath" | guarda el camino del jugador_

- Metodos Publicos: metodos publicos utiles
	- _Metodo "printMatrixShadow" | imprime el tablero de manera oculta_
—————————————————————————————————————————————————————————————————————————————————————————
__Componente | helperClass:__

