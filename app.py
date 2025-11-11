
import pandas as pd
import unicodedata
import streamlit as st

def normalizar_texto(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFKD', texto)
    texto = ''.join([c for c in texto if not unicodedata.combining(c)])
    return texto

st.title("Buscador de libros para lectura primaria")

try:
    df = pd.read_csv("libros_titulo.csv")
except FileNotFoundError:
    st.error("No se encontró el archivo 'libros_titulo.csv'. Asegúrate de que esté en el mismo directorio que este script.")
    st.stop()

if 'titulo' not in df.columns:
    st.error("La columna 'titulo' no se encuentra en el archivo CSV.")
    st.stop()

df['titulo_normalizado'] = df['titulo'].apply(normalizar_texto)

titulo_buscado = st.text_input("Introduce el título del libro")

if titulo_buscado:
    titulo_buscado_normalizado = normalizar_texto(titulo_buscado)
    resultados = df[df['titulo_normalizado'].str.contains(titulo_buscado_normalizado)]

    if not resultados.empty:
        st.success(f"Se encontraron {len(resultados)} resultados:")
        st.dataframe(resultados[['titulo']])
    else:
        st.warning("No se encontraron libros que coincidan con la búsqueda.")
