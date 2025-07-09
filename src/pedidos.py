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



def menu_pedidos():
    while True:
        print("\n=== Menú Pedidos ===")
        print("1. Nuevo pedido")
        print("2. Actualizar producto")
        print("3. Consultar producto por código")
        print("4. Eliminar producto")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_pedido()
        # elif opcion == "2":
        #     actualizar_producto()
        # elif opcion == "3":
        #     consultar_producto_codigo()
        # elif opcion == "4":
        #     eliminar_producto()
        elif opcion == "0":
            print("Muchas gracias. Adiós!")
            break
        else:
            print("Opción no válida.")
