"""Unit tests for Dimasa Phonology and Syllable Engine."""

import pytest
import dimasa


def test_phonemes_inventory():
    inv = dimasa.phonemes()
    assert inv["consonants_total"] == 17
    assert inv["vowels_total"] == 5
    consonant_symbols = [c["symbol"] for c in inv["consonants"]]
    assert "p" in consonant_symbols
    assert "b" in consonant_symbols
    assert "t" in consonant_symbols
    assert "d" in consonant_symbols
    assert "k" in consonant_symbols
    assert "g" in consonant_symbols
    assert "ʔ" in consonant_symbols
    assert "m" in consonant_symbols
    assert "n" in consonant_symbols
    assert "ng" in consonant_symbols
    assert "r" in consonant_symbols
    assert "s" in consonant_symbols
    assert "z" in consonant_symbols
    assert "h" in consonant_symbols
    assert "w" in consonant_symbols
    assert "l" in consonant_symbols
    assert "y" in consonant_symbols


def test_syllabify():
    # Monosyllable
    assert dimasa.syllabify("di") == ["di"]
    assert dimasa.syllabify("noh") == ["noh"]
    assert dimasa.syllabify("thang") == ["thang"]

    # Disyllable
    assert len(dimasa.syllabify("dimasa")) >= 2
    assert len(dimasa.syllabify("subun")) == 2

    # Sesquisyllable (initial minor pre-syllable)
    s = dimasa.syllabify("gdain")
    assert len(s) == 2
    assert s[0] == "g"


def test_to_ipa():
    ipa1 = dimasa.to_ipa("thang")
    assert "tʰ" in ipa1
    assert "ŋ" in ipa1

    ipa2 = dimasa.to_ipa("phai")
    assert "pʰ" in ipa2

    # Sesquisyllable realization
    ipa3 = dimasa.to_ipa("gdain")
    assert "ɡə" in ipa3


def test_analyze_phonology():
    res = dimasa.analyze_phonology("gdain")
    assert res["is_sesquisyllabic"] is True
    assert res["syllable_count"] >= 2
    assert res["tone_status"] == "non_phonemic_in_standard_haflong"

