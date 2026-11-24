"""Indexing structures for fast O(1) dictionary retrieval and search."""

import json
from pathlib import Path
from typing import Dict, List, Optional, Set
from .models import DictionaryEntry


class DictionaryIndex:
    """In-memory multi-lingual index supporting exact and inverted search."""

    def __init__(self, data_file: Optional[Path] = None):
        if data_file is None:
            data_file = Path(__file__).parent.parent / "data" / "dictionary.json"
        self.data_file = Path(data_file)
        self.entries: List[DictionaryEntry] = []
        self.headword_map: Dict[str, DictionaryEntry] = {}
        self.english_index: Dict[str, List[DictionaryEntry]] = {}
        self.hindi_index: Dict[str, List[DictionaryEntry]] = {}
        self.bengali_index: Dict[str, List[DictionaryEntry]] = {}
        self.root_index: Dict[str, List[DictionaryEntry]] = {}
        self.bengali_script_map: Dict[str, DictionaryEntry] = {}
        self.load()

    def load(self) -> None:
        """Load entries from json and build indexes."""
        if not self.data_file.exists():
            return

        with open(self.data_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data.get("entries", []):
                entry = DictionaryEntry(
                    headword=item["headword"],
                    english=item["english"],
                    hindi=item.get("hindi", ""),
                    bengali=item.get("bengali", ""),
                    part_of_speech=item.get("part_of_speech", ""),
                    phonetic_ipa=item.get("phonetic_ipa", ""),
                    romanized=item.get("romanized", item["headword"]),
                    bengali_script=item.get("bengali_script", ""),
                    example_sentence=item.get("example_sentence", ""),
                    example_translation=item.get("example_translation", ""),
                    morphological_root=item.get("morphological_root", ""),
                    derived_forms=item.get("derived_forms", []),
                    synonyms=item.get("synonyms", []),
                    antonyms=item.get("antonyms", []),
                    dialect=item.get("dialect", "general"),
                    source_id=item.get("source_id", ""),
                    verification_status=item.get("verification_status", "documented"),
                )
                self.entries.append(entry)

                # Headword index (exact and normalized lowercase)
                clean_hw = entry.headword.lower().strip()
                self.headword_map[clean_hw] = entry
                if entry.bengali_script:
                    self.bengali_script_map[entry.bengali_script.strip()] = entry

                # Derived forms indexing
                for df in entry.derived_forms:
                    df_clean = df.lower().strip()
                    if df_clean not in self.headword_map:
                        self.headword_map[df_clean] = entry

                # Root index
                if entry.morphological_root:
                    root_clean = entry.morphological_root.lower().strip()
                    self.root_index.setdefault(root_clean, []).append(entry)

                # Multilingual inverted word index
                self._index_text(entry.english, self.english_index, entry)
                self._index_text(entry.hindi, self.hindi_index, entry)
                self._index_text(entry.bengali, self.bengali_index, entry)

    def _index_text(self, text: str, target_index: Dict[str, List[DictionaryEntry]], entry: DictionaryEntry) -> None:
        """Tokenize and populate target inverted index."""
        if not text:
            return
        delimiters = [",", ";", "/", "(", ")", ".", "!", "?", " "]
        clean = text.lower()
        for d in delimiters:
            clean = clean.replace(d, " ")
        tokens = [t.strip() for t in clean.split() if t.strip()]
        for token in tokens:
            if entry not in target_index.setdefault(token, []):
                target_index[token].append(entry)

    def __len__(self) -> int:
        return len(self.entries)


# Singleton dictionary index
_dict_index: Optional[DictionaryIndex] = None


def get_index() -> DictionaryIndex:
    """Get or create singleton dictionary index."""
    global _dict_index
    if _dict_index is None:
        _dict_index = DictionaryIndex()
    return _dict_index

