import streamlit as st
import stanza
import fitz  # PyMuPDF

# Inicializar Stanza para español
@st.cache_resource
def load_nlp():
    stanza.download('es')
    return stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma')

nlp = load_nlp()

# Función para extraer títulos de libros desde libros.pdf
def extract_book_titles(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    # Suponemos que cada línea es un título de libro
    titles = [line.strip() for line in text.split('\n') if line.strip()]
    return titles

# Función para generar ficha de comprensión lectora
def generate_comprehension_card(title):
    doc = nlp(title)
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

# Función para análisis pedagógico (simulado)
def analyze_book(title):
    return f"📘 El libro '{title}' es adecuado para alumnos de primaria. Su contenido fomenta la lectura comprensiva, el desarrollo del vocabulario y el pensamiento crítico."

# Función para recomendar libros
def recommend_books(selected_title, all_titles):
    recomendaciones = [t for t in all_titles if t.lower() != selected_title.lower()]
    recomendaciones = recomendaciones[:3]
    pros_contras = {
        t: {
            "Pros": ["Estimula la imaginación", "Lenguaje enriquecido", "Temas educativos"],
            "Contras": ["Puede tener vocabulario avanzado", "Requiere acompañamiento"]
        } for t in recomendaciones
    }
    return recomendaciones, pros_contras

# Interfaz Streamlit
st.set_page_config(page_title="Buscador Pedagógico de Libros", layout="centered")
st.title("📚 Buscador y análisis pedagógico de libros")

# Cargar títulos desde libros.pdf
libros_pdf_path = "libros.pdf"
libros_disponibles = extract_book_titles(libros_pdf_path)

# Entrada del usuario
titulo = st.text_input("🔍 Introduce el título del libro que quieres analizar")

if titulo:
    if titulo in libros_disponibles:
        st.success(f"✅ Libro encontrado: {titulo}")

        # Análisis pedagógico
        st.subheader("🧠 Análisis pedagógico")
        st.write(analyze_book(titulo))

        # Ficha de comprensión lectora
        st.subheader("📋 Ficha de comprensión lectora")
        ficha = generate_comprehension_card(titulo)
        st.json(ficha)

        # Recomendaciones
        st.subheader("📈 Recomendaciones para avanzar")
        recomendaciones, pros_contras = recommend_books(titulo, libros_disponibles)
        for libro in recomendaciones:
            st.markdown(f"### {libro}")
            st.markdown(f"**Pros:** {', '.join(pros_contras[libro]['Pros'])}")
            st.markdown(f"**Contras:** {', '.join(pros_contras[libro]['Contras'])}")
    else:
        st.error("❌ Libro no encontrado en el archivo libros.pdf. Verifica el título.")

