import pandas as pd

# Load CSV (Ensure the correct path)
csv_path = r"C:\Users\rupanjana ghosh\Downloads\pythonproject\assignmentrupanjana\Starlink_news_with_sentiment_cleaned.csv"
df = pd.read_csv(csv_path).head(10)  # Process only the first 10 articles

# Select the correct sentiment columns
df_comparison = df[['Title', 'Title_Sentiment']]


comparison_result = []
for i in range(len(df_comparison)):
    for j in range(i + 1, len(df_comparison)):  
        article_1 = df_comparison.iloc[i]
        article_2 = df_comparison.iloc[j]

        comparison_result.append({
            "Article_1": article_1["Title"],
            "Article_2": article_2["Title"],
            "Sentiment_1": article_1["Title_Sentiment"],
            "Sentiment_2": article_2["Title_Sentiment"],
            "Sentiment_Match": "Same" if article_1["Title_Sentiment"] == article_2["Title_Sentiment"] else "Different"
        })

# Convert to DataFrame
df_comparison_table = pd.DataFrame(comparison_result)

# Save comparison results
output_csv = r"C:\Users\rupanjana ghosh\Downloads\pythonproject\assignmentrupanjana\Starlink_news_comparative_sentiment_analysis.csv"
df_comparison_table.to_csv(output_csv, index=False)

print(f"Comparative Sentiment Analysis completed! Results saved to {output_csv}")
