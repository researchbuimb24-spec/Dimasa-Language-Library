"""Dimasa Literary Heritage, Authors, and Traditional Oral Literature."""

from typing import Any, Dict, List


def list_authors() -> List[Dict[str, Any]]:
    """List documented pioneering Dimasa authors, scholars, and folklorists."""
    return [
        {
            "name": "Sonaram Thaosen (S.R. Thaosen)",
            "years": "1907-1971",
            "role": "Pioneering Dimasa writer, historian, social reformer, and politician",
            "key_works": ["Dimasa Kachari (1964)", "History of the Dimasas"],
            "contribution": "First systematic chronicler of the 40 Sengphongs and 42 Julus and traditional Dimasa customary law.",
            "verification_status": "community_verified",
        },
        {
            "name": "Mani Charan Barman",
            "years": "Late 19th - Early 20th century",
            "role": "Native scholar and author of early Kachari Grammar",
            "key_works": ["Kachari (Dimasa) Grammar Notes"],
            "contribution": "Collaborated with W.C.M. Dundas to record grammatical paradigms and English-Dimasa vocabularies.",
            "verification_status": "documented",
        },
        {
            "name": "Nagena Barua",
            "years": "20th Century",
            "role": "Anthropologist and ethnomusicologist",
            "key_works": ["Dimasha Society and Their Folk Songs (1980)"],
            "contribution": "Extensive transcription and translation of Dimasa ballads, Murithaih, and wedding songs.",
            "verification_status": "documented",
        },
    ]


def list_traditions() -> List[str]:
    """List traditional literature forms in Dimasa."""
    return [
        "Khurang (folktales and historical legends)",
        "Murithaih (traditional lyrical songs accompanied by Muri trumpet)",
        "Rjabkharmin (festive dance songs)",
        "Graothao (proverbs and ancestral riddles)",
    ]

