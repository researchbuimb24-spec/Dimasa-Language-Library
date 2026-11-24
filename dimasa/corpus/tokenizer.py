"""Tokenizer for Dimasa sentences and morphemes."""

import re
from typing import List


def tokenize(text: str) -> List[str]:
    """Tokenize Dimasa text into clean word tokens, preserving hyphens."""
    if not text or not isinstance(text, str):
        return []

    # Clean punctuation while keeping hyphens inside words
    tokens = re.findall(r"[A-Za-z0-9\-]+", text)
    return [t.strip("-") for t in tokens if t.strip("-")]


def tokenize_morphemes(word: str) -> List[str]:
    """Split a Dimasa hyphenated compound or inflected word into morphemes."""
    if not word:
        return []
    return [p for p in word.split("-") if p]

