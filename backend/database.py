from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["proyectoml"]

def guardarDocumento(texto, resultado):
    collection = db["documentos"]
    nuevo_id = collection.count_documents({}) + 1
    collection.insert_one({"_id": nuevo_id, "documento": texto, "resultado": resultado})
    print(f"Database => Documento {nuevo_id} guardado.")

def listarDocumentos():
    collection = db["documentos"]
    num_documentos = collection.count_documents({})

    if num_documentos == 0:
        print("Database => No se encontraron documentos en la colección 'documentos'.")
        return None
    else:
        print(f"Database => Se encontraron {num_documentos} documentos en la colección 'documentos'.")
        docs = collection.find()
        return docs