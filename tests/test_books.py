"""Unit tests for Dimasa Books and Literature Preservation Subsystem."""

import pytest
import dimasa


def test_books_counts():
    assert dimasa.total_books() >= 3
    assert dimasa.total_pages() >= 10
    assert dimasa.total_words() >= 250


def test_books_listing():
    books = dimasa.list_books()
    assert len(books) >= 3
    b_ids = [b.id for b in books]
    assert "dundas-1908" in b_ids
    assert "grierson-1903" in b_ids
    assert "dimasa-folklore-2021" in b_ids


def test_book_page_reading():
    book = dimasa.get_book("dundas-1908")
    assert book is not None
    assert book.title == "An Outline Grammar and Dictionary of the Kachari (Dimasa) Language"
    assert book.author.startswith("W. C. M. Dundas")

    page1 = book.get_page(1)
    assert page1 is not None
    assert page1.page_number == 1
    assert "North Cachar" in page1.content

    # Out of bounds page
    page_invalid = book.get_page(999)
    assert page_invalid is None


def test_book_search_inside():
    book = dimasa.get_book("dundas-1908")
    assert book is not None
    matches = book.search("classifier")
    assert len(matches) > 0
    assert any(m["page_number"] == 4 for m in matches)


def test_cross_book_search():
    results = dimasa.search_books("Sangsari")
    assert len(results) > 0
    assert any(r["book_id"] == "dimasa-folklore-2021" for r in results)
