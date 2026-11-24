"""Command-line interface for the Dimasa linguistic library."""

import json
import click
from .. import __version__
from ..books import get_book, list_books, search_books, total_books, total_pages, total_words
from ..corpus import get_corpus
from ..culture import (
    check_marriage_compatibility,
    get_dish,
    get_festival,
    get_place,
    list_attire,
    list_clans,
    list_dishes,
    list_festivals,
    list_instruments,
    list_places,
)
from ..dictionary import lookup, search
from ..grammar import get_grammar_rules_engine, grammar_rules
from ..morphology import analyze_word, conjugate, decline_noun, generate_forms, pluralize
from ..numerals import apply_classifier, num_to_words, words_to_num
from ..phonology import analyze_phonology, phonemes, syllabify, to_ipa
from ..stats import stats
from ..translation import translate
from ..transliteration import detect_script, normalize_text, to_bengali, to_roman


@click.group()
@click.version_option(__version__, prog_name="dimasa")
def cli():
    """Dimasa: Computational Linguistics & Cultural Preservation Library."""
    pass


@cli.command("stats")
def cmd_stats():
    """Display honest dataset statistics and rule verification counts."""
    s = stats()
    click.echo("\n=======================================================")
    click.echo("  DIMASA LINGUISTIC & DIGITAL PRESERVATION STATISTICS  ")
    click.echo("=======================================================")
    click.echo(f"  Verified Dictionary Entries:     {s['verified_dictionary_entries']}")
    click.echo(f"  Provisional Dictionary Entries:  {s['provisionally_documented_entries']}")
    click.echo(f"  Total Dictionary Entries:        {s['total_dictionary_entries']}")
    click.echo(f"  Documented Grammar Rules:        {s['grammar_rules']}")
    click.echo(f"  Morphological Rules Implemented: {s['morphological_rules']}")
    click.echo(f"  Cultural Heritage Records:       {s['cultural_records']}")
    click.echo(f"  Digitized Books:                 {s['books']}")
    click.echo(f"  Digitized Book Pages:            {s['pages']}")
    click.echo(f"  Aligned Corpus Sentences:        {s['corpus_sentences']}")
    click.echo(f"  Registered Source Citations:     {s['source_references']}")
    click.echo("=======================================================\n")


@cli.command("lookup")
@click.argument("word")
def cmd_lookup(word: str):
    """Look up a word in the Dimasa multilingual dictionary."""
    entry = lookup(word)
    if not entry:
        click.echo(f"Word '{word}' was not found in the Dimasa dictionary.")
        return

    click.echo(f"\nHeadword:     {entry.headword} [{entry.part_of_speech}]")
    click.echo(f"IPA:          /{entry.phonetic_ipa}/")
    click.echo(f"Bengali:      {entry.bengali_script}")
    click.echo(f"English:      {entry.english}")
    click.echo(f"Hindi:        {entry.hindi}")
    click.echo(f"Bengali Def:  {entry.bengali}")
    if entry.example_sentence:
        click.echo(f"Example:      {entry.example_sentence}")
        click.echo(f"Translation:  '{entry.example_translation}'")
    click.echo(f"Source:       {entry.source_id} ({entry.verification_status})\n")


@cli.command("search")
@click.argument("query")
@click.option("--language", "-l", default="english", help="Search language (english, dimasa, hindi, bengali, all)")
@click.option("--limit", "-n", default=10, help="Maximum number of results")
def cmd_search(query: str, language: str, limit: int):
    """Search dictionary entries across languages."""
    results = search(query, language=language, limit=limit)
    if not results:
        click.echo(f"No results found for '{query}' in language '{language}'.")
        return

    click.echo(f"\nFound {len(results)} match(es) for '{query}' [{language}]:")
    click.echo("-" * 60)
    for r in results:
        click.echo(f"• {r.headword} [{r.part_of_speech}] - {r.english} (Bengali: {r.bengali_script})")
    click.echo("-" * 60 + "\n")


@cli.command("translate")
@click.argument("text")
@click.option("--from-lang", "-f", default="english", help="Source language")
@click.option("--to", "-t", "to_lang", default="dimasa", help="Target language (dimasa, english, hindi, bengali)")
def cmd_translate(text: str, from_lang: str, to_lang: str):
    """Translate text between Dimasa and English, Hindi, or Bengali."""
    res = translate(text, source=from_lang, target=to_lang)
    click.echo(f"\nTranslation:  {res.text}")
    click.echo(f"Confidence:   {res.confidence * 100:.1f}%")
    click.echo(f"Method:       {res.method}")
    click.echo(f"Sources:      {', '.join(res.sources)}")
    if res.notes:
        click.echo(f"Notes:        {res.notes}")
    click.echo()


@cli.group("grammar")
def group_grammar():
    """Grammar rules and validation commands."""
    pass


@group_grammar.command("rules")
@click.option("--category", "-c", default=None, help="Filter by linguistic category")
def cmd_grammar_rules(category: str):
    """List documented Dimasa grammar rules."""
    engine = get_grammar_rules_engine()
    rules_list = engine.list_rules(category=category)
    click.echo(f"\nDocumented Dimasa Grammar Rules ({len(rules_list)}):")
    click.echo("-" * 65)
    for r in rules_list:
        click.echo(f"[{r.id}] {r.name} ({r.category})")
        click.echo(f"      Pattern: {r.formula}")
    click.echo("-" * 65 + "\n")


@group_grammar.command("explain")
@click.argument("rule_id")
def cmd_grammar_explain(rule_id: str):
    """Explain a specific Dimasa grammar rule by ID."""
    engine = get_grammar_rules_engine()
    click.echo("\n" + engine.explain(rule_id) + "\n")


@group_grammar.command("validate")
@click.argument("clause")
def cmd_grammar_validate(clause: str):
    """Validate a Dimasa clause against documented grammar rules."""
    engine = get_grammar_rules_engine()
    diag = engine.validate_clause(clause)
    click.echo(f"\nClause: '{diag.clause}'")
    click.echo(f"Supported Patterns: {len(diag.identified_rules)}")
    for d in diag.diagnostics:
        click.echo(f"  ✓ [{d.rule_id}] {d.rule_name}: {d.message}")
    click.echo(f"Notes: {diag.notes}\n")


@cli.group("morphology")
def group_morphology():
    """Morphological analysis and generation commands."""
    pass


@group_morphology.command("analyze")
@click.argument("word")
def cmd_morph_analyze(word: str):
    """Analyze and decompose a Dimasa word."""
    m = analyze_word(word)
    click.echo(f"\nWord:         {m.word}")
    click.echo(f"Root:         {m.root} ({m.root_meaning})")
    click.echo(f"POS:          {m.part_of_speech}")
    click.echo(f"Prefixes:     {m.prefixes}")
    click.echo(f"Suffixes:     {m.suffixes}")
    click.echo(f"Features:     {m.grammatical_features}")
    click.echo(f"Verified:     {m.is_verified}\n")


@group_morphology.command("generate")
@click.argument("root")
def cmd_morph_generate(root: str):
    """Generate inflectional paradigms for a verified root."""
    forms = generate_forms(root)
    click.echo(f"\nGenerated Forms for '{root}':")
    click.echo("-" * 40)
    for cat, form in forms.items():
        click.echo(f"  {cat:15}: {form}")
    click.echo("-" * 40 + "\n")


@cli.command("num")
@click.argument("value")
def cmd_num(value: str):
    """Convert number to Dimasa words or words to number."""
    if value.isdigit():
        n = int(value)
        words = num_to_words(n)
        click.echo(f"{n} -> {words}")
    else:
        try:
            num = words_to_num(value)
            click.echo(f"'{value}' -> {num}")
        except Exception as e:
            click.echo(f"Error: {e}")


@cli.group("culture")
def group_culture():
    """Cultural heritage database commands."""
    pass


@group_culture.command("festivals")
def cmd_culture_festivals():
    """List documented Dimasa festivals."""
    festivals = list_festivals()
    click.echo("\nDimasa Festivals:")
    for f in festivals:
        click.echo(f"• {f['name']} ({f['timing']}): {f['description'][:80]}...")
    click.echo()


@group_culture.command("attire")
def cmd_culture_attire():
    """List traditional Dimasa attire garments."""
    attire = list_attire()
    click.echo("\nTraditional Dimasa Attire:")
    for a in attire:
        click.echo(f"• {a['name']} ({a['category']}): {a['description'][:80]}...")
    click.echo()


@group_culture.command("clans")
def cmd_culture_clans():
    """List Dimasa Sengphong (40 patriclans) and Julu (42 matriclans)."""
    clans_data = list_clans()
    sengphongs = clans_data.get("sengphongs", [])
    julus = clans_data.get("julus", [])
    click.echo(f"\nSengphong (40 Male Clans) - Total: {len(sengphongs)}:")
    for sp in sengphongs[:15]:
        click.echo(f"  - {sp['name']} ({sp['meaning']})")
    click.echo(f"  ... and {len(sengphongs) - 15} more Sengphongs.")
    click.echo(f"\nJulu (Female Clans) - Total: {len(julus)}:")
    for jl in julus[:8]:
        click.echo(f"  - {jl['name']} ({jl['meaning']})")
    click.echo()


@group_culture.command("dishes")
def cmd_culture_dishes():
    """List traditional Dimasa cuisine and dishes."""
    dishes = list_dishes()
    click.echo("\nTraditional Dimasa Cuisine:")
    for d in dishes:
        click.echo(f"• {d['name']} ({d['category']}): {d['description'][:80]}...")
    click.echo()


@group_culture.command("places")
def cmd_culture_places():
    """List historical Dimasa settlements and landmarks."""
    places = list_places()
    click.echo("\nHistorical Landmarks and Settlements:")
    for p in places:
        click.echo(f"• {p['name']} ({p.get('historical_name', '')}): {p['description'][:80]}...")
    click.echo()


@cli.command("books")
def cmd_books():
    """List digitized books and public literature."""
    books_list = list_books()
    click.echo(f"\nDigitized Books in Catalog ({len(books_list)}):")
    click.echo("-" * 65)
    for b in books_list:
        click.echo(f"[{b.id}] {b.title} by {b.author} ({b.publication_year})")
        click.echo(f"     Pages: {b.total_pages} | Words: {b.total_words} | Status: {b.copyright_status}")
    click.echo("-" * 65 + "\n")


@cli.command("read")
@click.argument("book_id")
@click.option("--page", "-p", default=1, type=int, help="Page number to read")
def cmd_read(book_id: str, page: int):
    """Read a page from a digitized book."""
    book = get_book(book_id)
    if not book:
        click.echo(f"Book '{book_id}' not found.")
        return

    p = book.get_page(page)
    if not p:
        click.echo(f"Page {page} not found in '{book.title}' (Total pages: {book.total_pages}).")
        return

    click.echo(f"\n=== {book.title} (Page {p.page_number} / {book.total_pages}) ===")
    click.echo(f"Chapter/Title: {p.title}\n")
    click.echo(p.content)
    click.echo("=" * 60 + "\n")


@cli.command("search-books")
@click.argument("keyword")
def cmd_search_books(keyword: str):
    """Search for keyword across all catalogued books."""
    res = search_books(keyword)
    click.echo(f"\nFound {len(res)} matching book(s) for '{keyword}':")
    for b in res:
        click.echo(f"• {b['title']} by {b['author']} ({b['matches_count']} page match(es))")
        for m in b["page_matches"]:
            click.echo(f"    Page {m['page_number']}: {m['snippet']}")
    click.echo()


@cli.group("corpus")
def group_corpus():
    """Linguistic corpus commands."""
    pass


@group_corpus.command("stats")
def cmd_corpus_stats():
    """Display parallel corpus metrics."""
    c = get_corpus()
    s = c.stats()
    click.echo("\nDimasa Parallel Linguistic Corpus Statistics:")
    click.echo(f"  Total Sentences: {s['total_sentences']}")
    click.echo(f"  Total Tokens:    {s['total_tokens']}")
    click.echo(f"  Unique Tokens:   {s['unique_tokens']}")
    click.echo(f"  Genres:          {s['genres']}")
    click.echo()


@group_corpus.command("search")
@click.argument("keyword")
def cmd_corpus_search(keyword: str):
    """Search parallel aligned sentences in the corpus."""
    c = get_corpus()
    results = c.search(keyword)
    click.echo(f"\nCorpus matches for '{keyword}' ({len(results)}):")
    for r in results:
        click.echo(f"  • Dimasa:  {r.dimasa}")
        click.echo(f"    English: {r.english}")
        click.echo(f"    Source:  {r.source_id}")
    click.echo()


def main():
    """Entry point for console script."""
    cli()


if __name__ == "__main__":
    main()

