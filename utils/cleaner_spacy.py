# cleaner_spacy.py

import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# Load English NLP pipeline
nlp = spacy.load("en_core_web_sm")

def clean_ehr_with_spacy(text):
    text = text.lower()
    doc = nlp(text)

    tokens = [
        token.lemma_ for token in doc
        if token.is_alpha and not token.is_stop
    ]

    return " ".join(tokens)

if __name__ == "__main__":
    raw = "[NAME] presented to A&E with chest pain, hx of HTN, denies SOB."
    print(clean_ehr_with_spacy(raw))
