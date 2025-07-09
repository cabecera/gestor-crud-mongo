from conexion import conectar


def registrar_pedido():
    print("\n=== Registrar Pedido ===")
    # Solicitar el nombre del cliente y buscarlo en la base de datos
    nombre_cliente = input("Nombre del cliente: ")
    db = conectar()
    cliente = db.cliente.find_one({"nombre": nombre_cliente})
    if not cliente:
        print("No se encontró un cliente con ese nombre.")
        return

    productos_pedido = []
    # Bucle para agregar productos al pedido
    while True:
        codigo_producto = input("Código del producto (o 'fin' para terminar): ")
        if codigo_producto.lower() == 'fin':
            break
        # Buscar el producto por código
        producto = db.producto.find_one({"codigo_producto": codigo_producto})
        if not producto:
            print("No se encontró un producto con ese código.")
            continue
        try:
            # Solicitar la cantidad del producto
            cantidad = int(input(f"Cantidad de '{producto['nombre']}': "))
        except ValueError:
            print("Cantidad inválida. Intente de nuevo.")
            continue
        # Verificar stock suficiente
        try:
            stock_actual = int(producto["stock"])
        except (KeyError, ValueError):
            print("El stock del producto no es válido.")
            continue
        if cantidad > stock_actual:
            print(f"No hay suficiente stock. Stock disponible: {stock_actual}")
            continue
        # Restar la cantidad del stock del producto
        nuevo_stock = stock_actual - cantidad
        db.producto.update_one({"codigo_producto": codigo_producto}, {"$set": {"stock": str(nuevo_stock)}})
        # Agregar el producto y la cantidad al detalle del pedido
        productos_pedido.append({
            "codigo_producto": codigo_producto,
            "nombre": producto["nombre"],
            "cantidad": cantidad,
            "precio_unitario": producto["precio"]
        })

    if not productos_pedido:
        print("No se agregaron productos al pedido.")
        return

    # Solicitar el método de pago
    metodo_pago = input("Método de pago: ")

    # Crear el documento del pedido con cliente, productos y método de pago
    pedido = {
        "cliente": {
            "nombre": cliente["nombre"],
            "apellido": cliente["apellido"]
        },
        "productos": productos_pedido,
        "metodo_pago": metodo_pago
    }

    # Insertar el pedido en la colección 'pedido'
    db.pedido.insert_one(pedido)
    print("Pedido registrado con éxito.")


def actualizar_pedido():
    print("\n=== Actualizar Pedido ===")
    db = conectar()
    # Solicitar el ID del pedido a actualizar
    id_pedido = input("Ingrese el ID del pedido a actualizar: ")
    from bson.objectid import ObjectId
    try:
        # Buscar el pedido por su ObjectId
        pedido = db.pedido.find_one({"_id": ObjectId(id_pedido)})
    except Exception:
        print("ID de pedido no válido.")
        return
    if not pedido:
        print("No se encontró un pedido con ese ID.")
        return
    print("Deja en blanco los campos que no quieras modificar.")
    # Permitir actualizar el método de pago
    nuevo_metodo_pago = input(f"Nuevo método de pago (actual: {pedido.get('metodo_pago', '')}): ")
    nuevos_datos = {}
    if nuevo_metodo_pago:
        nuevos_datos["metodo_pago"] = nuevo_metodo_pago
    if not nuevos_datos:
        print("No se ingresaron datos para actualizar.")
        return
    # Actualizar el pedido en la base de datos
    resultado = db.pedido.update_one({"_id": ObjectId(id_pedido)}, {"$set": nuevos_datos})
    if resultado.matched_count:
        print("Pedido actualizado con éxito.")
    else:
        print("No se pudo actualizar el pedido.")


def eliminar_pedido():
    print("\n=== Eliminar Pedido ===")
    db = conectar()
    # Solicitar el ID del pedido a eliminar
    id_pedido = input("Ingrese el ID del pedido a eliminar: ")
    from bson.objectid import ObjectId
    try:
        # Intentar eliminar el pedido por su ObjectId
        resultado = db.pedido.delete_one({"_id": ObjectId(id_pedido)})
    except Exception:
        print("ID de pedido no válido.")
        return
    if resultado.deleted_count:
        print("Pedido eliminado con éxito.")
    else:
        print("No se encontró un pedido con ese ID.")


def buscar_pedidos_por_cliente():
    print("\n=== Buscar Pedidos por Cliente ===")
    # Solicitar el nombre del cliente
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    db = conectar()
    # Buscar todos los pedidos asociados al nombre del cliente
    pedidos = db.pedido.find({"cliente.nombre": nombre_cliente})
    encontrados = False
    for pedido in pedidos:
        encontrados = True
        print("\n--- Pedido ---")
        print(f"ID: {pedido.get('_id')}")
        print(f"Cliente: {pedido['cliente']['nombre']} {pedido['cliente']['apellido']}")
        print(f"Método de pago: {pedido.get('metodo_pago', '')}")
        print("Productos:")
        for prod in pedido.get('productos', []):
            print(f"  - {prod['nombre']} (Código: {prod['codigo_producto']}), Cantidad: {prod['cantidad']}, Precio unitario: {prod['precio_unitario']}")
    if not encontrados:
        print("No se encontraron pedidos para ese cliente.")


def menu_pedidos():
    while True:
        print("\n=== Menú Pedidos ===")
        print("1. Nuevo pedido")
        print("2. Actualizar pedido")
        print("3. Buscar pedidos por cliente")
        print("4. Eliminar pedido")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_pedido()
        elif opcion == "2":
            actualizar_pedido()
        elif opcion == "3":
            buscar_pedidos_por_cliente()
        elif opcion == "4":
            eliminar_pedido()
        elif opcion == "0":
            print("Muchas gracias. Adiós!")
            break
        else:
            print("Opción no válida.")
