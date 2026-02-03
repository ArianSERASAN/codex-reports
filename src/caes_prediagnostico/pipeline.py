from __future__ import annotations

from pathlib import Path
import json

from caes_prediagnostico.calculations import calculate_project_summary, summary_to_dict
from caes_prediagnostico.extractors import consolidate_sections, export_consolidated_json
from caes_prediagnostico.reporting import build_docx_report, build_pdf_report


def run_pipeline(input_dir: Path, output_dir: Path, project_name: str) -> Path:
    sections = consolidate_sections(input_dir)
    summary = calculate_project_summary(project_name=project_name, sections=sections)

    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "datos_consolidados.json"
    export_consolidated_json(sections, json_path)
    (output_dir / "resumen.json").write_text(
        json.dumps(summary_to_dict(summary), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    docx_path = output_dir / "informe_prediagnostico.docx"
    pdf_path = output_dir / "informe_prediagnostico.pdf"
    build_docx_report(summary, docx_path)
    build_pdf_report(summary, pdf_path)
    return docx_path
