from flask import Flask, request, jsonify
from flask_cors import CORS
import database as db
import nlp

app = Flask(__name__)
CORS(app)

@app.route('/guardar_documento', methods=['POST'])
def guardar_documento():
    filePdf = request.files['filePdf']
    resultado = request.form['resultado']

    # Aquí deberías procesar el PDF y extraer el texto
    texto_pdf = nlp.leerPdf(filePdf)
    
    # Realizar preprocesamiento de texto
    texto_preprocesado = nlp.preprocess_text([texto_pdf])[0]
    
    # Guardar el documento preprocesado en la base de datos
    db.guardarDocumento(texto_preprocesado, resultado)
    
    return jsonify({'message': 'Documento procesado y guardado exitosamente.'}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')