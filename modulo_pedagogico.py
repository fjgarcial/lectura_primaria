
def generar_recomendaciones(analisis):
    recomendaciones = []
    if analisis["legibilidad"] < 50:
        recomendaciones.append("Texto complejo: añade actividades de vocabulario.")
    if analisis["longitud_media"] > 20:
        recomendaciones.append("Oraciones largas: trabaja comprensión sintáctica.")
    if analisis["tokens"] > 1000:
        recomendaciones.append("Texto extenso: divide la lectura en secciones.")
    return recomendaciones
