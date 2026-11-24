"""Dimasa Traditional Ecological Knowledge, Flora, and Fauna."""

from typing import Any, Dict, List


def list_flora() -> List[Dict[str, Any]]:
    """List culturally significant botanical plants and crops."""
    return [
        {
            "name": "Thembra",
            "scientific_name": "Acacia pennata",
            "dimasa_usage": "Bark crushed to prepare Humao (yeast starter culture) for brewing GI-tagged Judima rice wine.",
            "verification_status": "community_verified",
        },
        {
            "name": "Maiju",
            "scientific_name": "Oryza sativa var. glutinosa",
            "dimasa_usage": "Traditional sticky/glutinous rice variety cultivated in jhum fields for festive preparations and Judima.",
            "verification_status": "community_verified",
        },
        {
            "name": "Wathisa",
            "scientific_name": "Bambusa tulda",
            "dimasa_usage": "Indigenous hill bamboo used for weaving baskets, house building, hollow vessels for Napham fermentation, and flutes.",
            "verification_status": "documented",
        },
    ]


def list_fauna() -> List[Dict[str, Any]]:
    """List culturally recognized fauna in Dimasa terminology."""
    return [
        {"dimasa": "misi", "english": "tiger", "cultural_note": "Revered hill animal associated with forest guardianship"},
        {"dimasa": "mi", "english": "deer", "cultural_note": "Pastoral game animal in oral ballads"},
        {"dimasa": "dao", "english": "bird/fowl", "cultural_note": "Sacred omen bird and festival offering"},
        {"dimasa": "mshou", "english": "cow/cattle", "cultural_note": "Agricultural draft animal counted with classifier khoro-"},
    ]

