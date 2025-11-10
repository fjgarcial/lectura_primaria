
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title='Lectura Primaria', layout='wide')
st.markdown('## 📚 Elige una de las opciones')

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('🔍 Busca libros'):
        switch_page('1_busqueda_libros')

with col2:
    if st.button('📖 Análisis pedagógico y Recomendaciones'):
        switch_page('2_analisis_pedagogico')

with col3:
    if st.button('📊 Progreso de alumnos'):
        switch_page('3_progreso_alumnos')
