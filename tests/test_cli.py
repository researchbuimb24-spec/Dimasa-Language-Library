"""Unit tests for Dimasa Command-Line Interface (CLI)."""

import pytest
from click.testing import CliRunner
from dimasa.cli.main import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_version(runner):
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "dimasa" in result.output


def test_cli_stats(runner):
    result = runner.invoke(cli, ["stats"])
    assert result.exit_code == 0
    assert "DIMASA LINGUISTIC & DIGITAL PRESERVATION STATISTICS" in result.output
    assert "Verified Dictionary Entries:" in result.output


def test_cli_lookup(runner):
    result = runner.invoke(cli, ["lookup", "di"])
    assert result.exit_code == 0
    assert "Headword:     di" in result.output
    assert "water" in result.output.lower()


def test_cli_search(runner):
    result = runner.invoke(cli, ["search", "water", "--language", "english"])
    assert result.exit_code == 0
    assert "di" in result.output


def test_cli_translate(runner):
    result = runner.invoke(cli, ["translate", "Hello", "--to", "dimasa"])
    assert result.exit_code == 0
    assert "khurthao" in result.output.lower()


def test_cli_grammar_rules(runner):
    result = runner.invoke(cli, ["grammar", "rules"])
    assert result.exit_code == 0
    assert "PHON-01" in result.output


def test_cli_grammar_explain(runner):
    result = runner.invoke(cli, ["grammar", "explain", "PHON-01"])
    assert result.exit_code == 0
    assert "Five Vowel System" in result.output


def test_cli_grammar_validate(runner):
    result = runner.invoke(cli, ["grammar", "validate", "ang di lung-du"])
    assert result.exit_code == 0
    assert "SYNT-01" in result.output


def test_cli_morphology_analyze(runner):
    result = runner.invoke(cli, ["morphology", "analyze", "thang-du"])
    assert result.exit_code == 0
    assert "Root:         thang" in result.output


def test_cli_num(runner):
    result = runner.invoke(cli, ["num", "25"])
    assert result.exit_code == 0
    assert "bisasi mabowa" in result.output


def test_cli_culture_festivals(runner):
    result = runner.invoke(cli, ["culture", "festivals"])
    assert result.exit_code == 0
    assert "Bushu Dima" in result.output


def test_cli_culture_clans(runner):
    result = runner.invoke(cli, ["culture", "clans"])
    assert result.exit_code == 0
    assert "Langthasa" in result.output


def test_cli_books_and_read(runner):
    result = runner.invoke(cli, ["books"])
    assert result.exit_code == 0
    assert "dundas-1908" in result.output

    read_result = runner.invoke(cli, ["read", "dundas-1908", "--page", "1"])
    assert read_result.exit_code == 0
    assert "North Cachar" in read_result.output


def test_cli_corpus_stats(runner):
    result = runner.invoke(cli, ["corpus", "stats"])
    assert result.exit_code == 0
    assert "Total Sentences:" in result.output

