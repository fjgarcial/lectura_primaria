
import spacy
import textstat

nlp = spacy.load("es_core_news_md")

def analizar_texto(texto):
    doc = nlp(texto)
    num_tokens = len(doc)
    num_sentences = len(list(doc.sents))
    avg_sentence_length = num_tokens / num_sentences if num_sentences > 0 else 0
    legibilidad = textstat.flesch_reading_ease(texto)
    pos_counts = {}
    for token in doc:
        pos_counts[token.pos_] = pos_counts.get(token.pos_, 0) + 1
    return {
        "tokens": num_tokens,
        "oraciones": num_sentences,
        "longitud_media": avg_sentence_length,
        "legibilidad": legibilidad,
        "pos_counts": pos_counts
    }
