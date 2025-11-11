
# ?? Lectura Primaria

Aplicaci?n Streamlit para analizar libros infantiles y generar fichas pedag?gicas, r?bricas de evaluaci?n y recomendaciones. La b?squeda de libros es insensible a may?sculas y acentos.

---

## ?? B?squeda flexible
La aplicaci?n permite buscar t?tulos de libros sin importar si el usuario escribe:
- "camino"
- "CAMINO"
- "Camin?"
- "El Camino"

Todos estos ejemplos encontrar?n el libro "El Camino".

---

## ??? Instalaci?n local

1. Clona el repositorio:
```bash
git clone https://github.com/fjgarcial/lectura_primaria.git
cd lectura_primaria
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

---

## ?? Ejecuci?n local
```bash
streamlit run app.py
```

---

## ??? Despliegue en Streamlit Cloud

1. Aseg?rate de que el archivo `requirements.txt` incluya:
```
streamlit
pandas
python-docx
```

2. Sube los archivos `app.py`, `libros_titulo.csv`, `requirements.txt` y `README.md` al repositorio.
3. Accede a [https://streamlit.io/cloud](https://streamlit.io/cloud) y conecta tu cuenta de GitHub.
4. Selecciona el repositorio `lectura_primaria` y despliega la app.

---

## ?? Estructura del proyecto
```
lectura_primaria/
??????€ app.py
????€ libros_titulo.csv
????€ requirements.txt
????€ README.md
```

---

## ????Soluci?n a errores comunes

### ??ModuleNotFoundError: No module named 'docx'
**Soluci?n:** Aseg?rate de que `requirements.txt` incluya:
```
python-docx
```
Haz commit y push, luego reinicia el deploy en Streamlit Cloud.

---

## ?? Licencia
Este proyecto est? bajo licencia MIT.
