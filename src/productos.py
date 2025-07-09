# productos (código producto, nombre, precio, stock, estado)
from conexion import conectar


def registrar_producto():
    print("\n=== Ingreso de Producto ===")

    codigo_producto = input("Codigo: ")
    nombre_producto = input("Nombre: ")
    precio_producto = input("Precio: ")
    stock_producto = input("Stock: ")
    estado_producto = input("Estado: ")

    datos_producto = {
        "codigo_producto": codigo_producto,
        "nombre": nombre_producto,
        "precio": precio_producto,
        "stock": stock_producto,
        "estado": estado_producto
    }

    insertar_producto(datos_producto)

def insertar_producto(datos_producto):
    db = conectar()
    db.producto.insert_one(datos_producto)
    print("Producto agregado con éxito.")


def actualizar_producto():
    print("\n=== Actualizar Producto ===")
    codigo = input("Código del producto a actualizar: ")
    print("Deja en blanco los campos que no quieras modificar.")
    nuevo_nombre = input("Nuevo nombre: ")
    nuevo_precio = input("Nuevo precio: ")
    nuevo_stock = input("Nuevo stock: ")
    nuevo_estado = input("Nuevo estado: ")

    nuevos_datos = {}
    if nuevo_nombre:
        nuevos_datos["nombre"] = nuevo_nombre
    if nuevo_precio:
        nuevos_datos["precio"] = nuevo_precio
    if nuevo_stock:
        nuevos_datos["stock"] = nuevo_stock
    if nuevo_estado:
        nuevos_datos["estado"] = nuevo_estado

    if not nuevos_datos:
        print("No se ingresaron datos para actualizar.")
        return

    db = conectar()
    resultado = db.producto.update_one({"codigo_producto": codigo}, {"$set": nuevos_datos})
    if resultado.matched_count:
        print("Producto actualizado con éxito.")
    else:
        print("No se encontró un producto con ese código.")


def eliminar_producto():
    print("\n=== Eliminar Producto ===")
    codigo = input("Ingrese el código del producto a eliminar: ")
    db = conectar()
    resultado = db.producto.delete_one({"codigo_producto": codigo})
    if resultado.deleted_count:
        print("Producto eliminado con éxito.")
    else:
        print("No se encontró un producto con ese código.")


def consultar_producto_codigo():
    print("\n=== Consultar Producto por Código ===")
    codigo = input("Ingrese el código del producto: ")
    db = conectar()
    producto = db.producto.find_one({"codigo_producto": codigo})
    if producto:
        print("\n-------- Producto encontrado --------")
        print("\n--- Datos del Producto encontrado ---")

        print(f"Código: {producto.get('codigo_producto', '')}")
        print(f"Nombre: {producto.get('nombre', '')}")
        print(f"Precio: {producto.get('precio', '')}")
        print(f"Stock: {producto.get('stock', '')}")
        print(f"Estado: {producto.get('estado', '')}")
    else:
        print("No se encontró un producto con ese código.")


def menu_productos():
    while True:
        print("\n=== Menú Productos ===")
        print("1. Registrar producto")
        print("2. Actualizar producto")
        print("3. Consultar producto por código")
        print("4. Eliminar producto")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            actualizar_producto()
        elif opcion == "3":
            consultar_producto_codigo()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "0":
            print("Muchas gracias. Adiós!")
            break
        else:
            print("Opción no válida.")
