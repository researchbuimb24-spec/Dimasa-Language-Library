"""Dimasa Traditional Proverbs, Idioms (Graothao), and Sayings."""

from typing import Any, Dict, List
from .data_loader import get_culture_data


def list_idioms() -> List[Dict[str, Any]]:
    """List documented Dimasa proverbs and idiomatic expressions with translations."""
    return get_culture_data().get("idioms", [])

