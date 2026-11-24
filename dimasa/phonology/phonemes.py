"""Phoneme inventory and phonetic classifications for Dimasa."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ConsonantPhoneme:
    """Consonant phoneme description."""
    symbol: str
    ipa: str
    manner: str
    place: str
    voicing: str
    examples: List[str]


@dataclass
class VowelPhoneme:
    """Vowel phoneme description."""
    symbol: str
    ipa: str
    height: str
    backness: str
    rounding: str
    examples: List[str]


# 17 native consonant phonemes documented by Evans & Langthasa (2024) and Longmailai (2014)
CONSONANTS: List[ConsonantPhoneme] = [
    ConsonantPhoneme("p", "p", "stop", "bilabial", "voiceless", ["pha", "phai"]),
    ConsonantPhoneme("b", "b", "stop", "bilabial", "voiced", ["bo", "bosi"]),
    ConsonantPhoneme("t", "t", "stop", "alveolar", "voiceless", ["tai", "tamah"]),
    ConsonantPhoneme("d", "d", "stop", "alveolar", "voiced", ["di", "dain"]),
    ConsonantPhoneme("k", "k", "stop", "velar", "voiceless", ["khoro", "kham"]),
    ConsonantPhoneme("g", "g", "stop", "velar", "voiced", ["grao", "giri"]),
    ConsonantPhoneme("ʔ", "ʔ", "stop", "glottal", "voiceless", ["internal syllable break"]),
    ConsonantPhoneme("m", "m", "nasal", "bilabial", "voiced", ["mai", "mairang"]),
    ConsonantPhoneme("n", "n", "nasal", "alveolar", "voiced", ["noh", "nu"]),
    ConsonantPhoneme("ng", "ŋ", "nasal", "velar", "voiced", ["ang", "thang"]),
    ConsonantPhoneme("r", "ɾ", "tap", "alveolar", "voiced", ["ri", "rigu"]),
    ConsonantPhoneme("s", "s", "fricative", "alveolar", "voiceless", ["san", "subun"]),
    ConsonantPhoneme("z", "z", "fricative", "alveolar", "voiced", ["zi", "judima"]),
    ConsonantPhoneme("h", "h", "fricative", "glottal", "voiceless", ["ha", "hor"]),
    ConsonantPhoneme("w", "w", "approximant", "bilabial", "voiced", ["wai", "hawar"]),
    ConsonantPhoneme("l", "l", "approximant", "alveolar", "voiced", ["lung", "la"]),
    ConsonantPhoneme("y", "j", "approximant", "palatal", "voiced", ["ya", "yau"]),
]

# 5 tense vowel phonemes
VOWELS: List[VowelPhoneme] = [
    VowelPhoneme("i", "i", "close", "front", "unrounded", ["di", "zi", "ri"]),
    VowelPhoneme("e", "e", "close-mid", "front", "unrounded", ["ebe", "repgon"]),
    VowelPhoneme("a", "a", "open", "central", "unrounded", ["ha", "ang", "san"]),
    VowelPhoneme("o", "o", "close-mid", "back", "rounded", ["noh", "hor", "bo"]),
    VowelPhoneme("u", "u", "close", "back", "rounded", ["nu", "thu", "subun"]),
]


def phonemes() -> Dict[str, Any]:
    """Return the complete authentic Dimasa phoneme inventory."""
    return {
        "consonants_total": len(CONSONANTS),
        "vowels_total": len(VOWELS),
        "consonants": [
            {
                "symbol": c.symbol,
                "ipa": c.ipa,
                "manner": c.manner,
                "place": c.place,
                "voicing": c.voicing,
                "examples": c.examples,
            }
            for c in CONSONANTS
        ],
        "vowels": [
            {
                "symbol": v.symbol,
                "ipa": v.ipa,
                "height": v.height,
                "backness": v.backness,
                "rounding": v.rounding,
                "examples": v.examples,
            }
            for v in VOWELS
        ],
        "notes": (
            "Based on Jonathan P. Evans & Dhrubajit Langthasa (2024), "
            "focusing on the Haflong variety. Haflong Dimasa does not exhibit "
            "phonemic tone contrasts. Stop voicing contrast is two-way."
        ),
    }

