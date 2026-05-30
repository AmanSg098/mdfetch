# page.py
from bs4 import BeautifulSoup


class Page:
    def __init__(self, url: str, html: str, status_code: int, headers: dict):
        self.url = url
        self.html = html
        self.status_code = status_code
        self.headers = headers

    def text(self):
        soup = BeautifulSoup(self.html, "html.parser")
        return soup.get_text(separator="\n", strip=True)