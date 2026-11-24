"""Exact, case-insensitive, and root-based lookup for Dimasa dictionary."""

from typing import List, Optional
from .index import get_index
from .models import DictionaryEntry


def lookup(word: str) -> Optional[DictionaryEntry]:
    """Look up a word in the Dimasa dictionary.

    Supports:
    - Exact Dimasa headword lookup
    - Case-insensitive lookup
    - Bengali-Assamese script lookup
    - Derived form lookup
    - Root-based fallback lookup
    """
    if not word or not isinstance(word, str):
        return None

    clean = word.strip().lower()
    index = get_index()

    # 1. Exact or case-insensitive headword
    if clean in index.headword_map:
        return index.headword_map[clean]

    # 2. Bengali-Assamese script representation
    raw_clean = word.strip()
    if raw_clean in index.bengali_script_map:
        return index.bengali_script_map[raw_clean]

    # 3. Check with hyphens stripped or replaced
    no_hyphen = clean.replace("-", "")
    if no_hyphen in index.headword_map:
        return index.headword_map[no_hyphen]

    # 4. Root based lookup
    if clean in index.root_index:
        entries = index.root_index[clean]
        if entries:
            return entries[0]

    return None


def lookup_root(root: str) -> List[DictionaryEntry]:
    """Find all dictionary entries sharing a given morphological root."""
    if not root:
        return []
    index = get_index()
    return index.root_index.get(root.strip().lower(), [])

