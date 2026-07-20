# utils/text_processing.py

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_features=50)

def process_text(notes_list):
    return vectorizer.fit_transform(notes_list).toarray()