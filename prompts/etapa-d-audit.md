# Etapa D – Auditoría

Continúa con la auditoría del pipeline 7Cs → Spec Kit.

Ejecuta la skill `7cs-spec-audit` utilizando como entrada:

- `prompt_specify`
- `prompt_constitution`
- `trace_annex`
- todos los Canvas Object Models (COM) de la carpeta `com/`

Respeta estrictamente el contrato definido en el `SKILL.md`.

Genera los siguientes outputs:

- `audit_report`
- `clarify_input`
- `checklist_input`
- `verdict`

Guarda todos los resultados en la carpeta `audit/`.

No modifiques la especificación.
No resuelvas dudas marcadas como `[NEEDS CLARIFICATION]`.

Recalcula desde cero las métricas:

- Cobertura (C)
- Ambigüedad (A)
- Contaminación técnica (T)
- Verificabilidad (V)

Verifica además:

- cobertura completa de los post-it;
- una traza por post-it;
- ausencia de contaminación técnica en `prompt_specify`;
- escenarios Dado/Cuando/Entonces en todos los FR verificables;
- checklist completo definido por la metodología.

Si la corrida resulta inválida, explica claramente los motivos, indicando qué reglas del pipeline no se cumplen.

Al finalizar, entrega un resumen con:

- el veredicto final (VÁLIDA o INVÁLIDA);
- las métricas C, A, T y V;
- los archivos generados en `audit/`;
- las observaciones más relevantes detectadas por la auditoría.