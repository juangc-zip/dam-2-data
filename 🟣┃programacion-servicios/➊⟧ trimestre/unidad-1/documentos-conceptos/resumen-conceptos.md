##   CONCEPTOS | PROGRAMACION SERVICIOS
—————————————————————————————————————————
###  CONCEPTOS BASICOS | 1
- **Ejecutables:** archivo con la estructura necesaria para que el sistema operativo pueda iniciar el programa que hay dentro.
- **Procesos:** es la ejecucion de un programa bajo el control del sistema operativo, y puede atravesar varias etapas a lo largo de su "ciclo de vida".
- **Estados de los Procesos:**
	- ***Nuevo:***  el *proceso está siendo creado* a partir del ejecutable
	- ***Listo:*** el proceso no se encuentra en ejecución, pero está esperando para hacerlo. el planificador del sistema operativo no le ha asignado todavía un procesado.
	- ***En Ejecuccion:*** el *proceso se está ejecutando*, está dentro del microprocesador. el sistema operativo utiliza el mecanismo de interrupciones para controlar su ejecución.
	- ***Bloqueado:*** el *proceso está bloqueado* esperando que ocurra algún suceso.
	- ***Terminado:***  el *proceso ha finalizado* su ejecución y libera su imagen de memoria.
- **Tipos de Procesos:**
	- ***Demonio:*** *proceso no interactivo* que está ejecutándose continuamente en segundo plano.
	- ***Servicio:*** *programa* que atiende a otro programa.
	- ***Hilo:*** *proceso ligero*, *subproceso* o *parte de un proceso* que puede ser ejecutado por el sistema operativo. un hilo sí *puede acceder* a los *datos* de *otro hilo* del *mismo proceso*.
- **Sistema Operativo:** *capa de software* que *equipa* a las *computadoras*, cuya labor es la de *administrar y gestionar* todo el *hardware* que *interactúa* en la misma y *proporcionar* una *interfaz sencilla* a los programas para comunicarse con dicho hardware.
- **Programacion Concurrente:**
	- ***Programacion Paralela:*** un ordenador ejecuta una o mas tareas a la vez, repartiendo el tiempo de proceso.
	- ***Programacion Distribuida:*** el software se ejcuta en varios ordenadores a la vez que estan comunicados entre ellos a traves de la red. tiene mejor rendimiento y no se comparte memoria entre los procesadores.
—————————————————————————————————————————