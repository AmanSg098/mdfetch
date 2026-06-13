# __init__.py
from .fetcher import fetch
from .exceptions import MarkDFetchError, FetchError

__all__ = [
    "fetch",
    "MarkDFetchError",
    "FetchError",
]

__version__ = "0.1.0"