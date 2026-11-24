"""Verb conjugation and verbal inflection for Dimasa."""

from typing import Dict, List, Optional

# Documented verbal suffixes
VERBAL_TAM_SUFFIXES: Dict[str, str] = {
    "present": "-du",              # Present imperfective / continuous
    "present_continuous": "-du",
    "past": "-ba",                 # Non-future past imperfective / narrative
    "past_imperfective": "-ba",
    "perfective": "-kadu",         # Past completive / perfective
    "future": "-ma",               # Future / prospective
    "future_prospective": "-ma",
    "imperative": "-bo",           # Affirmative command
}


def conjugate(verb: str, tense: str = "present", negative: bool = False, causative: bool = False) -> str:
    """Conjugate a Dimasa verb root into the requested tense/aspect/polarity.

    Parameters
    ----------
    verb : str
        Dimasa verbal root (e.g. 'thang', 'zi', 'lung', 'phai', 'nu', 'thu').
    tense : str
        Target tense/aspect: 'present', 'past', 'future', 'perfective', 'imperative'.
    negative : bool
        Whether to generate the negative form.
        Applies Dimasa tense-aspect neutralization under negation:
        - Negative declarative verbs neutralize TAM suffixes and take suffix -ja.
        - Negative imperative (prohibitive) takes prefix da-.
    causative : bool
        Whether to add causative valence suffix -ri (cause to X).

    Returns
    -------
    str
        Conjugated Dimasa verb form.
    """
    if not verb:
        return ""

    root = verb.strip().lower()

    # Strip existing hyphen if passed (e.g. "thang-du" -> "thang")
    if "-" in root:
        root = root.split("-")[0]

    # Apply causative derivation if requested
    stem = f"{root}-ri" if causative else root

    tense_clean = tense.strip().lower()

    # 1. Negative conjugation
    if negative:
        # Negative imperative -> Prohibitive prefix da-
        if tense_clean in ("imperative", "prohibitive", "command"):
            return f"da-{stem}"
        # Negative declarative -> Tense-aspect neutralized suffix -ja
        return f"{stem}-ja"

    # 2. Affirmative conjugation
    if tense_clean in ("present", "present_continuous", "imperfective"):
        return f"{stem}-du"

    if tense_clean in ("past", "past_imperfective", "preterite"):
        return f"{stem}-ba"

    if tense_clean in ("perfective", "past_perfective", "completive"):
        return f"{stem}-kadu"

    if tense_clean in ("future", "prospective"):
        return f"{stem}-ma"

    if tense_clean in ("imperative", "command"):
        return f"{stem}-bo"

    raise ValueError(
        f"Unsupported verbal tense/mood: '{tense}'. Supported: "
        f"{list(VERBAL_TAM_SUFFIXES.keys())}"
    )

