from pymongo import MongoClient

# Función para conectar a la base de datos MongoDB
try:
    def conectar():
        # Crear un cliente de MongoDB al servidor local
        client = MongoClient("mongodb://localhost:27017/")
        # Seleccionar la base de datos "proyecto_mongo"
        bd = client["proyecto_mongo"]
        # Retornar el objeto de base de datos para usar en las operaciones (debas archivos y funciones.py)
        return bd

except Exception as ex:
    # Si ocurre un error al conectar, mostrar el mensaje y salir
    print(f"Error al conectar a la base de datos: {ex}")
    exit()