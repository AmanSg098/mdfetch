# page.py
from bs4 import BeautifulSoup
import html2text
from urllib.parse import urljoin


class Page:
    def __init__(self, url: str, html: str, status_code: int, headers: dict):
        self.url = url
        self.html = html
        self.status_code = status_code
        self.headers = headers

    def text(self):
        soup = BeautifulSoup(self.html, "html.parser")
        return soup.get_text(separator="\n", strip=True)

    def markdown(self, exclude=None, include=None):
        converter = html2text.HTML2Text()
        converter.ignore_links = False

        soup = BeautifulSoup(self.html, "html.parser")

        if exclude:
            for tag in exclude:
                for element in soup.find_all(tag):
                    element.decompose()

        if include:
            html = ""
            for tag in include:
                for element in soup.find_all(tag):
                    html += str(element)
        else:
            html = str(soup)

        return converter.handle(html)
    
    def links(self, skip_empty: bool = False):
        soup = BeautifulSoup(self.html, "html.parser")

        links: list[dict] = []

        for a in soup.find_all("a", href=True):
            text = a.get_text(strip=True)

            if skip_empty and not text:
                continue

            links.append(
                {
                    "url": urljoin(self.url, a["href"]),
                    "text": text,
                }
            )

        return links

