"""IPA (International Phonetic Alphabet) transcription for Dimasa."""

import re
from typing import Any, Dict, List
from .syllables import syllabify


def to_ipa(word: str) -> str:
    """Convert Dimasa orthographic word to International Phonetic Alphabet (IPA).

    Parameters
    ----------
    word : str
        Dimasa word in standard Roman orthography.

    Returns
    -------
    str
        IPA transcription representing standard Haflong pronunciation.
    """
    if not word or not isinstance(word, str):
        return ""

    clean = word.strip().lower()

    # Digraph replacements
    ipa = clean
    ipa = ipa.replace("kh", "kʰ")
    ipa = ipa.replace("ph", "pʰ")
    ipa = ipa.replace("th", "tʰ")
    ipa = ipa.replace("ng", "ŋ")
    ipa = ipa.replace("sh", "ʃ")
    ipa = ipa.replace("j", "dʒ")
    ipa = ipa.replace("r", "ɾ")
    ipa = ipa.replace("y", "j")

    # Sesquisyllabic clusters: gd, gs, gj, gp, gb -> [ɡə...]
    ipa = re.sub(r"^g([dstpjkɾm])", r"ɡə\1", ipa)
    ipa = re.sub(r"^m([ʃs])", r"mə\1", ipa)

    return ipa


def analyze_phonology(word: str) -> Dict[str, Any]:
    """Perform comprehensive phonological analysis on a Dimasa word."""
    if not word:
        return {}

    clean = word.strip().lower()
    syllables = syllabify(clean)
    ipa_transcription = to_ipa(clean)

    # Check for sesquisyllabic structure
    is_sesquisyllabic = (
        clean.startswith(("gd", "gs", "gp", "gj", "gb", "gk", "gt", "msh"))
        or "ɡə" in ipa_transcription
    )

    return {
        "word": word,
        "syllables": syllables,
        "syllable_count": len(syllables),
        "ipa": ipa_transcription,
        "is_sesquisyllabic": is_sesquisyllabic,
        "tone_status": "non_phonemic_in_standard_haflong",
        "voicing_contrast": "two_way_stop_contrast",
    }

