import unicodedata

# Función para normalizar texto (eliminar acentos y convertir a minúsculas)
def normalizar_texto(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFKD', texto)
    texto = ''.join([c for c in texto if not unicodedata.combining(c)])
    return texto

# Normalizar lista de libros disponibles
libros_normalizados = [normalizar_texto(l) for l in libros_disponibles]

# Normalizar el título introducido por el usuario
titulo_libro_normalizado = normalizar_texto(titulo_libro)

if buscar and titulo_libro:
    if titulo_libro_normalizado not in libros_normalizados:
        st.warning("El libro no se encuentra en la base de datos.")
    else:
        # Recuperar el título original para mostrarlo en análisis y descargas
        indice = libros_normalizados.index(titulo_libro_normalizado)
        titulo_original = libros_disponibles[indice]

        with st.spinner("Analizando el libro..."):
            analisis = analizar_libro(titulo_original)

            st.subheader("🔎 Análisis pedagógico")
            st.write(f"**Número de palabras:** {analisis['palabras']}")
            st.write(f"**Estructuras gramaticales:** {', '.join(analisis['estructuras'])}")
            st.write(f"**Complejidad del texto:** {analisis['complejidad']}")
            st.write(f"**Vocabulario:** {analisis['vocabulario']}")
            st.write(f"**Tiempos verbales predominantes:** {analisis['tiempos']}")
            st.write(f"**Nivel de dificultad:** {analisis['nivel_dificultad']}")

            st.subheader("📄 Ficha de comprensión lectora")
            ficha_path = generar_ficha(titulo_original, analisis)
            with open(ficha_path, "rb") as f:
                st.download_button("📥 Descargar ficha", f, file_name=ficha_path)

            st.subheader("📊 Rúbrica de evaluación")
            rubrica_path = generar_rubrica(titulo_original)
            with open(rubrica_path, "rb") as f:
                st.download_button("📥 Descargar rúbrica", f, file_name=rubrica_path)

            st.subheader("📚 Recomendaciones pedagógicas")
            recomendaciones = recomendar_libros(titulo_original, libros_disponibles)
            for rec in recomendaciones:
                st.markdown(f"**Título:** {rec['título']}")
                st.markdown(f"✅ Pros: {', '.join(rec['pros'])}")
                st.markdown(f"⚠️ Contras: {', '.join(rec['contras'])}")
                st.markdown("---")