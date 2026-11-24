"""Dimasa Traditional Attire and Handloom Database."""

from typing import Any, Dict, List, Optional
from .data_loader import get_culture_data


def list_attire() -> List[Dict[str, Any]]:
    """List all documented traditional Dimasa attire garments and textiles."""
    data = get_culture_data()
    return data.get("attire", [])


def get_attire(attire_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve specific attire record by ID (e.g. 'rigu', 'rikhaosa', 'sgaopha')."""
    if not attire_id:
        return None
    clean_id = attire_id.strip().lower()
    for item in list_attire():
        if item.get("id", "").lower() == clean_id or item.get("name", "").lower() == clean_id:
            return item
    return None

