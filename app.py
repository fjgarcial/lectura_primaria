import streamlit as st
import json
from PyPDF2 import PdfReader

# Leer listado de libros desde el PDF
reader = PdfReader("Listado_100_Libros_Infantiles.pdf")
libros = []
for page in reader.pages:
    libros += page.extract_text().split("\n")

st.set_page_config(page_title='Análisis Pedagógico con IA', layout='wide')
st.title("📚 Web Educativa con IA para Itinerarios de Lectura")

st.markdown("Esta aplicación permite a docentes analizar libros infantiles, recibir recomendaciones lectoras automáticas y generar fichas de comprensión lectora.")

# Sección 1: Análisis del libro inicial
st.header("1️⃣ Análisis del libro inicial")
titulo = st.text_input("Título del libro")
vocabulario = st.selectbox("Nivel de vocabulario", ["Básico", "Intermedio", "Avanzado"])
sintaxis = st.selectbox("Complejidad sintáctica", ["Oraciones simples", "Oraciones compuestas", "Subordinadas múltiples"])
tiempos = st.multiselect("Tiempos verbales presentes", ["Presente", "Pasado simple", "Pasado compuesto", "Condicional", "Futuro"])
complejidad = st.slider("Complejidad textual (1=baja, 10=alta)", 1, 10)
tematica = st.text_area("Temática principal")

# Sección 2: Recomendaciones lectoras con IA
st.header("2️⃣ Recomendaciones lectoras con IA")
recomendaciones = []
pros_contras = {}
if titulo:
    recomendaciones = [lib for lib in libros if lib.strip().lower() != titulo.strip().lower()][:3]
    for rec in recomendaciones:
        pros_contras[rec] = {
            "Pros": [
                f"Lenguaje más elaborado que en '{titulo}'",
                "Mayor profundidad temática",
                "Estructura narrativa más compleja"
            ],
            "Contras": [
                "Requiere mayor atención lectora",
                "Algunos pasajes pueden ser difíciles sin mediación"
            ]
        }
    st.write("📖 Libros recomendados:")
    for rec in recomendaciones:
        st.markdown(f"### {rec}")
        st.markdown("**Pros:**")
        for pro in pros_contras[rec]["Pros"]:
            st.markdown(f"- {pro}")
        st.markdown("**Contras:**")
        for con in pros_contras[rec]["Contras"]:
            st.markdown(f"- {con}")

# Sección 3: Ficha de comprensión lectora
st.header("3️⃣ Ficha de comprensión lectora generada")
if titulo:
    st.subheader("Preguntas Literales")
    st.markdown(f"1. ¿Quién es el personaje principal de '{titulo}'?")
    st.markdown("2. ¿Dónde ocurre la historia?")

    st.subheader("Preguntas Inferenciales")
    st.markdown("3. ¿Por qué el personaje actúa de esa manera?")
    st.markdown("4. ¿Qué emociones transmite el texto?")

    st.subheader("Preguntas Críticas")
    st.markdown("5. ¿Estás de acuerdo con las decisiones del personaje? ¿Por qué?")
    st.markdown("6. ¿Qué cambiarías tú en la historia?")

    informe = {
        "Libro inicial": titulo,
        "Análisis pedagógico": {
            "Vocabulario": vocabulario,
            "Sintaxis": sintaxis,
            "Tiempos verbales": tiempos,
            "Complejidad textual": complejidad,
            "Temática": tematica
        },
        "Libros recomendados": recomendaciones,
        "Pros y Contras": pros_contras,
        "Ficha de comprensión": {
            "Literales": [f"¿Quién es el personaje principal de '{titulo}'?", "¿Dónde ocurre la historia?"],
            "Inferenciales": ["¿Por qué el personaje actúa de esa manera?", "¿Qué emociones transmite el texto?"],
            "Críticas": ["¿Estás de acuerdo con las decisiones del personaje? ¿Por qué?", "¿Qué cambiarías tú en la historia?"]
        }
    }

    st.download_button("📥 Descargar informe en JSON", data=json.dumps(informe, indent=2), file_name="informe_lectura_IA.json")
