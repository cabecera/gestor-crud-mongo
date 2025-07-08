from pymongo import MongoClient


try:
    def conectar():
        client = MongoClient("mongodb://localhost:27017/")
        bd = client["proyecto_mongo"]
        return bd

except Exception as ex:
    print(f"Error al conectar a la base de datos: {ex}")
    exit()