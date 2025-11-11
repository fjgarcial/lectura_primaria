
import streamlit as st

st.set_page_config(page_title="Lectura Primaria", layout="centered")

st.title("📚 Lectura Primaria")
st.markdown("Bienvenido al entorno de lectura para primaria. Selecciona una aplicación para comenzar:")

st.page_link("pages/1_Busca_libros.py", label="🔍 Busca libros", icon="🔍")
st.page_link("pages/2_Analisis_pedagogico.py", label="📖 Análisis pedagógico", icon="📖")
st.page_link("pages/3_Seguimiento_lector.py", label="📚 Seguimiento lector", icon="📚")
