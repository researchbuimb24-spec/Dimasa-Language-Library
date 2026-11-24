"""Cardinal numbers and conversion between digits and Dimasa words."""

import json
from pathlib import Path
from typing import Dict, Optional

DATA_FILE = Path(__file__).parent.parent / "data" / "numerals.json"

# Base numerals
NUMERAL_WORDS_1_TO_10: Dict[int, str] = {
    1: "masi",
    2: "magin",
    3: "matham",
    4: "mabri",
    5: "mabowa",
    6: "madoh",
    7: "masini",
    8: "majai",
    9: "masukhu",
    10: "maji",
}

NUMERAL_ROOTS: Dict[int, str] = {
    1: "si",
    2: "gin",
    3: "tham",
    4: "bri",
    5: "bowa",
    6: "doh",
    7: "sini",
    8: "jai",
    9: "sukhu",
    10: "ji",
}

WORDS_TO_NUMERAL: Dict[str, int] = {
    "masi": 1,
    "isi": 1,
    "si": 1,
    "magin": 2,
    "gni": 2,
    "gin": 2,
    "magni": 2,
    "matham": 3,
    "magtham": 3,
    "gatham": 3,
    "tham": 3,
    "mabri": 4,
    "bdiri": 4,
    "bri": 4,
    "mabowa": 5,
    "banga": 5,
    "bowa": 5,
    "madoh": 6,
    "doh": 6,
    "masini": 7,
    "sini": 7,
    "majai": 8,
    "jaji": 8,
    "jai": 8,
    "masukhu": 9,
    "masikhi": 9,
    "sukhu": 9,
    "maji": 10,
    "ji": 10,
    "majise": 11,
    "majigin": 12,
    "majitham": 13,
    "majibri": 14,
    "majibowa": 15,
    "majidoh": 16,
    "majisini": 17,
    "majijai": 18,
    "majisukhu": 19,
    "bisasi": 20,
    "makhon": 20,
    "mathimji": 30,
    "mabriji": 40,
    "mabowaji": 50,
    "madohji": 60,
    "masiniji": 70,
    "majaiji": 80,
    "masukhuji": 90,
    "rausi": 100,
    "sa-si": 100,
}


def num_to_words(number: int) -> str:
    """Convert an integer into its authentic Dimasa numeral word.

    Parameters
    ----------
    number : int
        Integer from 1 to 100+.

    Returns
    -------
    str
        Dimasa numeral phrase.
    """
    if not isinstance(number, int) or number < 1:
        raise ValueError("Number must be a positive integer >= 1.")

    # 1. Direct table lookup
    if number in NUMERAL_WORDS_1_TO_10:
        return NUMERAL_WORDS_1_TO_10[number]

    # 2. Teens (11 to 19): majise, majigin, ...
    if 11 <= number <= 19:
        unit = number - 10
        if unit == 1:
            return "majise"
        unit_root = NUMERAL_ROOTS[unit]
        return f"maji{unit_root}"

    # 3. Exact decades
    decades = {
        20: "bisasi",
        30: "mathimji",
        40: "mabriji",
        50: "mabowaji",
        60: "madohji",
        70: "masiniji",
        80: "majaiji",
        90: "masukhuji",
        100: "rausi",
    }
    if number in decades:
        return decades[number]

    # 4. Composite numbers 21-99
    if 21 <= number <= 99:
        tens = (number // 10) * 10
        unit = number % 10
        tens_word = decades.get(tens, f"{num_to_words(tens // 10)}ji")
        unit_word = NUMERAL_WORDS_1_TO_10[unit]
        return f"{tens_word} {unit_word}"

    if number == 100:
        return "rausi"

    # Beyond 100: rausi + remainder
    if 101 <= number <= 199:
        rem = number - 100
        return f"rausi {num_to_words(rem)}"

    hundreds = number // 100
    rem = number % 100
    base = f"rau-{NUMERAL_ROOTS.get(hundreds, str(hundreds))}"
    if rem == 0:
        return base
    return f"{base} {num_to_words(rem)}"


def words_to_num(words: str) -> int:
    """Convert a Dimasa numeral word into an integer."""
    if not words or not isinstance(words, str):
        raise ValueError("Words must be a valid non-empty string.")

    clean = words.strip().lower()

    if clean in WORDS_TO_NUMERAL:
        return WORDS_TO_NUMERAL[clean]

    # Multi-word composite (e.g. "bisasi mabowa")
    parts = clean.split()
    if len(parts) == 2:
        part1, part2 = parts[0], parts[1]
        val1 = WORDS_TO_NUMERAL.get(part1, 0)
        val2 = WORDS_TO_NUMERAL.get(part2, 0)
        if val1 and val2:
            return val1 + val2

    raise ValueError(f"Unable to parse Dimasa numeral word: '{words}'.")

