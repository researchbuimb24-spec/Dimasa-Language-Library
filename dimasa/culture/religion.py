"""Dimasa Spiritual Traditions, Deities, and the Daikho System."""

from typing import Any, Dict, List, Optional
from .data_loader import get_culture_data


def list_deities() -> List[Dict[str, Any]]:
    """List traditional deities, spiritual concepts, and religious offices."""
    return get_culture_data().get("religion", [])


def list_daikhos() -> List[str]:
    """List the 12 sacred territorial Daikhos of the Dimasa kingdom."""
    for item in list_deities():
        if item.get("id") == "daikho_system":
            return item.get("daikhos_list", [])
    return []

