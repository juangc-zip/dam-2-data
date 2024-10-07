##  DESARROLLO INTERFACES | UNIDAD 1 | EJERCICIO TABLERO | MARIO BROS
—————————————————————————————————————————————————————————————————————————————————————————————————
###   EJERCICIO | ENUNCIADO BASE
Tenemos un tablero de 8x8. Podemos rellenar aleatorio cada celda con valores que pueden ser 0/1/2. 
Mario necesita minimo 5 de pócima para salvar a Peach. El 0 quita una vida, el 1 le damos una vida y el 2 coge pócima ( 2 ml).
Nosotros manejaremos a Mario moviendolo de arriba a abajo , de derecha a izquierda.
El juego nos indicará.
El juego se acaba cuando consigue los 5 ml de pócima o se quede sin vidas.
Pócima inicial: 0 ml
Vidas iniciales: 3
—————————————————————————————————————————————————————————————————————————————————————————
###   EJERCICIO | ESQUEMA RESUMEN
####    TABLERO DE JUEGO
- El juego se desarrolla en un tablero de 8x8 casillas.
- Cada casilla se rellena aleatoriamente con uno de tres valores posibles: 0, 1 o 2.
—————————————————————————————————————————————————————————————————————————————————
####    OBJETIVO DE JUEGO
Mario debe recolectar al menos 5 ml de pócima para salvar a la Princesa Peach.
—————————————————————————————————————————————————————————————————————————————————
####    MECANICA DE JUEGO
- **Movimiento**: El jugador controla a Mario, moviéndolo por el tablero en cuatro direcciones: arriba, abajo, izquierda y derecha.
- **Efectos de las casillas**:
  - 0: Mario pierde una vida
  - 1: Mario gana una vida
  - 2: Mario obtiene 2 ml de pócima
—————————————————————————————————————————————————————————————————————————————————
####    ESTADO INICIAL
- Mario comienza con 0 ml de pócima
- Mario tiene 3 vidas al inicio del juego
—————————————————————————————————————————————————————————————————————————————————
####    CONDICION DE FINALIZACION
El juego termina cuando ocurre una de estas dos situaciones:
1. Mario consigue 5 ml o más de pócima (victoria)
2. Mario pierde todas sus vidas (derrota)
—————————————————————————————————————————————————————————————————————————————————
####    INTERFAZ
El juego debe proporcionar información sobre el estado actual, como la cantidad de pócima recolectada y las vidas restantes.
—————————————————————————————————————————————————————————————————————————————————————————————————