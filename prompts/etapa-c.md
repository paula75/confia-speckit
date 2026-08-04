# Etapa C – Composición

Continúa con la Etapa C del pipeline 7Cs → Spec Kit.

Ejecuta la skill `7cs-spec-compose` utilizando todos los fragmentos generados en `mapping/`.

Respeta estrictamente el contrato definido en el SKILL.md.

Genera los siguientes outputs:

- prompt_constitution
- prompt_specify
- clarify_input
- plan_input
- trace_annex

Guarda los resultados en la carpeta `composed/`.

No reescribas, resumas ni "mejores" el contenido de los fragmentos.

No resuelvas dudas; las dudas deben mantenerse como `[NEEDS CLARIFICATION]`.

No dejes tecnología en `prompt_specify`; debe trasladarse a `plan_input`.

No ejecutes todavía `7cs-spec-audit`.

Al finalizar, entrega un resumen indicando:

- los archivos generados en `composed/`;
- el número de requisitos compuestos;
- el número de trazas consolidadas;
- cualquier advertencia detectada durante la composición.