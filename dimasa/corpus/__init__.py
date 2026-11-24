"""Dimasa Searchable Linguistic Corpus Package."""

from .corpus import CorpusManager, get_corpus
from .models import CorpusSentence
from .tokenizer import tokenize, tokenize_morphemes


def search(query: str, limit: int = 20):
    """Search parallel sentences in the Dimasa corpus."""
    return get_corpus().search(query, limit=limit)


def word_frequency(top_n: int = 50):
    """Compute token frequency across the Dimasa corpus."""
    return get_corpus().word_frequency(top_n=top_n)


def sentence_examples(word: str, limit: int = 10):
    """Find aligned example sentences for a word."""
    return get_corpus().sentence_examples(word, limit=limit)


def stats():
    """Return corpus statistics and counts."""
    return get_corpus().stats()


__all__ = [
    "CorpusSentence",
    "CorpusManager",
    "get_corpus",
    "tokenize",
    "tokenize_morphemes",
    "search",
    "word_frequency",
    "sentence_examples",
    "stats",
]

