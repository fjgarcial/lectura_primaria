
from transformers import pipeline

def generar_texto_con_ia(titulo):
    generator = pipeline("text-generation", model="tiiuae/falcon-7b-instruct")
    prompt = f"Genera un resumen breve y educativo del libro infantil titulado '{titulo}'."
    resultado = generator(prompt, max_length=300, do_sample=True)
    return resultado[0]['generated_text']
