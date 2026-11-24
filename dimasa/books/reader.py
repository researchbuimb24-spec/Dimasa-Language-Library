"""Book reader and representation model for Dimasa digitized books."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class BookPage:
    """A single page of a digitized book."""
    page_number: int
    title: str
    content: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "page_number": self.page_number,
            "title": self.title,
            "content": self.content,
        }


@dataclass
class Book:
    """Digitized Dimasa linguistic or literary work."""
    id: str
    title: str
    author: str
    publication_year: int
    publisher: str
    place: str
    language: str
    copyright_status: str
    description: str
    source_id: str
    verification_status: str
    pages: List[BookPage] = field(default_factory=list)

    @property
    def total_pages(self) -> int:
        """Total number of pages in the book."""
        return len(self.pages)

    @property
    def total_words(self) -> int:
        """Count total words across all pages of the book."""
        count = 0
        for p in self.pages:
            count += len(p.content.split())
        return count

    def get_page(self, page_number: int) -> Optional[BookPage]:
        """Retrieve a specific page by 1-based page number."""
        if not self.pages or page_number < 1 or page_number > len(self.pages):
            return None
        return self.pages[page_number - 1]

    def search(self, keyword: str) -> List[Dict[str, Any]]:
        """Search for a keyword inside the book pages."""
        if not keyword:
            return []
        clean = keyword.strip().lower()
        matches: List[Dict[str, Any]] = []
        for p in self.pages:
            if clean in p.content.lower() or clean in p.title.lower():
                matches.append({
                    "page_number": p.page_number,
                    "title": p.title,
                    "snippet": self._extract_snippet(p.content, clean),
                })
        return matches

    def _extract_snippet(self, text: str, query: str, window: int = 120) -> str:
        """Extract snippet surrounding query match."""
        idx = text.lower().find(query)
        if idx == -1:
            return text[:window] + "..." if len(text) > window else text
        start = max(0, idx - 40)
        end = min(len(text), idx + len(query) + 80)
        prefix = "..." if start > 0 else ""
        suffix = "..." if end < len(text) else ""
        return prefix + text[start:end].strip() + suffix

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "publisher": self.publisher,
            "place": self.place,
            "language": self.language,
            "copyright_status": self.copyright_status,
            "description": self.description,
            "source_id": self.source_id,
            "verification_status": self.verification_status,
            "total_pages": self.total_pages,
            "total_words": self.total_words,
        }

