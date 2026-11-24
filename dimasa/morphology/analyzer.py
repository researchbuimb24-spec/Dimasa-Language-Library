"""Morphological analysis and decomposition for Dimasa words."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from .roots import KNOWN_ROOTS


@dataclass
class MorphemeAnalysis:
    """Decomposition of a Dimasa word into constituent morphemes."""
    word: str
    root: str
    root_meaning: str
    part_of_speech: str
    prefixes: List[str] = field(default_factory=list)
    suffixes: List[str] = field(default_factory=list)
    grammatical_features: List[str] = field(default_factory=list)
    is_verified: bool = False

    def to_dict(self) -> Dict[str, Any]:
        """Convert analysis to dictionary."""
        return {
            "word": self.word,
            "root": self.root,
            "root_meaning": self.root_meaning,
            "part_of_speech": self.part_of_speech,
            "prefixes": self.prefixes,
            "suffixes": self.suffixes,
            "grammatical_features": self.grammatical_features,
            "is_verified": self.is_verified,
        }


def analyze_word(word: str) -> MorphemeAnalysis:
    """Analyze and decompose a Dimasa word into stem and grammatical morphemes."""
    if not word or not isinstance(word, str):
        return MorphemeAnalysis(
            word=str(word),
            root="",
            root_meaning="",
            part_of_speech="unknown",
            is_verified=False,
        )

    clean = word.strip().lower()
    prefixes: List[str] = []
    suffixes: List[str] = []
    features: List[str] = []

    # 1. Check for personal pronouns with morphophonemic velar nasal drop
    pronominal_forms = {
        "ani": ("ang", "pronoun", "my / mine", ["genitive"]),
        "ane": ("ang", "pronoun", "to me", ["dative"]),
        "anthane": ("ang", "pronoun", "to me", ["dative_extended"]),
        "nini": ("ning", "pronoun", "your / yours", ["genitive"]),
        "nine": ("ning", "pronoun", "to you", ["dative"]),
        "ninthane": ("ning", "pronoun", "to you", ["dative_extended"]),
        "chini": ("ching", "pronoun", "our / ours", ["genitive"]),
        "chine": ("ching", "pronoun", "to us", ["dative"]),
        "chinthane": ("ching", "pronoun", "to us", ["dative_extended"]),
        "boni": ("bo", "pronoun", "his / her", ["genitive"]),
        "bone": ("bo", "pronoun", "to him / her", ["dative"]),
        "bothane": ("bo", "pronoun", "to him / her", ["dative_extended"]),
        "bosini": ("bosi", "pronoun", "their / theirs", ["genitive"]),
        "bosine": ("bosi", "pronoun", "to them", ["dative"]),
    }
    if clean in pronominal_forms:
        root, pos, meaning, feats = pronominal_forms[clean]
        return MorphemeAnalysis(
            word=word,
            root=root,
            root_meaning=meaning,
            part_of_speech=pos,
            prefixes=[],
            suffixes=["-ni" if "genitive" in feats else "-ne"],
            grammatical_features=feats + ["velar_nasal_drop"],
            is_verified=True,
        )

    # 2. Check for prohibitive prefix da-
    stem = clean
    if stem.startswith("da-"):
        prefixes.append("da-")
        features.append("prohibitive")
        stem = stem[3:]
    elif stem.startswith("da") and len(stem) > 3 and stem not in ("daodi", "daosa", "daothu", "daphang"):
        # Check if remainder is known verb
        remainder = stem[2:]
        if remainder in KNOWN_ROOTS and KNOWN_ROOTS[remainder]["pos"] == "verb":
            prefixes.append("da-")
            features.append("prohibitive")
            stem = remainder

    # 3. Check for stative adjectival prefix g-
    if stem.startswith("g-") and len(stem) > 2:
        prefixes.append("g-")
        features.append("stative_prefix")
        stem = stem[2:]

    # 4. Strip recognized suffixes
    known_suffixes = [
        ("-niphang", "ablative", "noun"),
        ("-kadu", "perfective", "verb"),
        ("-jawa", "comitative", "noun"),
        ("-thane", "dative_extended", "noun"),
        ("-rao", "human_plural", "noun"),
        ("-shi", "instrumental", "noun"),
        ("-khe", "accusative", "noun"),
        ("-ke", "accusative", "noun"),
        ("-ha", "locative", "noun"),
        ("-ni", "genitive", "noun"),
        ("-ne", "dative", "noun"),
        ("-du", "present_continuous", "verb"),
        ("-ba", "past_imperfective", "verb"),
        ("-ma", "future_prospective", "verb"),
        ("-bo", "imperative", "verb"),
        ("-ja", "negative", "verb"),
        ("-ya", "negative", "verb"),
        ("-ri", "causative", "verb"),
        ("-na", "interrogative", "clausal"),
    ]

    changed = True
    while changed:
        changed = False
        for sfx, feat, pos_hint in known_suffixes:
            if stem.endswith(sfx):
                suffixes.insert(0, sfx)
                features.append(feat)
                stem = stem[:-len(sfx)]
                changed = True
                break

    # 5. Check if remaining stem is in KNOWN_ROOTS
    if stem in KNOWN_ROOTS:
        meta = KNOWN_ROOTS[stem]
        return MorphemeAnalysis(
            word=word,
            root=stem,
            root_meaning=meta["meaning"],
            part_of_speech=meta["pos"],
            prefixes=prefixes,
            suffixes=suffixes,
            grammatical_features=features,
            is_verified=True,
        )

    # 6. Fallback analysis
    return MorphemeAnalysis(
        word=word,
        root=stem,
        root_meaning="",
        part_of_speech="noun" if any(f in features for f in ("locative", "genitive", "accusative", "human_plural")) else "verb" if any(f in features for f in ("present_continuous", "past_imperfective", "imperative")) else "unknown",
        prefixes=prefixes,
        suffixes=suffixes,
        grammatical_features=features,
        is_verified=False,
    )


def morphological_roots(word: str) -> List[str]:
    """Extract candidate morphological roots from a word."""
    analysis = analyze_word(word)
    if analysis.root:
        return [analysis.root]
    return []

