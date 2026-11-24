"""Bidirectional Roman <-> Bengali/Assamese script transliteration for Dimasa."""

import unicodedata
from typing import Dict, List, Tuple

# Mapping from Roman Digraphs and Letters to Bengali/Assamese graphemes
ROMAN_TO_BENGALI_CONSONANTS: List[Tuple[str, str]] = [
    ("kh", "খ"),
    ("ph", "ফ"),
    ("th", "থ"),
    ("ng", "ং"),
    ("sh", "শ"),
    ("k", "ক"),
    ("g", "গ"),
    ("p", "প"),
    ("b", "ব"),
    ("t", "ত"),
    ("d", "দ"),
    ("m", "ম"),
    ("n", "ন"),
    ("r", "র"),
    ("l", "ল"),
    ("s", "স"),
    ("z", "জ"),
    ("j", "জ"),
    ("h", "হ"),
    ("w", "ওয়"),
    ("y", "য়"),
]

ROMAN_TO_BENGALI_VOWELS_INITIAL: Dict[str, str] = {
    "ai": "আই",
    "ao": "আও",
    "a": "আ",
    "i": "ই",
    "u": "উ",
    "e": "এ",
    "o": "ও",
}

ROMAN_TO_BENGALI_VOWELS_MEDIAL: Dict[str, str] = {
    "ai": "াই",
    "ao": "াও",
    "a": "া",
    "i": "ি",
    "u": "ু",
    "e": "ে",
    "o": "ো",
}

BENGALI_TO_ROMAN_MAP: Dict[str, str] = {
    "ক": "k",
    "খ": "kh",
    "গ": "g",
    "ঘ": "gh",
    "ঙ": "ng",
    "ং": "ng",
    "চ": "ch",
    "ছ": "chh",
    "জ": "j",
    "ঝ": "jh",
    "ট": "t",
    "ঠ": "th",
    "ড": "d",
    "ঢ": "dh",
    "ত": "t",
    "থ": "th",
    "দ": "d",
    "ধ": "dh",
    "ন": "n",
    "প": "p",
    "ফ": "ph",
    "ব": "b",
    "ভ": "bh",
    "ম": "m",
    "য": "y",
    "য়": "y",
    "র": "r",
    "ল": "l",
    "শ": "sh",
    "ষ": "s",
    "স": "s",
    "হ": "h",
    "ড়": "r",
    "ঢ়": "rh",
    # Independent vowels
    "অ": "a",
    "আ": "a",
    "ই": "i",
    "ঈ": "i",
    "উ": "u",
    "ঊ": "u",
    "এ": "e",
    "ঐ": "ai",
    "ও": "o",
    "ঔ": "au",
    # Vowel signs (Matras)
    "া": "a",
    "ি": "i",
    "ী": "i",
    "ু": "u",
    "ূ": "u",
    "ে": "e",
    "ৈ": "ai",
    "ো": "o",
    "ৌ": "au",
    "্": "",  # Halant
    "।": ".",
}


# Documented Dimasa words with attested Eastern Nagari (Bengali/Assamese) script forms
DOCUMENTED_ROMAN_TO_BENGALI: Dict[str, str] = {
    "di": "দি",
    "dima": "দিমা",
    "disa": "দিসা",
    "dimasa": "দিমাসা",
    "noh": "নহ",
    "nohkhor": "নহখোর",
    "san": "সান",
    "hor": "হর",
    "dain": "দাইন",
    "wai": "ওয়াই",
    "ha": "হা",
    "hasao": "হাসাও",
    "hawar": "হাওয়ার",
    "bongphang": "বংফাং",
    "bil": "বিল",
    "kham": "খাম",
    "thaigir": "থাইগির",
    "mai": "মাই",
    "mairang": "মাইরাং",
    "sisa": "সিসা",
    "alu": "আলু",
    "dao": "দাও",
    "daosa": "দাওসা",
    "daodi": "দাওদি",
    "na": "না",
    "napham": "নাফাম",
    "judima": "জুদিমা",
    "bushu": "বুশু",
    "subun": "সুবুন",
    "ai": "আই",
    "pha": "ফা",
    "sa": "সা",
    "hinjaosa": "হিনজাওসা",
    "garosa": "গারওসা",
    "ang": "আং",
    "ching": "ছিং",
    "ning": "নিং",
    "nisi": "নিসি",
    "bo": "বো",
    "bosi": "বোসি",
    "zi": "জি",
    "lung": "লুং",
    "thang": "থাং",
    "phai": "ফাই",
    "nu": "নু",
    "thu": "থু",
    "ri": "রি",
    "la": "লা",
    "dong": "দং",
    "doŋ": "দং",
    "giri": "গিরি",
    "hamba": "হামবা",
    "hama": "হামা",
    "gdain": "গদাইন",
    "gazam": "গাজাম",
    "gphu": "গফু",
    "gsom": "গসোম",
    "gjah": "গজাহ",
    "gjao": "গজাও",
    "ma": "মা",
    "gbang": "গবাং",
    "sar": "সার",
    "tamah": "তামাহ",
    "baha": "বাহা",
    "baphai": "বাফাই",
    "bedehe": "বেদেহো",
    "nadinang": "নাদিনাং",
    "rigu": "রিগু",
    "rikhaosa": "রিখাওসা",
    "rigdo": "রিগদো",
    "rimsao": "রিমসাও",
    "sgaopha": "স্গাওফা",
    "khram": "খ্রাম",
    "muri": "মুরি",
    "khoro": "খোরো",
    "dikhor": "দিখোর",
    "khur": "খুর",
    "ya": "য়া",
    "lama": "লামা",
    "grao": "গ্রাও",
    "daikho": "দাইখো",
    "sengphong": "সেংফং",
    "julu": "জুলু",
    "khunang": "খুনাং",
    "gundru": "গুন্দ্রু",
    "habar": "হাবার",
    "nokhli": "নখলি",
    "mosho": "মশো",
    "rjab": "রজাব",
    "baidima": "বাইদিমা",
    "masi": "মাসি",
    "magin": "মাগিন",
    "matham": "মাথাম",
    "mabri": "মাব্রি",
    "mabowa": "মাবোয়া",
    "madoh": "মাদহ",
    "masini": "মাসিনি",
    "majai": "মাজাই",
    "masukhu": "মাসুখু",
    "maji": "মাজি",
    "majise": "মাজিসে",
    "bisasi": "বিসাসি",
    "mathimji": "মাথিমজি",
    "rausi": "রাওসি",
    "sao": "সাও",
    "gong": "গং",
    "phang": "ফাং",
    "khang": "খাং",
    "thai": "থাই",
    "lagao": "লাগাও",
    "haba": "হাবা",
    "daothu": "দাওথু",
    "mshou": "মশৌ",
    "misi": "মিসি",
    "mi": "মি",
    "haju": "হাজু",
    "solob": "সলব",
    "ran": "রান",
    "grun": "গ্রুন",
    "gji": "গজি",
    "klai": "কলাই",
    "tai": "তাই",
    "longtai": "লংতাই",
    "khun": "খুন",
    "da": "দা",
    "daphang": "দাফাং",
    "seng": "সেং",
    "dilib": "দিলিব",
    "khuneb": "খুনেব",
    "nodikhor": "নদিখোর",
    "sengbra": "সেংব্রা",
    "sikla": "সিকলা",
    "hangseu": "হাংসেরু",
    "sibarai": "সিবরাই",
    "khulum": "খুলুম",
    "khunthang": "খুনথাং",
    "repgon": "রেপগন",
    "lekhabil": "লেখা-বিল",
    "khurthao": "খুরথাও",
    "hambai": "হামবাই",
}

DOCUMENTED_BENGALI_TO_ROMAN: Dict[str, str] = {v: k for k, v in DOCUMENTED_ROMAN_TO_BENGALI.items()}


def to_bengali(text: str) -> str:
    """Transliterate Romanized Dimasa text into Bengali-Assamese script."""
    if not text:
        return ""

    words = text.split(" ")
    converted_words: List[str] = []

    for word in words:
        if not word:
            continue
        # Preserve punctuation
        clean_word = word
        prefix_punct = ""
        suffix_punct = ""
        while clean_word and not clean_word[0].isalnum():
            prefix_punct += clean_word[0]
            clean_word = clean_word[1:]
        while clean_word and not clean_word[-1].isalnum():
            suffix_punct = clean_word[-1] + suffix_punct
            clean_word = clean_word[:-1]

        if not clean_word:
            converted_words.append(word)
            continue

        # Check documented vocabulary first
        lower_cw = clean_word.lower()
        if lower_cw in DOCUMENTED_ROMAN_TO_BENGALI:
            converted_words.append(prefix_punct + DOCUMENTED_ROMAN_TO_BENGALI[lower_cw] + suffix_punct)
            continue

        parts = clean_word.split("-")
        converted_parts: List[str] = []
        for part in parts:
            if part.lower() in DOCUMENTED_ROMAN_TO_BENGALI:
                converted_parts.append(DOCUMENTED_ROMAN_TO_BENGALI[part.lower()])
            else:
                conv = _transliterate_part_to_bengali(part.lower())
                converted_parts.append(conv)

        converted_words.append(prefix_punct + "-".join(converted_parts) + suffix_punct)

    return " ".join(converted_words)


def _transliterate_part_to_bengali(part: str) -> str:
    """Transliterate a single lowercase segment into Bengali script."""
    if part in DOCUMENTED_ROMAN_TO_BENGALI:
        return DOCUMENTED_ROMAN_TO_BENGALI[part]

    i = 0
    n = len(part)
    out: List[str] = []
    prev_was_consonant = False

    while i < n:
        # Check diphthongs
        if i + 1 < n and part[i:i+2] in ("ai", "ao"):
            diph = part[i:i+2]
            if prev_was_consonant:
                out.append(ROMAN_TO_BENGALI_VOWELS_MEDIAL[diph])
            else:
                out.append(ROMAN_TO_BENGALI_VOWELS_INITIAL[diph])
            prev_was_consonant = False
            i += 2
            continue

        # Check digraph consonants
        matched_consonant = False
        for rom_c, ben_c in ROMAN_TO_BENGALI_CONSONANTS:
            if part.startswith(rom_c, i):
                out.append(ben_c)
                prev_was_consonant = True
                i += len(rom_c)
                matched_consonant = True
                break

        if matched_consonant:
            continue

        # Check single vowel
        ch = part[i]
        if ch in ROMAN_TO_BENGALI_VOWELS_INITIAL:
            if prev_was_consonant:
                out.append(ROMAN_TO_BENGALI_VOWELS_MEDIAL[ch])
            else:
                out.append(ROMAN_TO_BENGALI_VOWELS_INITIAL[ch])
            prev_was_consonant = False
            i += 1
            continue

        # Other characters
        out.append(ch)
        prev_was_consonant = False
        i += 1

    return "".join(out)


def to_roman(text: str) -> str:
    """Transliterate Bengali-Assamese Dimasa text into Romanized representation."""
    if not text:
        return ""

    words = text.split(" ")
    converted_words: List[str] = []

    for word in words:
        if not word:
            continue
        clean_word = word.strip(".,!?\"'-")
        if clean_word in DOCUMENTED_BENGALI_TO_ROMAN:
            # Re-attach punctuation
            converted = word.replace(clean_word, DOCUMENTED_BENGALI_TO_ROMAN[clean_word])
            converted_words.append(converted)
        else:
            # Fallback character by character
            chars: List[str] = []
            for ch in word:
                if ch in BENGALI_TO_ROMAN_MAP:
                    chars.append(BENGALI_TO_ROMAN_MAP[ch])
                else:
                    chars.append(ch)
            converted_words.append("".join(chars))

    return " ".join(converted_words)
