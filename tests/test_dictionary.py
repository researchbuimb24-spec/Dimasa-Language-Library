"""Unit tests for Dimasa Multilingual Dictionary Subsystem."""

import pytest
import dimasa


def test_dictionary_exact_lookup():
    entry = dimasa.lookup("di")
    assert entry is not None
    assert entry.headword == "di"
    assert "water" in entry.english.lower()
    assert entry.part_of_speech == "noun"
    assert entry.phonetic_ipa == "di"
    assert entry.bengali_script == "দি"
    assert entry.verification_status == "documented"
    assert entry.source_id == "SRC-EVANS-2024"


def test_dictionary_case_insensitive_lookup():
    entry1 = dimasa.lookup("NOH")
    assert entry1 is not None
    assert entry1.headword == "noh"
    assert "house" in entry1.english.lower()

    entry2 = dimasa.lookup("HaSaO")
    assert entry2 is not None
    assert entry2.headword == "hasao"


def test_dictionary_bengali_script_lookup():
    entry = dimasa.lookup("দি")
    assert entry is not None
    assert entry.headword == "di"

    entry2 = dimasa.lookup("নহ")
    assert entry2 is not None
    assert entry2.headword == "noh"


def test_dictionary_derived_form_lookup():
    entry = dimasa.lookup("dimasa")
    assert entry is not None
    assert "dimasa" in entry.headword.lower()

    entry2 = dimasa.lookup("disa")
    assert entry2 is not None
    assert "stream" in entry2.english.lower() or "brook" in entry2.english.lower()


def test_dictionary_root_lookup():
    entries = dimasa.lookup_root("di")
    assert len(entries) >= 2
    headwords = [e.headword for e in entries]
    assert "di" in headwords
    assert "dima" in headwords or "disa" in headwords


def test_dictionary_multilingual_search():
    # English search
    res_en = dimasa.search("water", language="english")
    assert len(res_en) > 0
    assert any(e.headword == "di" for e in res_en)

    # Bengali search
    res_bn = dimasa.search("জল", language="bengali")
    assert len(res_bn) > 0
    assert any(e.headword == "di" for e in res_bn)

    # Hindi search
    res_hi = dimasa.search("पानी", language="hindi")
    assert len(res_hi) > 0
    assert any(e.headword == "di" for e in res_hi)

    # Dimasa headword prefix search
    res_dis = dimasa.search("da", language="dimasa")
    assert len(res_dis) > 0


def test_dictionary_prefix_search():
    res = dimasa.prefix_search("dao")
    assert len(res) >= 2
    hws = [e.headword for e in res]
    assert "dao" in hws


def test_dictionary_unknown_word_handling():
    res = dimasa.lookup("nonexistentwordxyz123")
    assert res is None

    empty_res = dimasa.lookup("")
    assert empty_res is None


def test_dictionary_entry_to_dict():
    entry = dimasa.lookup("bushu")
    assert entry is not None
    d = entry.to_dict()
    assert isinstance(d, dict)
    assert d["headword"] == "bushu"
    assert "post-harvest" in d["english"]

