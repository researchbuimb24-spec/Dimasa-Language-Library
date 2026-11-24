"""Grammar categories and metadata for Dimasa linguistic rules."""

from enum import Enum
from typing import Dict, List


class GrammarCategory(str, Enum):
    """Linguistic categories for Dimasa grammar rules."""
    PHONOLOGY = "phonology"
    PHONETICS = "phonetics"
    ORTHOGRAPHY = "orthography"
    MORPHOLOGY = "morphology"
    NOUN_FORMATION = "noun formation"
    PRONOUNS = "pronouns"
    CASE_MARKING = "case marking"
    VERB_MORPHOLOGY = "verb morphology"
    TENSE_AND_ASPECT = "tense and aspect"
    MOOD = "mood"
    NEGATION = "negation"
    SYNTAX = "syntax"
    SENTENCE_FORMATION = "sentence formation"
    QUESTIONS = "questions"
    REDUPLICATION = "reduplication"
    WORD_FORMATION = "word formation"
    NUMERALS_AND_CLASSIFIERS = "numerals and classifiers"


CATEGORY_DESCRIPTIONS: Dict[GrammarCategory, str] = {
    GrammarCategory.PHONOLOGY: "Vowel and consonant systems, phonotactic distributions, phoneme inventory",
    GrammarCategory.PHONETICS: "Acoustic realization, epenthetic transitions, sesquisyllabic structures",
    GrammarCategory.ORTHOGRAPHY: "Standard Roman orthography and historical Eastern Nagari representations",
    GrammarCategory.MORPHOLOGY: "Root structure, compounding, affixation, morphophonemic alternations",
    GrammarCategory.NOUN_FORMATION: "Compound nouns, nominal suffixes, gender and collective plural markers",
    GrammarCategory.PRONOUNS: "Personal, demonstrative, interrogative, and suppletive pronominal systems",
    GrammarCategory.CASE_MARKING: "Differential case marking, clitic postpositions (-ke, -ni, -ne, -ha, -niphang)",
    GrammarCategory.VERB_MORPHOLOGY: "Predicative roots, person/gender neutrality, verbal suffix slots",
    GrammarCategory.TENSE_AND_ASPECT: "Present imperfective (-du), past (-ba), perfective (-kadu), future (-ma)",
    GrammarCategory.MOOD: "Imperative directive (-bo), permissive, modal clitics",
    GrammarCategory.NEGATION: "Prohibitive prefix (da-), negative suffix (-ja), TAM neutralization, giri copula",
    GrammarCategory.SYNTAX: "Canonical SOV word order, head-final postpositional phrasing, clause chaining",
    GrammarCategory.SENTENCE_FORMATION: "Clause coordination, nominalization, embedded relative clauses",
    GrammarCategory.QUESTIONS: "Polar question marker (-na), wh-in-situ interrogative constructions",
    GrammarCategory.REDUPLICATION: "Complete and partial reduplication for aspectual intensification and state",
    GrammarCategory.WORD_FORMATION: "Stative adjectival prefixation (g-), nominal derivation from verbs",
    GrammarCategory.NUMERALS_AND_CLASSIFIERS: "Cardinal numbers, ordinal formation, and sortal classifiers (sao, gong, phang, khang, ma)",
}

