"""Syllable segmentation and phonotactics for Dimasa."""

import re
from typing import List, Tuple

VOWEL_PATTERNS = r"(ai|ao|au|a|i|u|e|o)"
CONSONANT_CLUSTERS = [
    "kh", "ph", "th", "ng", "sh", "kl", "kr", "pl", "pr", "bl", "br",
    "gl", "gr", "gd", "gs", "gp", "gj"
]


def syllabify(word: str) -> List[str]:
    """Segment a Dimasa word into constituent syllables.

    Handles sesquisyllabic structures and native Bodo-Garo phonotactics.
    """
    if not word or not isinstance(word, str):
        return []

    clean = word.strip().lower()
    # If hyphenated, syllabify parts
    if "-" in clean:
        parts = clean.split("-")
        res: List[str] = []
        for p in parts:
            res.extend(syllabify(p))
        return res

    # Check for initial sesquisyllable (e.g., gdain -> g + dain, gsom -> g + som)
    if clean.startswith("g") and len(clean) >= 3 and clean[1] in ("d", "s", "p", "j", "b", "k", "t"):
        prefix = clean[0]
        remainder = clean[1:]
        return [prefix] + _syllabify_stem(remainder)

    return _syllabify_stem(clean)


def _syllabify_stem(stem: str) -> List[str]:
    """Syllabify an un-hyphenated stem."""
    if not stem:
        return []

    # Find vowel centers
    matches = list(re.finditer(VOWEL_PATTERNS, stem))
    if not matches:
        return [stem]
    if len(matches) == 1:
        return [stem]

    syllables: List[str] = []
    prev_boundary = 0

    for i in range(len(matches) - 1):
        curr_vowel_end = matches[i].end()
        next_vowel_start = matches[i + 1].start()
        intervocalic_consonants = stem[curr_vowel_end:next_vowel_start]

        if len(intervocalic_consonants) == 0:
            split_idx = curr_vowel_end
        elif len(intervocalic_consonants) == 1:
            split_idx = curr_vowel_end
        elif len(intervocalic_consonants) == 2:
            # Check digraphs (kh, ph, th, ng, sh)
            if intervocalic_consonants in ("kh", "ph", "th", "ng", "sh"):
                split_idx = curr_vowel_end
            else:
                split_idx = curr_vowel_end + 1
        else:
            split_idx = curr_vowel_end + 1

        syllables.append(stem[prev_boundary:split_idx])
        prev_boundary = split_idx

    syllables.append(stem[prev_boundary:])
    return syllables
