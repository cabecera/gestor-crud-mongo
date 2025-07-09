# DOCUMENTACIÓN DE FUNCIONALIDADES

A continuación se describen en detalle las funcionalidades implementadas hasta el momento en el sistema.

------------------------------------------------------------

## CONEXIÓN A LA BASE DE DATOS

### Función: conectar()

Propósito:
Establecer una conexión con el servidor de MongoDB que se ejecuta localmente en el puerto mongodb://localhost:27017/. Esta función crea un cliente de MongoDB y accede a la base de datos llamada 'proyecto_mongo', devolviendo el objeto de base de datos para ser utilizado en las operaciones posteriores.

Entradas:
No recibe parámetros.

Salidas:
Devuelve el objeto de base de datos de MongoDB correspondiente a 'proyecto_mongo'.

Comportamiento:
- Si la conexión es exitosa, el objeto de base de datos puede ser utilizado para acceder a las colecciones y realizar operaciones CRUD.
- Si el servidor de MongoDB no está disponible, se producirá una excepción al intentar conectar con el mensaje: Error al conectar a la base de datos

------------------------------------------------------------

## GESTIÓN DE CLIENTES

### Función: registrar_cliente()

Propósito:
Solicitar al usuario, a través de la consola, los datos necesarios para registrar un nuevo cliente en el sistema. Los datos solicitados son: nombre, apellido, dirección y fecha de registro. Una vez obtenidos, se agrupan en un diccionario y se envían como parámetro a la función insertar_cliente para guardar el cliente en la base de datos.

Entradas:
No recibe parámetros directamente; los datos se obtienen mediante la interacción con el usuario.

Salidas:
No retorna valor. Muestra mensajes en consola indicando el resultado de la operación.

Comportamiento:
- Solicita los datos al usuario uno por uno.
- Agrupa los datos en un diccionario.
- Guarda el diccionario como parámetro en insertar_cliente.
- Llama a la función insertar_cliente para guardar el cliente en la base de datos.
- Informa al usuario si el registro fue exitoso.

### Función: insertar_cliente(datos_cliente)

Propósito:
Recibir un diccionario con los datos de un cliente y guardarlo como un nuevo documento en la colección 'cliente' de la base de datos.

Entradas:
- datos_cliente: Diccionario con las claves nombre, apellido, direccion y fecha_registro.

Salidas:
No retorna valor. Muestra un mensaje en consola indicando si el cliente fue registrado con éxito. "Cliente registrado con éxito."

Comportamiento:
- Conecta a la base de datos utilizando la función conectar.
- Inserta el diccionario recibido como un nuevo documento en la colección 'cliente'.
- Informa al usuario del éxito de la operación.

### Función: actualizar_cliente()

Propósito:
Permitir al usuario modificar los datos de un cliente existente, identificándolo por su nombre. El usuario puede actualizar el apellido, la dirección y la fecha de registro. Solo se actualizan los campos que el usuario desee modificar. Los datos se agrupan en un diccionario y se pasan como parámetro a la actualización en la base de datos.

Entradas:
No recibe parámetros directamente; los datos se obtienen mediante la interacción con el usuario.

Salidas:
No retorna valor. Muestra mensajes en consola indicando el resultado de la operación.

Comportamiento:
- Solicita al usuario el nombre del cliente a actualizar.
- Permite dejar en blanco los campos que no se desean modificar.
- Agrupa los nuevos datos en un diccionario.
- Si no se ingresan datos nuevos, informa al usuario y termina la operación.
- Realiza la actualización en la base de datos usando el nombre como filtro y el diccionario de nuevos datos como parámetro.
- Informa si la actualización fue exitosa ("Cliente actualizado con éxito.") o si no se encontró el cliente ("No se encontró un cliente con ese nombre.").

### Función: eliminar_cliente()

Propósito:
Eliminar un cliente de la base de datos, identificándolo por su nombre. El nombre se solicita al usuario y se utiliza como filtro para eliminar el primer cliente que coincida.

Entradas:
No recibe parámetros directamente; el nombre se solicita al usuario por consola.

Salidas:
No retorna valor. Muestra mensajes en consola indicando el resultado de la operación.

Comportamiento:
- Solicita al usuario el nombre del cliente a eliminar.
- Busca y elimina el primer cliente que coincida con el nombre proporcionado.
- Informa si la eliminación fue exitosa ("Cliente eliminado con éxito.") o si no se encontró el cliente ("No se encontró un cliente con ese nombre.").

### Función: buscar_cliente()

Propósito:
Buscar y mostrar los datos de todos los clientes cuyo nombre coincida con el proporcionado por el usuario. El nombre se solicita al usuario y se utiliza como filtro para buscar en la base de datos.

Entradas:
No recibe parámetros directamente; el nombre se solicita al usuario por consola.

Salidas:
No retorna valor. Muestra en consola los datos de los clientes encontrados o un mensaje si no se encuentra ninguno.

Comportamiento:
- Solicita al usuario el nombre a buscar.
- Realiza una búsqueda en la colección 'cliente' filtrando por el nombre.
- Muestra los datos de cada cliente encontrado (nombre, apellido, calle, número, ciudad, fecha de registro).
- Informa si no se encontró ningún cliente con ese nombre.

### Función: buscar_cliente_ciudad()

Propósito:
Buscar y mostrar los datos de todos los clientes que tengan registrada una ciudad específica en su dirección. La ciudad se solicita al usuario y se utiliza como filtro para buscar en la base de datos.

Entradas:
No recibe parámetros directamente; la ciudad se solicita al usuario por consola.

Salidas:
No retorna valor. Muestra en consola los datos de los clientes encontrados o un mensaje si no se encuentra ninguno.

Comportamiento:
- Solicita al usuario la ciudad a buscar.
- Realiza una búsqueda en la colección 'cliente' filtrando por el campo anidado 'direccion.ciudad'.
- Muestra los datos de cada cliente encontrado (nombre, apellido, calle, número, ciudad, fecha de registro).
- Informa si no se encontró ningún cliente en esa ciudad.

### Función: buscar_cliente_fecha()

Propósito:
Buscar y mostrar los datos de todos los clientes que hayan sido registrados en una fecha específica. La fecha se solicita al usuario y se utiliza como filtro para buscar en la base de datos.

Entradas:
No recibe parámetros directamente; la fecha se solicita al usuario por consola (formato YYYY-MM-DD).

Salidas:
No retorna valor. Muestra en consola los datos de los clientes encontrados o un mensaje si no se encuentra ninguno.

Comportamiento:
- Solicita al usuario la fecha de registro a buscar.
- Realiza una búsqueda en la colección 'cliente' filtrando por el campo 'fecha_registro'.
- Muestra los datos de cada cliente encontrado (nombre, apellido, calle, número, ciudad, fecha de registro).
- Informa si no se encontró ningún cliente registrado en esa fecha.

------------------------------------------------------------

## GESTIÓN DE PRODUCTOS

### Función: registrar_producto()

Propósito:
Solicitar al usuario, a través de la consola, los datos necesarios para registrar un nuevo producto en el sistema. Los datos solicitados son: código, nombre, precio, stock y estado. Una vez obtenidos, se agrupan en un diccionario y se envían como parámetro a la función insertar_producto para guardar el producto en la base de datos.

Entradas:
No recibe parámetros directamente; los datos se obtienen mediante la interacción con el usuario.

Salidas:
No retorna valor. Muestra mensajes en consola indicando el resultado de la operación.

Comportamiento:
- Solicita los datos al usuario uno por uno.
- Agrupa los datos en un diccionario.
- Guarda el diccionario como parámetro en insertar_producto.
- Llama a la función insertar_producto para guardar el producto en la base de datos.
- Informa al usuario si el registro fue exitoso.

### Función: insertar_producto(datos_producto)

Propósito:
Recibir un diccionario con los datos de un producto y guardarlo como un nuevo documento en la colección 'producto' de la base de datos.

Entradas:
- datos_producto: Diccionario con las claves codigo_producto, nombre, precio, stock y estado.

Salidas:
No retorna valor. Muestra un mensaje en consola indicando si el producto fue registrado con éxito. "Producto agregado con éxito."

Comportamiento:
- Conecta a la base de datos utilizando la función conectar.
- Inserta el diccionario recibido como un nuevo documento en la colección 'producto'.
- Informa al usuario del éxito de la operación.

### Función: actualizar_producto()

Propósito:
Permitir al usuario modificar los datos de un producto existente, identificándolo por su código. El usuario puede actualizar el nombre, precio, stock y estado. Solo se actualizan los campos que el usuario desee modificar. Los datos se agrupan en un diccionario y se pasan como parámetro a la actualización en la base de datos.

Entradas:
No recibe parámetros directamente; los datos se obtienen mediante la interacción con el usuario.

Salidas:
No retorna valor. Muestra mensajes en consola indicando el resultado de la operación.

Comportamiento:
- Solicita al usuario el código del producto a actualizar.
- Permite dejar en blanco los campos que no se desean modificar.
- Agrupa los nuevos datos en un diccionario.
- Si no se ingresan datos nuevos, informa al usuario y termina la operación.
- Realiza la actualización en la base de datos usando el código como filtro y el diccionario de nuevos datos como parámetro.
- Informa si la actualización fue exitosa ("Producto actualizado con éxito.") o si no se encontró el producto ("No se encontró un producto con ese código.").

### Función: eliminar_producto()

Propósito:
Eliminar un producto de la base de datos, identificándolo por su código. El código se solicita al usuario y se utiliza como filtro para eliminar el primer producto que coincida.

Entradas:
No recibe parámetros directamente; el código se solicita al usuario por consola.

Salidas:
No retorna valor. Muestra mensajes en consola indicando el resultado de la operación.

Comportamiento:
- Solicita al usuario el código del producto a eliminar.
- Busca y elimina el primer producto que coincida con el código proporcionado.
- Informa si la eliminación fue exitosa ("Producto eliminado con éxito.") o si no se encontró el producto ("No se encontró un producto con ese código.").

### Función: consultar_producto_codigo()

Propósito:
Buscar y mostrar los datos de un producto cuyo código coincida con el proporcionado por el usuario. El código se solicita al usuario y se utiliza como filtro para buscar en la base de datos.

Entradas:
No recibe parámetros directamente; el código se solicita al usuario por consola.

Salidas:
No retorna valor. Muestra en consola los datos del producto encontrado o un mensaje si no se encuentra ninguno.

Comportamiento:
- Solicita al usuario el código a buscar.
- Realiza una búsqueda en la colección 'producto' filtrando por el código.
- Muestra los datos del producto encontrado (código, nombre, precio, stock, estado).
- Informa si no se encontró ningún producto con ese código.

------------------------------------------------------------

## GESTIÓN DE PEDIDOS

### Función: registrar_pedido()

Propósito:
Permitir registrar un nuevo pedido asociado a un cliente, con detalle de los productos solicitados, cantidad de cada uno y método de pago. Al registrar el pedido, se descuenta automáticamente la cantidad pedida del stock de cada producto.

Entradas:
No recibe parámetros directamente; los datos se obtienen mediante la interacción con el usuario.

Salidas:
No retorna valor. Muestra mensajes en consola indicando el resultado de la operación.

Comportamiento:
- Solicita el nombre del cliente y lo busca en la base de datos.
- Si el cliente no existe, informa y cancela el registro del pedido.
- Permite agregar uno o varios productos al pedido, solicitando el código y la cantidad de cada uno.
- Verifica que exista suficiente stock para cada producto antes de agregarlo al pedido.
- Si hay suficiente stock, descuenta la cantidad pedida del stock del producto en la base de datos.
- Si no hay suficiente stock, informa al usuario y no permite agregar ese producto al pedido.
- Solicita el método de pago.
- Crea un documento de pedido con los datos del cliente, el detalle de productos (código, nombre, cantidad, precio unitario) y el método de pago.
- Inserta el pedido en la colección 'pedido' de la base de datos.
- Informa al usuario si el pedido fue registrado con éxito.

### Función: actualizar_pedido()

Propósito:
Permitir modificar el método de pago de un pedido existente, identificándolo por su ID. Solo se actualizan los campos que el usuario desee modificar.

Entradas:
No recibe parámetros directamente; el ID del pedido y los nuevos datos se solicitan al usuario por consola.

Salidas:
No retorna valor. Muestra mensajes en consola indicando el resultado de la operación.

Comportamiento:
- Solicita al usuario el ID del pedido a actualizar.
- Busca el pedido en la base de datos usando el ObjectId.
- Permite dejar en blanco los campos que no se desean modificar.
- Si no se ingresan datos nuevos, informa al usuario y termina la operación.
- Realiza la actualización en la base de datos usando el ID como filtro y el diccionario de nuevos datos como parámetro.
- Informa si la actualización fue exitosa ("Pedido actualizado con éxito.") o si no se pudo actualizar el pedido.

### Función: eliminar_pedido()

Propósito:
Eliminar un pedido de la base de datos, identificándolo por su ID. El ID se solicita al usuario y se utiliza como filtro para eliminar el pedido correspondiente.

Entradas:
No recibe parámetros directamente; el ID se solicita al usuario por consola.

Salidas:
No retorna valor. Muestra mensajes en consola indicando el resultado de la operación.

Comportamiento:
- Solicita al usuario el ID del pedido a eliminar.
- Busca y elimina el pedido que coincida con el ID proporcionado.
- Informa si la eliminación fue exitosa ("Pedido eliminado con éxito.") o si no se encontró el pedido ("No se encontró un pedido con ese ID.").

### Función: buscar_pedidos_por_cliente()

Propósito:
Permitir consultar todos los pedidos realizados por un cliente específico, identificándolo por su nombre.

Entradas:
No recibe parámetros directamente; el nombre del cliente se solicita al usuario por consola.

Salidas:
No retorna valor. Muestra en consola los datos de los pedidos encontrados o un mensaje si no se encuentra ninguno.

Comportamiento:
- Solicita al usuario el nombre del cliente a buscar.
- Realiza una búsqueda en la colección 'pedido' filtrando por el nombre del cliente.
- Muestra los datos de cada pedido encontrado (ID, cliente, método de pago, productos, cantidad, precio unitario).
- Informa si no se encontró ningún pedido para ese cliente.

------------------------------------------------------------

## MENÚ PRINCIPAL

### Función: menu()

Propósito:
Presentar al usuario un menú interactivo en la consola para gestionar clientes. Permite seleccionar entre registrar, actualizar, buscar, eliminar clientes o salir del sistema.

Entradas:
No recibe parámetros.

Salidas:
No retorna valor. Controla el flujo del programa y muestra mensajes en consola.

Comportamiento:
- Muestra las opciones disponibles en el menú.
- Solicita al usuario que seleccione una opción.
- Llama a la función correspondiente según la opción elegida.
- Permite salir del sistema de forma segura.

------------------------------------------------------------

Nota: Los módulos de productos y pedidos aún no tienen funcionalidades implementadas.
