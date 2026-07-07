import re
import string
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")


def preprocess_text(text):
    """
    Clean and preprocess resume text
    """

    # Convert to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Remove email addresses
    text = re.sub(r"\S+@\S+", " ", text)

    # Remove phone numbers
    text = re.sub(r"\+?\d[\d\s\-]{8,}\d", " ", text)

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    # NLP Processing
    doc = nlp(text)

    cleaned_words = []

    for token in doc:

        if token.is_stop:
            continue

        if token.is_punct:
            continue

        if token.like_num:
            continue

        lemma = token.lemma_.strip()

        if len(lemma) > 1:
            cleaned_words.append(lemma)

    return " ".join(cleaned_words)