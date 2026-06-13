# page.py
from bs4 import BeautifulSoup
import html2text
from urllib.parse import urljoin


class Page:
    """
    Represents a fetched web page and provides
    methods for extracting content.
    """
    def __init__(self, url: str, html: str, status_code: int, headers: dict):
        self.url = url
        self.html = html
        self.status_code = status_code
        self.headers = headers

    def text(
        self,
        selector: str | None = None,
    ) -> str:
        """
        Extract plain text from the page.

        Args:
            selector: Optional CSS selector.

        Returns:
            str: Extracted text.
        """
        soup = BeautifulSoup(self.html, "html.parser")

        if selector:
            elements = soup.select(selector)

            return "\n".join(
                element.get_text(separator="\n", strip=True)
                for element in elements
            )

        return soup.get_text(separator="\n", strip=True)

    def markdown(
        self,
        exclude: list[str] | None = None,
        include: list[str] | None = None,
        selector: str | None = None,
    ) -> str:
        """
        Convert page content to Markdown.

        Args:
            exclude: Tags to remove before conversion.
            include: Tags to include before conversion.
            selector: CSS selector to target content.

        Returns:
            str: Markdown content.
        """
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
    
    def links(
        self,
        skip_empty: bool = False,
        unique: bool = False,
    ) -> list[dict[str, str]]:
        """
        Extract links from the page.

        Args:
            skip_empty: Skip links without text.
            unique: Remove duplicate URLs.

        Returns:
            list[dict]: Extracted links.
        """
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

