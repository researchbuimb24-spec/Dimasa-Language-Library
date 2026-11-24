"""Roman script orthography utilities for Dimasa."""

import unicodedata
from typing import List


def format_roman(text: str) -> str:
    """Format Romanized Dimasa text according to standard orthography."""
    if not text:
        return ""
    normalized = unicodedata.normalize("NFC", text)
    return normalized.strip()

