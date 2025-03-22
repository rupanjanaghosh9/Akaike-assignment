import streamlit as st
import pandas as pd
from gtts import gTTS
from deep_translator import GoogleTranslator

# Load the cleaned CSV file
csv_path = "Starlink_news_with_sentiment_cleaned.csv"
df = pd.read_csv(csv_path)

# Load comparative sentiment scores and analysis files
comparative_scores_path = "Starlink_news_comparative_scores.csv"
comparative_sentiment_path = "Starlink_news_comparative_sentiment_analysis.csv"
comparative_scores_df = pd.read_csv(comparative_scores_path)
comparative_sentiment_df = pd.read_csv(comparative_sentiment_path)

# Function to generate Hindi speech from text
def text_to_speech(text, filename):
    if pd.isna(text) or text.strip() == "":
        st.warning("Empty text, skipping TTS.")
        return
    
    # Translate text to Hindi
    translated_text = GoogleTranslator(source="en", target="hi").translate(text)
    
    # Convert translated text to speech
    tts = gTTS(text=translated_text, lang="hi")
    tts.save(filename)  # Save the speech as an MP3 file
    st.success(f"Generated speech for: {filename}")

# Function to perform comparative sentiment analysis
def perform_comparative_analysis(company_name):
    # Filter comparative scores and sentiment analysis for the company
    comparative_scores = comparative_scores_df[
        (comparative_scores_df['Article_1'].str.contains(company_name, case=False)) |
        (comparative_scores_df['Article_2'].str.contains(company_name, case=False))
    ]
    
    comparative_sentiment = comparative_sentiment_df[
        (comparative_sentiment_df['Article_1'].str.contains(company_name, case=False)) |
        (comparative_sentiment_df['Article_2'].str.contains(company_name, case=False))
    ]
    
    if not comparative_scores.empty:
        st.subheader("Comparative Sentiment Score Analysis")
        st.write("This section compares the sentiment scores between articles related to the company.")
        st.dataframe(comparative_scores)
    
    if not comparative_sentiment.empty:
        st.subheader("Comparative Sentiment Analysis")
        st.write("This section compares the sentiment (Positive, Negative, Neutral) between articles related to the company.")
        st.dataframe(comparative_sentiment)

# Streamlit App
def main():
    st.title("News Summarization and Text-to-Speech Application")
    company_name = st.text_input("Enter the company name (e.g., Starlink):")
    
    if company_name:
        filtered_news = df[df['Title'].str.contains(company_name, case=False)]
        
        if not filtered_news.empty:
            st.write(f"Found 10 articles related to {company_name}:")
            
            for idx, row in filtered_news.iterrows():
                st.subheader(row['Title'])
                st.write(f"**Summary:** {row['Summary']}")
                st.write(f"**Title Sentiment:** {row['Title_Sentiment']}")
                st.write(f"**Summary Sentiment:** {row['Summary_Sentiment']}")
                
                # Generate TTS for the summary
                output_file = f"Summary_{idx+1}.mp3"
                text_to_speech(row['Summary'], output_file)
                
                # Play the audio file
                st.audio(output_file, format='audio/mp3')
            
            # Perform comparative sentiment analysis
            perform_comparative_analysis(company_name)
        else:
            st.warning(f"No articles found related to {company_name}.")

if __name__ == "__main__":
    main()
