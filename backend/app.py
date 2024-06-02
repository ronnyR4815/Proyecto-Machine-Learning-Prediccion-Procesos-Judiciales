from flask import Flask, request, jsonify
from flask_cors import CORS
import database as db
import nlp
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/guardar_documento', methods=['POST'])
def guardar_documento():
    filePdf = request.files['filePdf']
    resultado = request.form['resultado']
    nombre = request.form['nombre']

    # Aquí deberías procesar el PDF y extraer el texto
    texto_pdf = nlp.leerPdf(filePdf)
    
    # Realizar preprocesamiento de texto
    texto_preprocesado = nlp.preprocess_text([texto_pdf])[0]
    
    # Guardar el documento preprocesado en la base de datos
    db.guardarDocumento(nombre, texto_preprocesado, resultado)

    docs = db.extraerDocumentos()
    tf_idf = nlp.procesar_documentos(docs)
    distance_matrix = nlp.procesar_matriz_distancias(tf_idf)

    db.guardarMatrizTfidf(tf_idf)
    db.guardarMatrizDistancias(distance_matrix)
    
    return jsonify({'message': 'Documento procesado y guardado exitosamente.'}), 200

@app.route('/test', methods=['POST'])
def analizar_documento():
    filePdf = request.files['file']

    # Aquí deberías procesar el PDF y extraer el texto
    texto_pdf = nlp.leerPdf(filePdf)
    
    # Realizar preprocesamiento de texto
    doc_prediccion = nlp.preprocess_text([texto_pdf])[0]

    docs = db.extraerDocumentos()
    docs.append(doc_prediccion)

    tf_idf = nlp.procesar_documentos(docs)
    distance_matrix = nlp.procesar_matriz_distancias(tf_idf)

    # Índice del último documento
    last_index = distance_matrix.shape[0] - 1

    inocente_index = last_index - 2
    culpable_index = last_index - 1

    # Distancias entre el último documento y los documentos "inocente" y "culpable"
    distance_to_innocent = distance_matrix[last_index, inocente_index]
    distance_to_guilty = distance_matrix[last_index, culpable_index]

    # Determina cuál de los dos documentos tiene la menor distancia
    if distance_to_innocent <= distance_to_guilty:
        print("Inocente")
        return jsonify({"message": "Inocente"}), 200
    else:
        print("Culpable")
        return jsonify({"message": "Culpable"}), 200

@app.route('/bolsa_palabras', methods=['GET'])
def bolsa_palabras():
    documentos = db.extraerDocumentos()
    return nlp.full_inverted_index(*documentos)


if __name__ == "__main__":
    app.run(host='0.0.0.0')