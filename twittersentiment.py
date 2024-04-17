import streamlit as st
import re
import emoji
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
import joblib

stop_words = set(stopwords.words('english'))

# Initialize WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# Define custom functions
def cleaner(input_data):
    cleaned_data = []
    for data in input_data:
        if isinstance(data, str):  # If input is a string
            cleaned_tweet = clean_tweet(data)
            cleaned_data.append(cleaned_tweet)
        elif isinstance(data, list):  # If input is a list of tokens
            cleaned_tokens = clean_tokens(data)
            cleaned_tweet = ' '.join(cleaned_tokens)
            cleaned_data.append(cleaned_tweet)
        else:
            cleaned_data.append('')  # Append empty string for other types of input
    return cleaned_data

def clean_tweet(tweet):
    # Clean the tweet
    tweet = re.sub(r'\d+', '', tweet)  # Remove numbers
    tweet = re.sub(r'[^\w\s]', '', tweet)  # Remove punctuation and special characters
    tweet = tweet.lower()  # Convert to lowercase
    tweet = re.sub("@[A-Za-z0-9]+", "", tweet)  # Remove @ sign
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet)  # Remove URLs
    tweet = emoji.demojize(tweet)  # Remove emojis
    tweet = tweet.replace("#", "").replace("_", " ")  # Remove hashtag symbol and underscores
    tweet = " ".join(tweet.split())  # Remove extra whitespaces
    return tweet

def clean_tokens(tokens):
    cleaned_tokens = []
    for token in tokens:
        if isinstance(token, str):  # Check if token is a string
            cleaned_token = clean_token(token)
            cleaned_tokens.append(cleaned_token)
    return cleaned_tokens

def clean_token(token):
    # Clean the token
    token = re.sub(r'\d+', '', token)  # Remove numbers
    token = re.sub(r'[^\w\s]', '', token)  # Remove punctuation and special characters
    token = token.lower()  # Convert to lowercase
    token = emoji.demojize(token)  # Remove emojis
    return token

def tokenize_tweets(tweets):
    tokenized_tweets = [word_tokenize(tweet) for tweet in tweets]
    return tokenized_tweets

def remove_stopwords(tokens):
    return [[word for word in tweet_tokens if word not in stop_words] for tweet_tokens in tokens]

def lemmatize_tokens(tokens):
    return [[lemmatizer.lemmatize(token) for token in tweet_tokens] for tweet_tokens in tokens]

def join_tokens_into_string(token_lists):
    return [' '.join(tokens) for tokens in token_lists]

# Load the pickled model
model = joblib.load('sentiment_model.pkl')

# Load the pickled TfidfVectorizer
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Set page configuration
st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Create a Streamlit app
def main():
    # Display header image
    st.image("https://iliyaz.hashnode.dev/twitter-sentiment-analysis", use_column_width=True)

    # Set title and description
    st.title('Sentiment Analysis of Covid-19 Vaccine Tweets')
    st.markdown("*Welcome to our sentiment analysis app! Enter some text below to analyze the sentiment.*")

    # User input for prediction
    text_input = st.text_area('Enter text for sentiment analysis:', '', height=150)

    # Apply TF-IDF vectorization
    tfidf_vectorizer = TfidfVectorizer()

    # Combine preprocessing steps into a pipeline
    pipeline = Pipeline([
        ('cleaner', FunctionTransformer(cleaner)),
        ('tokenizer', FunctionTransformer(tokenize_tweets)),
        ('stopword_remover', FunctionTransformer(remove_stopwords)),
        ('lemmatizer', FunctionTransformer(lemmatize_tokens)),
        ('join_tokens', FunctionTransformer(join_tokens_into_string)),
        ('tfidf_vectorizer', tfidf_vectorizer),
        ('model', model)
    ])

    # Make prediction
    if st.button("Analyze Sentiment"):
        with st.spinner("Analyzing..."):
            prediction = pipeline.predict([text_input])

        # Display prediction
        st.write('Sentiment:', prediction)

if __name__ == '__main__':
    main()