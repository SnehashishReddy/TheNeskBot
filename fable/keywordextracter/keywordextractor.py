from keybert import KeyBERT


def extract_keywords(doc: str) -> str:
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(
        doc, keyphrase_ngram_range=(1, 1), stop_words=None)
    return keywords


def extract_keyphrases(doc: str, length: int) -> str:
    kw_model = KeyBERT()
    keyphrases = kw_model.extract_keywords(
        doc, keyphrase_ngram_range=(1, length), stop_words=None)
    return keyphrases
