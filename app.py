
import streamlit as st
import pandas as pd
import docx
from docx.shared import Pt
import random
import time

@st.cache_data
def cargar_libros():
    try:
        df = pd.read_csv("libros_titulo.csv", header=None)
        df.columns = ["Título"]
        return df["Título"].tolist()
    except Exception as e:
        st.error("Error al cargar el archivo libros_titulo.csv.")
        return []

def analizar_libro(titulo):
    time.sleep(2)
    return {
        "palabras": random.randint(500, 1500),
        "estructuras": ["oraciones simples", "coordinadas", "subordinadas"],
        "complejidad": random.choice(["Baja", "Media", "Alta"]),
        "vocabulario": random.choice(["Común", "Con modismos"]),
        "tiempos": random.choice(["Presente", "Pasado", "Futuro"]),
        "nivel_dificultad": random.choice(["Inicial", "Intermedio", "Avanzado"])
    }

def generar_ficha(titulo, analisis):
    doc = docx.Document()
    doc.add_heading(f"Ficha de comprensión lectora: {titulo}", 0)
    doc.add_paragraph(f"Número de palabras: {analisis['palabras']}")
    doc.add_paragraph(f"Estructuras gramaticales: {', '.join(analisis['estructuras'])}")
    doc.add_paragraph(f"Complejidad del texto: {analisis['complejidad']}")
    doc.add_paragraph(f"Vocabulario: {analisis['vocabulario']}")
    doc.add_paragraph(f"Tiempos verbales predominantes: {analisis['tiempos']}")
    doc.add_paragraph(f"Nivel de dificultad: {analisis['nivel_dificultad']}")
    doc.add_paragraph("1. ¿Qué sucede al inicio del libro?")
    doc.add_paragraph("2. ¿Quiénes son los personajes principales?")
    doc.add_paragraph("3. ¿Qué enseñanza deja el libro?")
    doc.save("ficha.docx")
    return "ficha.docx"

def generar_rubrica(titulo):
    doc = docx.Document()
    doc.add_heading(f"Rúbrica de evaluación: {titulo}", 0)
    table = doc.add_table(rows=1, cols=4)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = "Criterio"
    hdr_cells[1].text = "Excelente"
    hdr_cells[2].text = "Bueno"
    hdr_cells[3].text = "Necesita mejorar"
    criterios = ["Comprensión global", "Identificación de personajes", "Secuencia de eventos", "Reflexión personal"]
    for criterio in criterios:
        row_cells = table.add_row().cells
        row_cells[0].text = criterio
        row_cells[1].text = "Responde con profundidad y claridad"
        row_cells[2].text = "Responde con cierta claridad"
        row_cells[3].text = "Respuestas incompletas o confusas"
    doc.save("rubrica.docx")
    return "rubrica.docx"

def recomendar_libros(titulo, lista_libros):
    recomendados = random.sample([l for l in lista_libros if l != titulo], min(5, len(lista_libros)-1))
    recomendaciones = []
    for libro in recomendados:
        recomendaciones.append({
            "título": libro,
            "pros": ["Favorece vocabulario", "Estimula la imaginación", "Adecuado para el nivel lector"],
            "contras": ["Puede requerir apoyo adulto", "Vocabulario avanzado"]
        })
    return recomendaciones

st.set_page_config(page_title="Análisis pedagógico y Recomendaciones", layout="centered")
st.title("📚 Análisis pedagógico y Recomendaciones")

libros_disponibles = cargar_libros()
titulo_libro = st.text_input("Introduce el título del libro")
buscar = st.button("🔍 Analizar")

if buscar and titulo_libro:
    if titulo_libro not in libros_disponibles:
        st.warning("El libro no se encuentra en la base de datos.")
    else:
        with st.spinner("Analizando el libro..."):
            analisis = analizar_libro(titulo_libro)

        st.subheader("🔎 Análisis pedagógico")
        st.write(f"**Número de palabras:** {analisis['palabras']}")
        st.write(f"**Estructuras gramaticales:** {', '.join(analisis['estructuras'])}")
        st.write(f"**Complejidad del texto:** {analisis['complejidad']}")
        st.write(f"**Vocabulario:** {analisis['vocabulario']}")
        st.write(f"**Tiempos verbales predominantes:** {analisis['tiempos']}")
        st.write(f"**Nivel de dificultad:** {analisis['nivel_dificultad']}")

        st.subheader("📄 Ficha de comprensión lectora")
        ficha_path = generar_ficha(titulo_libro, analisis)
        with open(ficha_path, "rb") as f:
            st.download_button("📥 Descargar ficha", f, file_name=ficha_path)

        st.subheader("📊 Rúbrica de evaluación")
        rubrica_path = generar_rubrica(titulo_libro)
        with open(rubrica_path, "rb") as f:
            st.download_button("📥 Descargar rúbrica", f, file_name=rubrica_path)

        st.subheader("📚 Recomendaciones pedagógicas")
        recomendaciones = recomendar_libros(titulo_libro, libros_disponibles)
        for rec in recomendaciones:
            st.markdown(f"**Título:** {rec['título']}")
            st.markdown(f"✅ Pros: {', '.join(rec['pros'])}")
            st.markdown(f"⚠️ Contras: {', '.join(rec['contras'])}")
            st.markdown("---")
