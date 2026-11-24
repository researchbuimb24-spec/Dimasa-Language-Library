"""Dimasa Historical Geography and Heritage Landmarks."""

from typing import Any, Dict, List, Optional
from .data_loader import get_culture_data


def list_places() -> List[Dict[str, Any]]:
    """List documented historical Dimasa settlements, capitals, and landmarks."""
    return get_culture_data().get("geography", [])


def get_place(place_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve historical place record (e.g. 'dimapur', 'maibang', 'khaspur', 'dima_hasao')."""
    if not place_id:
        return None
    clean = place_id.strip().lower()
    for p in list_places():
        if p.get("id", "").lower() == clean or p.get("name", "").lower() == clean:
            return p
    return None

