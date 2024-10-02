##   CONCEPTOS 2 | PROCESOS E HILOS
—————————————————————————————————————————
metodos de creacion de hilos
```java
public class CrearHiloRunnable implements Runnable {
  @Override
  public void run () {
	System.out.println ("Hola soy " + Thread.currentThread().getName());
	System.out.println ("Prioridad " + Thread.currentThread().getPriority());
	System.out.println ("ID: " + Thread.currentThread().getId());
	System.out.println ("Hilos: " + Thread.currentThread().activeCount());
  }
}
```

crear clase que sea un hilo
```java
public class usarHiloRunnable {
  public static void main (String[] args) {
	Thread hilo = new Thread(new CrearHiloRunnable());
	hilo.start();
  }
}
```

extender de Thread
```java
public class CrearHilos extends Thread {
  public static void main (String[] args) {
	System.out.println ("Hola soy " + Thread.currentThread().getName());
	System.out.println ("Prioridad " + Thread.currentThread().getPriority());
	System.out.println ("ID: " + Thread.currentThread().getId());
	System.out.println ("Hilos: " + Thread.currentThread().activeCount());
  }
}

public class UsarCrearHilo {
  public static void main (String[] args) {
	Thread.currentThread().setName("Principal");
	System.out.println (Thread.currentThread().getName());
	System.out.println (Thread.currentThread().toString());

	CrearHilos h = null;

	for (int i=0; i<3; i++) {
	  hilo = CrearHilos();
	  hilo.setName("hilo"+i);
	  hilo.setPriority(i+1);
	  hilo.start();
	  System.out.println ("Info de " + h.getName() + ": " +  h.toString());
	}

	System.out.println ("2 Hilos Creados...");
	System.out.println ("Hilos activos: " + Thread.activeCount());
  }
}
```

