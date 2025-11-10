import sqlite3

def obtener_datos_alumno(db_path, nombre):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alumnos WHERE nombre = ?', (nombre,))
    datos = cursor.fetchone()
    conn.close()
    return datos
