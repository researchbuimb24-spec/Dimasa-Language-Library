"""Multilingual search, prefix search, and fuzzy search for Dimasa dictionary."""

import difflib
from typing import List, Optional
from .index import get_index
from .models import DictionaryEntry


def search(query: str, language: str = "english", limit: int = 20) -> List[DictionaryEntry]:
    """Search dictionary entries across languages.

    Parameters
    ----------
    query : str
        Search query keyword.
    language : str
        Target search language: 'english', 'dimasa', 'bengali', 'hindi', or 'all'.
    limit : int
        Maximum number of results to return.

    Returns
    -------
    List[DictionaryEntry]
        List of matching dictionary entries.
    """
    if not query or not isinstance(query, str):
        return []

    clean = query.strip().lower()
    index = get_index()
    results: List[DictionaryEntry] = []
    seen: set = set()

    lang = language.lower()

    if lang in ("dimasa", "all"):
        # 1. Headword prefix or substring match
        for hw, entry in index.headword_map.items():
            if clean in hw:
                if entry.headword not in seen:
                    results.append(entry)
                    seen.add(entry.headword)
                    if len(results) >= limit:
                        return results

    if lang in ("english", "all"):
        # Match tokens in inverted index
        if clean in index.english_index:
            for entry in index.english_index[clean]:
                if entry.headword not in seen:
                    results.append(entry)
                    seen.add(entry.headword)
                    if len(results) >= limit:
                        return results

        # Substring in definition
        for entry in index.entries:
            if clean in entry.english.lower():
                if entry.headword not in seen:
                    results.append(entry)
                    seen.add(entry.headword)
                    if len(results) >= limit:
                        return results

    if lang in ("hindi", "all"):
        raw_query = query.strip()
        if raw_query in index.hindi_index:
            for entry in index.hindi_index[raw_query]:
                if entry.headword not in seen:
                    results.append(entry)
                    seen.add(entry.headword)
                    if len(results) >= limit:
                        return results
        for entry in index.entries:
            if raw_query in entry.hindi:
                if entry.headword not in seen:
                    results.append(entry)
                    seen.add(entry.headword)
                    if len(results) >= limit:
                        return results

    if lang in ("bengali", "all"):
        raw_query = query.strip()
        if raw_query in index.bengali_index:
            for entry in index.bengali_index[raw_query]:
                if entry.headword not in seen:
                    results.append(entry)
                    seen.add(entry.headword)
                    if len(results) >= limit:
                        return results
        for entry in index.entries:
            if raw_query in entry.bengali or raw_query in entry.bengali_script:
                if entry.headword not in seen:
                    results.append(entry)
                    seen.add(entry.headword)
                    if len(results) >= limit:
                        return results

    # Fuzzy search fallback if no direct matches found
    if not results and lang in ("dimasa", "english"):
        all_headwords = list(index.headword_map.keys())
        matches = difflib.get_close_matches(clean, all_headwords, n=limit, cutoff=0.6)
        for m in matches:
            entry = index.headword_map[m]
            if entry.headword not in seen:
                results.append(entry)
                seen.add(entry.headword)

    return results[:limit]


def prefix_search(prefix: str, limit: int = 15) -> List[DictionaryEntry]:
    """Find words starting with a given prefix."""
    if not prefix:
        return []
    clean = prefix.strip().lower()
    index = get_index()
    results: List[DictionaryEntry] = []
    seen: set = set()

    for hw, entry in index.headword_map.items():
        if hw.startswith(clean) and entry.headword not in seen:
            results.append(entry)
            seen.add(entry.headword)
            if len(results) >= limit:
                break

    return results

