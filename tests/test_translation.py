"""Unit tests for Dimasa Translation Subsystem."""

import pytest
import dimasa


def test_translation_exact_greeting_phrase():
    res = dimasa.translate("Hello", source="english", target="dimasa")
    assert res.text.lower() == "khurthao"
    assert res.confidence >= 0.90
    assert len(res.sources) > 0
    assert "SRC-DSS-2018" in res.sources


def test_translation_exact_thanks_phrase():
    res = dimasa.translate("Thank you", source="english", target="dimasa")
    assert res.text.lower() == "hambai"
    assert res.confidence >= 0.90


def test_translation_aligned_corpus_sentence():
    res = dimasa.translate("I am drinking water.", source="english", target="dimasa")
    assert "di" in res.text
    assert "lung-du" in res.text
    assert res.confidence >= 0.85


def test_translation_english_to_hindi():
    res = dimasa.translate("Hello", source="english", target="hindi")
    assert "नमस्ते" in res.text or "नमस्कार" in res.text


def test_translation_dimasa_to_english_single_word():
    res = dimasa.translate("di", source="dimasa", target="english")
    assert "water" in res.text.lower()
    assert res.confidence > 0.70


def test_translation_dimasa_to_bengali_single_word():
    res = dimasa.translate("di", source="dimasa", target="bengali")
    assert "জল" in res.text or "পানি" in res.text


def test_translation_unknown_token_transparent_handling():
    res = dimasa.translate("A hypothetical unicorn gallops", source="english", target="dimasa")
    # Must flag untranslated tokens rather than hallucinating
    assert res.is_partial is True
    assert len(res.untranslated_tokens) > 0
    assert "unicorn" in res.untranslated_tokens or "[unicorn]" in res.text


def test_translation_empty_string():
    res = dimasa.translate("", source="english", target="dimasa")
    assert res.text == ""
    assert res.confidence == 0.0

