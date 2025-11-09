import streamlit as st
import stanza
import fitz  # PyMuPDF
import os

# Inicializar el pipeline de Stanza para español
@st.cache_resource
def load_nlp():
    stanza.download('es')
    return stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma')

nlp = load_nlp()

# Función para extraer texto de un PDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Función para generar ficha de comprensión lectora
def generate_comprehension_card(text):
    doc = nlp(text)
    num_sentences = len(doc.sentences)
    num_words = sum(len(sentence.words) for sentence in doc.sentences)
    keywords = list(set(
        word.lemma for sentence in doc.sentences for word in sentence.words
        if word.upos in ['NOUN', 'VERB']
    ))
    return {
        "Número de frases": num_sentences,
        "Número de palabras": num_words,
        "Palabras clave": keywords[:10]
    }

# Lista de libros disponibles
libros_disponibles = [
    "Matilda",
    "El Principito",
    "Cien años de soledad",
    "Don Quijote de la Mancha",
    "La casa de los espíritus",
    "Rayuela",
    "Pedro Páramo",
    "La sombra del viento"
]

# Función para recomendar libros
def recommend_books(selected_book):
    recomendaciones = [libro for libro in libros_disponibles if libro != selected_book][:3]
    pros_contras = {
        libro: {
            "Pros": ["Enriquece vocabulario", "Profundiza en temas humanos"],
            "Contras": ["Puede tener lenguaje complejo", "Requiere atención"]
        } for libro in recomendaciones
    }
    return recomendaciones, pros_contras

# Interfaz de Streamlit
st.set_page_config(page_title="Análisis Pedagógico de Libros", layout="wide")
st.title("📚 Análisis Pedagógico de Libros en PDF")

uploaded_file = st.file_uploader("📤 Sube el archivo PDF del libro", type="pdf")

if uploaded_file:
    texto = extract_text_from_pdf(uploaded_file)
    st.subheader("📝 Texto extraído")
    st.text_area("Contenido del libro (primeros 1000 caracteres)", texto[:1000], height=300)

    ficha = generate_comprehension_card(texto)
    st.subheader("📋 Ficha de comprensión lectora")
    st.json(ficha)

    libro_seleccionado = st.selectbox("📖 Selecciona el libro analizado", libros_disponibles)
    recomendaciones, pros_contras = recommend_books(libro_seleccionado)

    st.subheader("📈 Recomendaciones para avanzar")
    for libro in recomendaciones:
        st.markdown(f"### {libro}")
        st.markdown(f"**Pros:** {', '.join(pros_contras[libro]['Pros'])}")
        st.markdown(f"**Contras:** {', '.join(pros_contras[libro]['Contras'])}")
