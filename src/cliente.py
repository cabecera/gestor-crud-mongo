from conexion import conectar

# Nueva función para pedir datos al usuario y registrar el cliente
def registrar_cliente():
    print("\n=== Ingreso de Cliente ===")

    nombre_cliente = input("Nombre: ")
    apellido_cliente = input("Apellido: ")
    direccion_cliente = input("Dirección: ")
    fecha_registro = input("Fecha de registro (YYYY-MM-DD): ")

    # Se crea un diccionario con los datos del cliente
    datos_cliente = {
        "nombre": nombre_cliente,
        "apellido": apellido_cliente,
        "direccion": direccion_cliente,
        "fecha_registro": fecha_registro
    }

    # Guarda los datos del cliente en la funcion insertar_cliente para usarlo
    # en una funcion que guarda en la base de datos MONGODB
    insertar_cliente(datos_cliente)

def insertar_cliente(datos_cliente):
    db = conectar()
    db.cliente.insert_one(datos_cliente)  #se inserta en la coleccion "cliente"
    print("Cliente registrado con éxito.")


# actualizar_cliente(id, data)

def actualizar_cliente():
    print("\n=== Actualizar Cliente ===")

    nombre = input("Nombre del cliente a actualizar: ")

    print("Deja en blanco los campos que no quieras modificar.")
    nuevo_apellido = input("Nuevo apellido: ")
    nueva_direccion = input("Nueva dirección: ")
    nueva_fecha = input("Nueva fecha de registro (YYYY-MM-DD): ")

    nuevos_datos = {}
    if nuevo_apellido:
        nuevos_datos["apellido"] = nuevo_apellido
    if nueva_direccion:
        nuevos_datos["direccion"] = nueva_direccion
    if nueva_fecha:
        nuevos_datos["fecha_registro"] = nueva_fecha

    if not nuevos_datos:
        print("No se ingresaron datos para actualizar.")
        return

    db = conectar()
    # se actualiza el cliente con los nuevos datos {busca el nombre}
    # y actualiza {los datos}
    resultado = db.cliente.update_one({"nombre": nombre}, {"$set": nuevos_datos})
    # matched_count: Indica cuántos documentos existentes coincidieron con el filtro aplicado,
    # antes de realizar la actualización.
    if resultado.matched_count:
        print("Cliente actualizado con éxito.")
    else:
        print("No se encontró un cliente con ese nombre.")

# eliminar_cliente(id)

def eliminar_cliente():
    print("\n=== Eliminar Cliente ===")

    db = conectar()
    nombre = input("Ingrese el nombre del cliente a eliminar: ")
    resultado = db.cliente.delete_one({"nombre": nombre})
    if resultado.deleted_count:
        print("Cliente eliminado con éxito.")
    else:
        print("No se encontró un cliente con ese nombre.")

# buscar_clientes_por_ciudad(ciudad)
def buscar_cliente():
    print("\n=== Buscar Cliente ===")

    db = conectar()
    nombre = input("Ingrese el nombre: ")
    resultados = db.cliente.find({"nombre": nombre})

    encontrados = False
    for cliente in resultados:
        encontrados = True
        print("\n--- Cliente encontrado ---")
        # get('apellido', '')
        # buscamos la clave 'apellido' y '' valor si no existe
        print(f"Nombre: {cliente.get('nombre', '')}")
        print(f"Apellido: {cliente.get('apellido', '')}")
        print(f"Dirección: {cliente.get('direccion', '')}")
        print(f"Fecha de registro: {cliente.get('fecha_registro', '')}")
    if not encontrados:
        print("No se encontró ningún cliente con ese nombre.")


# buscar_clientes_por_fecha(fecha)

