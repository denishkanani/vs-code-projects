from search import google_search

query = "Machine Learning"

results = google_search(query)

print("\nGoogle Search Results:\n")

for index, url in enumerate(results, start=1):
    print(f"{index}. {url}")