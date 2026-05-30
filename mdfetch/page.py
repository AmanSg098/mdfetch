# page.py
from bs4 import BeautifulSoup
import html2text


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

