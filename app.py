import streamlit as st
import json

libros = [
    "Donde viven los monstruos",
    "Las aventuras de Alicia en el país de las maravillas",
    "Pippi Calzaslargas",
    "El principito",
    "El hobbit",
    "Luces del norte",
    "Matilda",
    "Momo",
    "La historia interminable",
    "El prodigioso viaje de Edward Tulane",
    # Puedes añadir más títulos del listado si lo deseas
]

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

# Sección 2: Recomendaciones lectoras
st.header("2️⃣ Recomendaciones lectoras con IA")
sugerencias = []
if titulo:
    sugerencias = [lib for lib in libros if lib.lower() != titulo.lower()][:3]
    st.write("📖 Libros recomendados:")
    for libro in sugerencias:
        st.markdown(f"- {libro}")

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
        "Libros recomendados": sugerencias,
        "Ficha de comprensión": {
            "Literales": [f"¿Quién es el personaje principal de '{titulo}'?", "¿Dónde ocurre la historia?"],
            "Inferenciales": ["¿Por qué el personaje actúa de esa manera?", "¿Qué emociones transmite el texto?"],
            "Críticas": ["¿Estás de acuerdo con las decisiones del personaje? ¿Por qué?", "¿Qué cambiarías tú en la historia?"]
        }
    }

    st.download_button("📥 Descargar informe en JSON", data=json.dumps(informe, indent=2), file_name="informe_lectura_IA.json")