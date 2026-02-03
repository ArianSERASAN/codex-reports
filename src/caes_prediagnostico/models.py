from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class SectionDocument:
    path: str
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class SectionResult:
    name: str
    documents: list[SectionDocument] = field(default_factory=list)
    extracted_facts: dict[str, Any] = field(default_factory=dict)
    notes: list[str] = field(default_factory=list)


@dataclass
class ProjectSummary:
    project_name: str
    created_at: datetime
    sections: list[SectionResult]
    totals: dict[str, Any]
    measures: list[dict[str, Any]]
    caes: list[dict[str, Any]]
