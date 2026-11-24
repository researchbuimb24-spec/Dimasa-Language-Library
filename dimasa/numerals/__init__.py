"""Dimasa Numerals and Classifier System."""

from .classifiers import apply_classifier, list_classifiers
from .numbers import num_to_words, words_to_num

__all__ = [
    "num_to_words",
    "words_to_num",
    "apply_classifier",
    "list_classifiers",
]

