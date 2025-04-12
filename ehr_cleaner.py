# ehr_cleaner.py
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download resources if not already present
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_ehr_text(text):
    # Lowercase the text
    text = text.lower()

    # Remove PHI-like placeholders like [NAME], [DATE]
    text = re.sub(r"\[.*?\]", "", text)

    # Remove numbers and punctuation
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Tokenise
    tokens = word_tokenize(text)

    # Remove stopwords
    filtered = [w for w in tokens if w not in stop_words]

    # Join and strip
    cleaned = " ".join(filtered).strip()
    return cleaned

# Optional CLI test block
if __name__ == "__main__":
    sample_text = "[NAME] presented to A&E with c/o chest pain. Hx of HTN, DM. Denies SOB or dizziness."
    print("Original Text:")
    print(sample_text)
    print("\nCleaned Text:")
    cleaned_output = clean_ehr_text(sample_text)
    print(cleaned_output)

    # Optional: Save to file
    with open("cleaned_sample.txt", "w") as f:
        f.write(cleaned_output)

