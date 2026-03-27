import joblib
import re
import string
import logging

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

import nltk
from nltk.tokenize import sent_tokenize

# =========================
# 📥 DOWNLOAD NLTK DATA
# =========================
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# =========================
# 📝 LOGGING SETUP
# =========================
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# =========================
# 🚀 FLASK APP SETUP
# =========================
app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

# =========================
# 📦 LOAD MODEL & VECTORIZER
# =========================
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# =========================
# 🧹 TEXT CLEANING FUNCTION
# =========================
def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(f"[{string.punctuation}]", "", text)
    text = re.sub(r'\w*\d\w*', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# =========================
# 📄 FRONTEND ROUTES
# =========================
@app.route('/')
def home():
    return render_template("Frontend.html")

@app.route('/fake-news')
def fake_news():
    return render_template("Fake News Detector.html")

@app.route('/summary-page')
def summary_page():
    return render_template("Summary.html")

@app.route('/news')
def news():
    return render_template("News Communicator.html")

# =========================
# 🧠 SUMMARIZATION ROUTE
# =========================
@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        text = data.get("text", "").strip()

        if not text:
            return jsonify({"error": "No text provided"}), 400

        sentences = sent_tokenize(text)

        if not sentences:
            return jsonify({"summary": "Unable to summarize text."})

        if len(sentences) <= 2:
            summary = text
        else:
            summary = sentences[0] + " " + sentences[len(sentences)//2]

        return jsonify({"summary": summary})

    except Exception as e:
        logging.error(f"Summarization error: {e}")
        return jsonify({"error": "Summarization failed"}), 500

# =========================
# 📰 FAKE NEWS PREDICTION
# =========================
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        text = data.get("text", "").strip()

        if not text:
            return jsonify({"error": "No text provided"}), 400

        cleaned_text = clean_text(text)
        text_vector = vectorizer.transform([cleaned_text])
        prediction = model.predict(text_vector)[0]

        return jsonify({"prediction": str(prediction)})

    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return jsonify({"error": "Prediction failed"}), 500

# =========================
# 🤖 SMART CHATBOT ROUTE
# =========================
@app.route('/check', methods=['POST'])
def check_news():
    try:
        data = request.get_json()
        user_input = data.get("text", "").strip()

        if not user_input:
            return jsonify({"reply": "Please type something 😊"})

        text = user_input.lower()

        # =========================
        # 💬 CONVERSATION HANDLING
        # =========================
        if text in ["hi", "hello", "hey"]:
            return jsonify({
                "reply": "Hey there! 👋\n\nI can check whether news is real or fake.\nJust send me a news article 📰"
            })

        if "how are you" in text:
            return jsonify({
                "reply": "I'm running smoothly 😄 Ready to detect fake news!"
            })

        if "what can you do" in text:
            return jsonify({
                "reply": "I can:\n📰 Detect fake news\n📊 Analyze text\n🧠 Help verify information\n\nTry sending me a news article!"
            })

        if "who are you" in text:
            return jsonify({
                "reply": "I'm your News Assistant 🤖 powered by AI.\nI help you verify news authenticity."
            })

        # =========================
        # ⚠️ INPUT VALIDATION
        # =========================
        if len(user_input.split()) < 5:
            return jsonify({
                "reply": "⚠️ Please send a proper news sentence or paragraph."
            })

        # =========================
        # 🧠 FAKE NEWS DETECTION
        # =========================
        cleaned_text = clean_text(user_input)
        text_vector = vectorizer.transform([cleaned_text])
        prediction = model.predict(text_vector)[0]

        label = "🟢 Real News" if str(prediction) == "True" else "🔴 Fake News"

        # Optional confidence
        try:
            prob = model.predict_proba(text_vector)[0]
            confidence = max(prob)
            confidence_text = f"\nConfidence: {confidence:.2f}"
        except:
            confidence_text = ""

        # Dummy sources
        sources = [
            "https://news.google.com",
            "https://bbc.com"
        ]

        reply = f"{label}{confidence_text}\n\n🔎 Verify from:\n" + "\n".join(sources)

        logging.info(f"[CHATBOT] Input: {user_input}")
        logging.info(f"[CHATBOT] Prediction: {prediction}")

        return jsonify({"reply": reply})

    except Exception as e:
        logging.error(f"Chatbot error: {e}")
        return jsonify({"reply": "❌ Something went wrong. Please try again."})

# =========================
# ▶️ RUN SERVER
# =========================
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)