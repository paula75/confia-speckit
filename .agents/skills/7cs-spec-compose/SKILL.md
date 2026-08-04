---
name: 7cs-spec-compose
description: Etapa C del pipeline 7Cs→Spec Kit (orquestación). Ordena los fragmentos emitidos por los 6 skills de mapeo, resuelve duplicados entre canvas y emite los comandos de Spec Kit listos para pegar (/speckit.constitution, /speckit.specify, insumos de /speckit.clarify y /speckit.plan), con el anexo de trazabilidad completo. Usar cuando los skills de mapeo 7cs-* ya produjeron sus fragmentos y hay que componer el prompt final, o cuando el usuario pida "el prompt para Spec Kit", "componer la especificación" o "los comandos listos para pegar" desde canvas 7Cs.
---

# 7cs-spec-compose — Etapa C · Composición

El orquestador es **deliberadamente delgado**: secuencia A → B → C, propaga el
identificador de entrega y la versión de plantilla, y **no reescribe contenido**.
Ordena, deduplica por trazabilidad y ensambla.

Leer `references/reglas-reescritura.md` para verificar forma canónica al ensamblar.

## Contrato

```yaml
name: 7cs-spec-compose
when_to_use: >
  Los 6 skills de mapeo ya emitieron fragment/constitution_lines/traces/clarifications
  para una entrega. Ejecutar después de la etapa B y antes de 7cs-spec-audit.
inputs:
  fragments: {business, architectural, system, structural, functional[], deployment}
  delivery_id: string
  template_version: string      # p.ej. "7Cs v1.1 June 2026"
outputs:
  prompt_constitution: markdown # listo para pegar en /speckit.constitution
  prompt_specify: markdown      # listo para pegar en /speckit.specify
  clarify_input: markdown       # lista NEEDS CLARIFICATION ordenada por impacto
  plan_input: markdown          # contexto técnico "dado por la organización" para /speckit.plan
  trace_annex: tabla            # post_it_id | canvas | seccion | texto | regla | destino | id_req
guardrails:
  - Prohibido reescribir, resumir o "mejorar" el contenido de los fragmentos.
  - Prohibido resolver una duda: las dudas se numeran, no se resuelven.
  - Prohibido dejar tecnología en prompt_specify (se mueve a plan_input).
acceptance:
  - un prompt por entrega, autocontenido
  - cero nombres de producto o framework en prompt_specify
  - el anexo tiene exactamente una fila por post-it de la entrega
```

## Orden de ensamblado de `/speckit.specify`

1. Enunciado raíz (una frase: qué construir y qué reemplaza).
2. `CONTEXTO (BCC)` — del skill business-context.
3. `PERFILES (BCC/Business roles)` — con sus dudas inline.
4. `ALCANCE (BCC/System's functional areas + SCC)` — incluye "Fuera de alcance".
5. `ENTIDADES (BCC + Functional/Data objects)` — unificadas, atributos por confirmar.
6. `INTEGRACIONES (SCC)`.
7. `REQUISITOS` — FR de frontera (SCC) + FR por bundle con prefijos del censo
   (`INT`, `ETL`, `CMS`, …). Cada requisito conserva forma canónica, al menos un
   escenario Dado/Cuando/Entonces y su traza `←`.
8. `CRITERIOS DE ÉXITO (ACC)` — con dudas de métrica.
9. `RESTRICCIONES (ACC + Structural/Constraints)`.
10. `NFR DE OPERACIÓN (Deployment)`.
11. **Guardrail final dirigido al agente de Spec Kit** (última línea, literal):
    `NO incluir decisiones de tecnología en esta especificación: el contexto técnico se entrega por separado en /speckit.plan.`

**Todo párrafo declara su canvas de origen entre paréntesis.** Es la trazabilidad mínima
legible: quien revise la especificación puede volver al PDF sin preguntar.

## Deduplicación entre canvas

Un mismo hecho puede aparecer en dos canvas (p.ej. una restricción del ACC que genera un
FR compensatorio que reaparece en el Functional del bundle). **Se une por trazabilidad,
no se duplica**: un solo requisito con ambas trazas citadas (`← SCC/... ; causa: ACC/R-n`).
Los agrupadores (jerarquías de actores) se conservan; nunca se aplanan.

## Encaje con el flujo de Spec Kit

Inicialización previa (una vez por proyecto):
`uvx --from git+https://github.com/github/spec-kit.git specify init <PROYECTO>`
(o `specify init .` si se instaló con pipx). Cada entrega de canvas se trabaja en **su
propia rama de Git**, porque los comandos detectan la feature activa por la rama.

| Comando | Skill que lo alimenta | Contenido que se pega |
|---|---|---|
| `/speckit.constitution` | architectural + business | Principios P1–Pn y límites no negociables. Una sola vez por proyecto, antes de toda especificación |
| `/speckit.specify` | spec-compose (business + system + functional) | Contexto, perfiles, entidades, integraciones, FR con escenarios y criterios de éxito. **Sin una sola tecnología nombrada** |
| `/speckit.clarify` | spec-audit | Lista `[NEEDS CLARIFICATION]` ordenada por impacto |
| `/speckit.checklist` | spec-audit | Verificación de calidad: forma canónica, escenario por FR, traza por FR |
| `/speckit.plan` | structural + deployment | Capas, runtimes, proxy, BD, contenedores, redes y operación, marcados "dados por la organización". **Aquí y solo aquí** |
| `/speckit.tasks` | (derivado) | Tareas desde FR + plan; el prefijo por bundle evita duplicados |
| `/speckit.analyze` | spec-audit | Consistencia spec/plan/tareas + cobertura de canvas |
| `/speckit.implement` | — | Ejecución por fases; cada commit revisable contra su post-it |

**Regla de orden estricta:** nunca ejecutar `/speckit.plan` antes de haber cerrado las
dudas del `clarify`. Si el plan se genera con dudas abiertas, el agente elegirá por
omisión periodicidades, esquemas y permisos, y esas elecciones quedarán fijadas en las
tareas y en el código sin que nadie las haya decidido.

## Anexo de trazabilidad (obligatorio)

Tabla `post-it → requisito → tarea`, una fila por post-it de la entrega:

```
post_it_id | canvas | seccion | texto | regla | destino | id_req | tarea
E1-SCC-14  | system_context | User data input interfaces
           | "UI Carga manual archivos CSV (u-papers)"
           | R2 | spec.md#FR-002 | FR-002 | T-012
```

La fila es el registro atómico de la evidencia: permite responder "¿de dónde salió este
requisito?" y "¿qué pasó con este post-it?" en tiempo constante. Es el insumo del skill
de auditoría y la base de las métricas.
