import streamlit as st
import pandas as pd

# Load CSV files
df_sentiment = pd.read_csv("Starlink_news_with_sentiment_cleaned.csv")
df_comparative = pd.read_csv("Starlink_news_comparative_sentiment.csv")

# Streamlit UI
st.title("Starlink Sentiment Analysis Dashboard ")
st.write("### News Sentiment Data")
st.dataframe(df_sentiment)

st.write("### Comparative Sentiment Data")
st.dataframe(df_comparative)

# Audio player section
st.header("News Audio Summaries ")
audio_files = [
    "audio/news_1.mp3", "audio/news_2.mp3", "audio/news_3.mp3", "audio/news_4.mp3", "audio/news_5.mp3",
    "audio/news_6.mp3", "audio/news_7.mp3", "audio/news_8.mp3", "audio/news_9.mp3", "audio/news_10.mp3",
    "audio/Summary_1.mp3", "audio/Summary_2.mp3", "audio/Summary_3.mp3", "audio/Summary_4.mp3", 
    "audio/Summary_5.mp3", "audio/Summary_6.mp3", "audio/Summary_7.mp3", "audio/Summary_8.mp3",
    "audio/Summary_9.mp3", "audio/Summary_10.mp3"
]

for audio_file in audio_files:
    try:
        st.audio(audio_file)
    except FileNotFoundError:
        st.error(f"Audio file {audio_file} not found!")
