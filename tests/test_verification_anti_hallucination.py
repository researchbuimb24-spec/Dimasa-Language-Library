"""Linguistic validation and anti-hallucination tests."""

import pytest
import dimasa
from dimasa.sources import get_source_registry


def test_anti_hallucination_stats_honesty():
    """Verify that dimasa.stats() returns actual counts, not inflated marketing numbers."""
    s = dimasa.stats()
    # Ensure no fabricated 500,000 entries
    assert s["total_dictionary_entries"] < 50000
    assert s["total_dictionary_entries"] >= 50
    assert s["verified_dictionary_entries"] > 0
    assert s["grammar_rules"] >= 20
    assert s["cultural_records"] >= 50
    assert s["books"] >= 3
    assert s["corpus_sentences"] >= 20
    assert s["source_references"] >= 10


def test_source_attribution_integrity():
    """Verify every registered source has an authentic bibliographic record."""
    registry = get_source_registry()
    sources = registry.list_sources()
    assert len(sources) >= 10
    source_ids = [src.id for src in sources]
    assert "SRC-EVANS-2024" in source_ids
    assert "SRC-DUNDAS-1908" in source_ids
    assert "SRC-SINGHA-2010" in source_ids
    assert "SRC-GRIERSON-1903" in source_ids

    for src in sources:
        assert src.title
        assert len(src.authors) > 0
        assert src.year > 1800
        assert src.reliability in ("primary_academic", "historical_attested", "community_authoritative", "standardizing_body", "primary_archive", "primary_ethnographic", "secondary_academic")


def test_no_kokborok_linguistic_leakage():
    """Verify Dimasa specific morphology is NOT copied from Kokborok.

    In Kokborok:
    - Present tense is often '-o' or '-wi tongo'
    - Past is '-kha'
    - Future is '-nai'
    In Dimasa:
    - Present imperfective is '-du'
    - Past non-future is '-ba'
    - Future is '-ma'
    """
    # 1. Past tense must be -ba, not Kokborok -kha
    past_form = dimasa.conjugate("thang", tense="past")
    assert past_form == "thang-ba"
    assert "kha" not in past_form

    # 2. Present tense must be -du, not Kokborok -o
    pres_form = dimasa.conjugate("thang", tense="present")
    assert pres_form == "thang-du"

    # 3. Future must be -ma, not Kokborok -nai
    fut_form = dimasa.conjugate("thang", tense="future")
    assert fut_form == "thang-ma"
    assert "nai" not in fut_form

    # 4. Prohibitive must be da-, not Kokborok ta-
    proh_form = dimasa.conjugate("thang", tense="imperative", negative=True)
    assert proh_form == "da-thang"
    assert proh_form != "ta-thang"


def test_unsupported_case_explicit_rejection():
    """Ensure that requesting unsupported cases raises an explicit error rather than inventing suffixes."""
    with pytest.raises(ValueError):
        dimasa.decline_noun("noh", case="fictional_unattested_case")

