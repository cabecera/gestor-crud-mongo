from pymongo import MongoClient

def conectar():
    cliente = MongoClient("mongodb://localhost:27017/")
    bd = cliente["proyecto_mongo"]
    return bd