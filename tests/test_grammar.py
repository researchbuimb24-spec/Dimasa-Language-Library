"""Unit tests for Dimasa Grammar Rules and Validation Engine."""

import pytest
import dimasa
from dimasa.grammar import GrammarCategory, get_grammar_rules_engine


def test_grammar_rules_retrieval():
    rules = dimasa.grammar_rules()
    assert len(rules) >= 20
    rule_ids = [r.id for r in rules]
    assert "PHON-01" in rule_ids
    assert "CASE-02" in rule_ids
    assert "TAM-01" in rule_ids
    assert "NEG-01" in rule_ids
    assert "SYNT-01" in rule_ids


def test_grammar_rules_engine_get():
    engine = dimasa.get_grammar_rules_engine()
    rule = engine.get("PHON-01")
    assert rule is not None
    assert rule.id == "PHON-01"
    assert rule.name == "Five Vowel System"
    assert rule.category == "phonology"
    assert "five" in rule.description.lower()
    assert rule.source_id == "SRC-EVANS-2024"

    # Case-insensitive ID lookup
    rule_lower = engine.get("phon-01")
    assert rule_lower is not None
    assert rule_lower.id == "PHON-01"


def test_grammar_rules_search():
    engine = dimasa.get_grammar_rules_engine()
    results = engine.search("phonology")
    assert len(results) >= 2
    for r in results:
        assert (
            "phonology" in r.category.lower()
            or "phonology" in r.description.lower()
            or "phonology" in r.name.lower()
        )


def test_grammar_rules_filter_by_category():
    engine = dimasa.get_grammar_rules_engine()
    case_rules = engine.list_rules(category="case marking")
    assert len(case_rules) >= 5
    for r in case_rules:
        assert r.category == "case marking"


def test_grammar_rule_explanation_format():
    engine = dimasa.get_grammar_rules_engine()
    explanation = engine.explain("CASE-02")
    assert "Accusative" in explanation
    assert "SRC-EVANS-2024" in explanation
    assert "Formula" in explanation


def test_clause_validation_sov_and_imperfective():
    engine = dimasa.get_grammar_rules_engine()
    diagnostics = engine.validate_clause("ang di lung-du")
    assert diagnostics.is_supported is True
    matched_ids = [r.id for r in diagnostics.identified_rules]
    assert "SYNT-01" in matched_ids   # SOV word order
    assert "TAM-01" in matched_ids    # -du imperfective


def test_clause_validation_prohibitive_negation():
    engine = dimasa.get_grammar_rules_engine()
    diag = engine.validate_clause("da-thang!")
    assert diag.is_supported is True
    matched_ids = [r.id for r in diag.identified_rules]
    assert "NEG-01" in matched_ids    # Prohibitive prefix da-


def test_clause_validation_negative_existential_giri():
    engine = dimasa.get_grammar_rules_engine()
    diag = engine.validate_clause("noh-ha di giri")
    assert diag.is_supported is True
    matched_ids = [r.id for r in diag.identified_rules]
    assert "NEG-04" in matched_ids    # Negative copula giri
    assert "CASE-05" in matched_ids   # Locative -ha


def test_clause_validation_pronominal_velar_drop():
    engine = dimasa.get_grammar_rules_engine()
    diag = engine.validate_clause("ani noh-ha bo doŋ")
    assert diag.is_supported is True
    matched_ids = [r.id for r in diag.identified_rules]
    assert "PRON-02" in matched_ids   # Velar nasal drop in 'ani'
    assert "CASE-03" in matched_ids   # Genitive possession


def test_clause_validation_unsupported_or_unknown():
    engine = dimasa.get_grammar_rules_engine()
    diag = engine.validate_clause("random string without known patterns")
    assert diag.is_supported is False
    assert len(diag.identified_rules) == 0

