from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load the CSV files
sentiment_cleaned_path = r"C:\Users\rupanjana ghosh\Downloads\pythonproject\assignmentrupanjana\Starlink_news_with_sentiment_cleaned.csv"
comparative_sentiment_path = r"C:\Users\rupanjana ghosh\Downloads\pythonproject\assignmentrupanjana\Starlink_news_comparative_sentiment.csv"

df_sentiment_cleaned = pd.read_csv(sentiment_cleaned_path)
df_comparative_sentiment = pd.read_csv(comparative_sentiment_path)

@app.route('/sentiment_cleaned', methods=['GET'])
def get_sentiment_cleaned():
    """
    API endpoint to return the sentiment analysis data from the cleaned CSV.
    """
    # Convert DataFrame to JSON
    data = df_sentiment_cleaned.to_dict(orient='records')
    return jsonify(data)

@app.route('/comparative_sentiment', methods=['GET'])
def get_comparative_sentiment():
    """
    API endpoint to return the comparative sentiment analysis data.
    """
    # Convert DataFrame to JSON
    data = df_comparative_sentiment.to_dict(orient='records')
    return jsonify(data)

@app.route('/')
def home():
    return "Welcome to the Starlink Sentiment Analysis API! Use /sentiment_cleaned or /comparative_sentiment to access the data."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
