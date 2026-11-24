"""Noun and pronoun declension for Dimasa case marking."""

from typing import Dict, List, Optional

# Supported case markers in Dimasa
CASE_SUFFIXES: Dict[str, str] = {
    "nominative": "",
    "accusative": "-khe",
    "genitive": "-ni",
    "dative": "-ne",
    "dative_extended": "-thane",
    "locative": "-ha",
    "ablative": "-niphang",
    "instrumental": "-shi",
    "comitative": "-jawa",
}

# Special morphophonemic declension for personal pronouns
PRONOUN_DECLENSIONS: Dict[str, Dict[str, str]] = {
    "ang": {
        "nominative": "ang",
        "accusative": "ang-khe",
        "genitive": "ani",        # velar nasal drop: ang + ni -> ani
        "dative": "ane",          # ang + ne -> ane
        "dative_extended": "anthane",  # ang + thane -> anthane
        "locative": "ang-ha",
        "ablative": "ani-niphang",
        "instrumental": "ang-shi",
        "comitative": "ang-jawa",
        "plural": "ching",
    },
    "ching": {
        "nominative": "ching",
        "accusative": "ching-khe",
        "genitive": "chini",      # ching + ni -> chini
        "dative": "chine",        # ching + ne -> chine
        "dative_extended": "chinthane",
        "locative": "ching-ha",
        "ablative": "chini-niphang",
        "instrumental": "ching-shi",
        "comitative": "ching-jawa",
        "plural": "ching",
    },
    "ning": {
        "nominative": "ning",
        "accusative": "ning-khe",
        "genitive": "nini",       # ning + ni -> nini
        "dative": "nine",         # ning + ne -> nine
        "dative_extended": "ninthane",
        "locative": "ning-ha",
        "ablative": "nini-niphang",
        "instrumental": "ning-shi",
        "comitative": "ning-jawa",
        "plural": "nisi",
    },
    "nisi": {
        "nominative": "nisi",
        "accusative": "nisi-khe",
        "genitive": "nisini",
        "dative": "nisine",
        "dative_extended": "nisithane",
        "locative": "nisi-ha",
        "ablative": "nisi-niphang",
        "instrumental": "nisi-shi",
        "comitative": "nisi-jawa",
        "plural": "nisi",
    },
    "bo": {
        "nominative": "bo",
        "accusative": "bo-khe",
        "genitive": "boni",
        "dative": "bone",
        "dative_extended": "bothane",
        "locative": "bo-ha",
        "ablative": "boni-niphang",
        "instrumental": "bo-shi",
        "comitative": "bo-jawa",
        "plural": "bosi",
    },
    "bosi": {
        "nominative": "bosi",
        "accusative": "bosi-khe",
        "genitive": "bosini",
        "dative": "bosine",
        "dative_extended": "bosithane",
        "locative": "bosi-ha",
        "ablative": "bosi-niphang",
        "instrumental": "bosi-shi",
        "comitative": "bosi-jawa",
        "plural": "bosi-rao",
    },
}


def decline_noun(noun: str, case: str = "genitive") -> str:
    """Decline a Dimasa noun or pronoun into the specified case.

    Parameters
    ----------
    noun : str
        Base noun or personal pronoun.
    case : str
        Target grammatical case:
        'nominative', 'accusative', 'genitive', 'dative',
        'locative', 'ablative', 'instrumental', 'comitative'.

    Returns
    -------
    str
        Declined word form with authentic morphophonemics.
    """
    if not noun:
        return ""

    clean_noun = noun.strip().lower()
    case_clean = case.strip().lower()

    # 1. Check for personal pronouns with morphophonemic velar nasal drop
    if clean_noun in PRONOUN_DECLENSIONS:
        declension_table = PRONOUN_DECLENSIONS[clean_noun]
        if case_clean in declension_table:
            return declension_table[case_clean]
        if case_clean in ("dat", "indirect_object"):
            return declension_table["dative"]
        if case_clean in ("gen", "possessive"):
            return declension_table["genitive"]
        if case_clean in ("acc", "direct_object"):
            return declension_table["accusative"]
        if case_clean in ("loc", "location"):
            return declension_table["locative"]
        if case_clean in ("abl", "source"):
            return declension_table["ablative"]
        if case_clean in ("ins", "instrumental"):
            return declension_table["instrumental"]
        if case_clean in ("com", "comitative"):
            return declension_table["comitative"]

    # 2. General noun declension
    if case_clean in ("nominative", "nom", "absolutive"):
        return clean_noun

    if case_clean in ("accusative", "acc"):
        return f"{clean_noun}-khe"

    if case_clean in ("genitive", "gen", "possessive"):
        return f"{clean_noun}-ni"

    if case_clean in ("dative", "dat"):
        return f"{clean_noun}-ne"

    if case_clean in ("dative_extended", "recipient"):
        return f"{clean_noun}-thane"

    if case_clean in ("locative", "loc"):
        return f"{clean_noun}-ha"

    if case_clean in ("ablative", "abl"):
        return f"{clean_noun}-niphang"

    if case_clean in ("instrumental", "ins"):
        return f"{clean_noun}-shi"

    if case_clean in ("comitative", "com"):
        return f"{clean_noun}-jawa"

    # Unsupported case requested
    raise ValueError(
        f"Unsupported case: '{case}'. Supported Dimasa cases: "
        f"{list(CASE_SUFFIXES.keys())}"
    )


def pluralize(noun: str) -> str:
    """Generate the collective plural for a Dimasa noun or pronoun.

    Human nouns and pronouns take collective plural marker -rao or suppletive forms.
    Inanimate nouns are zero-marked in plural and rely on numeral classifiers.
    """
    if not noun:
        return ""

    clean = noun.strip().lower()

    # Pronominal suppletion
    if clean in PRONOUN_DECLENSIONS and "plural" in PRONOUN_DECLENSIONS[clean]:
        return PRONOUN_DECLENSIONS[clean]["plural"]

    # Human nouns taking collective suffix -rao
    human_nouns = {
        "subun", "mansi", "hinjaosa", "garosa", "damusa", "sengbra",
        "sikla", "sa", "bosa", "pha", "bopha", "ai", "lagao", "khunang"
    }

    if clean in human_nouns or clean.endswith("sa"):
        return f"{clean}-rao"

    # Default for animate/inanimate: attaches -rao or returns noun with classifier note
    return f"{clean}-rao"

