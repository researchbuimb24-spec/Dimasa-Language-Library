"""DIMASA: Comprehensive Python NLP, Linguistic & Cultural Preservation Library.

Preservation, documentation, computational processing, and digital revitalization
of the Dimasa language (Grao Dima / Dimasa Kachari, ISO 639-3: dis).
"""

from .__version__ import __author__, __license__, __version__

# Dictionary
from .dictionary import (
    DictionaryEntry,
    lookup,
    lookup_root,
    prefix_search,
    search,
)

# Grammar
from .grammar import (
    ClauseValidator,
    GrammarCategory,
    GrammarRule,
    GrammarRulesEngine,
    ValidationDiagnostic,
    ValidationResult,
    get_grammar_rules_engine,
    grammar_rules,
)

# Morphology
from .morphology import (
    MorphemeAnalysis,
    analyze_word,
    conjugate,
    decline_noun,
    generate_forms,
    morphological_roots,
    pluralize,
)

# Translation
from .translation import (
    TranslationEngine,
    TranslationResult,
    get_translation_engine,
    translate,
)

# Transliteration
from .transliteration import (
    detect_script,
    format_roman,
    normalize_text,
    to_bengali,
    to_roman,
)

# Phonology
from .phonology import (
    analyze_phonology,
    phonemes,
    syllabify,
    to_ipa,
)

# Numerals and Classifiers
from .numerals import (
    apply_classifier,
    list_classifiers,
    num_to_words,
    words_to_num,
)

# Cultural Heritage
from .culture import (
    check_marriage_compatibility,
    get_attire,
    get_dish,
    get_festival,
    get_instrument,
    get_julus,
    get_place,
    get_sengphongs,
    list_attire,
    list_authors,
    list_clans,
    list_daikhos,
    list_deities,
    list_dishes,
    list_fauna,
    list_festivals,
    list_flora,
    list_idioms,
    list_instruments,
    list_narratives,
    list_places,
    list_traditions,
)

# Books and Literature
from .books import (
    Book,
    BookCatalog,
    BookPage,
    get_book,
    get_catalog,
    list_books,
    search_books,
    total_books,
    total_pages,
    total_words,
)

# Linguistic Corpus
from . import corpus

# Sources and Statistics
from .sources import Source, SourceRegistry, get_source_registry
from .stats import stats

__all__ = [
    "__version__",
    "__author__",
    "__license__",
    # Dictionary
    "lookup",
    "lookup_root",
    "search",
    "prefix_search",
    "DictionaryEntry",
    # Grammar
    "grammar_rules",
    "get_grammar_rules_engine",
    "GrammarRulesEngine",
    "GrammarRule",
    "GrammarCategory",
    "ClauseValidator",
    "ValidationDiagnostic",
    "ValidationResult",
    # Morphology
    "analyze_word",
    "generate_forms",
    "conjugate",
    "pluralize",
    "decline_noun",
    "morphological_roots",
    "MorphemeAnalysis",
    # Translation
    "translate",
    "TranslationResult",
    "TranslationEngine",
    "get_translation_engine",
    # Transliteration
    "to_roman",
    "to_bengali",
    "normalize_text",
    "detect_script",
    "format_roman",
    # Phonology
    "phonemes",
    "syllabify",
    "to_ipa",
    "analyze_phonology",
    # Numerals
    "num_to_words",
    "words_to_num",
    "apply_classifier",
    "list_classifiers",
    # Culture
    "list_attire",
    "get_attire",
    "list_festivals",
    "get_festival",
    "list_clans",
    "get_sengphongs",
    "get_julus",
    "check_marriage_compatibility",
    "list_dishes",
    "get_dish",
    "list_idioms",
    "list_places",
    "get_place",
    "list_instruments",
    "get_instrument",
    "list_deities",
    "list_daikhos",
    "list_flora",
    "list_fauna",
    "list_narratives",
    "list_authors",
    "list_traditions",
    # Books
    "total_books",
    "total_pages",
    "total_words",
    "list_books",
    "get_book",
    "search_books",
    "Book",
    "BookPage",
    "BookCatalog",
    # Corpus
    "corpus",
    # Sources & Stats
    "stats",
    "get_source_registry",
    "SourceRegistry",
    "Source",
]

