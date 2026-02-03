# Prediagnóstico CAEs para PYMEs

Herramienta en Python para organizar documentación de proyectos de eficiencia
energética/renovación, extraer información clave y generar un informe técnico
extenso con cálculos, propuestas y medidas compatibles con CAEs.

## Funcionalidades principales

- Ingesta de carpetas con hasta ~50 archivos (facturas, MEE, CAEs, planos,
  listas de equipos, etc.).
- Extracción de texto y números clave (consumos, costes, potencias, superficies).
- Consolidación de hallazgos por sección.
- Cálculos reales en Python (consumo anual, coste anual, ahorro potencial).
- Generación de informe en **DOCX** y **PDF**.

## Requisitos

- Python 3.10+
- Dependencias del proyecto (ver `requirements.txt`)

Instalación:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Uso rápido

```bash
python -m caes_prediagnostico.cli \
  --input ./datos_proyecto \
  --output ./salidas \
  --project-name "Proyecto CAEs PYME"
```

La herramienta generará:

- `salidas/informe_prediagnostico.docx`
- `salidas/informe_prediagnostico.pdf`
- `salidas/datos_consolidados.json`

## Estructura de carpetas recomendada

```
datos_proyecto/
  facturas/
  MEE/
  CAEs/
  planos/
  listas_equipos/
  otros/
```

## Notas

El extractor trabaja con texto de PDFs/DOCX y con hojas de cálculo (XLSX).
Para mejores resultados, se recomienda que los documentos estén digitalizados
y no sean únicamente imágenes escaneadas.
