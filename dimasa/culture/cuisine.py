"""Dimasa Traditional Cuisine and Fermentation Heritage."""

from typing import Any, Dict, List, Optional
from .data_loader import get_culture_data


def list_dishes() -> List[Dict[str, Any]]:
    """List all documented traditional Dimasa dishes and beverages."""
    return get_culture_data().get("cuisine", [])


def get_dish(dish_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve specific dish record (e.g. 'judima', 'napham', 'gundru', 'khar')."""
    if not dish_id:
        return None
    clean = dish_id.strip().lower()
    for dish in list_dishes():
        if dish.get("id", "").lower() == clean or dish.get("name", "").lower() == clean:
            return dish
    return None

