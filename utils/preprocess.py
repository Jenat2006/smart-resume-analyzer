import re
import nltk
from nltk.corpus import stopwords

# Download stopwords (first time only)
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def preprocess_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation and special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Remove stopwords
    words = text.split()

    filtered_words = [word for word in words if word not in stop_words]

    return " ".join(filtered_words)