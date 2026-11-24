"""Dimasa Clans and Double-Descent Kinship System (40 Sengphong & 42 Julu)."""

from typing import Any, Dict, List, Optional, Tuple
from .data_loader import get_culture_data


def list_clans(clan_type: str = "all") -> Dict[str, Any]:
    """List Dimasa clans: 'all', 'sengphong' (male), or 'julu' (female)."""
    data = get_culture_data()
    clans_data = data.get("clans", {})
    t = clan_type.strip().lower()
    if t in ("sengphong", "male", "patriclans"):
        return {"sengphongs": clans_data.get("sengphongs", []), "total": len(clans_data.get("sengphongs", []))}
    if t in ("julu", "female", "matriclans", "jadi"):
        return {"julus": clans_data.get("julus", []), "total": len(clans_data.get("julus", []))}
    return clans_data


def get_sengphongs() -> List[Dict[str, Any]]:
    """Return the list of traditional 40 Sengphongs (male patriclans)."""
    return get_culture_data().get("clans", {}).get("sengphongs", [])


def get_julus() -> List[Dict[str, Any]]:
    """Return documented Julus (matriclans)."""
    return get_culture_data().get("clans", {}).get("julus", [])


def check_marriage_compatibility(
    groom_sengphong: str,
    groom_julu: str,
    bride_sengphong: str,
    bride_julu: str
) -> Tuple[bool, str]:
    """Verify marriage compatibility under strict Dimasa double-exogamy customary law.

    In Dimasa society:
    1. Marriage within the same Sengphong (father's clan) is strictly forbidden.
    2. Marriage within the same Julu (mother's clan) is strictly forbidden.
    """
    g_sp = groom_sengphong.strip().lower()
    g_jl = groom_julu.strip().lower()
    b_sp = bride_sengphong.strip().lower()
    b_jl = bride_julu.strip().lower()

    if g_sp == b_sp:
        return (
            False,
            f"Prohibited: Groom and Bride belong to the same Sengphong ('{groom_sengphong}'). "
            "Patriclan exogamy strictly forbids marriage within the same male clan lineage."
        )

    if g_jl == b_jl:
        return (
            False,
            f"Prohibited: Groom and Bride belong to the same Julu ('{groom_julu}'). "
            "Matriclan exogamy strictly forbids marriage within the same female clan lineage."
        )

    return (
        True,
        f"Compatible: Groom ({groom_sengphong}/{groom_julu}) and Bride ({bride_sengphong}/{bride_julu}) "
        "belong to distinct Sengphongs and Julus, satisfying customary double-exogamy regulations."
    )

