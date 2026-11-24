"""Diagnostic validator for Dimasa grammatical clauses."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from .rules import GrammarRule


@dataclass
class ValidationDiagnostic:
    """A single diagnostic notice produced by clause validation."""
    rule_id: str
    rule_name: str
    severity: str  # 'info', 'matched', 'warning'
    message: str
    pattern_identified: str


@dataclass
class ValidationResult:
    """Grammatical clause analysis result."""
    clause: str
    tokens: List[str]
    identified_rules: List[GrammarRule]
    diagnostics: List[ValidationDiagnostic]
    is_supported: bool
    notes: str

    def to_dict(self) -> Dict[str, Any]:
        """Convert result to dictionary."""
        return {
            "clause": self.clause,
            "tokens": self.tokens,
            "identified_rules": [r.to_dict() for r in self.identified_rules],
            "diagnostics": [
                {
                    "rule_id": d.rule_id,
                    "rule_name": d.rule_name,
                    "severity": d.severity,
                    "message": d.message,
                    "pattern": d.pattern_identified,
                }
                for d in self.diagnostics
            ],
            "is_supported": self.is_supported,
            "notes": self.notes,
        }


class ClauseValidator:
    """Validates Dimasa clauses against implemented linguistic rules.

    Does not claim complete grammatical correctness; identifies supported
    patterns and transparently flags unsupported or unverified structures.
    """

    def __init__(self, rules_by_id: Dict[str, GrammarRule]):
        self.rules = rules_by_id

    def validate(self, clause: str) -> ValidationResult:
        """Analyze a Dimasa clause and return diagnostic results."""
        if not clause or not isinstance(clause, str):
            return ValidationResult(
                clause=str(clause),
                tokens=[],
                identified_rules=[],
                diagnostics=[],
                is_supported=False,
                notes="Empty or invalid clause provided.",
            )

        clean = clause.strip()
        tokens = [t.strip(".,!?\"'") for t in clean.split() if t.strip()]
        lower_tokens = [t.lower() for t in tokens]

        identified_rules: List[GrammarRule] = []
        diagnostics: List[ValidationDiagnostic] = []

        def add_match(rule_id: str, message: str, pattern: str) -> None:
            rule = self.rules.get(rule_id)
            if rule and rule not in identified_rules:
                identified_rules.append(rule)
            diagnostics.append(
                ValidationDiagnostic(
                    rule_id=rule_id,
                    rule_name=rule.name if rule else rule_id,
                    severity="matched",
                    message=message,
                    pattern_identified=pattern,
                )
            )

        # 1. Check for SOV basic pattern (Subject pronoun / noun ... Verb ending in -du, -ba, -ma, -bo, -ja, or copula)
        subject_pronouns = {"ang", "ching", "jing", "ning", "nisi", "nishi", "bo", "bosi", "bunshi"}
        verb_suffixes = ("-du", "-ba", "-ma", "-bo", "-ja", "-ya", "-kadu")
        copulas = {"doŋ", "dong", "giri"}

        has_subject = any(t in subject_pronouns for t in lower_tokens[:2])
        last_token = lower_tokens[-1] if lower_tokens else ""
        has_final_verb = (
            any(last_token.endswith(sfx) for sfx in verb_suffixes)
            or last_token in copulas
            or last_token.rstrip("?").endswith(("-na", "?"))
        )

        if has_subject and has_final_verb:
            add_match("SYNT-01", "Clause exhibits canonical head-final SOV structural alignment.", f"{lower_tokens[0]} ... {last_token}")

        # 2. Check for Prohibitive da-
        for t in lower_tokens:
            if t.startswith("da-") or (t.startswith("da") and len(t) > 3 and t not in ("daodi", "daosa", "daothu", "daphang")):
                add_match("NEG-01", f"Prohibitive prefix 'da-' identified in negative imperative token '{t}'.", t)

        # 3. Check for Negative suffix -ja / -ya
        for t in lower_tokens:
            if t.endswith(("-ja", "-ya")):
                add_match("NEG-02", f"Declarative negative suffix '-ja/-ya' identified on predicate '{t}'.", t)
                add_match("NEG-03", f"Tense-aspect neutralization rule applies: TAM suffix neutralized by negative polarity.", t)

        # 4. Check for Negative existential copula 'giri'
        if "giri" in lower_tokens:
            add_match("NEG-04", "Dedicated negative existential copula 'giri' identified (non-existence/absence).", "giri")

        # 5. Check for Present Imperfective -du
        for t in lower_tokens:
            if t.endswith("-du") or (t.endswith("du") and len(t) > 3):
                add_match("TAM-01", f"Present imperfective / continuous suffix '-du' identified on predicate '{t}'.", t)

        # 6. Check for Past non-future -ba
        for t in lower_tokens:
            if t.endswith("-ba"):
                add_match("TAM-02", f"Non-future past imperfective marker '-ba' identified on '{t}'.", t)

        # 7. Check for Future -ma
        for t in lower_tokens:
            if t.endswith("-ma") and t not in ("dima", "judima", "sikla"):
                add_match("TAM-04", f"Future prospective marker '-ma' identified on '{t}'.", t)

        # 8. Check for Imperative -bo
        for t in lower_tokens:
            if t.endswith("-bo") and t != "bo":
                add_match("MOOD-01", f"Imperative directive marker '-bo' identified on '{t}'.", t)

        # 9. Check for Accusative case -ke / -khe
        for t in lower_tokens:
            if t.endswith(("-ke", "-khe", "=ke", "=khe")):
                add_match("CASE-02", f"Accusative differential object marker '-ke/-khe' identified on '{t}'.", t)

        # 10. Check for Genitive case -ni and morphophonemic velar nasal drop
        for t in lower_tokens:
            if t in ("ani", "nini", "chini", "jini"):
                add_match("PRON-02", f"Morphophonemic velar nasal drop verified on pronominal genitive '{t}'.", t)
                add_match("CASE-03", f"Genitive possession marker '-ni' verified on '{t}'.", t)
            elif t.endswith("-ni"):
                add_match("CASE-03", f"Genitive marker '-ni' identified on '{t}'.", t)

        # 11. Check for Locative -ha
        for t in lower_tokens:
            if t.endswith("-ha") and t not in ("baha", "baraha", "hamba", "hama"):
                add_match("CASE-05", f"Locative case postposition '-ha' identified on '{t}'.", t)

        # 12. Check for Ablative -niphang / -nipra
        for t in lower_tokens:
            if "-niphang" in t or "-nipra" in t:
                add_match("CASE-06", f"Ablative source postposition '-niphang' identified on '{t}'.", t)

        # 13. Check for Interrogative polar -na
        for t in lower_tokens:
            if t.endswith(("-na", "-na?")):
                add_match("QUES-01", f"Polar interrogative enclitic '-na' identified on '{t}'.", t)

        # 14. Check for Wh-in-situ questions
        wh_words = {"sar", "sere", "tamah", "nadi", "baha", "baraha", "baphai", "bakhali", "bedehe", "nadinang"}
        for t in lower_tokens:
            if t in wh_words:
                add_match("QUES-02", f"Content question word '{t}' in in-situ syntactic position.", t)

        # 15. Check for Numeral Classifiers (sao-, gon-, phang-, khang-, ma-, thai-, khoro-)
        clf_prefixes = ("sao-", "gon-", "gong-", "phang-", "khang-", "ma-", "thai-", "khoro-")
        for t in lower_tokens:
            for pfx in clf_prefixes:
                if t.startswith(pfx):
                    if pfx == "sao-":
                        add_match("NUM-02", f"Human classifier 'sao-' identified in '{t}'.", t)
                    elif pfx in ("gon-", "gong-"):
                        add_match("NUM-03", f"Long/rigid classifier 'gong-' identified in '{t}'.", t)
                    elif pfx == "phang-":
                        add_match("NUM-04", f"Botanical classifier 'phang-' identified in '{t}'.", t)
                    elif pfx == "khang-":
                        add_match("NUM-05", f"Flat planar classifier 'khang-' identified in '{t}'.", t)
                    elif pfx == "ma-":
                        add_match("NUM-06", f"Default/animate classifier 'ma-' identified in '{t}'.", t)
                    add_match("NUM-01", f"Classifier-numeral construction verified on '{t}'.", t)
                    break

        # 16. Check for Human plural -rao
        for t in lower_tokens:
            if t.endswith("-rao"):
                add_match("NOUN-02", f"Human collective plural suffix '-rao' identified on '{t}'.", t)

        # Determine support status
        is_supported = len(identified_rules) > 0
        note = (
            f"Clause matched {len(identified_rules)} documented Dimasa grammar rule(s). "
            "Note: Rule validation confirms presence of documented patterns; "
            "it does not guarantee native idiomaticity beyond the implemented rule set."
        )

        return ValidationResult(
            clause=clause,
            tokens=tokens,
            identified_rules=identified_rules,
            diagnostics=diagnostics,
            is_supported=is_supported,
            notes=note,
        )

