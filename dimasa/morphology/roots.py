"""Attested morphological roots for Dimasa."""

from typing import Dict, List, Optional, Set

# Known and verified Dimasa roots with part of speech
KNOWN_ROOTS: Dict[str, Dict[str, str]] = {
    # Verbs
    "zi": {"pos": "verb", "meaning": "eat", "source": "SRC-EVANS-2024"},
    "lung": {"pos": "verb", "meaning": "drink", "source": "SRC-EVANS-2024"},
    "thang": {"pos": "verb", "meaning": "go", "source": "SRC-EVANS-2024"},
    "phai": {"pos": "verb", "meaning": "come", "source": "SRC-EVANS-2024"},
    "nu": {"pos": "verb", "meaning": "see", "source": "SRC-EVANS-2024"},
    "thu": {"pos": "verb", "meaning": "sleep", "source": "SRC-EVANS-2024"},
    "ri": {"pos": "verb", "meaning": "give", "source": "SRC-EVANS-2024"},
    "la": {"pos": "verb", "meaning": "take", "source": "SRC-EVANS-2024"},
    "klai": {"pos": "verb", "meaning": "do / fall", "source": "SRC-EVANS-2024"},
    "solob": {"pos": "verb", "meaning": "learn / study", "source": "SRC-EVANS-2024"},
    "mosho": {"pos": "verb", "meaning": "dance", "source": "SRC-BARUA-1980"},
    "rjab": {"pos": "verb", "meaning": "sing", "source": "SRC-BARUA-1980"},
    "ran": {"pos": "verb", "meaning": "dry", "source": "SRC-SINGHA-2010"},
    "da": {"pos": "verb", "meaning": "weave", "source": "SRC-VKIC-2005"},
    "kham": {"pos": "verb", "meaning": "burn", "source": "SRC-EVANS-2024"},
    "kat": {"pos": "verb", "meaning": "run", "source": "SRC-EVANS-2024"},
    "bir": {"pos": "verb", "meaning": "fly", "source": "SRC-EVANS-2024"},
    "son": {"pos": "verb", "meaning": "cook", "source": "SRC-DUNDAS-1908"},
    "su": {"pos": "verb", "meaning": "wash", "source": "SRC-EVANS-2024"},
    "ling": {"pos": "verb", "meaning": "call", "source": "SRC-EVANS-2024"},
    "dong": {"pos": "verb", "meaning": "exist", "source": "SRC-EVANS-2024"},
    "giri": {"pos": "verb", "meaning": "not exist", "source": "SRC-EVANS-2024"},

    # Nouns
    "di": {"pos": "noun", "meaning": "water / river", "source": "SRC-EVANS-2024"},
    "noh": {"pos": "noun", "meaning": "house", "source": "SRC-EVANS-2024"},
    "san": {"pos": "noun", "meaning": "sun / day", "source": "SRC-EVANS-2024"},
    "hor": {"pos": "noun", "meaning": "night", "source": "SRC-DUNDAS-1908"},
    "dain": {"pos": "noun", "meaning": "moon / month", "source": "SRC-SINGHA-2010"},
    "wai": {"pos": "noun", "meaning": "fire", "source": "SRC-EVANS-2024"},
    "ha": {"pos": "noun", "meaning": "earth / land", "source": "SRC-EVANS-2024"},
    "mai": {"pos": "noun", "meaning": "rice / paddy", "source": "SRC-EVANS-2024"},
    "dao": {"pos": "noun", "meaning": "bird / fowl", "source": "SRC-EVANS-2024"},
    "sisa": {"pos": "noun", "meaning": "dog", "source": "SRC-EVANS-2024"},
    "alu": {"pos": "noun", "meaning": "cat", "source": "SRC-SINGHA-2010"},
    "na": {"pos": "noun", "meaning": "fish", "source": "SRC-EVANS-2024"},
    "subun": {"pos": "noun", "meaning": "person / human", "source": "SRC-EVANS-2024"},
    "ai": {"pos": "noun", "meaning": "mother", "source": "SRC-DUNDAS-1908"},
    "pha": {"pos": "noun", "meaning": "father", "source": "SRC-EVANS-2024"},
    "sa": {"pos": "noun", "meaning": "child / son", "source": "SRC-EVANS-2024"},
    "grao": {"pos": "noun", "meaning": "word / speech", "source": "SRC-EVANS-2024"},
    "khoro": {"pos": "noun", "meaning": "head", "source": "SRC-EVANS-2024"},
    "khur": {"pos": "noun", "meaning": "hand", "source": "SRC-EVANS-2024"},
    "ya": {"pos": "noun", "meaning": "leg / foot", "source": "SRC-EVANS-2024"},
    "dikhor": {"pos": "noun", "meaning": "eye", "source": "SRC-SINGHA-2010"},
    "tai": {"pos": "noun", "meaning": "stone", "source": "SRC-DUNDAS-1908"},
    "rigu": {"pos": "noun", "meaning": "Dimasa skirt", "source": "SRC-VKIC-2005"},
    "rikhaosa": {"pos": "noun", "meaning": "Dimasa shawl", "source": "SRC-VKIC-2005"},
    "bushu": {"pos": "noun", "meaning": "festival", "source": "SRC-THAOSEN-1964"},
    "judima": {"pos": "noun", "meaning": "rice wine", "source": "SRC-VKIC-2005"},

    # Pronouns
    "ang": {"pos": "pronoun", "meaning": "1SG (I)", "source": "SRC-EVANS-2024"},
    "ching": {"pos": "pronoun", "meaning": "1PL (we)", "source": "SRC-EVANS-2024"},
    "ning": {"pos": "pronoun", "meaning": "2SG (you)", "source": "SRC-EVANS-2024"},
    "nisi": {"pos": "pronoun", "meaning": "2PL (you all)", "source": "SRC-EVANS-2024"},
    "bo": {"pos": "pronoun", "meaning": "3SG (he/she)", "source": "SRC-EVANS-2024"},
    "bosi": {"pos": "pronoun", "meaning": "3PL (they)", "source": "SRC-EVANS-2024"},

    # Stative / Adjectives
    "ham": {"pos": "adjective", "meaning": "good", "source": "SRC-EVANS-2024"},
    "dain_adj": {"pos": "adjective", "meaning": "new", "source": "SRC-EVANS-2024"},
    "som": {"pos": "adjective", "meaning": "black", "source": "SRC-EVANS-2024"},
    "phu": {"pos": "adjective", "meaning": "white", "source": "SRC-EVANS-2024"},
    "jah": {"pos": "adjective", "meaning": "red", "source": "SRC-EVANS-2024"},
    "jao": {"pos": "adjective", "meaning": "long", "source": "SRC-SINGHA-2010"},
}

