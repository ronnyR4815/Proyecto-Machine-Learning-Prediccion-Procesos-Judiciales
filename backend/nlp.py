import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from scipy.cluster.hierarchy import linkage, fcluster
from sklearn.metrics.cluster import adjusted_rand_score, normalized_mutual_info_score, adjusted_mutual_info_score
import PyPDF2
import re
import numpy as np
import os


# nltk.download('stopwords')
# nltk.download('punkt')

# Leer PDF
def leerPdfs(path):
    textos = []
    for filename in os.listdir(path):
        if filename.endswith('.pdf'):
            complete_path = os.path.join(path, filename)
            with open(complete_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ''

                # Lee el texto de cada página
                for page in reader.pages:
                    text += page.extract_text()

                clear_text = re.sub('^.*?OFICIO\\s*\\([^)]*\\)\\s*', '', text, flags=re.DOTALL) # Limpieza cabecera del proceso
                clear_text = re.sub('\\d{2}/\\d{2}/\\d{4} \\d{2}:\\d{2}.*?\\n', '', clear_text)  # Limpieza de subitulos-etiquetas,fechas,horas
                clear_text = re.sub('[^\\w\\s]|\\d', '',clear_text) # Limpieza de caracteres especiales y numeros
            textos.append(clear_text)
    return textos

def leerPdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ''

    # Lee el texto de cada página
    for page in reader.pages:
        text += page.extract_text()

    clear_text = re.sub('^.*?OFICIO\\s*\\([^)]*\\)\\s*', '', text, flags=re.DOTALL) # Limpieza cabecera del proceso
    clear_text = re.sub('\\d{2}/\\d{2}/\\d{4} \\d{2}:\\d{2}.*?\\n', '', clear_text)  # Limpieza de subitulos-etiquetas,fechas,horas
    clear_text = re.sub('[^\\w\\s]|\\d', '',clear_text) # Limpieza de caracteres especiales y numeros
    return clear_text


def preprocess_text(docs):
    text = []
    for i in docs:
      text1 = re.sub('[^\\w\\s]+',' ',i, flags=re.UNICODE)
      # Tokenización
      tokens = word_tokenize(text1.lower())
      # Eliminación de stopwords
      stop_words = set(stopwords.words("spanish"))
      stop_words.update(["página", "culpable", "inocente"])
      filtered_tokens = [word for word in tokens if word not in stop_words]
      # Stemming
      stemmer = SnowballStemmer("spanish")
      tokens_stemmer = []
      for i in filtered_tokens:
        tokens_stemmer.append(stemmer.stem(i))
      # Reconstrucción del texto preprocesado
      preprocessed_text = ' '.join(tokens_stemmer)
      text.append(preprocessed_text)
    return text

# for i, docs in enumerate(docs, start=1):
#     database.guardarDocumento(i, docs)

# request = database.listarDocumentos()
# datos = []
# for i in request:
#     datos.append(i["doc"])