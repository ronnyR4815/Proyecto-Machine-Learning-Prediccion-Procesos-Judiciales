from pymongo import MongoClient
import numpy as np

client = MongoClient("mongodb://localhost:27017/")
db = client["proyectoml"]

def guardarDocumento(nombre, texto, resultado):
    collection = db["documentos"]
    nuevo_id = collection.count_documents({}) + 1
    collection.insert_one({"_id": nuevo_id, "nombre": nombre, "documento": texto, "resultado": resultado})
    print(f"Database => Documento {nuevo_id} guardado.")

def extraerDocumentos():
    collection = db["documentos"]
    documentos = collection.find({})
    return [doc['documento'] for doc in documentos]

def getDocumentos():
    collection = db['documentos']
    documentos = collection.find({}, {'_id': 1, 'nombre': 1, 'resultado': 1})  # Proyección para incluir solo id, nombre y resultado
    return list(documentos)

def guardarMatrizTfidf(tfidf):
    collection = db["matriz_tfidf"]
    collection.drop()
    matrix_tfidf = tfidf.tolist()
    collection.insert_one({"_id": 1, "matriz": matrix_tfidf})
    print("Database => Matriz TF-IDF guardada.")

def consultarTfidf():
    collection = db["matriz_tfidf"]
    tfidf = collection.find_one({"_id": 1})
    tfidf = np.array(tfidf['matriz'])
    return tfidf

def guardarMatrizDistancias(distance_matrix):
    collection = db["matriz_distancias"]
    collection.drop()
    distance_matrix_list = distance_matrix.tolist()
    collection.insert_one({"_id": 1, "matriz": distance_matrix_list})
    print("Database => Matriz de distancias guardada.")