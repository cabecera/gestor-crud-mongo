from conexion import conectar

# Registrar un nuevo cliente solicitando todos los datos necesarios

def registrar_cliente():
    print("\n=== Ingreso de Cliente ===")

    nombre_cliente = input("Nombre: ")
    apellido_cliente = input("Apellido: ")
    calle_cliente = input("Calle: ")
    numero_cliente = input("Número: ")
    ciudad_cliente = input("Ciudad: ")
    fecha_registro = input("Fecha de registro (YYYY-MM-DD): ")

    datos_cliente = {
        "nombre": nombre_cliente,
        "apellido": apellido_cliente,
        "direccion": {
            "calle": calle_cliente,
            "numero": int(numero_cliente),
            "ciudad": ciudad_cliente
        },
        "fecha_registro": fecha_registro
    }

    insertar_cliente(datos_cliente)

# Insertar un cliente en la base de datos

def insertar_cliente(datos_cliente):
    db = conectar()
    db.cliente.insert_one(datos_cliente)
    print("Cliente registrado con éxito.")

# Actualizar los datos de un cliente existente

def actualizar_cliente():
    print("\n=== Actualizar Cliente ===")
    nombre = input("Nombre del cliente a actualizar: ")
    print("Deja en blanco los campos que no quieras modificar.")
    nuevo_apellido = input("Nuevo apellido: ")
    nueva_calle = input("Nueva calle: ")
    nuevo_numero = input("Nuevo número: ")
    nueva_ciudad = input("Nueva ciudad: ")
    nueva_fecha = input("Nueva fecha de registro (YYYY-MM-DD): ")

    nuevos_datos = {}

    if nuevo_apellido:
        nuevos_datos["apellido"] = nuevo_apellido
    direccion = {}
    if nueva_calle:
        direccion["calle"] = nueva_calle
    if nuevo_numero:
        direccion["numero"] = int(nuevo_numero)
    if nueva_ciudad:
        direccion["ciudad"] = nueva_ciudad
    if direccion:
        nuevos_datos["direccion"] = direccion
    if nueva_fecha:
        nuevos_datos["fecha_registro"] = nueva_fecha

    if not nuevos_datos:
        print("No se ingresaron datos para actualizar.")
        return

    db = conectar()
    resultado = db.cliente.update_one({"nombre": nombre}, {"$set": nuevos_datos})
    if resultado.matched_count:
        print("Cliente actualizado con éxito.")
    else:
        print("No se encontró un cliente con ese nombre.")

# Eliminar un cliente por nombre

def eliminar_cliente():
    print("\n=== Eliminar Cliente ===")
    nombre = input("Ingrese el nombre del cliente a eliminar: ")
    db = conectar()
    resultado = db.cliente.delete_one({"nombre": nombre})
    if resultado.deleted_count:
        print("Cliente eliminado con éxito.")
    else:
        print("No se encontró un cliente con ese nombre.")

# Buscar clientes por nombre y mostrar todos los datos desglosados

def buscar_cliente():
    print("\n=== Buscar Cliente ===")
    nombre = input("Ingrese el nombre: ")
    db = conectar()
    resultados = db.cliente.find({"nombre": nombre})
    encontrados = False
    for cliente in resultados:
        encontrados = True
        print("\n--- Cliente encontrado ---")
        print(f"Nombre: {cliente.get('nombre', '')}")
        print(f"Apellido: {cliente.get('apellido', '')}")
        direccion = cliente.get('direccion', {})
        print(f"Calle: {direccion.get('calle', '')}")
        print(f"Número: {direccion.get('numero', '')}")
        print(f"Ciudad: {direccion.get('ciudad', '')}")
        print(f"Fecha de registro: {cliente.get('fecha_registro', '')}")
    if not encontrados:
        print("No se encontró ningún cliente con ese nombre.")

