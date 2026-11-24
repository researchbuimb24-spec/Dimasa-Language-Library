"""Unit tests for Dimasa Morphology Subsystem."""

import pytest
import dimasa


def test_morphology_analyze_word():
    # Present imperfective verb
    m1 = dimasa.analyze_word("thang-du")
    assert m1.root == "thang"
    assert m1.part_of_speech == "verb"
    assert "-du" in m1.suffixes
    assert "present_continuous" in m1.grammatical_features
    assert m1.is_verified is True

    # Past non-future verb
    m2 = dimasa.analyze_word("zi-ba")
    assert m2.root == "zi"
    assert m2.part_of_speech == "verb"
    assert "-ba" in m2.suffixes
    assert "past_imperfective" in m2.grammatical_features

    # Negative imperative with prohibitive prefix
    m3 = dimasa.analyze_word("da-zi")
    assert m3.root == "zi"
    assert "da-" in m3.prefixes
    assert "prohibitive" in m3.grammatical_features

    # Human plural noun
    m4 = dimasa.analyze_word("subun-rao")
    assert m4.root == "subun"
    assert "-rao" in m4.suffixes
    assert "human_plural" in m4.grammatical_features


def test_morphology_pronominal_velar_nasal_drop():
    # 1SG genitive: ang + ni -> ani
    m1 = dimasa.analyze_word("ani")
    assert m1.root == "ang"
    assert "genitive" in m1.grammatical_features
    assert "velar_nasal_drop" in m1.grammatical_features

    # 2SG genitive: ning + ni -> nini
    m2 = dimasa.analyze_word("nini")
    assert m2.root == "ning"
    assert "genitive" in m2.grammatical_features

    # 1PL genitive: ching + ni -> chini
    m3 = dimasa.analyze_word("chini")
    assert m3.root == "ching"
    assert "genitive" in m3.grammatical_features


def test_morphology_conjugate_verb():
    # Present
    assert dimasa.conjugate("thang", tense="present") == "thang-du"
    # Past
    assert dimasa.conjugate("thang", tense="past") == "thang-ba"
    # Future
    assert dimasa.conjugate("thang", tense="future") == "thang-ma"
    # Imperative
    assert dimasa.conjugate("zi", tense="imperative") == "zi-bo"
    # Prohibitive (negative imperative)
    assert dimasa.conjugate("zi", tense="imperative", negative=True) == "da-zi"
    # Declarative negative with TAM neutralization
    assert dimasa.conjugate("zi", tense="present", negative=True) == "zi-ja"
    # Causative
    assert dimasa.conjugate("zi", tense="present", causative=True) == "zi-ri-du"


def test_morphology_decline_noun():
    # Regular nouns
    assert dimasa.decline_noun("noh", case="nominative") == "noh"
    assert dimasa.decline_noun("noh", case="locative") == "noh-ha"
    assert dimasa.decline_noun("noh", case="genitive") == "noh-ni"
    assert dimasa.decline_noun("noh", case="accusative") == "noh-khe"
    assert dimasa.decline_noun("noh", case="dative") == "noh-ne"
    assert dimasa.decline_noun("noh", case="ablative") == "noh-niphang"
    assert dimasa.decline_noun("seng", case="instrumental") == "seng-shi"

    # Pronoun with morphophonemic velar nasal drop
    assert dimasa.decline_noun("ang", case="genitive") == "ani"
    assert dimasa.decline_noun("ang", case="dative") == "ane"
    assert dimasa.decline_noun("ning", case="genitive") == "nini"
    assert dimasa.decline_noun("ching", case="genitive") == "chini"
    assert dimasa.decline_noun("bo", case="genitive") == "boni"


def test_morphology_pluralize():
    # Human nouns
    assert dimasa.pluralize("subun") == "subun-rao"
    assert dimasa.pluralize("hinjaosa") == "hinjaosa-rao"
    assert dimasa.pluralize("garosa") == "garosa-rao"

    # Pronouns
    assert dimasa.pluralize("ang") == "ching"
    assert dimasa.pluralize("ning") == "nisi"
    assert dimasa.pluralize("bo") == "bosi"


def test_morphology_generate_forms():
    forms = dimasa.generate_forms("thang")
    assert forms["root"] == "thang"
    assert forms["present"] == "thang-du"
    assert forms["past"] == "thang-ba"
    assert forms["future"] == "thang-ma"
    assert forms["prohibitive"] == "da-thang"
    assert forms["negative"] == "thang-ja"


def test_morphological_roots():
    roots = dimasa.morphological_roots("lung-du")
    assert "lung" in roots

