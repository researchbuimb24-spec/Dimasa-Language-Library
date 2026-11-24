"""Dimasa Morphological Analysis and Generation Package."""

from .analyzer import MorphemeAnalysis, analyze_word, morphological_roots
from .conjugation import conjugate
from .declension import decline_noun, pluralize
from .generator import generate_forms
from .roots import KNOWN_ROOTS

__all__ = [
    "MorphemeAnalysis",
    "analyze_word",
    "morphological_roots",
    "conjugate",
    "decline_noun",
    "pluralize",
    "generate_forms",
    "KNOWN_ROOTS",
]

