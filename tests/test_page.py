import mdfetch
import pytest
from mdfetch import fetch
from mdfetch.exceptions import FetchError


def test_fetch():
    page = mdfetch.fetch("https://example.com")

    assert page.status_code == 200
    assert "Example Domain" in page.html


def test_text():
    page = mdfetch.fetch("https://example.com")

    text = page.text()

    assert "Example Domain" in text


def test_markdown():
    page = mdfetch.fetch("https://example.com")

    md = page.markdown()

    assert "# Example Domain" in md


def test_links():
    page = mdfetch.fetch("https://example.com")

    links = page.links()

    assert len(links) > 0
    assert "url" in links[0]
    assert "text" in links[0]


def test_fetch_error():
    with pytest.raises(FetchError):
        fetch("https://this-domain-should-not-exist-12345.com")