"""Translation backends: phrase, morphological, and grammar-aware reordering."""

import re
from typing import List, Optional, Tuple
from ..corpus import get_corpus
from ..dictionary import lookup, search
from ..morphology import KNOWN_ROOTS, analyze_word, conjugate, decline_noun
from .models import TranslationResult

# High-frequency greeting / conversational phrases
PHRASE_TRANSLATIONS: List[dict] = [
    {
        "english": "hello",
        "dimasa": "khurthao",
        "hindi": "नमस्ते",
        "bengali": "নমস্কার",
        "source": "SRC-DSS-2018",
    },
    {
        "english": "greetings",
        "dimasa": "khurthao",
        "hindi": "नमस्कार",
        "bengali": "শুভেচ্ছা",
        "source": "SRC-DSS-2018",
    },
    {
        "english": "thank you",
        "dimasa": "hambai",
        "hindi": "धन्यवाद",
        "bengali": "ধন্যবাদ",
        "source": "SRC-DSS-2018",
    },
    {
        "english": "thanks",
        "dimasa": "hambai",
        "hindi": "शुक्रिया",
        "bengali": "ধন্যবাদ",
        "source": "SRC-DSS-2018",
    },
    {
        "english": "where are you going?",
        "dimasa": "ning baha thang-du?",
        "hindi": "तुम कहाँ जा रहे हो?",
        "bengali": "তুমি কোথায় যাচ্ছ?",
        "source": "SRC-EVANS-2024",
    },
    {
        "english": "i am drinking water.",
        "dimasa": "ang di lung-du.",
        "hindi": "मैं पानी पी रहा हूँ।",
        "bengali": "আমি জল খাচ্ছি।",
        "source": "SRC-EVANS-2024",
    },
    {
        "english": "give me water.",
        "dimasa": "ane di ri-bo.",
        "hindi": "मुझे पानी दो।",
        "bengali": "আমাকে জল দাও।",
        "source": "SRC-EVANS-2024",
    },
    {
        "english": "do not go!",
        "dimasa": "da-thang!",
        "hindi": "मत जाओ!",
        "bengali": "যেও না!",
        "source": "SRC-EVANS-2024",
    },
    {
        "english": "we are dimasa people.",
        "dimasa": "ching dimasa subun-rao doŋ.",
        "hindi": "हम दिमासा लोग हैं।",
        "bengali": "আমরা দিমাসা সম্প্রদায়ের মানুষ।",
        "source": "SRC-THAOSEN-1964",
    },
]


def check_corpus_and_phrases(text: str, source_lang: str, target_lang: str) -> Optional[TranslationResult]:
    """Check aligned corpus and phrasebook for exact matches."""
    clean = text.strip().lower()

    # 1. Check curated conversational phrasebook
    for p in PHRASE_TRANSLATIONS:
        src_val = p.get(source_lang, "").lower()
        if clean == src_val or clean.rstrip(".,!?") == src_val.rstrip(".,!?"):
            tgt_val = p.get(target_lang, "")
            if tgt_val:
                return TranslationResult(
                    text=tgt_val,
                    confidence=0.98,
                    sources=[p.get("source", "SRC-EVANS-2024")],
                    source_language=source_lang,
                    target_language=target_lang,
                    method="attested_phrasebook",
                    notes="Direct match from documented Dimasa conversational corpus.",
                    is_partial=False,
                )

    # 2. Check parallel corpus
    corpus = get_corpus()
    for s in corpus.sentences:
        src_val = getattr(s, source_lang, "").strip().lower()
        if clean == src_val or clean.rstrip(".,!?") == src_val.rstrip(".,!?"):
            tgt_val = getattr(s, target_lang, "")
            if tgt_val:
                return TranslationResult(
                    text=tgt_val,
                    confidence=0.95,
                    sources=[s.source_id],
                    source_language=source_lang,
                    target_language=target_lang,
                    method="parallel_corpus",
                    notes="Verified sentence match from aligned linguistic corpus.",
                    is_partial=False,
                )

    return None

