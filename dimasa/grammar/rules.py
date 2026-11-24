"""Grammar rule data structures and loaders."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class GrammarRule:
    """A documented, authentic Dimasa grammatical rule with source attribution."""
    id: str
    name: str
    category: str
    description: str
    formula: str
    examples: List[Dict[str, str]] = field(default_factory=list)
    explanation: str = ""
    source_id: str = ""
    verification_status: str = "documented"

    def to_dict(self) -> Dict[str, Any]:
        """Convert rule to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "formula": self.formula,
            "examples": self.examples,
            "explanation": self.explanation,
            "source_id": self.source_id,
            "verification_status": self.verification_status,
        }

    def format_explanation(self) -> str:
        """Format rule into a human-readable explanation."""
        lines = [
            f"=== Rule {self.id}: {self.name} ===",
            f"Category: {self.category.title()} | Status: {self.verification_status}",
            f"Description: {self.description}",
            f"Formula / Pattern: {self.formula}",
            f"Source: {self.source_id}",
            "",
            "Authentic Dimasa Examples:",
        ]
        for ex in self.examples:
            dimasa = ex.get("dimasa", "")
            gloss = ex.get("gloss", "")
            tr = ex.get("translation", "")
            lines.append(f"  • {dimasa}")
            if gloss:
                lines.append(f"    Gloss: {gloss}")
            lines.append(f"    Translation: '{tr}'")
        if self.explanation:
            lines.extend(["", f"Linguistic Note: {self.explanation}"])
        return "\n".join(lines)

