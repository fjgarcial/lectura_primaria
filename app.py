import streamlit as st
import spacy
import nltk
import textstat
from PyPDF2 import PdfReader
from nltk.corpus import stopwords
from collections import Counter
import random
import io
from docx import Document

# Descargar recursos necesarios
nltk.download('punkt')
nltk.download('stopwords')

# Cargar modelo de spaCy en español
try:
    nlp = spacy.load("es_core_news_sm")
except:
    st.error("El modelo de spaCy 'es_core_news_sm' no está instalado. Añádelo en requirements.txt.")

# Leer listado de libros desde el PDF
reader = PdfReader("libros.pdf")
libros = []
for page in reader.pages:
    libros += page.extract_text().split("\n")
libros = [lib.strip() for lib in libros if lib.strip()]

# Interfaz Streamlit
st.set_page_config(page_title='Análisis Pedagógico con IA', layout='wide')
st.title("📚 Web Educativa con IA para Itinerarios de Lectura")

st.markdown("Esta aplicación permite analizar libros infantiles, generar recomendaciones lectoras y crear fichas de comprensión lectora.")

st.header("1️⃣ Introduce el texto del libro a analizar")
texto_libro = st.text_area("Pega aquí un fragmento representativo del libro")

if texto_libro:
    doc = nlp(texto_libro)
    tokens = [token.text.lower() for token in doc if token.is_alpha and token.text.lower() not in stopwords.words('spanish')]
    palabras_leidas = len(tokens)
    complejidad = textstat.flesch_reading_ease(texto_libro)
    tiempos_verbales = [token.tag_ for token in doc if token.pos_ == "VERB"]
    estructuras = [sent.text for sent in doc.sents if len(sent.text.split()) > 10]
    adjetivos = [token.text for token in doc if token.pos_ == "ADJ"]
    freq_adj = Counter(adjetivos).most_common(5)

    recomendaciones = random.sample([lib for lib in libros if texto_libro.lower() not in lib.lower()], 3)
    pros_contras = {
        rec: {
            "Pros": [
                "Introduce vocabulario más avanzado",
                "Trabaja estructuras narrativas más complejas",
                "Aborda temas con mayor profundidad emocional"
            ],
            "Contras": [
                "Puede requerir mediación docente",
                "Algunos pasajes pueden ser abstractos para ciertos niveles"
            ]
        } for rec in recomendaciones
    }

    # Crear documento Word
    docx_file = Document()
    docx_file.add_heading("Informe Pedagógico de Lectura", 0)
    docx_file.add_heading("1. Análisis pedagógico del libro", level=1)
    docx_file.add_paragraph(f"Palabras leídas: {palabras_leidas}")
    docx_file.add_paragraph(f"Complejidad textual (Flesch): {complejidad:.2f}")
    docx_file.add_paragraph(f"Tiempos verbales utilizados: {', '.join(set(tiempos_verbales))}")
    docx_file.add_paragraph(f"Número de oraciones con estructura compleja: {len(estructuras)}")
    docx_file.add_paragraph(f"Adjetivos más frecuentes: {', '.join([adj for adj, _ in freq_adj])}")

    docx_file.add_heading("2. Recomendaciones lectoras", level=1)
    for rec in recomendaciones:
        docx_file.add_heading(rec, level=2)
        docx_file.add_paragraph("Pros:")
        for pro in pros_contras[rec]["Pros"]:
            docx_file.add_paragraph(f"- {pro}", style='List Bullet')
        docx_file.add_paragraph("Contras:")
        for con in pros_contras[rec]["Contras"]:
            docx_file.add_paragraph(f"- {con}", style='List Bullet')

    docx_file.add_heading("3. Ficha de comprensión lectora", level=1)
    docx_file.add_heading("Preguntas Literales", level=2)
    docx_file.add_paragraph("1. ¿Quién es el personaje principal del texto?")
    docx_file.add_paragraph("2. ¿Dónde ocurre la historia?")
    docx_file.add_heading("Preguntas Inferenciales", level=2)
    docx_file.add_paragraph("3. ¿Por qué el personaje actúa de esa manera?")
    docx_file.add_paragraph("4. ¿Qué emociones transmite el texto?")
    docx_file.add_heading("Preguntas Críticas", level=2)
    docx_file.add_paragraph("5. ¿Estás de acuerdo con las decisiones del personaje? ¿Por qué?")
    docx_file.add_paragraph("6. ¿Qué cambiarías tú en la historia?")

    # Descargar DOCX
    buffer = io.BytesIO()
    docx_file.save(buffer)
    buffer.seek(0)

    st.download_button(
        label="📥 Descargar informe en Word",
        data=buffer,
        file_name="informe_lectura.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

