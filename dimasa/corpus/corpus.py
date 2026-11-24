"""Corpus search, frequency analysis, concordance, and statistics."""

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Optional
from .models import CorpusSentence
from .tokenizer import tokenize

CORPUS_FILE = Path(__file__).parent.parent / "data" / "corpus.json"


class CorpusManager:
    """Manages searchable parallel Dimasa linguistic corpus."""

    def __init__(self, data_file: Optional[Path] = None):
        if data_file is None:
            data_file = CORPUS_FILE
        self.data_file = Path(data_file)
        self.sentences: List[CorpusSentence] = []
        self.load()

    def load(self) -> None:
        """Load corpus sentences from json."""
        if not self.data_file.exists():
            return
        with open(self.data_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data.get("sentences", []):
                sent = CorpusSentence(
                    id=item["id"],
                    dimasa=item["dimasa"],
                    english=item.get("english", ""),
                    hindi=item.get("hindi", ""),
                    bengali=item.get("bengali", ""),
                    tokens=item.get("tokens", tokenize(item["dimasa"])),
                    pos_tags=item.get("pos_tags", []),
                    gloss=item.get("gloss", ""),
                    source_id=item.get("source_id", ""),
                    verification_status=item.get("verification_status", "documented"),
                    genre=item.get("genre", "general"),
                )
                self.sentences.append(sent)

    def search(self, query: str, limit: int = 20) -> List[CorpusSentence]:
        """Search parallel corpus across Dimasa, English, Hindi, or Bengali."""
        if not query:
            return self.sentences[:limit]

        clean = query.strip().lower()
        results: List[CorpusSentence] = []

        for s in self.sentences:
            if (
                clean in s.dimasa.lower()
                or clean in s.english.lower()
                or clean in s.hindi
                or clean in s.bengali
                or clean in s.gloss.lower()
            ):
                results.append(s)
                if len(results) >= limit:
                    break

        return results

    def word_frequency(self, top_n: int = 50) -> Dict[str, int]:
        """Compute word frequency distribution across the Dimasa corpus."""
        counter: Counter = Counter()
        for s in self.sentences:
            for token in s.tokens:
                clean_tok = token.strip().lower()
                # If hyphenated, count base stem
                base = clean_tok.split("-")[0]
                counter[base] += 1
                if clean_tok != base:
                    counter[clean_tok] += 1

        return dict(counter.most_common(top_n))

    def sentence_examples(self, word: str, limit: int = 10) -> List[Dict[str, str]]:
        """Find aligned sentence examples containing a target word."""
        if not word:
            return []

        clean = word.strip().lower()
        examples: List[Dict[str, str]] = []

        for s in self.sentences:
            matched = False
            # Check exact match on token base or full token
            for t in s.tokens:
                clean_t = t.lower().strip(".,!?\"'")
                base_t = clean_t.split("-")[0]
                if clean == base_t or clean == clean_t:
                    matched = True
                    break

            if not matched:
                # English word boundary matching
                pattern = r"\b" + re.escape(clean) + r"\b"
                if re.search(pattern, s.english, re.IGNORECASE):
                    matched = True

            if matched:
                examples.append({
                    "dimasa": s.dimasa,
                    "english": s.english,
                    "hindi": s.hindi,
                    "bengali": s.bengali,
                    "gloss": s.gloss,
                    "source": s.source_id,
                })
                if len(examples) >= limit:
                    break

        return examples

    def stats(self) -> Dict[str, Any]:
        """Return corpus metrics and statistics."""
        total_words = sum(len(s.tokens) for s in self.sentences)
        genres = Counter(s.genre for s in self.sentences)
        sources = Counter(s.source_id for s in self.sentences)

        return {
            "total_sentences": len(self.sentences),
            "total_tokens": total_words,
            "unique_tokens": len(self.word_frequency(top_n=1000)),
            "genres": dict(genres),
            "sources": dict(sources),
        }


# Singleton manager
_corpus_mgr: Optional[CorpusManager] = None


def get_corpus() -> CorpusManager:
    """Get or create singleton corpus manager."""
    global _corpus_mgr
    if _corpus_mgr is None:
        _corpus_mgr = CorpusManager()
    return _corpus_mgr
