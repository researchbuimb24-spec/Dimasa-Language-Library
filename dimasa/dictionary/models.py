"""Data models for Dimasa multilingual dictionary."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class DictionaryEntry:
    """Multilingual dictionary entry with phonetic, morphological and source information."""
    headword: str
    english: str
    hindi: str
    bengali: str
    part_of_speech: str
    phonetic_ipa: str = ""
    romanized: str = ""
    bengali_script: str = ""
    example_sentence: str = ""
    example_translation: str = ""
    morphological_root: str = ""
    derived_forms: List[str] = field(default_factory=list)
    synonyms: List[str] = field(default_factory=list)
    antonyms: List[str] = field(default_factory=list)
    dialect: str = "general"
    source_id: str = ""
    verification_status: str = "documented"

    def to_dict(self) -> Dict[str, Any]:
        """Convert entry to dictionary."""
        return {
            "headword": self.headword,
            "english": self.english,
            "hindi": self.hindi,
            "bengali": self.bengali,
            "part_of_speech": self.part_of_speech,
            "phonetic_ipa": self.phonetic_ipa,
            "romanized": self.romanized,
            "bengali_script": self.bengali_script,
            "example_sentence": self.example_sentence,
            "example_translation": self.example_translation,
            "morphological_root": self.morphological_root,
            "derived_forms": self.derived_forms,
            "synonyms": self.synonyms,
            "antonyms": self.antonyms,
            "dialect": self.dialect,
            "source_id": self.source_id,
            "verification_status": self.verification_status,
        }

    def __str__(self) -> str:
        return f"{self.headword} [{self.part_of_speech}]: {self.english}"

