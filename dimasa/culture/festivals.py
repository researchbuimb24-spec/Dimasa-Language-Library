"""Dimasa Festivals and Community Rituals."""

from typing import Any, Dict, List, Optional
from .data_loader import get_culture_data


def list_festivals() -> List[Dict[str, Any]]:
    """List all documented Dimasa festivals and rituals."""
    return get_culture_data().get("festivals", [])


def get_festival(festival_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve festival record by ID (e.g. 'bushu_dima', 'rajini_gabra', 'harni_gabra')."""
    if not festival_id:
        return None
    clean = festival_id.strip().lower()
    for item in list_festivals():
        if item.get("id", "").lower() == clean or item.get("name", "").lower() == clean or clean in item.get("id", ""):
            return item
    return None

