"""Dimasa Phonology, Tone, and Syllable Engine."""

from .ipa import analyze_phonology, to_ipa
from .phonemes import CONSONANTS, VOWELS, phonemes
from .syllables import syllabify

__all__ = [
    "phonemes",
    "syllabify",
    "to_ipa",
    "analyze_phonology",
    "CONSONANTS",
    "VOWELS",
]

