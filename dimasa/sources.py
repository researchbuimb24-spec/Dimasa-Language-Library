"""Source registry and bibliographic citations for the Dimasa library."""

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional


@dataclass
class Source:
    """Bibliographic source with reliability assessment."""
    id: str
    title: str
    authors: List[str]
    year: int
    publisher: str
    place: str
    series: str
    url: str
    linguistic_info: str
    reliability: str

    def to_citation(self) -> str:
        """Format source as an academic citation string."""
        authors_str = ", ".join(self.authors)
        return (
            f"{authors_str} ({self.year}). {self.title}. "
            f"{self.publisher}, {self.place}."
        )


class SourceRegistry:
    """Registry managing linguistic and ethnographic citations."""

    def __init__(self, data_path: Optional[Path] = None):
        if data_path is None:
            data_path = Path(__file__).parent / "data" / "sources.json"
        self.data_path = Path(data_path)
        self._sources: Dict[str, Source] = {}
        self.load()

    def load(self) -> None:
        """Load sources from json."""
        if not self.data_path.exists():
            return
        with open(self.data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data.get("sources", []):
                source = Source(
                    id=item["id"],
                    title=item["title"],
                    authors=item.get("authors", []),
                    year=item.get("year", 0),
                    publisher=item.get("publisher", ""),
                    place=item.get("place", ""),
                    series=item.get("series", ""),
                    url=item.get("url", ""),
                    linguistic_info=item.get("linguistic_info", ""),
                    reliability=item.get("reliability", "unverified"),
                )
                self._sources[source.id] = source

    def get(self, source_id: str) -> Optional[Source]:
        """Retrieve source by ID."""
        return self._sources.get(source_id)

    def list_sources(self) -> List[Source]:
        """List all registered sources."""
        return list(self._sources.values())

    def __len__(self) -> int:
        return len(self._sources)


# Module singleton
_registry: Optional[SourceRegistry] = None


def get_source_registry() -> SourceRegistry:
    """Get or create singleton source registry."""
    global _registry
    if _registry is None:
        _registry = SourceRegistry()
    return _registry

