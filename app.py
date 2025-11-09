import streamlit as st
import pandas as pd
import stanza

# Inicializar Stanza para español
stanza.download('es')
nlp = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma')

# Cargar títulos desde libros.csv
libros_df = pd.read_csv("libros.csv")
libros = libros_df["Título"].dropna().tolist()

# Función para generar ficha de comprensión lectora
def generar_ficha(texto):
    doc = nlp(texto)
    num_frases = len(doc.sentences)
    num_palabras = sum(len(sent.words) for sent in doc.sentences)
    palabras_clave = list(set(
        word.lemma for sent in doc.sentences for word in sent.words
        if word.upos in ["NOUN", "VERB"]
    ))
    return {
        "Número de frases": num_frases,
        "Número de palabras": num_palabras,
        "Palabras clave": palabras_clave[:10]
    }

# Función para análisis pedagógico (simulado)
def analizar_libro(titulo):
    return f"El libro '{titulo}' es adecuado para alumnos de primaria. Promueve la lectura comprensiva, el desarrollo del vocabulario y el pensamiento crítico."

# Función para recomendar libros
def recomendar_libros(titulo, lista):
    candidatos = [t for t in lista if t.lower() != titulo.lower()]
    recomendaciones = candidatos[:3]
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

# Entrada del usuario
titulo = st.text_input("🔍 Introduce el título del libro que quieres analizar")

if titulo:
    coincidencias = [t for t in libros if titulo.lower() in t.lower()]
    if coincidencias:
        seleccionado = coincidencias[0]
        st.success(f"✅ Libro encontrado: {seleccionado}")

        # Análisis pedagógico
        st.subheader("🧠 Análisis pedagógico")
        st.write(analizar_libro(seleccionado))

        # Ficha de comprensión lectora
        st.subheader("📋 Ficha de comprensión lectora")
        ficha = generar_ficha(seleccionado)
        st.json(ficha)

        # Recomendaciones
        st.subheader("📈 Recomendaciones para avanzar")
        recomendaciones, pros_contras = recomendar_libros(seleccionado, libros)
        for libro in recomendaciones:
            st.markdown(f"### {libro}")
            st.markdown(f"**Pros:** {', '.join(pros_contras[libro]['Pros'])}")
            st.markdown(f"**Contras:** {', '.join(pros_contras[libro]['Contras'])}")
    else:
        st.error("❌ No se encontró el título en libros.csv. Verifica el texto o intenta con otra palabra clave.")
