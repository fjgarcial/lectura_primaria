import streamlit as st
from modulo_ia import generar_texto_con_ia
from modulo_analisis import analizar_texto
from modulo_pedagogico import generar_recomendaciones
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Análisis lingüístico y pedagógico con IA", layout="wide")
st.title("📚 Análisis lingüístico y pedagógico con IA")

# Entrada del usuario
titulo_libro = st.text_input("Introduce el título del libro infantil")
buscar = st.button("🔍 Generar y analizar")

# Flujo principal
if buscar and titulo_libro:
    # Generar texto con IA
    with st.spinner("Generando texto con IA..."):
        texto_generado = generar_texto_con_ia(titulo_libro)

    st.subheader("📄 Resumen generado por IA")
    st.write(texto_generado)

    # Analizar texto
    with st.spinner("Analizando texto..."):
        analisis = analizar_texto(texto_generado)

    # Mostrar métricas lingüísticas
    st.subheader("🔍 Análisis lingüístico")
    st.write(f"**Número de tokens:** {analisis['tokens']}")
    st.write(f"**Número de oraciones:** {analisis['oraciones']}")
    st.write(f"**Longitud media de oración:** {analisis['longitud_media']:.2f}")
    st.write(f"**Índice de legibilidad (Flesch):** {analisis['legibilidad']:.2f}")

    # Visualización de categorías gramaticales
    st.subheader("📊 Distribución de categorías gramaticales")
    pos_data = analisis['pos_counts']
    fig = px.bar(
        x=list(pos_data.keys()),
        y=list(pos_data.values()),
        labels={'x': 'Categoría gramatical', 'y': 'Frecuencia'},
        title="Frecuencia de categorías gramaticales"
    )
    st.plotly_chart(fig)

    # Recomendaciones pedagógicas
    st.subheader("📚 Recomendaciones pedagógicas")
    recomendaciones = generar_recomendaciones(analisis)
    for rec in recomendaciones:
        st.markdown(f"✅ {rec}")