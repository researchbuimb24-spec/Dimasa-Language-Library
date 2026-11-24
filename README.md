# Dimasa: Python NLP, Linguistic & Cultural Preservation Library

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://pypi.org/project/dimasa/)
[![Python version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)](https://pypi.org/project/dimasa/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/dimasa-preservation/dimasa)
[![Language](https://img.shields.io/badge/Language-Dimasa%20(dis)-orange.svg)](https://iso639-3.sil.org/code/dis)

**Dimasa** is an open-source Python computational linguistics and digital heritage preservation library for the **Dimasa language** (*Grao Dima*, ISO 639-3: `dis`), spoken primarily in Assam (Dima Hasao, Cachar, Karbi Anglong, Hojai, Nagaon) and parts of Nagaland in Northeast India.

Dimasa belongs to the Bodo-Garo (Sal) branch of the Sino-Tibetan / Tibeto-Burman language family. This library provides a modular, offline-first toolkit featuring a multilingual dictionary, grammar rules and validation engine, morphological analyzer and generator, bidirectional transliteration, phonological and syllable processor, numeral classifier engine, cultural heritage database, digitized literature catalog, searchable parallel corpus, and a command-line interface.

---

## Key Features

1. **Multilingual Dictionary (`dimasa.dictionary`)**:
   - Exact, case-insensitive, root-based, and prefix lookup.
   - Multilingual search across Dimasa, English, Hindi, and Bengali.
   - Rich lexical metadata: part of speech, IPA transcription, Bengali-Assamese script, example sentences, morphological root, synonyms, antonyms, and bibliographic provenance.

2. **Grammar Rules & Validation Engine (`dimasa.grammar`)**:
   - Structured registry of documented Dimasa grammar rules categorized into phonology, morphology, case marking, verb morphology, tense-aspect-mood, negation, and syntax.
   - Clause validator diagnosing canonical SOV alignment, differential object marking (`-ke/-khe`), prohibitive prefixation (`da-`), tense-aspect neutralization under negation, pronominal velar nasal deletion, and postpositional phrasing.

3. **Morphology & Verb Conjugation (`dimasa.morphology`)**:
   - Morphological decomposition of inflected words into root and affixes.
   - Authentic noun declension across 8 grammatical cases.
   - Pronominal suppletion and morphophonemic rules (e.g. *ang* + *-ni* $\rightarrow$ *ani*).
   - Verbal conjugation for present imperfective (`-du`), past (`-ba`), perfective (`-kadu`), future (`-ma`), imperative (`-bo`), causative (`-ri`), and declarative negation (`-ja`).

4. **Multi-lingual Translation (`dimasa.translation`)**:
   - Translation between Dimasa and English, Hindi, and Bengali.
   - Backed by curated phrasebooks, aligned parallel sentences, and lexical lookup with SOV grammatical reordering.
   - Transparent confidence scores and explicit flagging of untranslated tokens.

5. **Script & Transliteration Engine (`dimasa.transliteration`)**:
   - Bidirectional transliteration between standard Roman orthography and Eastern Nagari (Bengali/Assamese) script.
   - Unicode NFC text normalization and automatic script detection.

6. **Phonology & Syllable Engine (`dimasa.phonology`)**:
   - Full 17 consonant phoneme and 5 vowel inventory.
   - Syllable segmentation supporting native sesquisyllabic clusters (e.g. *gdain* $\rightarrow$ `['g', 'dain']`).
   - International Phonetic Alphabet (IPA) conversion for Haflong standard pronunciation.

7. **Numerals & Classifier Subsystem (`dimasa.numerals`)**:
   - Conversion of numbers (1 to 100+) to Dimasa numeral words and vice-versa.
   - Sortal classifiers: `sao-` (human), `ma-` (animate/generic), `gong-` (rigid cylindrical), `phang-` (botanical/trees), `khang-` (flat planar), `thai-` (round fruits), `khoro-` (livestock).
   - Syntax-aware ordering: *Classifier-Numeral + Noun* (indefinite) vs *Noun + Classifier-Numeral* (definite).

8. **Cultural Heritage Database (`dimasa.culture`)**:
   - Attire and textiles (*Rigu*, *Rikhaosa*, *Rigdo*, *Bathormai*, *Rimsao*, *Sgaopha*).
   - The dual-clan system: 40 male patriclans (*Sengphong*) and 42 female matriclans (*Julu*) with a custom marriage compatibility validator verifying double-exogamy.
   - Culinary traditions (*Judima* [GI tagged], *Napham*, *Gundru*, *Khar*).
   - Festivals (*Bushu Dima*, *Rajini Gabra*, *Harni Gabra*), spiritual lore (*Sibarai*, 12 *Daikhos*), music (*Khram*, *Muri*), and historical geography (*Dimapur*, *Maibang*, *Khaspur*).

9. **Digitized Literature & Book Catalog (`dimasa.books`)**:
   - Structured metadata and page-by-page reader for public domain and community-archived linguistic monographs.
   - In-book keyword search and cross-catalog full-text search.

10. **Searchable Linguistic Corpus (`dimasa.corpus`)**:
    - Parallel sentences aligned across Dimasa, English, Hindi, and Bengali with POS tags and interlinear glosses.
    - Token frequency analysis, concordance lookups, and corpus metrics.

11. **CLI & Anti-Hallucination Statistics (`dimasa.cli` & `dimasa.stats`)**:
    - Command-line interface with commands for lookup, search, translate, grammar, morphology, numerals, culture, books, and corpus.
    - Transparent statistical reporting verifying actual documented entries without inflated numbers.

---

## Installation

```bash
pip install dimasa
```

For development and running tests:
```bash
git clone https://github.com/dimasa-preservation/dimasa.git
cd dimasa
pip install -e .[dev]
pytest
```

---

## Quick Start

```python
import dimasa

# 1. Dictionary lookup
entry = dimasa.lookup("di")
print(f"Headword: {entry.headword} [{entry.part_of_speech}]")
print(f"English:  {entry.english}")
print(f"IPA:      /{entry.phonetic_ipa}/")
print(f"Bengali:  {entry.bengali_script}")

# 2. Multilingual search
results = dimasa.search("water", language="english")
for r in results:
    print(f"• {r.headword} -> {r.english}")

# 3. Morphological analysis
analysis = dimasa.analyze_word("thang-du")
print(f"Root: {analysis.root}, Features: {analysis.grammatical_features}")

# 4. Verb conjugation
past_form = dimasa.conjugate("thang", tense="past")
print(f"Conjugated (past): {past_form}")  # thang-ba

neg_form = dimasa.conjugate("thang", tense="present", negative=True)
print(f"Conjugated (neg):  {neg_form}")   # thang-ja

# 5. Pronominal velar nasal drop
genitive_my = dimasa.decline_noun("ang", case="genitive")
print(f"1SG Genitive: {genitive_my}")     # ani (ang + ni -> ani)

# 6. Numerals and Classifiers
words = dimasa.num_to_words(25)
print(f"25 in Dimasa: {words}")           # bisasi mabowa

phrase = dimasa.apply_classifier(2, "sao", noun="subun", definite=True)
print(f"Definite phrase: {phrase}")       # subun sao-gin

# 7. Grammar clause validation
diag = dimasa.get_grammar_rules_engine().validate_clause("ang di lung-du")
print(f"Supported: {diag.is_supported}, Rules: {[r.id for r in diag.identified_rules]}")

# 8. Cultural heritage & clan compatibility
compat, msg = dimasa.check_marriage_compatibility("Langthasa", "Maireng", "Thaosen", "Saidima")
print(f"Marriage allowed: {compat} ({msg})")

# 9. Translation
result = dimasa.translate("Hello", source="english", target="dimasa")
print(f"Translation: {result.text} (Confidence: {result.confidence})")
```

---

## Command-Line Interface (CLI)

```bash
# View honest dataset metrics
dimasa stats

# Dictionary lookup & search
dimasa lookup di
dimasa search water --language english

# Translation
dimasa translate "Hello" --to dimasa

# Grammar inspection and validation
dimasa grammar rules
dimasa grammar explain PHON-01
dimasa grammar validate "ang di lung-du"

# Morphology
dimasa morphology analyze thang-du
dimasa morphology generate thang

# Numerals
dimasa num 25

# Cultural database
dimasa culture festivals
dimasa culture attire
dimasa culture clans
dimasa culture dishes
dimasa culture places

# Books and Corpus
dimasa books
dimasa read dundas-1908 --page 1
dimasa corpus stats
dimasa corpus search water
```

---

## Data Quality & Anti-Hallucination Policy

The Dimasa library strictly prioritizes linguistic authenticity over arbitrary numerical claims:
- Every lexical entry, grammar formula, and cultural record links to an authenticated bibliographic source.
- `dimasa.stats()` reports true dataset counts.
- Unknown vocabulary returns transparent unverified flags rather than fabricated text.
- Dimasa grammar rules are independently modeled from Bodo-Garo linguistic documentation and are never conflated with other regional languages.

---

## Citation & Primary Sources

If you use this library in linguistic or computational research, please cite:
- **Jonathan P. Evans & Dhrubajit Langthasa (2024)**. *Dimasa Language: Structure and Texts*. Institute of Linguistics, Academia Sinica, Taipei.
- **W. C. M. Dundas & Mani Charan Barman (1908)**. *An Outline Grammar and Dictionary of the Kachari (Dimasa) Language*. Eastern Bengal and Assam Secretariat Press, Shillong.
- **Kh. Dhiren Singha (2010)**. *Dimasa Word Book: A Classified Vocabulary*. DVS Publishers, Guwahati.
- **Monali Longmailai (2014)**. *A Descriptive Analysis of Dimasa*. Gauhati University.

---

## License

This project is licensed under the [MIT License](LICENSE).

