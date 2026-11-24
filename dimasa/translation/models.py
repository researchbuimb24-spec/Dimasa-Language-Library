"""Data models for Dimasa translation subsystem."""

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class TranslationResult:
    """Result of a translation query with confidence and provenance."""
    text: str
    confidence: float
    sources: List[str] = field(default_factory=list)
    source_language: str = "english"
    target_language: str = "dimasa"
    method: str = "dictionary_phrase"
    notes: str = ""
    is_partial: bool = False
    untranslated_tokens: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Convert translation result to dictionary."""
        return {
            "text": self.text,
            "confidence": self.confidence,
            "sources": self.sources,
            "source_language": self.source_language,
            "target_language": self.target_language,
            "method": self.method,
            "notes": self.notes,
            "is_partial": self.is_partial,
            "untranslated_tokens": self.untranslated_tokens,
        }

    def __str__(self) -> str:
        return self.text

