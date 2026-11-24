"""Unit tests for Dimasa Script and Transliteration Engine."""

import pytest
import dimasa


def test_transliteration_to_bengali():
    assert dimasa.to_bengali("di") == "দি"
    assert dimasa.to_bengali("noh") == "নহ"
    assert dimasa.to_bengali("dima") == "দিমা"
    assert dimasa.to_bengali("grao") == "গ্রাও"


def test_transliteration_to_roman():
    assert dimasa.to_roman("দি") == "di"
    assert dimasa.to_roman("নহ") == "noh"
    assert dimasa.to_roman("দিমা") == "dima"


def test_detect_script():
    assert dimasa.detect_script("grao dima") == "roman"
    assert dimasa.detect_script("গ্রাও দিমা") == "bengali"
    assert dimasa.detect_script("grao দিমা") == "mixed"
    assert dimasa.detect_script("12345") == "unknown"


def test_normalize_text():
    raw = "dima   hasao  —  assam"
    norm = dimasa.normalize_text(raw)
    assert norm == "dima hasao - assam"

