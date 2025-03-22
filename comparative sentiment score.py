import pandas as pd

# Load the first 10 rows from the CSV file
csv_path = r"C:\Users\rupanjana ghosh\Downloads\pythonproject\assignmentrupanjana\Starlink_news_with_sentiment_scores.csv"
df = pd.read_csv(csv_path).head(10)

# Extract Title and Sentiment Score
df = df[['Title', 'Title_Sentiment_Score']]

# Compare sentiment scores
comparison_results = []
for i in range(len(df)):
    for j in range(i + 1, len(df)):
        score_diff = abs(df.iloc[i]["Title_Sentiment_Score"] - df.iloc[j]["Title_Sentiment_Score"])
        comparison_results.append([df.iloc[i]["Title"], df.iloc[j]["Title"], score_diff])

# Convert to DataFrame
df_comparison = pd.DataFrame(comparison_results, columns=["Article_1", "Article_2", "Score_Difference"])

# Save to CSV
output_csv = r"C:\Users\rupanjana ghosh\Downloads\pythonproject\assignmentrupanjana\Starlink_news_comparative_scores.csv"
df_comparison.to_csv(output_csv, index=False)

print(f" Comparative sentiment score analysis saved to {output_csv}")
