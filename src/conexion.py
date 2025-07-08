from pymongo import MongoClient


try:
    def conectar():
        cliente = MongoClient("mongodb://localhost:27017/")
        bd = cliente["proyecto_mongo"]
        return bd

except Exception as ex:
    print(f"Error al conectar a la base de datos: {ex}")
    exit()