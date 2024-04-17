import streamlit as st
import pickle

# Load the pickled model
with open('sentiment_pipeline.pkl', 'rb') as f:
    model = pickle.load(f)

# Create a Streamlit app
def main():
    st.title('Sentiment Analysis of Covid-19 Vaccine Tweets')

    # User input for prediction
    text_input = st.text_input('Enter text for sentiment analysis:', '')

    # Make prediction
    prediction = model.predict([text_input])

    # Display prediction
    st.write('Sentiment:', prediction)

if __name__ == '__main__':
    main()
