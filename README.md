
# Lectura Primaria

Este proyecto contiene una plataforma educativa para la gestión y análisis de libros en educación primaria. Está desarrollado con **Streamlit** y se compone de tres aplicaciones principales y una página de inicio (landing page).

## 📁 Estructura del proyecto

```
lectura_primaria/
├── libros.csv                # Archivo con el catálogo de libros (no modificar)
├── landing_page.py          # Página principal de navegación
├── pages/
│   ├── 1_Busca_libros.py     # App para buscar libros por edad
│   ├── 2_Analisis_pedagogico.py # App para ver detalles pedagógicos por título
│   └── 3_Seguimiento_lector.py  # App para leer el texto de los libros
```

## 📚 Aplicaciones

### 1. Busca libros
Filtra libros por edad si la columna `edad` está disponible en `libros.csv`. Muestra una tabla con los resultados.

### 2. Análisis pedagógico
Permite seleccionar un título (si existe la columna `titulo`) y ver sus detalles pedagógicos.

### 3. Seguimiento lector
Muestra el texto del libro seleccionado si existen las columnas `titulo` y `texto`.

### 🏠 Landing Page
Página principal con enlaces a las tres aplicaciones.

## 🚀 Cómo desplegar en Streamlit Cloud

1. Sube todos los archivos al repositorio de GitHub `lectura_primaria`.
2. Asegúrate de que `libros.csv` esté en el directorio raíz.
3. Entra a [streamlit.io/cloud](https://streamlit.io/cloud) y crea una nueva app.
4. Selecciona el repositorio y configura `landing_page.py` como archivo principal.

## ⚠️ Recomendaciones
- **No modificar el archivo `libros.csv`**.
- Si alguna columna no está disponible, las apps mostrarán una advertencia en lugar de fallar.
- Mantén los nombres de los archivos tal como están.

## 🧑‍💻 Requisitos
- Python 3.8+
- Streamlit
- Pandas

## 📬 Contacto
Para dudas o mejoras, contacta a FRANCISCO.
