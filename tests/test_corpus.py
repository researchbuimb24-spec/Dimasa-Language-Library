"""Unit tests for Dimasa Searchable Linguistic Corpus."""

import pytest
import dimasa


def test_corpus_search():
    res = dimasa.corpus.search("water")
    assert len(res) > 0
    assert any("di" in s.dimasa for s in res)


def test_corpus_word_frequency():
    freq = dimasa.corpus.word_frequency(top_n=20)
    assert len(freq) > 0
    assert isinstance(freq, dict)
    # Fundamental words should appear
    assert "di" in freq or "ang" in freq or "bo" in freq


def test_corpus_sentence_examples():
    examples = dimasa.corpus.sentence_examples("di")
    assert len(examples) > 0
    for ex in examples:
        assert "di" in ex["dimasa"] or "water" in ex["english"].lower()


def test_corpus_stats():
    st = dimasa.corpus.stats()
    assert st["total_sentences"] >= 20
    assert st["total_tokens"] >= 60
    assert "genres" in st
    assert "sources" in st

