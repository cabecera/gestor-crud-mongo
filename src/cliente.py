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
            "numero": numero_cliente,
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
        direccion["numero"] = nuevo_numero
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

# Buscar clientes por ciudad correctamente

def buscar_cliente_ciudad():
    print("\n=== Buscar Cliente por Ciudad ===")
    ciudad = input("Ingrese ciudad: ")
    db = conectar()
    resultados = db.cliente.find({"direccion.ciudad": ciudad})
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
        print("No se encontró ningún cliente en esa ciudad.")

# Buscar clientes por fecha de registro

def buscar_cliente_fecha():
    print("\n=== Buscar Cliente por Fecha de Registro ===")
    fecha = input("Ingrese la fecha de registro (YYYY-MM-DD): ")
    db = conectar()
    resultados = db.cliente.find({"fecha_registro": fecha})
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
        print("No se encontró ningún cliente registrado en esa fecha.")



def menu_clientes():
    while True:
        print("\n=== Menú Clientes ===")
        print("1. Registrar cliente")
        print("2. Actualizar cliente")
        print("3. Buscar cliente por nombre")
        print("4. Buscar cliente por ciudad")
        print("5. Buscar cliente por fecha")
        print("6. Eliminar cliente")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            actualizar_cliente()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            buscar_cliente_ciudad()
        elif opcion == "5":
            buscar_cliente_fecha()
        elif opcion == "6":
            eliminar_cliente()
        elif opcion == "0":
            print("Muchas gracias. Adiós!")
            break
        else:
            print("Opción no válida.")
