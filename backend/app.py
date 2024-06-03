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

@app.route('/analizar_documento', methods=['POST'])
def analizar_documento():
    filePdf = request.files['file']

    # Aquí deberías procesar el PDF y extraer el texto
    texto_pdf = nlp.leerPdf(filePdf)
    
    # Realizar preprocesamiento de texto
    doc_prediccion = nlp.preprocess_text([texto_pdf])[0]

    docs = db.extraerDocumentos()
    docs.append(doc_prediccion)

    tf_idf = nlp.procesar_documentos(docs)

    last_index = tf_idf.shape[1] - 1

    inocente_index = last_index - 2
    culpable_index = last_index - 1

    # Compara las filas de last_index con las de inocente_index y culpable_index para determinar si son distintas de cero
    filas_distintas_a_cero_inocente = tf_idf[:, last_index] != 0
    filas_distintas_a_cero_culpable = tf_idf[:, last_index] != 0

    # Suma los valores de las filas distintas de cero en la columna inocente_index
    suma_inocente = np.sum(tf_idf[filas_distintas_a_cero_inocente, inocente_index])

    # Suma los valores de las filas distintas de cero en la columna culpable_index
    suma_culpable = np.sum(tf_idf[filas_distintas_a_cero_culpable, culpable_index])

    if suma_inocente > suma_culpable:
        return jsonify({"message": "Inocente"}), 200
    else:
        return jsonify({"message": "Culpable"}), 200

@app.route('/bolsa_palabras', methods=['GET'])
def bolsa_palabras():
    documentos = db.extraerDocumentos()
    index = nlp.full_inverted_index(*documentos)
    return jsonify(index), 200

@app.route('/get_documentos', methods=['GET'])
def validaciones():
    documentos = db.getDocumentos()
    for doc in documentos:
        doc['_id'] = str(doc['_id'])
    return jsonify(documentos), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')