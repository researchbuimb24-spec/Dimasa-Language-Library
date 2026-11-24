"""Data model and loader for Dimasa linguistic corpus."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class CorpusSentence:
    """A parallel aligned sentence in the Dimasa corpus."""
    id: str
    dimasa: str
    english: str
    hindi: str
    bengali: str
    tokens: List[str] = field(default_factory=list)
    pos_tags: List[str] = field(default_factory=list)
    gloss: str = ""
    source_id: str = ""
    verification_status: str = "documented"
    genre: str = "general"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "dimasa": self.dimasa,
            "english": self.english,
            "hindi": self.hindi,
            "bengali": self.bengali,
            "tokens": self.tokens,
            "pos_tags": self.pos_tags,
            "gloss": self.gloss,
            "source_id": self.source_id,
            "verification_status": self.verification_status,
            "genre": self.genre,
        }

