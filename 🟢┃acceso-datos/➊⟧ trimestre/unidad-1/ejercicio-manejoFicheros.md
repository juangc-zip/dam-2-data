##   EJERCICIO | MANEJO DE FICHEROS
———————————————————————————————————————————
###  DISTRIBUCION DIRECTORIOS
mainProyecto
_carpetaModelo_
  modeloFile ==>
    _private String_ ruta
     -------------------------------------------------|
	_Constructores ->_
	  modeloFile () {super()}
	_Metodos Publicos & Privados ->_
	  _File_ getFileDeRuta ()
	_Getters & Setters ->_
	  _String_ getRuta ()
	  _void_ setRuta (String ruta)
   |-----------------------------------------------------|
  Carpeta **extends** modeloFile ==>
    _private String_ ruta
     -------------------------------------------------|
	_Constructores ->_
	  Carpeta (String ruta) | Carpeta ()
	_Metodos Publicos & Privados ->_
	  _void_ crearCarpeta ()
	  _void_ crearCarpeta (String nombreNuevoDirectorio)
	  _void_ crearCarpeta (File directorioPadre, String nombreDirectorio)
	   -------------------------------------------------|
	  _void_ leerCarpeta (File rutaCarpeta)
	  _File_ getFileDeRuta ()
	_Getters & Setters ->_
	  _String_ getRuta ()
	  _void_ setRuta (String ruta)
  Archivo **extends** modeloFile ==>
    _private String_ ruta
	_private String_ nombre
     -------------------------------------------------|
	_Constructores ->_
	  Archivo (String ruta, String nombre) | Archivo ()
	_Metodos Publicos & Privados ->_
	  _void_ crearArchivo (File ruta, String nombre)
	  _File_ getFileDeRuta ()
	_Getters & Setters ->_
	  _String_ getRuta ()
	  _void_ setRuta (String ruta)
	  _String_ getNombre ()
	  _void_ setNombre (String nombre)
   |-----------------------------------------------------|
_carpetaControlador_
  ControlCarpeta ==>
	private final InterfazVista vista;
	private final Carpeta modelo;
	 -------------------------------------------------|
	_Constructores ->_
	  ControlCarpeta (InterfazVista vista, Carpeta modelo)
	_Metodos Publicos & Privados ->_
	  _void_ actionPerformed (ActionEvent evento)
	_Getters & Setters ->_
_carpetaVista_
  InterfazVista ==>
	_static final String_ CREAR_CARPETA_CON_RUTA_COMPLETA
	_static final String_ CREAR_CARPETA_CON_RUTA_PADRE_Y_NOMBRE
	_static final String_ CREAR_CARPETA_CON_FILE_Y_NOMBRE
	_static final String_ CREAR_ARCHIVO_CON_RUTA_Y_NOMBRE
	 -------------------------------------------------|
	_Constructores ->_
	_Metodos Publicos & Privados ->_
	  _void_ setControlador (ControlCarpeta c)
	  _void_ arranca ()
	  _String_ getRuta ()
	  _String_ getNombre ()
	_Getters & Setters ->_
   |-----------------------------------------------------|
  VentanaCarpetaTexto **implements** InterfazVista ==>
    _Constructores ->_
      VentanaCarpetaTexto () {super()}
	_Metodos Publicos & Privados ->_
	  _String_ leerString ()
	  _int_ leerOpcion ()
	  _void_ mostrarMenu ()
	  _void_ procesarNuevaOperacion ()
	  _void_ opcionInvalida ()
	   -------------------------------------------------|
	  _void_ setControlador (ControlCarpeta c)
	  _void_ arranca ()
	_Getters & Setters ->_
	  _String_ getRuta ()
	  _String_ getNombre ()
   |-----------------------------------------------------|
  VentanaCarpetaGrafico **implements** InterfazVista ==>
   |-----------------------------------------------------|