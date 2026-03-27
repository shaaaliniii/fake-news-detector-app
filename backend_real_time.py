from wsgiref import headers

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import joblib
import requests
from bs4 import BeautifulSoup
from googlesearch import search

# Load trained model & vectorizer
model_path = "fake_news_model.pkl"
vectorizer_path = "vectorizer.pkl"

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

app = FastAPI()

# ✅ Enable CORS properly
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all frontend requests
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, etc.
    allow_headers=["*"],  # Allows all headers
)

def get_news_sources(query):
    short_query = " ".join(query.split()[:8])  # shorter query works better

    try:
        search_results = list(search(short_query, num_results=3))
    except:
        return {}

    sources = {}

    for url in search_results:
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers, timeout=3)

            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all('p')

            text = " ".join([p.get_text() for p in paragraphs])
            sources[url] = text[:200]

        except:
            continue

    return sources



@app.get("/predict")
@app.get("/predict/")
async def predict_news(news_text: str):
    if not news_text:
        raise HTTPException(status_code=400, detail="News text is required")

    # Convert text to feature vector
    transformed_text = vectorizer.transform([news_text])
    prediction = model.predict(transformed_text)[0]

    # Get real-time news sources
    sources = get_news_sources(news_text)

    return {"prediction": prediction, "sources": sources}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
