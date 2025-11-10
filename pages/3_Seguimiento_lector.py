
import streamlit as st
import pandas as pd

st.title("Seguimiento lector")

libros = pd.read_csv("libros.csv")
libros.columns = libros.columns.str.lower()

if "texto" in libros.columns and "titulo" in libros.columns:
    titulos = libros["titulo"].dropna().unique().tolist()
    seleccion = st.selectbox("Selecciona un título para leer", titulos)
    libro = libros[libros["titulo"] == seleccion]
    texto = libro["texto"].values[0] if not libro["texto"].isna().all() else "Texto no disponible."
    st.subheader("Texto del libro")
    st.write(texto)
else:
    st.warning("Las columnas 'titulo' o 'texto' no están disponibles en el archivo CSV.")
