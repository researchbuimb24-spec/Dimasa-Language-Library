"""Unicode normalization and script detection for Dimasa texts."""

import re
import unicodedata
from typing import Literal

ScriptType = Literal["roman", "bengali", "mixed", "unknown"]


def normalize_text(text: str) -> str:
    """Normalize Dimasa text into standardized Unicode NFC form."""
    if not text or not isinstance(text, str):
        return ""

    # Canonical Unicode NFC decomposition/composition
    normalized = unicodedata.normalize("NFC", text)

    # Standardize hyphenation and whitespace
    normalized = normalized.replace("—", "-").replace("–", "-")
    normalized = re.sub(r"[ \t]+", " ", normalized)
    return normalized.strip()


def detect_script(text: str) -> ScriptType:
    """Detect whether text is written in Roman, Bengali-Assamese, or Mixed script."""
    if not text or not isinstance(text, str):
        return "unknown"

    has_roman = False
    has_bengali = False

    for ch in text:
        code = ord(ch)
        # Bengali/Assamese Unicode block: U+0980 to U+09FF
        if 0x0980 <= code <= 0x09FF:
            has_bengali = True
        # Basic Latin letters: A-Z, a-z
        elif (0x0041 <= code <= 0x005A) or (0x0061 <= code <= 0x007A):
            has_roman = True

    if has_roman and has_bengali:
        return "mixed"
    if has_bengali:
        return "bengali"
    if has_roman:
        return "roman"
    return "unknown"

