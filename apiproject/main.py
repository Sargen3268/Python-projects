import requests
query = "artificial intelligence"
api = "5943b07d069442ec9e954ad09988138f"
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-05-15&sortBy=publishedAt&apiKey={api}"

print(url)

r =requests.get(url)
data = r.json()
articles = data['articles']

for index, article in enumerate(articles):
    print(index+1)
    print(article['title'])
    print(article['description'])
    print(article['url'])
    print("\n***************************************\n")

