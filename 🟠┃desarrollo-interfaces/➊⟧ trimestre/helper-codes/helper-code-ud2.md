###  DI 1 | UNIDAD 2 | CODE SNIPPETS
####   OBJETOS | CODE SNIPPETS
Para poder realizar una buena aplicacion de objetos dentro del proyecto necesitamos minimo 3 constructores, un constructor vacio, un constructor completo sin ID, y por ultimo un constructor con todos los atributos del objeto.
```csharp
internal class Objeto {
  private int _id;
  private string _nombre;
  private int _edad;

  private List<Persona> listPersonas;
  public ObjetoManager om;

	// constructores -->
  public Objeto () => om = new ObjetoManager();

  public Objeto (string nombre, int edad) {
	om = new ObjetoManager();
	this._id = om.getLastId(this);

	this._nombre = nombre;
	this._edad = edad;
  }

  public Objeto (int id, string nombre, int edad) {
	om = new ObjetoManager();
	this._id = id;
	this._nombre = nombre;
	this._edad = edad;
  }
}
```

Tambien solemos necesitar un metodo para obtener una lista de todos nuestros objetos, para ello debemos crear un metodo llamada __genListaObjeto()__ este nos debera devolver una lista de nuestro objeto.
```csharp
public List<Objeto> genListObjeto() {
  listaObjeto = pm.leerObjeto();
  return listaObjeto;
}
```
---
####   OBJETOS MANAGER | CODE SNIPPETS

---
####   MAIN WINDOW | CODE SNIPPETS

----
