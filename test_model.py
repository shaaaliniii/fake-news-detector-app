import joblib

# load model
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# SAME CLEANING FUNCTION
import re, string
def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(f"[{string.punctuation}]", "", text)
    text = re.sub(r'\w*\d\w*', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# TEST
real = "India won the Cricket World Cup in 2011"
fake = "Aliens landed in Delhi yesterday"

print("REAL:", model.predict(vectorizer.transform([clean_text(real)])))
print("FAKE:", model.predict(vectorizer.transform([clean_text(fake)])))