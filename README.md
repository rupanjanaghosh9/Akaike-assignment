# Akaike-assignment
A web application that analyzes sentiment in Starlink news articles, generates Hindi audio analysis, and provides comparative sentiment insights.
##  Features

- **Sentiment Analysis**: VADER-based sentiment scoring for news titles and summaries
- **Audio Summaries**: Hindi TTS conversion of English articles
- **Comparative Analysis**: Title vs. summary sentiment comparison
- **Interactive Querying**: Filter articles by company name or sentiment
- **Data Export**: Download analysis results as CSV

# **Project Documentation**

## **1. Project Setup**
### **Installation Steps:**
1. **Clone the Repository:**
   ```sh
   git clone <repository-url>
   cd <project-directory>
   ```
2. **Create a Virtual Environment:**
   ```sh
   python -m venv env
   ```
3. **Activate the Virtual Environment:**
   - **Windows:**
     ```sh
     env\Scripts\activate
     ```
4. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
5. **Run the Flask API:**
   ```sh
   python api.py
   ```
6. **Run the Streamlit Application:**
   ```sh
   streamlit run main.py
   ``


---

## **2. Model Details**
### **Summarization Model:**
- Uses **BeautifulSoup** to extract and clean article summaries.
- Prepares structured summaries for sentiment analysis.

### **Sentiment Analysis Model:**
- **VADER (Valence Aware Dictionary and sEntiment Reasoner)** is used for sentiment classification.
- Analyzes sentiment for both article **Titles** and **Summaries**.
- Generates scores that categorize sentiment as **Positive, Negative, or Neutral**.

### **Text-to-Speech (TTS) Model:**
- Uses **gTTS (Google Text-to-Speech)** for Hindi speech conversion.
- Converts summarized text and sentiment details into Hindi audio files.

---

## **3. API Development**
### **Overview of APIs:**
The project provides API endpoints for accessing processed news, sentiment scores, and comparative analysis.

### **Endpoints:**
| Endpoint                     | Method | Description |
|-----------------------------|--------|-------------|
| `/`                          | GET    | API Home Page |
| `/sentiment_cleaned`         | GET    | Returns sentiment analysis results along with news ,title , summary |
| `/comparative_sentiment`     | GET    | Returns comparative sentiment analysis results |
| `/comparative_scores`        | GET    | Returns comparative sentiment score analysis |

### **Running the API:**
To start the API, run:
```sh
python api.py
```

---

## **4. API Usage**
### **Testing with Postman:**
1. **Open Postman** and click **"New Request"**.
2. **Enter URL:**
   - `http://127.0.0.1:5000/` (For Home Page)
   - `http://127.0.0.1:5000/sentiment_cleaned`
   - `http://127.0.0.1:5000/comparative_sentiment`
   - `http://127.0.0.1:5000/comparative_scores`
3. **Select GET Method** and Click **"Send"**.
4. View JSON response containing news sentiment and analysis.

---

## **5. Third-Party API Usage**
### **APIs Used:**
| API                        | Purpose |
|---------------------------|----------|
| **Google News RSS**        | Fetches latest news articles |
| **Google Translator API**  | Converts text from English to Hindi |
| **gTTS (Google TTS API)**  | Converts Hindi text into speech |

### **Integration Details:**
- **Google News RSS:** Used for extracting latest news articles dynamically.
- **Google Translator API:** Integrated into the text-to-speech function to ensure Hindi output.
- **gTTS API:** Used for generating Hindi speech files.

###*Deployment on hugging face:**
Step-by-Step Deployment
1.Create a New Space:
-Go to Hugging Face Spaces
-Click Create new Space

Configure:
Name: rupanjana_assignment
SDK: Select Streamlit
Hardware: Free CPU (upgrade if needed)
Visibility: Public/Private

Upload Files:
Method: Web Interface

Go to your Space → "Files and versions" → "Add file"

-app.py
-main.py
-requirements.txt
- CSV files: Starlink_news_comparative_scores.csv,Starlink_news_comparative_sentiment.csv,Starlink_news_comparative_sentiment_analysis.csv,
  Starlink_news_with_sentiment_cleaned.csv
-Entire audio/ folder (drag and drop)

Launch Your App:
Hugging Face will automatically build and deploy your app.
Monitor progress in the Logs tab.

USAGE GUIDE-
Enter a company name via text input to fetch relevant news articles.



---
**Assumptions:
News Source Reliability:

The project assumes that the news articles fetched from Google News RSS are reliable and up-to-date.

It assumes that the articles are in English and can be processed for summarization and sentiment analysis.

Language Translation:

The project assumes that the Google Translator API will accurately translate English text to Hindi without significant loss of meaning.

Sentiment Analysis:

The VADER sentiment analysis model assumes that the text provided is suitable for sentiment classification and that the model's pre-trained lexicon is sufficient for accurate analysis.

Text-to-Speech:

The project assumes that the gTTS API will generate clear and understandable Hindi audio files from the translated text.

User Input:

The project assumes that users will interact with the system as intended, providing valid inputs and using the API endpoints correctly.

**Limitations:
News Source Dependency:

The project is dependent on the availability and structure of the Google News RSS feed. Any changes to the RSS feed structure may break the summarization functionality.

Language Translation Accuracy:

The translation from English to Hindi may not always be perfect, especially for complex sentences or domain-specific terminology.

Sentiment Analysis Accuracy:

The VADER model may not perform well on highly nuanced or context-dependent text, leading to potential inaccuracies in sentiment classification.

Text-to-Speech Quality:

The quality of the generated Hindi audio files depends on the gTTS API, which may not always produce natural-sounding speech.

Scalability:

The project is designed for small-scale use. Handling a large volume of news articles or high-frequency API requests may require additional optimization.

Internet Dependency:

The project relies on third-party APIs (Google News RSS, Google Translator, and gTTS), which require an active internet connection. Any downtime or rate limits on these services may affect functionality.

## **Conclusion**
This project provides a **web-based sentiment analysis tool** that extracts news, performs sentiment evaluation, generates comparative insights, and offers Hindi text-to-speech conversion. APIs allow external systems to interact with the data efficiently.

**End of Documentation.**


