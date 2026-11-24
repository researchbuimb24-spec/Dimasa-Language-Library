"""Dimasa Multilingual Dictionary Package."""

from .lookup import lookup, lookup_root
from .models import DictionaryEntry
from .search import prefix_search, search
from .index import get_index

__all__ = [
    "DictionaryEntry",
    "lookup",
    "lookup_root",
    "search",
    "prefix_search",
    "get_index",
]

