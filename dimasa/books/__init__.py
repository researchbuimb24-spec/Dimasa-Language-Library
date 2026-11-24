"""Dimasa Digital Book and Literature Preservation Package."""

from .catalog import BookCatalog, get_catalog
from .reader import Book, BookPage


def total_books() -> int:
    """Return total number of catalogued books."""
    return get_catalog().total_books()


def total_pages() -> int:
    """Return total pages across all catalogued books."""
    return get_catalog().total_pages()


def total_words() -> int:
    """Return total word count across all catalogued books."""
    return get_catalog().total_words()


def list_books():
    """List all books in catalog."""
    return get_catalog().list_books()


def get_book(book_id: str):
    """Retrieve book by ID."""
    return get_catalog().get_book(book_id)


def search_books(query: str):
    """Search for keyword across books and literature."""
    return get_catalog().search_books(query)


__all__ = [
    "Book",
    "BookPage",
    "BookCatalog",
    "get_catalog",
    "total_books",
    "total_pages",
    "total_words",
    "list_books",
    "get_book",
    "search_books",
]

