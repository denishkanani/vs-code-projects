"""
scraper.py
-----------
Web Scraper for AI Research Assistant
"""

import requests
from bs4 import BeautifulSoup
from config import Config


class WebScraper:
    """
    Scrapes webpage content and returns clean text.
    """

    def __init__(self):
        self.headers = {
            "User-Agent": Config.USER_AGENT
        }

        self.timeout = Config.REQUEST_TIMEOUT

    def scrape(self, url):
        """
        Scrape webpage.

        Args:
            url (str)

        Returns:
            dict
        """

        try:
            response = requests.get(
                url,
                headers=self.headers,
                timeout=self.timeout
            )

            response.raise_for_status()

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            # Remove unnecessary elements
            for tag in soup([
                "script",
                "style",
                "header",
                "footer",
                "nav",
                "aside",
                "noscript",
                "svg",
                "img"
            ]):
                tag.decompose()

            title = "No Title"

            if soup.title:
                title = soup.title.get_text(strip=True)

            paragraphs = soup.find_all("p")

            text = "\n".join(
                paragraph.get_text(" ", strip=True)
                for paragraph in paragraphs
            )

            if len(text) < 100:
                text = soup.get_text(
                    separator=" ",
                    strip=True
                )

            return {
                "success": True,
                "url": url,
                "title": title,
                "content": text
            }

        except Exception as e:

            return {
                "success": False,
                "url": url,
                "title": "",
                "content": "",
                "error": str(e)
            }


if __name__ == "__main__":

    scraper = WebScraper()

    url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

    result = scraper.scrape(url)

    if result["success"]:

        print("=" * 60)
        print("TITLE")
        print("=" * 60)
        print(result["title"])

        print("\n")

        print("=" * 60)
        print("CONTENT (First 1000 Characters)")
        print("=" * 60)

        print(result["content"][:1000])

    else:

        print("Error:")
        print(result["error"])