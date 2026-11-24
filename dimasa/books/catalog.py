"""Book catalog loader and cross-book search for Dimasa literature."""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional
from .reader import Book, BookPage

BOOKS_FILE = Path(__file__).parent.parent / "data" / "books.json"


class BookCatalog:
    """Catalog of digitized and public domain Dimasa literature."""

    def __init__(self, data_file: Optional[Path] = None):
        if data_file is None:
            data_file = BOOKS_FILE
        self.data_file = Path(data_file)
        self._books: Dict[str, Book] = {}
        self.load()

    def load(self) -> None:
        """Load books from json."""
        if not self.data_file.exists():
            return
        with open(self.data_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data.get("books", []):
                pages: List[BookPage] = []
                for p in item.get("pages", []):
                    pages.append(
                        BookPage(
                            page_number=p["page_number"],
                            title=p.get("title", f"Page {p['page_number']}"),
                            content=p.get("content", ""),
                        )
                    )
                book = Book(
                    id=item["id"],
                    title=item["title"],
                    author=item.get("author", "Unknown"),
                    publication_year=item.get("publication_year", 0),
                    publisher=item.get("publisher", ""),
                    place=item.get("place", ""),
                    language=item.get("language", "English, Dimasa"),
                    copyright_status=item.get("copyright_status", "public_domain"),
                    description=item.get("description", ""),
                    source_id=item.get("source_id", ""),
                    verification_status=item.get("verification_status", "documented"),
                    pages=pages,
                )
                self._books[book.id] = book

    def get_book(self, book_id: str) -> Optional[Book]:
        """Retrieve book by ID."""
        if not book_id:
            return None
        return self._books.get(book_id.strip().lower())

    def list_books(self) -> List[Book]:
        """List all books in catalog."""
        return list(self._books.values())

    def total_books(self) -> int:
        """Total number of available books."""
        return len(self._books)

    def total_pages(self) -> int:
        """Total number of pages across all books."""
        return sum(b.total_pages for b in self._books.values())

    def total_words(self) -> int:
        """Total word count across all books."""
        return sum(b.total_words for b in self._books.values())

    def search_books(self, query: str) -> List[Dict[str, Any]]:
        """Search across all books for a keyword."""
        if not query:
            return []
        clean = query.strip().lower()
        results: List[Dict[str, Any]] = []

        for book in self._books.values():
            # Check metadata
            meta_match = clean in book.title.lower() or clean in book.author.lower() or clean in book.description.lower()
            page_matches = book.search(clean)

            if meta_match or page_matches:
                results.append({
                    "book_id": book.id,
                    "title": book.title,
                    "author": book.author,
                    "matches_count": len(page_matches),
                    "page_matches": page_matches,
                })

        return results


# Singleton catalog
_catalog: Optional[BookCatalog] = None


def get_catalog() -> BookCatalog:
    """Get or create singleton book catalog."""
    global _catalog
    if _catalog is None:
        _catalog = BookCatalog()
    return _catalog

