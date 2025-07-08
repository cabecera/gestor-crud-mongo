DOCUMENTACIÓN DE FUNCIONALIDADES

A continuación se describen en detalle las funcionalidades implementadas hasta el momento en el sistema.

------------------------------------------------------------

CONEXIÓN A LA BASE DE DATOS

Función: conectar()

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

GESTIÓN DE CLIENTES

### Función: registrar_cliente()

Propósito:
Solicitar al usuario, a través de la consola, los datos necesarios para registrar un nuevo cliente en el sistem, son: nombre, apellido, direccion:{calle,numero,ciudad} y fecha de registro. Una vez obtenidos, se agrupan en un diccionario y se envían a la función encargada de insertar el cliente en la base de datos.

Entradas:
No recibe parámetros directamente; los datos se obtienen mediante la interacción con el usuario.

Salidas:
No retorna valor. Muestra mensajes en consola indicando el resultado de la operación.

Comportamiento:
- Solicita los datos al usuario uno por uno.
- Agrupa los datos en un diccionario.
- Guarda el diccionario como parametro en insertar_cliente
- Llama a la función insertar_cliente para guardar el cliente en la base de datos.
- Informa al usuario si el registro fue exitoso.

### Función: insertar_cliente(datos_cliente)

Propósito:
Insertar un nuevo documento en la colección 'cliente' de la base de datos, utilizando los datos proporcionados en un diccionario.

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
Permitir al usuario modificar los datos de un cliente existente, identificándolo por su nombre. El usuario puede actualizar el apellido, la dirección y la fecha de registro. Solo se actualizan los campos que el usuario desee modificar.

Entradas:
No recibe parámetros directamente; los datos se obtienen mediante la interacción con el usuario.

Salidas:
No retorna valor. Muestra mensajes en consola indicando el resultado de la operación.

Comportamiento:
- Solicita al usuario el nombre del cliente a actualizar.
- Permite dejar en blanco los campos que no se desean modificar.
- Construye un diccionario solo con los campos a actualizar.
- Realiza la actualización en la base de datos usando el nombre como filtro.
- Informa si la actualización fue exitosa o si no se encontró el cliente.

### Función: eliminar_cliente()

Propósito:
Eliminar un cliente de la base de datos, identificándolo por su nombre.

Entradas:
No recibe parámetros directamente; el nombre se solicita al usuario por consola.

Salidas:
No retorna valor. Muestra mensajes en consola indicando el resultado de la operación.

Comportamiento:
- Solicita al usuario el nombre del cliente a eliminar.
- Busca y elimina el primer cliente que coincida con el nombre proporcionado.
- Informa si la eliminación fue exitosa o si no se encontró el cliente.

### Función: buscar_cliente()

Propósito:
Buscar y mostrar los datos de todos los clientes cuyo nombre coincida con el proporcionado por el usuario.

Entradas:
No recibe parámetros directamente; el nombre se solicita al usuario por consola.

Salidas:
No retorna valor. Muestra en consola los datos de los clientes encontrados o un mensaje si no se encuentra ninguno.

Comportamiento:
- Solicita al usuario el nombre a buscar.
- Realiza una búsqueda en la colección 'cliente' filtrando por el nombre.
- Muestra los datos de cada cliente encontrado (nombre, apellido, dirección:{calle,numero,ciudad}, fecha de registro).
- Informa si no se encontró ningún cliente con ese nombre. "No se encontró ningún cliente con ese nombre."

------------------------------------------------------------

MENÚ PRINCIPAL

Función: menu()

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
