class MarkDFetchError(Exception):
    """Base exception for markdfetch."""
    pass


class FetchError(MarkDFetchError):
    """Raised when a page cannot be fetched."""
    pass