"""Dimasa Musical Instruments and Dance Heritage."""

from typing import Any, Dict, List, Optional
from .data_loader import get_culture_data


def list_instruments() -> List[Dict[str, Any]]:
    """List documented traditional Dimasa musical instruments (Khram, Muri, etc.)."""
    return get_culture_data().get("music", [])


def get_instrument(instrument_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve instrument record by ID."""
    if not instrument_id:
        return None
    clean = instrument_id.strip().lower()
    for item in list_instruments():
        if item.get("id", "").lower() == clean or item.get("name", "").lower() == clean:
            return item
    return None

