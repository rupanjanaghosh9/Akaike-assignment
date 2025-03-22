import requests
from bs4 import BeautifulSoup
import csv

# Define the search query
query = "Starlink"

# Google News RSS feed for Starlink
url = f"https://news.google.com/rss/search?q={query}"

# Make a request to the RSS feed
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "xml")  

    # Extract news items
    items = soup.find_all("item")[:10]

    # Store data in a list
    news_data = []
    for item in items:
        title = item.title.text if item.title else "No Title"
        description = item.find("description").text if item.find("description") else "No Summary"
       
        news_data.append([title, description])

    # Save to CSV
    with open("Starlink_news.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Summary"])  
        writer.writerows(news_data)

    print(f"Scraped {len(news_data)} news articles related to Starlink and saved to Starlink_news.csv.")

else:
    print("Failed to retrieve news articles.")
