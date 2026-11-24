"""Paradigm generator for verified Dimasa roots."""

from typing import Dict, List, Optional
from .conjugation import conjugate
from .declension import decline_noun, pluralize
from .roots import KNOWN_ROOTS


def generate_forms(root: str) -> Dict[str, str]:
    """Generate all attested morphological inflection forms for a Dimasa root.

    Parameters
    ----------
    root : str
        Dimasa root (verb, noun, or pronoun).

    Returns
    -------
    Dict[str, str]
        Dictionary mapping morphological categories to generated forms.
    """
    if not root:
        return {}

    clean = root.strip().lower()
    forms: Dict[str, str] = {"root": clean}

    # Determine part of speech
    pos = "unknown"
    if clean in KNOWN_ROOTS:
        pos = KNOWN_ROOTS[clean]["pos"]

    # If verb (or assumed verb)
    if pos in ("verb", "unknown"):
        try:
            forms["present"] = conjugate(clean, tense="present")
            forms["past"] = conjugate(clean, tense="past")
            forms["perfective"] = conjugate(clean, tense="perfective")
            forms["future"] = conjugate(clean, tense="future")
            forms["imperative"] = conjugate(clean, tense="imperative")
            forms["prohibitive"] = conjugate(clean, tense="imperative", negative=True)
            forms["negative"] = conjugate(clean, tense="present", negative=True)
            forms["causative"] = conjugate(clean, tense="present", causative=True)
        except Exception:
            pass

    # If noun or pronoun
    if pos in ("noun", "pronoun", "unknown"):
        try:
            forms["nominative"] = decline_noun(clean, case="nominative")
            forms["accusative"] = decline_noun(clean, case="accusative")
            forms["genitive"] = decline_noun(clean, case="genitive")
            forms["dative"] = decline_noun(clean, case="dative")
            forms["locative"] = decline_noun(clean, case="locative")
            forms["ablative"] = decline_noun(clean, case="ablative")
            forms["instrumental"] = decline_noun(clean, case="instrumental")
            forms["comitative"] = decline_noun(clean, case="comitative")
            forms["plural"] = pluralize(clean)
        except Exception:
            pass

    return forms

