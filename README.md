
# 📚 Lectura Primaria - Nueva Arquitectura con IA

Aplicación Streamlit para análisis lingüístico y pedagógico avanzado de libros infantiles. Ahora incluye:
- **Generación de texto con IA (HuggingFace)** a partir del título.
- **Análisis morfosintáctico** con spaCy.
- **Métricas de legibilidad** con textstat.
- **Recomendaciones pedagógicas dinámicas**.

---

## 🔍 ¿Cómo funciona?
1. El usuario introduce el título del libro.
2. La IA genera un resumen educativo del libro.
3. Se analiza el texto generado:
   - Número de tokens y oraciones.
   - Longitud media de oración.
   - Índice de legibilidad (Flesch).
   - Distribución de categorías gramaticales.
4. Se generan recomendaciones pedagógicas basadas en el análisis.

---

## ⚙️ Instalación local

1. Clona el repositorio:
```bash
git clone https://github.com/fjgarcial/lectura_primaria.git
cd lectura_primaria
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Descarga el modelo spaCy para español:
```bash
python -m spacy download es_core_news_md
```

---

## 🚀 Ejecución local
```bash
streamlit run app.py
```

---

## ☁️ Despliegue en Streamlit Cloud

1. Asegúrate de que `requirements.txt` incluya:
```
streamlit
pandas
python-docx
spacy
textstat
transformers
torch
```

2. Sube los archivos:
- `app.py`
- `módulo_ia.py`
- `módulo_analisis.py`
- `módulo_pedagogico.py`
- `requirements.txt`

3. Conecta tu cuenta en [Streamlit Cloud](https://streamlit.io/cloud) y despliega la app.

---

## 📂 Estructura del proyecto
```
lectura_primaria/
│
├── app.py
├── libros_titulo.csv
├── módulo_ia.py
├── módulo_analisis.py
├── módulo_pedagogico.py
└── requirements.txt
```

---

## 🛠️ Solución a errores comunes

### ❌ ModuleNotFoundError: No module named 'docx'
**Solución:** Añade `python-docx` en `requirements.txt`.

### ❌ Error al cargar modelo spaCy
**Solución:** Ejecuta:
```bash
python -m spacy download es_core_news_md
```

### ❌ Error instalando dependencias en Streamlit Cloud
**Solución:** Verifica que `requirements.txt` esté bien formateado y sin espacios extra.

---

## 📊 Próximas mejoras
- Integración con IA para generar actividades pedagógicas.
- Visualización avanzada de análisis sintáctico.
