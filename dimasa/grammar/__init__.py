"""Dimasa Grammar Rules and Validation Engine."""

from .categories import GrammarCategory, CATEGORY_DESCRIPTIONS
from .engine import GrammarRulesEngine, get_grammar_rules_engine, grammar_rules
from .rules import GrammarRule
from .validator import ClauseValidator, ValidationDiagnostic, ValidationResult

__all__ = [
    "GrammarCategory",
    "CATEGORY_DESCRIPTIONS",
    "GrammarRule",
    "ClauseValidator",
    "ValidationDiagnostic",
    "ValidationResult",
    "GrammarRulesEngine",
    "get_grammar_rules_engine",
    "grammar_rules",
]

