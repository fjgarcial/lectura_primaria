
import streamlit as st
import pandas as pd
import stanza
import docx
from io import BytesIO
import os

@st.cache_resource
def cargar_stanza():
    if not os.path.exists(os.path.expanduser('~/stanza_resources/es')):
        stanza.download('es')
    return stanza.Pipeline('es')

nlp = cargar_stanza()

def analizar_libro_con_stanza(texto):
    doc = nlp(texto)
    palabras = sum(len(sent.words) for sent in doc.sentences)
    estructuras = set()
    tiempos = set()
    vocabulario = set()

    for sent in doc.sentences:
        for word in sent.words:
            estructuras.add(word.deprel)
            tiempos.add(word.feats if word.feats else "N/A")
            vocabulario.add(word.text.lower())

    return {
        "palabras": palabras,
        "estructuras": list(estructuras)[:5],
        "complejidad": "media" if palabras > 500 else "baja",
        "vocabulario": "variado" if len(vocabulario) > 100 else "común",
        "tiempos": list(tiempos)[:3]
    }

def generar_ficha(titulo, analisis):
    doc = docx.Document()
    doc.add_heading(f'Ficha de comprensión lectora: {titulo}', 0)
    doc.add_paragraph(f"Número de palabras: {analisis['palabras']}")
    doc.add_paragraph(f"Estructuras gramaticales: {', '.join(analisis['estructuras'])}")
    doc.add_paragraph(f"Complejidad: {analisis['complejidad']}")
    doc.add_paragraph(f"Vocabulario: {analisis['vocabulario']}")
    doc.add_paragraph(f"Tiempos verbales: {', '.join(analisis['tiempos'])}")
    doc.add_paragraph("
Preguntas sugeridas:")
    doc.add_paragraph("1. ¿Qué sucede al inicio del libro?")
    doc.add_paragraph("2. ¿Qué personaje te ha gustado más y por qué?")
    doc.add_paragraph("3. ¿Qué enseñanza deja el libro?")
    buffer = BytesIO()
    doc.save(buffer)
    return buffer

def generar_rubrica(titulo):
    doc = docx.Document()
    doc.add_heading(f'Rúbrica de evaluación: {titulo}', 0)
    doc.add_paragraph("Criterios:")
    doc.add_paragraph("- Comprensión global del texto")
    doc.add_paragraph("- Identificación de personajes y trama")
    doc.add_paragraph("- Capacidad de inferencia")
    doc.add_paragraph("- Expresión escrita")
    doc.add_paragraph("- Participación en la actividad")
    buffer = BytesIO()
    doc.save(buffer)
    return buffer

@st.cache_data
def recomendar_libros(csv_path="libros_titulo.csv"):
    try:
        df = pd.read_csv(csv_path, header=None)
        libros = df[0].dropna().tolist()
        libros_recomendados = libros[:5]
        recomendaciones = []
        for libro in libros_recomendados:
            recomendaciones.append({
                "titulo": libro,
                "pros": ["Favorece la lectura autónoma", "Vocabulario enriquecido", "Trama motivadora"],
                "contras": ["Puede requerir apoyo adulto", "Extensión elevada", "Temática compleja"]
            })
        return recomendaciones
    except Exception as e:
        st.error(f"Error al cargar recomendaciones: {e}")
        return []

st.set_page_config(page_title="Análisis pedagógico", layout="centered")
st.title("📚 Análisis pedagógico y Recomendaciones")

titulo_libro = st.text_input("Título del libro")
texto_libro = st.text_area("Introduce el contenido del libro o un fragmento", height=300)

if st.button("🔍 Analizar"):
    if texto_libro:
        with st.spinner("Analizando lingüísticamente..."):
            analisis = analizar_libro_con_stanza(texto_libro)
            st.subheader("🔎 Análisis lingüístico")
            st.write(f"**Número de palabras:** {analisis['palabras']}")
            st.write(f"**Estructuras gramaticales:** {', '.join(analisis['estructuras'])}")
            st.write(f"**Complejidad del texto:** {analisis['complejidad']}")
            st.write(f"**Tipo de vocabulario:** {analisis['vocabulario']}")
            st.write(f"**Tiempos verbales predominantes:** {', '.join(analisis['tiempos'])}")

        st.subheader("📄 Ficha de comprensión lectora")
        ficha_buffer = generar_ficha(titulo_libro, analisis)
        st.download_button("📥 Descargar ficha .docx", data=ficha_buffer.getvalue(), file_name=f"ficha_{titulo_libro}.docx")

        st.subheader("📝 Rúbrica de evaluación")
        rubrica_buffer = generar_rubrica(titulo_libro)
        st.download_button("📥 Descargar rúbrica .docx", data=rubrica_buffer.getvalue(), file_name=f"rubrica_{titulo_libro}.docx")

        st.subheader("📚 Recomendaciones pedagógicas")
        recomendaciones = recomendar_libros()
        for rec in recomendaciones:
            st.markdown(f"**📘 {rec['titulo']}**")
            st.markdown("- ✅ Pros:")
            for pro in rec["pros"]:
                st.markdown(f"  - {pro}")
            st.markdown("- ❌ Contras:")
            for contra in rec["contras"]:
                st.markdown(f"  - {contra}")
            st.markdown("---")
    else:
        st.warning("Por favor, introduce el contenido del libro.")
