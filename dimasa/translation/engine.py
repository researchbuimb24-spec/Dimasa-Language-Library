"""Translation engine orchestrating language pairs and fallback handling."""

import re
from typing import List, Optional
from ..corpus import get_corpus
from ..dictionary import lookup, search
from ..morphology import KNOWN_ROOTS, analyze_word
from .backends import check_corpus_and_phrases
from .models import TranslationResult


class TranslationEngine:
    """Multi-lingual translation engine supporting Dimasa, English, Hindi, and Bengali."""

    def __init__(self):
        pass

    def translate(self, text: str, source: str = "english", target: str = "dimasa") -> TranslationResult:
        """Translate text between Dimasa and English, Hindi, or Bengali.

        Parameters
        ----------
        text : str
            Input text to translate.
        source : str
            Source language ('english', 'dimasa', 'hindi', 'bengali').
        target : str
            Target language ('dimasa', 'english', 'hindi', 'bengali').

        Returns
        -------
        TranslationResult
            Translation output with confidence, sources, and provenance notes.
        """
        if not text or not isinstance(text, str):
            return TranslationResult(
                text="",
                confidence=0.0,
                sources=[],
                source_language=source,
                target_language=target,
                notes="Empty text provided.",
            )

        src = source.strip().lower()
        tgt = target.strip().lower()

        # Handle identical source and target
        if src == tgt:
            return TranslationResult(
                text=text,
                confidence=1.0,
                sources=[],
                source_language=src,
                target_language=tgt,
                notes="Source and target languages are identical.",
            )

        # 1. Check exact phrase or corpus match
        phrase_match = check_corpus_and_phrases(text, src, tgt)
        if phrase_match:
            return phrase_match

        # 2. Single-word dictionary lookup
        clean_word = text.strip().lower().rstrip(".,!?")
        if " " not in clean_word:
            dict_res = self._translate_single_word(clean_word, src, tgt)
            if dict_res:
                return dict_res

        # 3. Sentence token-level translation with SOV grammatical reordering
        return self._translate_clause(text, src, tgt)

    def _translate_single_word(self, word: str, src: str, tgt: str) -> Optional[TranslationResult]:
        """Translate single word using dictionary and morphology."""
        # Dimasa -> other
        if src == "dimasa":
            entry = lookup(word)
            if entry:
                tgt_text = getattr(entry, tgt, "")
                if tgt_text:
                    # Pick first definition if multiple separated by comma
                    primary = tgt_text.split(",")[0].strip()
                    return TranslationResult(
                        text=primary,
                        confidence=0.88,
                        sources=[entry.source_id],
                        source_language=src,
                        target_language=tgt,
                        method="dictionary_lookup",
                        notes=f"Lexical entry: {entry.headword} [{entry.part_of_speech}].",
                    )
            # Try morphological analysis
            analysis = analyze_word(word)
            if analysis.is_verified:
                entry = lookup(analysis.root)
                if entry:
                    tgt_text = getattr(entry, tgt, "")
                    if tgt_text:
                        primary = tgt_text.split(",")[0].strip()
                        return TranslationResult(
                            text=primary,
                            confidence=0.75,
                            sources=[entry.source_id],
                            source_language=src,
                            target_language=tgt,
                            method="morphological_root_lookup",
                            notes=f"Derived from root '{analysis.root}' ({', '.join(analysis.grammatical_features)}).",
                        )

        # other -> Dimasa
        if tgt == "dimasa":
            matches = search(word, language=src, limit=5)
            if matches:
                entry = matches[0]
                return TranslationResult(
                    text=entry.headword,
                    confidence=0.85,
                    sources=[entry.source_id],
                    source_language=src,
                    target_language=tgt,
                    method="dictionary_search",
                    notes=f"Dictionary headword match for '{word}'.",
                )

        return None

    def _translate_clause(self, clause: str, src: str, tgt: str) -> TranslationResult:
        """Translate clause token by token, reordering syntax where applicable."""
        tokens = clause.strip().split()
        translated_tokens: List[str] = []
        sources: List[str] = []
        untranslated: List[str] = []

        for tok in tokens:
            clean_tok = tok.strip(".,!?\"'").lower()
            res = self._translate_single_word(clean_tok, src, tgt)
            if res and res.text:
                translated_tokens.append(res.text)
                for s in res.sources:
                    if s not in sources:
                        sources.append(s)
            else:
                translated_tokens.append(f"[{tok}]")
                untranslated.append(tok)

        is_partial = len(untranslated) > 0
        conf = 0.50 if not is_partial else max(0.20, 0.50 - (len(untranslated) * 0.10))

        # Basic SVO to SOV word order reordering for English -> Dimasa (3-word simple clause)
        if src == "english" and tgt == "dimasa" and len(translated_tokens) == 3 and not is_partial:
            # S V O -> S O V
            s, v, o = translated_tokens[0], translated_tokens[1], translated_tokens[2]
            translated_tokens = [s, o, v]

        final_text = " ".join(translated_tokens)
        notes = (
            "Rule-based grammatical translation. "
            if not is_partial else
            f"Partial translation: {len(untranslated)} token(s) unverified or absent from lexicon."
        )

        return TranslationResult(
            text=final_text,
            confidence=round(conf, 2),
            sources=sources if sources else ["SRC-EVANS-2024"],
            source_language=src,
            target_language=tgt,
            method="grammar_aware_token_composition",
            notes=notes,
            is_partial=is_partial,
            untranslated_tokens=untranslated,
        )


# Singleton engine
_engine: Optional[TranslationEngine] = None


def get_translation_engine() -> TranslationEngine:
    """Get or create singleton translation engine."""
    global _engine
    if _engine is None:
        _engine = TranslationEngine()
    return _engine


def translate(text: str, source: str = "english", target: str = "dimasa") -> TranslationResult:
    """Convenience translation function."""
    return get_translation_engine().translate(text, source=source, target=target)

