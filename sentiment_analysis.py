import pandas as pd
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load CSV (First 10 articles)
csv_path = r"C:\Users\rupanjana ghosh\Downloads\pythonproject\assignmentrupanjana\Starlink_news.csv"
df = pd.read_csv(csv_path).head(10)

# Function to clean HTML tags
def clean_text(text):
    return "" if pd.isna(text) else BeautifulSoup(str(text), "html.parser").get_text()

# Clean Title & Summary
df["Title"] = df["Title"].apply(clean_text)
df["Summary"] = df["Summary"].apply(clean_text) if "Summary" in df.columns else ""

# Sentiment Analysis
analyzer = SentimentIntensityAnalyzer()

# Function to get sentiment label and score
def get_sentiment(text):
    scores = analyzer.polarity_scores(text)
    compound_score = scores["compound"]
    if compound_score > 0:
        sentiment_label = "Positive"
    elif compound_score < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"
    return sentiment_label, compound_score

# Apply sentiment analysis to Title and Summary
df["Title_Sentiment"], df["Title_Sentiment_Score"] = zip(*df["Title"].apply(get_sentiment))
df["Summary_Sentiment"], df["Summary_Sentiment_Score"] = zip(*df["Summary"].apply(get_sentiment))

# Save Output
output_csv = r"C:\Users\rupanjana ghosh\Downloads\pythonproject\assignmentrupanjana\Starlink_news_with_sentiment_cleaned.csv"
df.to_csv(output_csv, index=False)

print(f"Sentiment analysis completed! Saved to: {output_csv}")

print("Available columns in CSV:", df.columns.tolist())
