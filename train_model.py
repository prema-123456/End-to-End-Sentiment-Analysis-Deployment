# train_model.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Small example dataset
texts = [
    "I love this product",
    "This is amazing",
    "I am so happy",
    "I hate this",
    "This is terrible",
    "I am sad",
    "Not bad",
    "Could be better",
    "Excellent work",
    "Very disappointing"
]

labels = [
    "Positive",
    "Positive",
    "Positive",
    "Negative",
    "Negative",
    "Negative",
    "Neutral",
    "Neutral",
    "Positive",
    "Negative"
]

# Step 1: Fit vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Step 2: Train model
model = LogisticRegression()
model.fit(X, labels)

# Step 3: Save fitted vectorizer
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

# Step 4: Save trained model
with open("sentiment_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model and vectorizer are trained and saved!")
