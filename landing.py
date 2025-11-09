import streamlit as st

st.set_page_config(page_title="Lectura Infantil", layout="wide")
st.title("Elige una de las opciones")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Busca libros"):
        st.switch_page("apps/busca_libros.py")

with col2:
    if st.button("Busca libro"):
        st.switch_page("apps/busca_libro.py")

with col3:
    if st.button("Progreso alumnos"):
        st.switch_page("apps/progreso_alumnos.py")