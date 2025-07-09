import tkinter as tk
from tkinter import messagebox, simpledialog
from conexion import conectar
from bson.objectid import ObjectId

# Ventana principal
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión MongoDB")
        self.geometry("500x500")
        self.create_main_menu()
        self.result_listbox = None  # Para mostrar resultados de búsqueda

    def create_main_menu(self):
        self.clear_window()
        tk.Label(self, text="Menú Principal", font=("Arial", 16)).pack(pady=10)
        tk.Button(self, text="Clientes", width=20, command=self.menu_clientes).pack(pady=5)
        tk.Button(self, text="Productos", width=20, command=self.menu_productos).pack(pady=5)
        tk.Button(self, text="Pedidos", width=20, command=self.menu_pedidos).pack(pady=5)
        tk.Button(self, text="Salir", width=20, command=self.destroy).pack(pady=20)

    # --- CLIENTES ---
    def menu_clientes(self):
        self.clear_window()
        tk.Label(self, text="Menú Clientes", font=("Arial", 14)).pack(pady=10)
        tk.Button(self, text="Registrar cliente", width=25, command=self.registrar_cliente).pack(pady=2)
        tk.Button(self, text="Actualizar cliente", width=25, command=self.actualizar_cliente).pack(pady=2)
        tk.Button(self, text="Buscar cliente por nombre", width=25, command=self.buscar_cliente).pack(pady=2)
        tk.Button(self, text="Eliminar cliente", width=25, command=self.eliminar_cliente).pack(pady=2)
        tk.Button(self, text="Volver", width=25, command=self.create_main_menu).pack(pady=10)
        self.create_result_listbox()

    def registrar_cliente(self):
        db = conectar()
        nombre = simpledialog.askstring("Registrar cliente", "Nombre:", parent=self)
        if not nombre: return
        apellido = simpledialog.askstring("Registrar cliente", "Apellido:", parent=self)
        calle = simpledialog.askstring("Registrar cliente", "Calle:", parent=self)
        numero = simpledialog.askstring("Registrar cliente", "Número:", parent=self)
        ciudad = simpledialog.askstring("Registrar cliente", "Ciudad:", parent=self)
        fecha = simpledialog.askstring("Registrar cliente", "Fecha de registro (YYYY-MM-DD):", parent=self)
        datos = {
            "nombre": nombre,
            "apellido": apellido,
            "direccion": {"calle": calle, "numero": numero, "ciudad": ciudad},
            "fecha_registro": fecha
        }
        db.cliente.insert_one(datos)
        messagebox.showinfo("Éxito", "Cliente registrado con éxito.", parent=self)

    def actualizar_cliente(self):
        db = conectar()
        nombre = simpledialog.askstring("Actualizar cliente", "Nombre del cliente a actualizar:", parent=self)
        if not nombre: return
        cliente = db.cliente.find_one({"nombre": nombre})
        if not cliente:
            messagebox.showerror("Error", "No se encontró el cliente.", parent=self)
            return
        nuevo_apellido = simpledialog.askstring("Actualizar cliente", "Nuevo apellido:", parent=self)
        nueva_calle = simpledialog.askstring("Actualizar cliente", "Nueva calle:", parent=self)
        nuevo_numero = simpledialog.askstring("Actualizar cliente", "Nuevo número:", parent=self)
        nueva_ciudad = simpledialog.askstring("Actualizar cliente", "Nueva ciudad:", parent=self)
        nueva_fecha = simpledialog.askstring("Actualizar cliente", "Nueva fecha de registro (YYYY-MM-DD):", parent=self)
        nuevos_datos = {}
        if nuevo_apellido: nuevos_datos["apellido"] = nuevo_apellido
        direccion = {}
        if nueva_calle: direccion["calle"] = nueva_calle
        if nuevo_numero: direccion["numero"] = nuevo_numero
        if nueva_ciudad: direccion["ciudad"] = nueva_ciudad
        if direccion: nuevos_datos["direccion"] = direccion
        if nueva_fecha: nuevos_datos["fecha_registro"] = nueva_fecha
        if not nuevos_datos:
            messagebox.showinfo("Info", "No se ingresaron datos para actualizar.", parent=self)
            return
        db.cliente.update_one({"nombre": nombre}, {"$set": nuevos_datos})
        messagebox.showinfo("Éxito", "Cliente actualizado.", parent=self)

    def buscar_cliente(self):
        db = conectar()
        nombre = simpledialog.askstring("Buscar cliente", "Nombre:", parent=self)
        if not nombre: return
        if not self.result_listbox:
            self.create_result_listbox()
        self.clear_result_listbox()
        clientes = db.cliente.find({"nombre": nombre})
        encontrados = False
        for c in clientes:
            encontrados = True
            texto = f"Nombre: {c.get('nombre','')}, Apellido: {c.get('apellido','')}, Ciudad: {c.get('direccion',{}).get('ciudad','')}, Fecha: {c.get('fecha_registro','')}"
            if self.result_listbox:
                self.result_listbox.insert(tk.END, texto)
        if not encontrados and self.result_listbox:
            self.result_listbox.insert(tk.END, "No se encontró ningún cliente.")

    def eliminar_cliente(self):
        db = conectar()
        nombre = simpledialog.askstring("Eliminar cliente", "Nombre del cliente a eliminar:", parent=self)
        if not nombre: return
        res = db.cliente.delete_one({"nombre": nombre})
        if res.deleted_count:
            messagebox.showinfo("Éxito", "Cliente eliminado.", parent=self)
        else:
            messagebox.showinfo("Info", "No se encontró el cliente.", parent=self)

    # --- PRODUCTOS ---
    def menu_productos(self):
        self.clear_window()
        tk.Label(self, text="Menú Productos", font=("Arial", 14)).pack(pady=10)
        tk.Button(self, text="Registrar producto", width=25, command=self.registrar_producto).pack(pady=2)
        tk.Button(self, text="Actualizar producto", width=25, command=self.actualizar_producto).pack(pady=2)
        tk.Button(self, text="Consultar producto por código", width=25, command=self.consultar_producto_codigo).pack(pady=2)
        tk.Button(self, text="Eliminar producto", width=25, command=self.eliminar_producto).pack(pady=2)
        tk.Button(self, text="Volver", width=25, command=self.create_main_menu).pack(pady=10)
        self.create_result_listbox()

    def registrar_producto(self):
        db = conectar()
        codigo = simpledialog.askstring("Registrar producto", "Código:", parent=self)
        if not codigo: return
        nombre = simpledialog.askstring("Registrar producto", "Nombre:", parent=self)
        precio = simpledialog.askstring("Registrar producto", "Precio:", parent=self)
        stock = simpledialog.askstring("Registrar producto", "Stock:", parent=self)
        estado = simpledialog.askstring("Registrar producto", "Estado:", parent=self)
        datos = {
            "codigo_producto": codigo,
            "nombre": nombre,
            "precio": precio,
            "stock": stock,
            "estado": estado
        }
        db.producto.insert_one(datos)
        messagebox.showinfo("Éxito", "Producto registrado con éxito.", parent=self)

    def actualizar_producto(self):
        db = conectar()
        codigo = simpledialog.askstring("Actualizar producto", "Código del producto a actualizar:", parent=self)
        if not codigo: return
        producto = db.producto.find_one({"codigo_producto": codigo})
        if not producto:
            messagebox.showerror("Error", "No se encontró el producto.", parent=self)
            return
        nuevo_nombre = simpledialog.askstring("Actualizar producto", "Nuevo nombre:", parent=self)
        nuevo_precio = simpledialog.askstring("Actualizar producto", "Nuevo precio:", parent=self)
        nuevo_stock = simpledialog.askstring("Actualizar producto", "Nuevo stock:", parent=self)
        nuevo_estado = simpledialog.askstring("Actualizar producto", "Nuevo estado:", parent=self)
        nuevos_datos = {}
        if nuevo_nombre: nuevos_datos["nombre"] = nuevo_nombre
        if nuevo_precio: nuevos_datos["precio"] = nuevo_precio
        if nuevo_stock: nuevos_datos["stock"] = nuevo_stock
        if nuevo_estado: nuevos_datos["estado"] = nuevo_estado
        if not nuevos_datos:
            messagebox.showinfo("Info", "No se ingresaron datos para actualizar.", parent=self)
            return
        db.producto.update_one({"codigo_producto": codigo}, {"$set": nuevos_datos})
        messagebox.showinfo("Éxito", "Producto actualizado.", parent=self)

    def consultar_producto_codigo(self):
        db = conectar()
        codigo = simpledialog.askstring("Consultar producto", "Código del producto:", parent=self)
        if not codigo: return
        if not self.result_listbox:
            self.create_result_listbox()
        self.clear_result_listbox()
        producto = db.producto.find_one({"codigo_producto": codigo})
        if producto and self.result_listbox:
            info = f"Código: {producto.get('codigo_producto','')}, Nombre: {producto.get('nombre','')}, Precio: {producto.get('precio','')}, Stock: {producto.get('stock','')}, Estado: {producto.get('estado','')}"
            self.result_listbox.insert(tk.END, info)
        elif self.result_listbox:
            self.result_listbox.insert(tk.END, "No se encontró el producto.")

    def eliminar_producto(self):
        db = conectar()
        codigo = simpledialog.askstring("Eliminar producto", "Código del producto a eliminar:", parent=self)
        if not codigo: return
        res = db.producto.delete_one({"codigo_producto": codigo})
        if res.deleted_count:
            messagebox.showinfo("Éxito", "Producto eliminado.", parent=self)
        else:
            messagebox.showinfo("Info", "No se encontró el producto.", parent=self)

    # --- PEDIDOS ---
    def menu_pedidos(self):
        self.clear_window()
        tk.Label(self, text="Menú Pedidos", font=("Arial", 14)).pack(pady=10)
        tk.Button(self, text="Registrar pedido", width=25, command=self.registrar_pedido).pack(pady=2)
        tk.Button(self, text="Actualizar pedido", width=25, command=self.actualizar_pedido).pack(pady=2)
        tk.Button(self, text="Buscar pedidos por cliente", width=25, command=self.buscar_pedidos_por_cliente).pack(pady=2)
        tk.Button(self, text="Eliminar pedido", width=25, command=self.eliminar_pedido).pack(pady=2)
        tk.Button(self, text="Volver", width=25, command=self.create_main_menu).pack(pady=10)
        self.create_result_listbox()

    def registrar_pedido(self):
        db = conectar()
        nombre_cliente = simpledialog.askstring("Registrar pedido", "Nombre del cliente:", parent=self)
        if not nombre_cliente: return
        cliente = db.cliente.find_one({"nombre": nombre_cliente})
        if not cliente:
            messagebox.showerror("Error", "No se encontró el cliente.", parent=self)
            return
        productos_pedido = []
        while True:
            codigo_producto = simpledialog.askstring("Producto", "Código del producto (o 'fin' para terminar):", parent=self)
            if not codigo_producto or codigo_producto.lower() == 'fin':
                break
            producto = db.producto.find_one({"codigo_producto": codigo_producto})
            if not producto:
                messagebox.showerror("Error", "No se encontró el producto.", parent=self)
                continue
            cantidad_str = simpledialog.askstring("Producto", f"Cantidad de '{producto['nombre']}':", parent=self)
            if cantidad_str is None:
                continue
            try:
                cantidad = int(cantidad_str)
            except Exception:
                messagebox.showerror("Error", "Cantidad inválida.", parent=self)
                continue
            try:
                stock_actual = int(producto["stock"])
            except (KeyError, ValueError):
                messagebox.showerror("Error", "El stock del producto no es válido.", parent=self)
                continue
            if cantidad > stock_actual:
                messagebox.showerror("Error", f"No hay suficiente stock. Stock disponible: {stock_actual}", parent=self)
                continue
            nuevo_stock = stock_actual - cantidad
            if nuevo_stock == 0:
                db.producto.update_one({"codigo_producto": codigo_producto}, {"$set": {"stock": "sin stock"}})
                messagebox.showinfo("Stock", f"El producto '{producto['nombre']}' ha quedado SIN STOCK.", parent=self)
            else:
                db.producto.update_one({"codigo_producto": codigo_producto}, {"$set": {"stock": str(nuevo_stock)}})
            productos_pedido.append({
                "codigo_producto": codigo_producto,
                "nombre": producto["nombre"],
                "cantidad": cantidad,
                "precio_unitario": producto["precio"]
            })
        if not productos_pedido:
            messagebox.showinfo("Info", "No se agregaron productos al pedido.", parent=self)
            return
        metodo_pago = simpledialog.askstring("Registrar pedido", "Método de pago:", parent=self)
        pedido = {
            "cliente": {
                "nombre": cliente["nombre"],
                "apellido": cliente["apellido"]
            },
            "productos": productos_pedido,
            "metodo_pago": metodo_pago
        }
        db.pedido.insert_one(pedido)
        messagebox.showinfo("Éxito", "Pedido registrado con éxito.", parent=self)

    def actualizar_pedido(self):
        db = conectar()
        id_pedido = simpledialog.askstring("Actualizar pedido", "ID del pedido a actualizar:", parent=self)
        if not id_pedido: return
        try:
            pedido = db.pedido.find_one({"_id": ObjectId(id_pedido)})
        except Exception:
            messagebox.showerror("Error", "ID de pedido no válido.", parent=self)
            return
        if not pedido:
            messagebox.showerror("Error", "No se encontró el pedido.", parent=self)
            return
        nuevo_metodo_pago = simpledialog.askstring("Actualizar pedido", f"Nuevo método de pago (actual: {pedido.get('metodo_pago','')}):", parent=self)
        if not nuevo_metodo_pago:
            messagebox.showinfo("Info", "No se ingresaron datos para actualizar.", parent=self)
            return
        db.pedido.update_one({"_id": ObjectId(id_pedido)}, {"$set": {"metodo_pago": nuevo_metodo_pago}})
        messagebox.showinfo("Éxito", "Pedido actualizado.", parent=self)

    def eliminar_pedido(self):
        db = conectar()
        id_pedido = simpledialog.askstring("Eliminar pedido", "ID del pedido a eliminar:", parent=self)
        if not id_pedido: return
        try:
            res = db.pedido.delete_one({"_id": ObjectId(id_pedido)})
        except Exception:
            messagebox.showerror("Error", "ID de pedido no válido.", parent=self)
            return
        if res.deleted_count:
            messagebox.showinfo("Éxito", "Pedido eliminado.", parent=self)
        else:
            messagebox.showinfo("Info", "No se encontró el pedido.", parent=self)

    def buscar_pedidos_por_cliente(self):
        db = conectar()
        nombre_cliente = simpledialog.askstring("Buscar pedidos", "Nombre del cliente:", parent=self)
        if not nombre_cliente: return
        if not self.result_listbox:
            self.create_result_listbox()
        self.clear_result_listbox()
        pedidos = db.pedido.find({"cliente.nombre": nombre_cliente})
        encontrados = False
        for pedido in pedidos:
            encontrados = True
            texto = f"ID: {pedido.get('_id')}, Cliente: {pedido['cliente']['nombre']} {pedido['cliente']['apellido']}, Método de pago: {pedido.get('metodo_pago','')}"
            for prod in pedido.get('productos', []):
                texto += f" | {prod['nombre']} (Código: {prod['codigo_producto']}), Cantidad: {prod['cantidad']}, Precio: {prod['precio_unitario']}"
            if self.result_listbox:
                self.result_listbox.insert(tk.END, texto)
        if not encontrados and self.result_listbox:
            self.result_listbox.insert(tk.END, "No se encontraron pedidos para ese cliente.")

    def create_result_listbox(self):
        self.result_listbox = tk.Listbox(self, width=80, height=10)
        self.result_listbox.pack(pady=10)

    def clear_result_listbox(self):
        if self.result_listbox:
            self.result_listbox.delete(0, tk.END)

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.result_listbox = None

if __name__ == "__main__":
    app = App()
    app.mainloop()