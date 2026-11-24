"""Dimasa Folklore and Creation Narratives."""

from typing import Any, Dict, List


def list_narratives() -> List[Dict[str, Any]]:
    """List core documented Dimasa creation narratives and folktale summaries."""
    return [
        {
            "id": "arikidima",
            "title": "Arikhidima and the Seven Divine Eggs",
            "category": "creation_myth",
            "summary": "The primordial bird Arikhidima nested at Sangsari Dingra and laid seven divine eggs from which hatched the gods, ancestors, and foundational spirits of the Dimasa.",
            "source_id": "SRC-BODODIMASA-ARCHIVE",
            "verification_status": "community_verified",
        },
        {
            "id": "hidimba_bhima",
            "title": "The Heritage of Hidimba and Bhima",
            "category": "epic_lore",
            "summary": "Dimasa royal genealogy traces descent from Prince Ghatotkacha, born to Pandava hero Bhima and Princess Hidimba in ancient Hedambapur (Dimapur).",
            "source_id": "SRC-THAOSEN-1964",
            "verification_status": "documented",
        },
    ]

