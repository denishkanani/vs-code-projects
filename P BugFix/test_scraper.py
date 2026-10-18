from scraper import WebScraper

scraper = WebScraper()

url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

result = scraper.scrape(url)

print("\nTitle:\n")
print(result["title"])

print("\n")

print(result["content"][:1500])