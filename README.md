# Sistema de Gestión de Clientes, Productos y Pedidos  Python
# Asignatura Base de Datos No Estructuradas

Aplicación en Python para gestionar clientes, productos y pedidos con operaciones CRUD y consultas personalizadas.

## Estructura del Proyecto

```plaintext
gestor-crud-mongo/
├── src/
│ ├── clientes.py # CRUD + búsqueda de clientes
│ ├── productos.py # CRUD + búsqueda de productos
│ ├── pedidos.py # CRUD + búsqueda de pedidos
│ ├── conexion.py # Manejo de la base de datos
│ └── init.py
├── tests/ # Pruebas unitarias
└── README.md
```



## Funcionalidades

#### Módulo de Clientes
```plaintext
registrar_cliente(data)                # Crea nuevo cliente
actualizar_cliente(id, data)           # Modifica cliente existente
eliminar_cliente(id)                   # Elimina cliente
buscar_clientes_por_ciudad(ciudad)     # Filtra por ciudad
buscar_clientes_por_fecha(fecha)       # Filtra por fecha de registro
```

#### Módulo de Productos
```plaintext
registrar_producto(data)               # Añade nuevo producto
actualizar_producto(id, data)          # Edita producto
eliminar_producto(id)                  # Elimina producto
buscar_producto_por_codigo(codigo)     # Busca por código
```

#### Módulo de Pedidos
```plaintext
registrar_pedido(data)                 # Crea nuevo pedido
actualizar_pedido(id, data)            # Modifica pedido
eliminar_pedido(id)                    # Cancela pedido
buscar_pedidos_por_cliente(cliente_id) # Historial por cliente
```

## Requisitos:
Python 3.8+




