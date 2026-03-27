# 📰 FakeOut - Fake News Detection System

## 👩‍💻 Author

**Shalini Singh**
GitHub: https://github.com/shaaaliniii

---

## 📌 Overview

FakeOut is an AI-powered web application that detects whether a news article is **real or fake** using machine learning techniques. It also provides **news summarization** to help users quickly understand long articles.

This project aims to combat misinformation and promote access to reliable information.

---

## 🚀 Features

* 🔍 Fake News Detection using Machine Learning
* ✂️ News Summarization
* ⚡ Real-time analysis of user input
* 🎨 Clean and responsive UI (Tailwind CSS)
* 🌐 Flask-based web application

---

## 🛠️ Technologies Used

### Frontend

* HTML
* CSS (Tailwind CSS)
* JavaScript

### Backend

* Python (Flask)

### Machine Learning

* TF-IDF Vectorizer
* Logistic Regression
* NLTK (Natural Language Processing)

---

## 📂 Project Structure

```text
Fake_News_Detector/
│
├── templates/        # HTML files
├── static/           # CSS & JS
├── app.py            # Flask backend
├── test_model.py
├── fake_news_model.pkl
├── vectorizer.pkl
└── README.md
```

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/shaaaliniii/fake-news-detector-app.git

# Navigate to project
cd fake-news-detector-app

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

---

## 🌐 Usage

1. Enter a news article
2. Click **Check News**
3. Get result: **Real / Fake**

For summarization:

* Enter article → get key points instantly

---

## 📊 Dataset

The dataset is not included due to size constraints.
You can use publicly available datasets like:

* Kaggle Fake News Dataset

---

## ⚠️ Note

* Large files (dataset) are excluded for better performance
* Model accuracy depends on training data

---





