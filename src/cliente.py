from conexion import conectar

# Nueva función para pedir datos al usuario y registrar el cliente
def registrar_cliente():
    print("\n=== Ingreso de Cliente ===")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    direccion = input("Dirección: ")
    fecha = input("Fecha de registro (YYYY-MM-DD): ")

    cliente = {
        "nombre": nombre,
        "apellido": apellido,
        "direccion": direccion,
        "fecha_registro": fecha
    }

    # Guarda los datos del cliente en la funcion insertar_cliente para usarlo
    # en una funcion que guarda en la base de datos MONGODB
    insertar_cliente(cliente)

def insertar_cliente(data):
    db = conectar()
    db.cliente.insert_one(data)  #se inserta en la coleccion "cliente"
    print("Cliente registrado con éxito.")


# actualizar_cliente(id, data)

# eliminar_cliente(id)

# buscar_clientes_por_ciudad(ciudad)

# buscar_clientes_por_fecha(fecha)

