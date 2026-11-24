"""Engine for managing, searching, and validating Dimasa grammar rules."""

import json
from pathlib import Path
from typing import Dict, List, Optional
from .categories import GrammarCategory
from .rules import GrammarRule
from .validator import ClauseValidator, ValidationResult


class GrammarRulesEngine:
    """Engine storing, searching, explaining, and validating Dimasa grammar rules."""

    def __init__(self, data_file: Optional[Path] = None):
        if data_file is None:
            data_file = Path(__file__).parent.parent / "data" / "grammar_rules.json"
        self.data_file = Path(data_file)
        self._rules: Dict[str, GrammarRule] = {}
        self._validator: Optional[ClauseValidator] = None
        self.load()

    def load(self) -> None:
        """Load grammar rules from json."""
        if not self.data_file.exists():
            return

        with open(self.data_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data.get("rules", []):
                rule = GrammarRule(
                    id=item["id"],
                    name=item["name"],
                    category=item.get("category", "morphology"),
                    description=item.get("description", ""),
                    formula=item.get("formula", ""),
                    examples=item.get("examples", []),
                    explanation=item.get("explanation", ""),
                    source_id=item.get("source_id", ""),
                    verification_status=item.get("verification_status", "documented"),
                )
                self._rules[rule.id] = rule
        self._validator = ClauseValidator(self._rules)

    def get(self, rule_id: str) -> Optional[GrammarRule]:
        """Get rule by ID (e.g. 'PHON-01', 'CASE-02')."""
        if not rule_id:
            return None
        return self._rules.get(rule_id.strip().upper())

    def search(self, query: str) -> List[GrammarRule]:
        """Search rules by name, description, category, or ID keyword."""
        if not query:
            return list(self._rules.values())

        clean = query.strip().lower()
        results: List[GrammarRule] = []

        for rule in self._rules.values():
            if (
                clean in rule.id.lower()
                or clean in rule.name.lower()
                or clean in rule.category.lower()
                or clean in rule.description.lower()
                or clean in rule.formula.lower()
                or clean in rule.explanation.lower()
            ):
                results.append(rule)
        return results

    def list_rules(self, category: Optional[str] = None) -> List[GrammarRule]:
        """List all rules, optionally filtered by category."""
        if category is None:
            return list(self._rules.values())
        cat_clean = category.strip().lower()
        return [r for r in self._rules.values() if r.category.lower() == cat_clean]

    def validate_clause(self, clause: str) -> ValidationResult:
        """Analyze and validate a Dimasa sentence clause against documented rules."""
        if self._validator is None:
            self._validator = ClauseValidator(self._rules)
        return self._validator.validate(clause)

    def explain(self, rule_id: str) -> str:
        """Return formatted explanation of a grammar rule."""
        rule = self.get(rule_id)
        if not rule:
            return f"Rule '{rule_id}' is not documented in the Dimasa grammar rules engine."
        return rule.format_explanation()

    def __len__(self) -> int:
        return len(self._rules)


# Module singleton
_engine: Optional[GrammarRulesEngine] = None


def get_grammar_rules_engine() -> GrammarRulesEngine:
    """Get or create singleton grammar rules engine."""
    global _engine
    if _engine is None:
        _engine = GrammarRulesEngine()
    return _engine


def grammar_rules(category: Optional[str] = None) -> List[GrammarRule]:
    """Convenience function returning list of documented grammar rules."""
    return get_grammar_rules_engine().list_rules(category=category)

