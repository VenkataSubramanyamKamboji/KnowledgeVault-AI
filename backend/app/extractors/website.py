import requests
from bs4 import BeautifulSoup


class WebsiteExtractor:

    def extract(self, url: str):

        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 "
                    "(Windows NT 10.0; Win64; x64)"
                )
            }
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        title = (
            soup.title.string.strip()
            if soup.title
            else "Untitled"
        )

        paragraphs = soup.find_all("p")

        raw_text = " ".join(
            p.get_text(strip=True)
            for p in paragraphs
        )

        return {
            "title": title,
            "raw_text": raw_text
        }