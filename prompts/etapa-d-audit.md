# Etapa D – Auditoría

Continúa con la auditoría del pipeline 7Cs → Spec Kit.

Ejecuta la skill `7cs-spec-audit` utilizando exclusivamente como entrada los artefactos existentes en la carpeta `composed/`:

- prompt_specify.md
- prompt_constitution.md
- trace_annex.md

y todos los Canvas Object Models (COM) contenidos en `com/`.

Respeta estrictamente el contrato definido en el `SKILL.md`.

## Restricciones

- Considera la carpeta `composed/` como **solo lectura**.
- No modifiques, regeneres, reordenes ni sobrescribas ningún archivo dentro de `composed/`.
- No modifiques los archivos de `com/`.
- No reconstruyas la composición.
- No resuelvas elementos marcados como `[NEEDS CLARIFICATION]`.

## Outputs

Genera únicamente los siguientes archivos:

- audit_report.md
- clarify_input.md
- checklist_input.md
- verdict.txt

Guárdalos exclusivamente en la carpeta:

audit/

No escribas ningún archivo dentro de `composed/`.

## Auditoría

Recalcula completamente desde cero las métricas:

- Cobertura (C)
- Ambigüedad (A)
- Contaminación técnica (T)
- Verificabilidad (V)

Verifica además:

- cobertura completa de los post-it;
- exactamente una traza por post-it;
- ausencia de contaminación técnica en `prompt_specify.md`;
- escenarios Dado/Cuando/Entonces para todos los FR verificables;
- cumplimiento del checklist definido por la metodología.

Si la corrida resulta inválida, explica claramente:

- qué reglas del pipeline no se cumplen;
- qué evidencia lo demuestra;
- qué acciones serían necesarias para obtener una corrida válida.

## Resumen final

Entrega un resumen indicando:

- veredicto final (VÁLIDA o INVÁLIDA);
- métricas C, A, T y V;
- archivos generados en `audit/`;
- principales observaciones detectadas.

La estructura esperada al finalizar la auditoría debe ser:

composed/
  - compose_manifest.json
  - plan_input.md
  - prompt_constitution.md
  - prompt_specify.md
  - prompt_specify_reconstruction_report.md
  - trace_annex.md

audit/
  - audit_report.md
  - clarify_input.md
  - checklist_input.md
  - verdict.txt