
import streamlit as st
import pandas as pd

st.title("Análisis pedagógico")

libros = pd.read_csv("libros.csv")
libros.columns = libros.columns.str.lower()

if "titulo" in libros.columns:
    titulos = libros["titulo"].dropna().unique().tolist()
    seleccion = st.selectbox("Selecciona un título", titulos)
    libro = libros[libros["titulo"] == seleccion]
    st.write("Detalles pedagógicos del libro seleccionado:")
    st.dataframe(libro)
else:
    st.warning("La columna 'titulo' no está disponible en el archivo CSV.")
