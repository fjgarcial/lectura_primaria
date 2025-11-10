
import streamlit as st
import pandas as pd

st.title("Busca libros")

libros = pd.read_csv("libros.csv")
libros.columns = libros.columns.str.lower()

if "edad" in libros.columns:
    edad = st.sidebar.multiselect("Edad", libros["edad"].dropna().unique())
    if edad:
        libros = libros[libros["edad"].isin(edad)]
else:
    st.sidebar.warning("La columna 'edad' no está disponible en el archivo CSV.")

st.write("Libros disponibles:")
st.dataframe(libros)
