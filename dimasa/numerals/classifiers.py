"""Numeral classifiers and classifier syntax in Dimasa."""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

DATA_FILE = Path(__file__).parent.parent / "data" / "numerals.json"

CLASSIFIER_ROOTS: Dict[str, Dict[str, str]] = {
    "sao": {
        "1": "sao-si",
        "2": "sao-gin",
        "3": "sao-tham",
        "4": "sao-bri",
        "5": "sao-bowa",
        "6": "sao-doh",
        "7": "sao-sini",
        "8": "sao-jai",
        "9": "sao-sukhu",
        "10": "sao-ji",
    },
    "ma": {
        "1": "ma-si",
        "2": "ma-gin",
        "3": "ma-tham",
        "4": "ma-bri",
        "5": "ma-bowa",
        "6": "ma-doh",
        "7": "ma-sini",
        "8": "ma-jai",
        "9": "ma-sukhu",
        "10": "ma-ji",
    },
    "gong": {
        "1": "gon-si",
        "2": "gon-gin",
        "3": "gon-tham",
        "4": "gon-bri",
        "5": "gon-bowa",
        "6": "gon-doh",
        "7": "gon-sini",
        "8": "gon-jai",
        "9": "gon-sukhu",
        "10": "gon-ji",
    },
    "phang": {
        "1": "phang-si",
        "2": "phang-gin",
        "3": "phang-tham",
        "4": "phang-bri",
        "5": "phang-bowa",
        "6": "phang-doh",
        "7": "phang-sini",
        "8": "phang-jai",
        "9": "phang-sukhu",
        "10": "phang-ji",
    },
    "khang": {
        "1": "khang-si",
        "2": "khang-gin",
        "3": "khang-tham",
        "4": "khang-bri",
        "5": "khang-bowa",
        "6": "khang-doh",
        "7": "khang-sini",
        "8": "khang-jai",
        "9": "khang-sukhu",
        "10": "khang-ji",
    },
    "thai": {
        "1": "thai-si",
        "2": "thai-gin",
        "3": "thai-tham",
        "4": "thai-bri",
        "5": "thai-bowa",
        "6": "thai-doh",
        "7": "thai-sini",
        "8": "thai-jai",
        "9": "thai-sukhu",
        "10": "thai-ji",
    },
    "khoro": {
        "1": "khoro-si",
        "2": "khoro-gin",
        "3": "khoro-tham",
        "4": "khoro-bri",
        "5": "khoro-bowa",
        "6": "khoro-doh",
        "7": "khoro-sini",
        "8": "khoro-jai",
        "9": "khoro-sukhu",
        "10": "khoro-ji",
    },
}

# Alias mapping
CLASSIFIER_ALIASES: Dict[str, str] = {
    "gon": "gong",
    "human": "sao",
    "animal": "ma",
    "default": "ma",
    "tree": "phang",
    "plant": "phang",
    "flat": "khang",
    "leaf": "khang",
    "paper": "khang",
    "fruit": "thai",
    "round": "thai",
    "cattle": "khoro",
    "cow": "khoro",
}


def apply_classifier(count: int, classifier: str, noun: Optional[str] = None, definite: bool = False) -> str:
    """Apply an authentic numeral classifier to a count and optional noun.

    Parameters
    ----------
    count : int
        Number of entities (1 to 10+).
    classifier : str
        Classifier name or category:
        'sao' (human), 'ma' (animal/generic), 'gong' (long rigid),
        'phang' (trees), 'khang' (flat objects), 'thai' (fruits), 'khoro' (cattle).
    noun : Optional[str]
        Head noun being counted.
    definite : bool
        Syntactic word order:
        - False (Indefinite): Classifier-Numeral + Noun (e.g. 'sao-si subun')
        - True (Definite): Noun + Classifier-Numeral (e.g. 'subun sao-si')

    Returns
    -------
    str
        Formatted Dimasa classifier construction.
    """
    clean_clf = classifier.strip().lower()
    canonical_clf = CLASSIFIER_ALIASES.get(clean_clf, clean_clf)

    if canonical_clf not in CLASSIFIER_ROOTS:
        raise ValueError(
            f"Unsupported classifier: '{classifier}'. Supported Dimasa classifiers: "
            f"{list(CLASSIFIER_ROOTS.keys())}"
        )

    clf_table = CLASSIFIER_ROOTS[canonical_clf]
    str_count = str(count)

    if str_count in clf_table:
        clf_num_phrase = clf_table[str_count]
    else:
        # Fallback compounding for larger numbers: prefix + count
        prefix = "gon" if canonical_clf == "gong" else canonical_clf
        clf_num_phrase = f"{prefix}-{count}"

    if not noun:
        return clf_num_phrase

    clean_noun = noun.strip()
    if definite:
        # Definite: Noun + Classifier-Numeral
        return f"{clean_noun} {clf_num_phrase}"
    else:
        # Indefinite: Classifier-Numeral + Noun
        return f"{clf_num_phrase} {clean_noun}"


def list_classifiers() -> List[Dict[str, Any]]:
    """Return catalog of documented Dimasa classifiers."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f).get("classifiers", [])
    return []

