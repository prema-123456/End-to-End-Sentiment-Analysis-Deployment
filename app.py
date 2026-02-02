import streamlit as st
import pickle

# Load the vectorizer and model
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("sentiment_model.pkl", "rb") as f:
    model = pickle.load(f)

# Title
st.title("Sentiment Analysis App")

# User input
user_input = st.text_area("Enter your text here:")

# Button to predict
if st.button("Predict Sentiment"):
    if user_input:
        # Transform text and predict
        transformed_input = vectorizer.transform([user_input])
        prediction = model.predict(transformed_input)[0]

        # Show result
        st.write(f"Predicted Sentiment: **{prediction}**")
    else:
        st.write("Please enter some text!")
