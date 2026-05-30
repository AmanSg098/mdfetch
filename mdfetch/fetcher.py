# /fetcher.py
import requests

from .page import Page


def fetch(
    url: str,
    timeout: int = 30,
    headers: dict | None = None,
):
    response = requests.get(
        url,
        timeout=timeout,
        headers=headers,
    )

    return Page(
        url=response.url,
        html=response.text,
        status_code=response.status_code,
        headers=dict(response.headers),
    )