
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Búsqueda de libros", layout="wide")
st.title("🔍 Búsqueda de libros")

@st.cache_data
def cargar_libros():
    return pd.read_csv("data/libros.csv")

libros = cargar_libros()

st.sidebar.header("🎯 Filtros Generales")
edad = st.sidebar.multiselect("Edad", libros["edad"].unique())
genero = st.sidebar.multiselect("Género", libros["genero"].unique())
tema = st.sidebar.multiselect("Tema", libros["tema"].unique())
idioma = st.sidebar.multiselect("Idioma", libros["idioma"].unique())
autor = st.sidebar.text_input("Autor")

st.sidebar.header("📘 Filtros Pedagógicos")
nivel = st.sidebar.multiselect("Nivel de lectura", libros["nivel_lectura"].unique())
complejidad = st.sidebar.multiselect("Complejidad gramatical", libros["complejidad_gramatical"].unique())
tiempos = st.sidebar.multiselect("Tiempos verbales", libros["tiempos_verbales"].unique())
estructura = st.sidebar.multiselect("Estructura del texto", libros["estructura_texto"].unique())
vocabulario = st.sidebar.multiselect("Vocabulario", libros["vocabulario"].unique())

filtro = libros.copy()
if edad: filtro = filtro[filtro["edad"].isin(edad)]
if genero: filtro = filtro[filtro["genero"].isin(genero)]
if tema: filtro = filtro[filtro["tema"].isin(tema)]
if idioma: filtro = filtro[filtro["idioma"].isin(idioma)]
if autor: filtro = filtro[filtro["autor"].str.contains(autor, case=False, na=False)]
if nivel: filtro = filtro[filtro["nivel_lectura"].isin(nivel)]
if complejidad: filtro = filtro[filtro["complejidad_gramatical"].isin(complejidad)]
if tiempos: filtro = filtro[filtro["tiempos_verbales"].isin(tiempos)]
if estructura: filtro = filtro[filtro["estructura_texto"].isin(estructura)]
if vocabulario: filtro = filtro[filtro["vocabulario"].isin(vocabulario)]

st.write(f"🔎 Se encontraron {len(filtro)} libros:")
st.dataframe(filtro[["titulo", "autor", "edad", "genero", "tema", "idioma"]])
