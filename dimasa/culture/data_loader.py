"""Cultural data loader and access helper."""

import json
from pathlib import Path
from typing import Any, Dict

CULTURE_FILE = Path(__file__).parent.parent / "data" / "culture.json"
_culture_data: Dict[str, Any] = {}


def get_culture_data() -> Dict[str, Any]:
    """Load culture dataset from json."""
    global _culture_data
    if not _culture_data and CULTURE_FILE.exists():
        with open(CULTURE_FILE, "r", encoding="utf-8") as f:
            _culture_data = json.load(f)
    return _culture_data

