# 🩺 EHR NLP Cleaner

An open-source NLP pipeline for cleaning and standardising Electronic Health Record (EHR) notes. Now powered by **NLTK or SpaCy**, with an optional **Streamlit interface** to upload raw `.txt` files and get cleaned output in seconds.

---

## 🔧 Features

- ✅ Removes PHI-like placeholders (`[NAME]`, `[DATE]`, etc.)
- ✅ Lowercases and strips punctuation/digits
- ✅ Removes stopwords using NLTK or SpaCy
- ✅ Tokenises and optionally lemmatises text
- ✅ Supports file uploads and preview
- ✅ Easy switch between NLTK and SpaCy pipelines
- ✅ Web-based UI using Streamlit

---

## 📦 Tech Stack

| Component    | Tool                       |
|--------------|----------------------------|
| Preprocessing| NLTK, SpaCy                |
| Web UI       | Streamlit                  |
| Language     | Python 3.10+               |
| Model (SpaCy)| `en_core_web_sm`           |

---

## 💻 How to Use

### 🧪 Local CLI (Terminal)

```bash
# Clone the repo
git clone https://github.com/glow28/ehr-nlp-cleaner.git
cd ehr-nlp-cleaner

# Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# Run directly
python ehr_cleaner.py

