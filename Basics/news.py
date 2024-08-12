import requests
import json

query = input("What type of news you are interested in? : ")

url = f"https://newsapi.org/v2/everything?q={query}&from=2024-07-12&sortBy=publishedAt&apiKey=9cddd5760b3444c18ad08ebe5cdfa885"

response = requests.get(url)
news = json.loads(response.text)
# print(news)

for article in news["articles"]:
    print(article["title"], "\n", article["description"])
    print("------------------------------------------")