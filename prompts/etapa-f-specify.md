# Etapa F – Generación de la Specification

Continúa el pipeline 7Cs → Spec Kit.

Ejecuta la skill `speckit-specify`.

Utiliza como entrada:

- `composed/prompt_specify.md`

Utiliza la Constitution vigente generada en la etapa anterior.

Respeta estrictamente el contrato definido por la propia skill.

Objetivos de esta etapa:

- Generar la Specification completa del sistema.
- Preservar la trazabilidad proveniente del pipeline 7Cs.
- Mantener la neutralidad tecnológica definida por la Constitution.
- No resolver elementos marcados como `[NEEDS CLARIFICATION]`.
- No incorporar información que no provenga del pipeline.
- No ejecutar automáticamente ninguna etapa posterior.

Al finalizar:

- Guarda los artefactos definidos por la propia skill.
- Informa cualquier conflicto detectado.
- Espera nuevas instrucciones antes de continuar con `/speckit.clarify`.