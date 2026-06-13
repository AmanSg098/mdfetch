# /fetcher.py
import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .page import Page
from .exceptions import FetchError


def fetch(
    url: str,
    retries: int = 3,
    **kwargs
):

    """
    Fetch a web page and return a Page object.

    Args:
        url: Target URL.
        retries: Number of retry attempts.
        **kwargs: Additional arguments passed directly to requests.Session.get().

    Returns:
        Page: A Page object containing the response data.

    Raises:
        FetchError: If the request fails.

    Examples:
        page = mdfetch.fetch(
            "https://example.com",
            timeout=30,
            headers={"User-Agent": "Mozilla/5.0"},
        )
    """
    session = requests.Session()

    retry_strategy = Retry(
        total=retries,
        backoff_factor=1,
        status_forcelist=[429,500,502,503,504],
    )

    adapter = HTTPAdapter(
        max_retries=retry_strategy
    )

    session.mount("http://", adapter)
    session.mount("https://", adapter)

    try:
        response = session.get(
            url,
            **kwargs,
        )
        response.raise_for_status()

    except requests.RequestException as e:
        raise FetchError(f"Failed to fetch {url}: {e}") from e
    
    return Page(
        url=response.url,
        html=response.text,
        status_code=response.status_code,
        headers=dict(response.headers),
    )