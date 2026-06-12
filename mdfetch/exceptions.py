class MDFetchError(Exception):
    """Base exception for mdfetch."""
    pass


class FetchError(MDFetchError):
    """Raised when a page cannot be fetched."""
    pass