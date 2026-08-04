# Etapa A – Canvas Ingest

Usa la skill `7cs-canvas-ingest`.

Procesa el archivo:

resources/Arquitectura para Sistema de Reservas con Agente Inteligente LLM.pdf

Ejecuta únicamente la Etapa A del pipeline 7Cs → Spec Kit.

Cumple el contrato definido en el SKILL.md:

- Genera un Canvas Object Model (COM) en formato JSON por cada canvas encontrado.
- Genera `page_index.json`.
- Genera `ingest_report.md`.
- Guarda las imágenes de evidencia en `evidence/`.
- Guarda los COM en `com/`.

No interpretes, resumas ni mapees los post-it.

No ejecutes ninguna skill de la Etapa B.

No ejecutes `7cs-spec-compose` ni `7cs-spec-audit`.