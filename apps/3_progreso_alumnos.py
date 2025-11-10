
import streamlit as st
import os
from utils.db_utils import obtener_datos_alumno

st.set_page_config(page_title="Progreso de alumnos", layout="wide")
st.title("📊 Seguimiento del progreso lector")

nombre = st.text_input("Introduce el nombre del alumno")

if nombre:
    bases = sorted(os.listdir("data/alumnos"))
    resultados = []
    for db in bases:
        datos = obtener_datos_alumno(f"data/alumnos/{db}", nombre)
        if datos:
            resultados.append((db, datos))

    if resultados:
        for db, datos in resultados:
            st.subheader(f"📚 Clase: {db}")
            st.write({
                "Nombre": datos[1],
                "Libros leídos": datos[2],
                "Palabras leídas": datos[3],
                "Tipología favorita": datos[4],
                "Vocabulario": datos[5],
                "Complejidad gramatical": datos[6],
                "Nivel de lectura": datos[7]
            })
    else:
        st.warning("Alumno no encontrado en ninguna base de datos.")
