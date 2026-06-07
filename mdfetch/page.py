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

    def text(self, selector: str | None = None):
        soup = BeautifulSoup(self.html, "html.parser")

        if selector:
            elements = soup.select(selector)

            return "\n".join(
                element.get_text(separator="\n", strip=True)
                for element in elements
            )

        return soup.get_text(separator="\n", strip=True)

    def markdown(self, exclude=None, include=None, selector: str | None = None):
        converter = html2text.HTML2Text()
        converter.ignore_links = False

        soup = BeautifulSoup(self.html, "html.parser")

        if exclude:
            for tag in exclude:
                for element in soup.find_all(tag):
                    element.decompose()

        if selector:
            html = "".join(
                str(element)
                for element in soup.select(selector)
            )

        elif include:
            html = ""
            for tag in include:
                for element in soup.find_all(tag):
                    html += str(element)

        else:
            html = str(soup)

        return converter.handle(html)
    
    def links(self, skip_empty: bool = False, unique: bool = False):
        soup = BeautifulSoup(self.html, "html.parser")

        links = []
        seen = set()

        for a in soup.find_all("a", href=True):
            url = urljoin(self.url, a["href"])
            text = a.get_text(strip=True)

            if skip_empty and not text:
                continue

            if unique:
                if url in seen:
                    continue
                seen.add(url)

            links.append(
                {
                    "url": url,
                    "text": text,
                }
            )

        return links

