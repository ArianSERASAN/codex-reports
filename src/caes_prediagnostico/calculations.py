from __future__ import annotations

from dataclasses import asdict
from datetime import datetime

from caes_prediagnostico.models import ProjectSummary, SectionResult


def _sum_values(values: list[float]) -> float:
    return round(sum(values), 2)


def calculate_project_summary(
    project_name: str,
    sections: list[SectionResult],
) -> ProjectSummary:
    totals: dict[str, float] = {
        "consumo_kwh": 0.0,
        "coste_eur": 0.0,
        "potencia_kw": 0.0,
        "superficie_m2": 0.0,
    }
    for section in sections:
        for key, values in section.extracted_facts.items():
            if key in totals:
                totals[key] += _sum_values(values)

    totals = {key: round(value, 2) for key, value in totals.items()}

    measures = _build_measures(totals)
    caes = _build_caes(measures)
    return ProjectSummary(
        project_name=project_name,
        created_at=datetime.utcnow(),
        sections=sections,
        totals=totals,
        measures=measures,
        caes=caes,
    )


def _build_measures(totals: dict[str, float]) -> list[dict[str, float | str]]:
    consumo = totals.get("consumo_kwh", 0.0)
    coste = totals.get("coste_eur", 0.0)
    ahorro_estimado = round(consumo * 0.12, 2)
    ahorro_eur = round(coste * 0.1, 2)
    return [
        {
            "medida": "Optimización de iluminación LED",
            "ahorro_kwh": round(consumo * 0.08, 2),
            "ahorro_eur": round(coste * 0.06, 2),
            "inversion_eur": 18000.0,
            "payback_anios": 3.2,
        },
        {
            "medida": "Mejora aislamiento térmico",
            "ahorro_kwh": round(consumo * 0.04, 2),
            "ahorro_eur": round(coste * 0.04, 2),
            "inversion_eur": 25000.0,
            "payback_anios": 4.5,
        },
        {
            "medida": "Gestión energética y monitorización",
            "ahorro_kwh": ahorro_estimado,
            "ahorro_eur": ahorro_eur,
            "inversion_eur": 12000.0,
            "payback_anios": 2.8,
        },
    ]


def _build_caes(measures: list[dict[str, float | str]]) -> list[dict[str, float | str]]:
    caes = []
    for medida in measures:
        ahorro_kwh = float(medida["ahorro_kwh"])
        caes.append(
            {
                "medida": medida["medida"],
                "cae_estimado_mwh": round(ahorro_kwh / 1000.0, 2),
                "factor_cae": 1.0,
                "ahorro_ponderado": round(ahorro_kwh * 1.0, 2),
            }
        )
    return caes


def summary_to_dict(summary: ProjectSummary) -> dict[str, object]:
    data = asdict(summary)
    data["created_at"] = summary.created_at.isoformat()
    return data
