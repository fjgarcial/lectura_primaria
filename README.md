
# Lectura Primaria 📚

Aplicación Streamlit para buscar libros de lectura primaria desde un archivo CSV. La búsqueda es insensible a mayúsculas y acentos, lo que permite una experiencia más amigable para el usuario.

## 🔍 Funcionalidad de búsqueda

La búsqueda se realiza normalizando tanto el texto ingresado por el usuario como los títulos del archivo CSV. Esto permite encontrar coincidencias sin importar si el usuario escribe:

- "camino"
- "CAMINO"
- "Caminó"
- "El Camino"

Todos estos ejemplos encontrarán el libro "El Camino".

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

## 🚀 Ejecución local

```bash
streamlit run app.py
```

## ☁️ Despliegue en Streamlit Cloud

1. Sube los archivos `app.py`, `libros_titulo.csv`, `requirements.txt` y `README.md` al repositorio.
2. Accede a [https://streamlit.io/cloud](https://streamlit.io/cloud) y conecta tu cuenta de GitHub.
3. Selecciona el repositorio `lectura_primaria` y despliega la app.

## 📁 Estructura del proyecto

```
lectura_primaria/
│
├── app.py
├── libros_titulo.csv
├── requirements.txt
└── README.md
```
