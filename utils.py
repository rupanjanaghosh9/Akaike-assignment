from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd


analyzer = SentimentIntensityAnalyzer()

def clean_text(text):
    """
    Clean HTML tags from the text using BeautifulSoup.
    """
    return "" if pd.isna(text) else BeautifulSoup(str(text), "html.parser").get_text()

def get_sentiment(text):
    """
    Perform sentiment analysis on the given text using VADER.
    Returns a tuple of (sentiment_label, sentiment_score).
    """
    scores = analyzer.polarity_scores(text)
    compound_score = scores["compound"]
    if compound_score > 0:
        sentiment_label = "Positive"
    elif compound_score < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"
    return sentiment_label, compound_score

def load_csv(file_path):
    """
    Load a CSV file into a pandas DataFrame.
    """
    return pd.read_csv(file_path)
