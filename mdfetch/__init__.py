# __init__.py
from .fetcher import fetch
from .exceptions import MDFetchError, FetchError

__all__ = [
    "fetch",
    "MDFetchError",
    "FetchError",
]

__version__ = "0.1.0"