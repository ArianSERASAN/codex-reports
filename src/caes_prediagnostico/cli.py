from __future__ import annotations

import argparse
from pathlib import Path

from caes_prediagnostico.pipeline import run_pipeline


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prediagnóstico de proyectos de eficiencia energética con CAEs."
    )
    parser.add_argument("--input", required=True, help="Directorio con documentación.")
    parser.add_argument("--output", required=True, help="Directorio de salida.")
    parser.add_argument("--project-name", required=True, help="Nombre del proyecto.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_dir = Path(args.input).expanduser().resolve()
    output_dir = Path(args.output).expanduser().resolve()
    run_pipeline(input_dir=input_dir, output_dir=output_dir, project_name=args.project_name)


if __name__ == "__main__":
    main()
