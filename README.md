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

Follow these steps to run the project locally on your system:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/shaaaliniii/fake-news-detector-app.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd fake-news-detector-app
```

### 3️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 4️⃣ Activate the Virtual Environment

* **Windows:**

```bash
venv\Scripts\activate
```

* **Mac/Linux:**

```bash
source venv/bin/activate
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 6️⃣ Run the Application

```bash
python app.py
```

### 7️⃣ Open in Browser

Go to:

```
http://127.0.0.1:5000
```

---

💡 **Tip:**
Make sure all required files (model `.pkl`, vectorizer, etc.) are present before running the app.




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





