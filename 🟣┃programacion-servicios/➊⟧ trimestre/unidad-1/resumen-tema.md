##  PSP | UNIDAD 1 | PROGRAMACION MULTIPROCESO
———————————————————————————————————————————————————————————————————————————
###   1. CONCEPTOS BASICOS
Un ejecutable es un archivo co la estructura ecesaria para que el sistema operativo pueda iniciar el programa que hay dentro. Cuando un programa se ejecuta crea un proceso que quda bajo control del sistema operativo. Un proceso a lo largo de su vida puede atravesar diferentes etapas.
- **Nuevo:** El proceso esta siendo creado a traves del ejecutable.
- **Listo:** El proceso no esta en ejecucion pero esta esperando para hacerlo.
- **En ejecucion:** El proceso se esta ejecutando, dentro del microprocesador.
- **Bloqueado:** El proceso esta bloqueado, esperando a que ocurra un evento/suceso.
- **Terminado:** El proceso ha terminado y libera su imagen en memoria.

Existen diferentes conceptos dentro de la ejecucion de un programa, depenediendo del plano en el que se ejecuten y la funcion que tengan.
- **Demonios:** Proceso no interactivo que esta ejecutandose siempre en segundo plano de manera continua. Suele proporcionar un servicio basico a otros procesos.
- **Servicio:** Programa que atiende a otro programa. Es un proceso que no muestra niguna interfaz grafica en pantalla ya que no esta pensado para que el usuario lo maneje manualmente.
- **Hilos:** Proceso ligero o subproceso que puede ser ejecutado por el sistema operativo. En Java puedes usar la clase `Thread` para definir los hilos de ejecucion. Un proceso no puede acceder al espacio de memoria de otro proceso pero un hilo puede acceder al espacio de memoria de otro hilo, siempre que esten en el mismo proceso.
- **Sistema Operativo:** Es la capa de software que equipa a los ordenadores, cuya funcion es administrar y gestionar el hardware que interactua en la misma y proporcionar una interfaz sencilla para el usuario.
———————————————————————————————————————————————————————————
###   2. PROGRAMACION CONCURRENTE, PARALELA Y DISTRIBUIDA
Existen 2 tipos de sistemas dependiendo del numero de procesos que puedan ejecutarse al mismo tiempo, podemos dividirlos en 2 clases; sistema monoproceso y multiproceso.
- **Sistema Monoproceso:** permite la ejecucion de un solo proceso, hasta que no finalize no atendera a ningun otro proceso.
- **Sistema Multiproceso:** permite la ejecucion de varios procesos de manera simultanea, en los que intenta maximizar la utilizacion de la CPU. Los procesos se ejecutan simultaneamente en la CPU y quedan a la espera si requieren algun recurso del sistema.

La programacion concurrente es la parte de la programaion que se ocupa de crear programas que pueden tener varios hilos para ejecutar un trabajo y aprovechar al maximo los sistemas multiproceso. Dentro de la programacion concurrente podemos separar 2 tipos, programacion paralela y programacion distribuida.
- **Programacion Paralela:** es la capacidad de un ordenador de ejecutar dos o mas tareas a la vez, normalmente repartiendo el tiempo de proceso entre la diferentes tareas.
- **Programacion Distribuida:** es el software que se ejecuta en ordenadores distintos y que estan comunicados a traves de un red. Se mejora el rendimiento y no se comparte memoria entre los procesadores por lo que los esquemas son mas complejos y costosos.
———————————————————————————————————————————————————————————
###   3. CREACION DE PROCESOS
Podemos crear procesos en Java utilizando la clase Process Builder, un ejemplo de la implementacion de la clase seria la siguiente:
```java
public class LanzadorProcesos {
  public void ejecutar (String ruta) {
	try {
	  pb = new ProcessBuilder(ruta);
	  pb.start();
	} catch (Exception e) {
	  e.printStackTrace();
	}
  }

  public static void main (String[] args) {
    String ruta = "C:\\Program Files\\Notepad++\\notepad++.exe";
    LanzadorProcesos lp = new LanzadorProcesos(ruta);
    lp.ejecutar(ruta);
    System.out.println(" > Finalizado");
  }
}
```

La clase ProcessBuilder es usada paa ejecutar programas en un proceso separado de un forma simple. El metodo `start()` crea un nuevo proceso, que es devuelto en una instancia de l clase `Process`, usada para gestionar el proceso creado. Se puede invocar repetidamente para crear mas procesos con los mismos o diferentes atributos.

Los procesos cuando finalizan devuelven el estado en el que terminaron, para saber dicho estado podemos usar la funcion `exitValue()`, para saber si el proceso ha finalizado correctamente el valor debe ser 0; cualquier otro valor se debe a un error.

Para ejecutar un proceso del S.O. utilizando ProcessBuilder, para finalizar el ejemplo falta: redirecccionar la salida, cambiar el directorio de trabajo y leer los dats devueltos por el proceso.
```java
public class Sumador {
  public static int sumar (int n1, int n2) {
    return (n1 + n2);
  }

  public static void main (String[] args) {
    int n1 = Integer.parseInt(args[0]);
    int n2 = Integer.parseInt(args[1]);
    int suma = Sumador.suma(n1, n2);
  }
}

public class Lanzador {
  public void LanzadorSumador (int n1, int n2) {
    String clase = "Sumador";
    ProcessBuilder pb;

	try {
	  pb = new ProcessBuilder("java", clase, String.valueOf(n1), String.valueOf(n2));
	  pb.start();
	} catch (Exception e) {
	  e.printStackTrace();
	}
  }

  public static void main (String[] args) {
    Lanzador l = new Lanzador();
    l.LanzardorSumador(1, 51);
    l.LanzardorSumador(51, 100);
  }
}
```
———————————————————————————————————————————————————————————
###   4. COMUNICACION DE PROCESOS
Las operaciones multiprocesos implican que sea necesario una comunicacion ente procesos, necesitaremos usar mecanismos especificos de comunicacion tanto en Java o diseñar uno propio para evitar los problemas que puedan aparecer. Podemos observar como funciona en el siguiente esquema:
```
stdin -> PROCESO:
			|=> stderr
			|=> stdout
```

El subproceso lee la entrada del teclado `stdin` que no hay que confundirlo con los parametros, despues escribe el resultado por la salida standar `stdout`, pero en caso de que haya algun error saldran por la salida de errores `stderr`. Lo habitual es configurar un fichero.log como salida estandar.

Utilizando en codigo anterior para entender como funcionan los subprocesos y la informacion ahora utilizando el mismo ejemplo vamos a ver como podemos mostrar los datos generales.
```java
public class Lanzador {
  public void lanzarSumador (int n1 int n2) throws IOException {
	try {
	  ProcessBuilder pb = new ProcessBuilder("java", "Sumador", String.valueOf(n1), String.valueOf(n2));
	   // cambiar el directorio de trabajo, al directorio que contiene los .class
	  pb.directory(new File("bin"));
	  pb.redirectError(new File ("files" + File.separator + "error.log"));

	  pb.start();
	} catch (Exception e) {
	  e.printStackTrace();
	}

	 // mostramos caracter a caracter la salida generada por Sumador
	try (InputStream is = process.getInputStream()) {
	  int c;
	  while ((c = is.readLine()) != null) {
	    System.out.println((char) c);
	  }
	} catch (IOExceptio e) {
	  e.printStackTrace();
	  throw e;
	}
  }

  public static void main (String[] args) {
	Lanzador l = new Lanzador();
	l.lanzarSumador(n1, n2);
  }
}
```

En el caso en el que queramos guardar la salida en un fichero.log deberiamos modificar y agregar una linea mas de codigo, en el siguiete codigo lo puedes observar:
```java
try {
  ProcessBuilder pb = new ProcessBuilder("java", "Sumador", String.valueOf(n1), String.valueOf(n2));
  // cambiar el directorio de trabajo, al directorio que contiene los .class
  pb.directory(new File("bin"));
  pb.redirectError(new File ("files" + File.separator + "error.log"));
  pb.redirectOutput(new File ("files" + File.separator + "salida.log"));

  pb.start();
} catch (Exception e) {
  e.printStackTrace();
}
```
———————————————————————————————————————————————————————————
###   5. GESTION DE PROCESOS
El arbol de procesos, un proceso puede estar pidiendo al sistema operativo la creacion de un nuevo proceso necesario para continuar con la funcion del proceso principal, a este proceso secundario se le denomina proceso hijo y normalmente depende de un proceso superior o proceso padre. El proceso hijo a su vez puede crear nuevos procesos formandose lo que conocemos como un arbol de directorios.
———————————————————————————————————————————————————————————
###   6. SINCRONIZACION DE PROCESOS

———————————————————————————————————————————————————————————
###   7. PROGRAMACION MULTIPROCESO