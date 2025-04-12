# app.py
import streamlit as st
import spacy

# Ensure SpaCy model is downloaded (for Streamlit Cloud)
spacy.cli.download("en_core_web_sm")

# Import cleaning functions
from utils.cleaner_spacy import clean_ehr_with_spacy
from ehr_cleaner import clean_ehr_text

# Page config
st.set_page_config(page_title="EHR NLP Cleaner", layout="wide")
st.title("🩺 Clean My EHR Notes")

st.markdown("Upload an EHR `.txt` file, choose an NLP engine (NLTK or SpaCy), and get a cleaned version of the notes.")

# Engine selection
method = st.radio("Choose NLP engine:", ["NLTK", "SpaCy"])

# File upload
uploaded_file = st.file_uploader("Upload a .txt file with EHR notes", type="txt")

if uploaded_file:
    raw_text = uploaded_file.read().decode("utf-8")

    st.subheader("📄 Original Text")
    st.text_area("Input", value=raw_text, height=200)

    if st.button("Clean Notes"):
        with st.spinner("🧹 Cleaning EHR notes..."):
            if method == "NLTK":
                cleaned = clean_ehr_text(raw_text)
            else:
                cleaned = clean_ehr_with_spacy(raw_text)

        st.subheader("✅ Cleaned Output")
        st.success(cleaned)

        # 🧾 Download cleaned output
        st.download_button(
            label="📥 Download Cleaned Notes",
            data=cleaned,
            file_name="cleaned_output.txt",
            mime="text/plain"
        )

