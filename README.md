# Sentiment Analysis App

**Predict text sentiment (Positive / Negative / Neutral) instantly using a Streamlit web app.**

---

## 🔹 Project Overview
A machine-learning-powered web application that predicts the sentiment of any English text in real time.  
- Built with **Python**, **scikit-learn**, and **Streamlit**.  
- Uses `TfidfVectorizer` + `LogisticRegression` for efficient sentiment classification.  
- Interactive text input with instant results.  
- Fully **deployed online** for free on Streamlit Community Cloud.

---

## 🔹 Live App
🌐 **Try the live application here:**  
👉 https://end-to-end-sentiment-analysis-deployment-ecjwplytppuz4mbcp5av3.streamlit.app/

---

## 🔹 Key Features
✔ Real-time sentiment prediction  
✔ Classifies text into **Positive / Negative / Neutral**  
✔ Simple and intuitive UI  
✔ Hosted online — no installation required  

---

## 🔹 Technology Stack
- **Python 3**  
- **Streamlit** for UI  
- **scikit‑learn** for ML modeling  
- **Pickle** for model serialization  

---

## 🔹 Project Structure
Sentiment-Analysis-App/
├── app.py # Streamlit app
├── train_model.py # Model training & saving
├── vectorizer.pkl # Fitted TF-IDF vectorizer
├── sentiment_model.pkl # Trained ML model
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## 🔹 Sample Predictions
| Input Text                     | Predicted Sentiment |
|--------------------------------|--------------------|
| "I love this product!"         | Positive           |
| "This is the worst service ever." | Negative        |
| "Not bad, could be better."    | Neutral            |

---

## 🔹 How to Run Locally

1️⃣ **Clone the repository**
```bash
git clone https://github.com/prema-123456/Sentiment-Analysis-App.git
cd Sentiment-Analysis-App

2️⃣ Install dependencies

pip install -r requirements.txt


3️⃣ Run the Streamlit app

streamlit run app.py


📌 Then open your browser to interact with the app locally.

🔹 Key Learnings

Preprocessing text using TF‑IDF vectorization

Training, saving, and loading ML models with scikit‑learn + pickle

Building interactive web apps using Streamlit

Deploying a machine learning app online (free)

🔹 Future Improvements

✔ Add support for longer paragraphs

✔ Integrate advanced transformer models (e.g., BERT)

✔ Add multi‑language sentiment options

✔ Enhance UI with icons and sentiment colors
