# /fetcher.py
import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .page import Page
from .exceptions import FetchError


def fetch(
    url: str,
    timeout: int = 30,
    headers: dict | None = None,
    cookies: dict | None = None,
    proxies: dict | None = None,
    params: dict | None = None,
    retries: int = 3,
):

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
            timeout=timeout,
            headers=headers,
            cookies=cookies,
            proxies=proxies,
            params=params,
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