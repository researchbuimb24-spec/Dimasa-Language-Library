"""Unit tests for Dimasa Numerals and Classifier System."""

import pytest
import dimasa


def test_num_to_words_1_to_10():
    assert dimasa.num_to_words(1) == "masi"
    assert dimasa.num_to_words(2) == "magin"
    assert dimasa.num_to_words(3) == "matham"
    assert dimasa.num_to_words(4) == "mabri"
    assert dimasa.num_to_words(5) == "mabowa"
    assert dimasa.num_to_words(6) == "madoh"
    assert dimasa.num_to_words(7) == "masini"
    assert dimasa.num_to_words(8) == "majai"
    assert dimasa.num_to_words(9) == "masukhu"
    assert dimasa.num_to_words(10) == "maji"


def test_num_to_words_higher_numbers():
    # 11
    assert dimasa.num_to_words(11) == "majise"
    # 20
    assert dimasa.num_to_words(20) == "bisasi"
    # 25
    assert dimasa.num_to_words(25) == "bisasi mabowa"
    # 30
    assert dimasa.num_to_words(30) == "mathimji"
    # 100
    assert dimasa.num_to_words(100) == "rausi"


def test_words_to_num():
    assert dimasa.words_to_num("masi") == 1
    assert dimasa.words_to_num("magin") == 2
    assert dimasa.words_to_num("matham") == 3
    assert dimasa.words_to_num("maji") == 10
    assert dimasa.words_to_num("majise") == 11
    assert dimasa.words_to_num("bisasi") == 20
    assert dimasa.words_to_num("bisasi mabowa") == 25
    assert dimasa.words_to_num("rausi") == 100


def test_apply_classifier_human():
    assert dimasa.apply_classifier(1, "sao") == "sao-si"
    assert dimasa.apply_classifier(2, "sao") == "sao-gin"
    assert dimasa.apply_classifier(3, "sao") == "sao-tham"

    # Indefinite syntax: Classifier-Numeral + Noun
    assert dimasa.apply_classifier(1, "sao", noun="subun", definite=False) == "sao-si subun"
    # Definite syntax: Noun + Classifier-Numeral
    assert dimasa.apply_classifier(1, "sao", noun="subun", definite=True) == "subun sao-si"


def test_apply_classifier_objects_and_animals():
    # Animal
    assert dimasa.apply_classifier(1, "ma", noun="sisa") == "ma-si sisa"

    # Long rigid object
    assert dimasa.apply_classifier(1, "gong", noun="repgon") == "gon-si repgon"

    # Tree
    assert dimasa.apply_classifier(1, "phang", noun="bongphang") == "phang-si bongphang"

    # Flat object
    assert dimasa.apply_classifier(1, "khang", noun="lekhabil") == "khang-si lekhabil"

    # Fruit
    assert dimasa.apply_classifier(1, "thai", noun="thaigir") == "thai-si thaigir"

    # Cattle head count
    assert dimasa.apply_classifier(1, "khoro", noun="mshou") == "khoro-si mshou"


def test_apply_classifier_unsupported():
    with pytest.raises(ValueError):
        dimasa.apply_classifier(2, "invented_fake_classifier")

