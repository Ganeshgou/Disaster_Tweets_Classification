import streamlit as st
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the saved model and vectorizer
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Define a function for predicting the class of a tweet
def predict_tweet(tweet):
    # Vectorize the tweet using the saved vectorizer
    vectorized_tweet = vectorizer.transform([tweet])

    # Predict the class using the saved model
    prediction = model.predict(vectorized_tweet)

    # Return the predicted class
    return prediction[0]

# Set up the Streamlit app
st.title('Disaster Tweet Classification')

# Get user input
user_input = st.text_input('Enter a tweet')

# Make a prediction if the user has entered a tweet
if user_input:
    prediction = predict_tweet(user_input)
    if prediction == 0:
        st.write('This tweet is not about a disaster.')
    else:
        st.write('This tweet is about a disaster.')
