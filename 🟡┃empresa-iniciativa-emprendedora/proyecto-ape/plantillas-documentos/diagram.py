from eralchemy import render_er

# Define the ER model in textual form
er_model = """
[Clientes] {
    + ClienteID: INTEGER (PK)
    Nombre: VARCHAR
    Apellido: VARCHAR
    Email: VARCHAR
    Telefono: VARCHAR
}

[Proveedores] {
    + ProveedorID: INTEGER (PK)
    Nombre: VARCHAR
    Contacto: VARCHAR
    Telefono: VARCHAR
    Email: VARCHAR
}

[Vehiculos] {
    + VehiculoID: INTEGER (PK)
    Familia: VARCHAR
    Subfamilia: VARCHAR
    Modelo: VARCHAR
    PrecioCompra: FLOAT
    PrecioVenta: FLOAT
    Disponibilidad: BOOLEAN
}

[Ventas] {
    + VentaID: INTEGER (PK)
    ClienteID: INTEGER (FK)
    FechaVenta: DATE
    TotalVenta: FLOAT
}

[FacturasVentas] {
    + FacturaVentaID: INTEGER (PK)
    VentaID: INTEGER (FK)
    FechaFactura: DATE
    Total: FLOAT
}

[Compras] {
    + CompraID: INTEGER (PK)
    ProveedorID: INTEGER (FK)
    FechaCompra: DATE
    TotalCompra: FLOAT
}

[FacturasCompras] {
    + FacturaCompraID: INTEGER (PK)
    CompraID: INTEGER (FK)
    FechaFactura: DATE
    Total: FLOAT
}

[MovimientosContables] {
    + MovimientoID: INTEGER (PK)
    Tipo: VARCHAR
    Monto: FLOAT
    Fecha: DATE
    Descripcion: VARCHAR
}

[Descuentos] {
    + DescuentoID: INTEGER (PK)
    Familia: VARCHAR
    ClienteID: INTEGER (FK)
    Porcentaje: FLOAT
}

[Estadisticas] {
    + EstadisticaID: INTEGER (PK)
    Año: INTEGER
    ClienteID: INTEGER (FK)
    VehiculoID: INTEGER (FK)
    TotalVentas: FLOAT
    TotalBeneficio: FLOAT
}

Clientes ClienteID *--1 Ventas VentaID
Ventas VentaID *--1 FacturasVentas FacturaVentaID
Proveedores ProveedorID *--1 Compras CompraID
Compras CompraID *--1 FacturasCompras FacturaCompraID
Vehiculos VehiculoID *--1 Ventas VentaID
Vehiculos Familia *--1 Descuentos Familia
Clientes ClienteID *--1 Descuentos ClienteID
Ventas VentaID *--1 MovimientosContables MovimientoID
Compras CompraID *--1 MovimientosContables MovimientoID
Clientes ClienteID *--1 Estadisticas ClienteID
Vehiculos VehiculoID *--1 Estadisticas VehiculoID
"""

# Define file path
db_diagram_path = "/mnt/data/BaseDatos_VentaVehiculos"

# Render the ER diagram
render_er(er_model, f"{db_diagram_path}.png")

db_diagram_path
