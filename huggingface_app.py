import streamlit as st
import pandas as pd
import os

# Load your CSV data
df_sentiment = pd.read_csv("Starlink_news_with_sentiment_cleaned.csv")

# Add audio file paths to your DataFrame (customize based on your naming convention)
df_sentiment["News_Audio"] = [f"audio/news_{i+1}.mp3" for i in range(len(df_sentiment))]
df_sentiment["Summary_Audio"] = [f"audio/Summary_{i+1}.mp3" for i in range(len(df_sentiment))]
df_comparative = pd.read_csv("Starlink_news_comparative_sentiment.csv")


# Configure Streamlit page
st.set_page_config(layout="wide")
st.title("Starlink News Articles with Audio Summaries and sentiment comparison")

# Display articles with dual audio players
for index, row in df_sentiment.iterrows():
    with st.container():
        col_article, col_audio = st.columns([3, 2])  # Adjust column ratio
        
        # Left Column: Article Details
        with col_article:
            st.subheader(f"**{row['Title']}**")  
            st. write(row['Summary'])  # Replace with your content column name
            st.write(f"Summary_Sentiment: {row['Summary_Sentiment']} | sentiment_score: {row['Summary_Sentiment_Score']:.2f}")
            st.write(f"Title_Sentiment: {row['Title_Sentiment']}" ) 
            st.write("### comparative Sentiment Data")
            st.dataframe(df_comparative)


        # Right Column: Audio Players
        with col_audio:
            # News Audio
            st.write("**Original News Audio**")
            if os.path.exists(row["News_Audio"]):
                st.audio(row["News_Audio"])
            else:
                st.error("News audio file missing!")
            
            # Summary Audio
            st.write("**Hindi Summary Audio**")
            if os.path.exists(row["Summary_Audio"]):
                st.audio(row["Summary_Audio"])
            else:
                st.error("Summary audio file missing!")
        
        st.markdown("---")  # Divider between articles
