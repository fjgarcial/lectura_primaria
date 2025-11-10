import streamlit as st

st.set_page_config(page_title="Lectura Primaria", layout="wide")
st.markdown("## 📚 Elige una de las opciones")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/1_Busca_libros.py", label="🔍 Busca libros", icon="🔍")

with col2:
    st.page_link("pages/2_Analisis_pedagogico.py", label="📖 Análisis pedagógico y Recomendaciones", icon="📖")

with col3:
    st.page_link("pages/3_Progreso_alumnos.py", label="📊 Progreso de alumnos", icon="📊")
