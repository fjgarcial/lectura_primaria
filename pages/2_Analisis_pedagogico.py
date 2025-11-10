
import streamlit as st
import pandas as pd
from utils.ia_analysis import analizar_texto
from utils.docx_generator import generar_ficha_comprension

st.set_page_config(page_title="Análisis pedagógico", layout="wide")
st.title("📖 Análisis pedagógico y recomendaciones")

libros = pd.read_csv("data/libros.csv")
titulos = libros["titulo"].tolist()
seleccion = st.selectbox("Selecciona un libro para analizar", titulos)

if seleccion:
    libro = libros[libros["titulo"] == seleccion].iloc[0]
    texto = libro["texto"]
    st.subheader("📊 Análisis del texto")
    resultado = analizar_texto(texto)
    st.json(resultado)

    st.subheader("📄 Generar ficha de comprensión")
    contenido = texto[:500] + "..."
    preguntas = [
        "¿Quién es el personaje principal?",
        "¿Dónde ocurre la historia?",
        "¿Qué problema se presenta?",
        "¿Cómo se resuelve?",
        "¿Qué opinas del final?"
    ]
    if st.button("Generar y descargar ficha DOCX"):
        archivo = generar_ficha_comprension(seleccion, contenido, preguntas)
        with open(archivo, "rb") as f:
            st.download_button("📥 Descargar ficha", f, file_name=archivo)
