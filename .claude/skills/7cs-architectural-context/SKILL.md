---
name: 7cs-architectural-context
description: Skill de mapeo del pipeline 7Cs→Spec Kit. Convierte el COM de un Architectural Context Canvas en principios para /speckit.constitution y en criterios de éxito, restricciones y NFR para /speckit.specify, con trazas y dudas [NEEDS CLARIFICATION]. Usar cuando exista un COM con canvas == "architectural_context" dentro del pipeline 7Cs, o cuando el usuario pida mapear el Architectural Context Canvas (principios, metas, estándares, restricciones) a Spec Kit.
---

# 7cs-architectural-context — Mapeo · Architectural Context Canvas

**Por qué este canvas va primero a la constitución:** en Spec Kit la constitución se
declara antes de cualquier especificación y condiciona a todas las siguientes. Los
principios del canvas son reglas transversales del proyecto: si se dejaran en `spec.md`
se repetirían en cada feature y se contradecirían entre ramas.

**Frontera fina:** las tecnologías nombradas ("Servidores Linux", "Proxy Nginx",
"BD PostgreSQL", "Docker") son **restricciones impuestas**, no elecciones del equipo.
Van a `plan.md` como contexto técnico dado, y a `constitution.md` como límite no
negociable. Nunca a `spec.md`.

Leer `references/reglas-reescritura.md` y `references/com-schema.md` antes de emitir salida.

## Contrato

```yaml
name: 7cs-architectural-context
when_to_use: >
  El COM tiene canvas == "architectural_context".
inputs:
  com: CanvasObjectModel        # única fuente de verdad; prohibido volver al PDF
  delivery_id: string
outputs:
  fragment: markdown            # criterios de éxito, restricciones y NFR para /speckit.specify
  constitution_lines: markdown  # principios P1..Pn para /speckit.constitution
  plan_context: markdown        # tecnologías dadas, para /speckit.plan
  traces: [ {sticky_id, section, target_id} ]
  clarifications: [ string ]
procedure:
  1. Verificar secciones esperadas (10). Faltantes → clarification.
  2. Para cada sección aplicar SU regla de mapeo (tabla fija).
  3. Normalizar cada post-it a una frase verificable (R1–R7).
  4. Emitir traza por post-it. Sin traza no hay salida.
  5. Nunca fusionar dos post-it en un requisito.
guardrails:
  - Prohibido inventar métricas, porcentajes o líneas base.
  - Prohibido escribir nombres de producto en el fragmento de spec (regla R-T).
  - Texto literal del post-it siempre citado entre comillas.
acceptance:
  - traces.length == total_stickies
  - fragment sin nombres de productos ni frameworks
  - toda meta sin número lleva su duda de métrica adjunta
```

## Tabla de mapeo (una fila por sección; destino único)

| Sección del canvas | Qué produce el skill |
|---|---|
| Stakeholders | Lista de quién valida la aceptación de cada requisito |
| Business strategy | `constitution.md` § Objetivos de la organización |
| IT strategy | `constitution.md` § Principios de plataforma (centralización, control de la arquitectura) |
| Business goals & drivers | **§Criterios de éxito medibles**: cada meta exige una métrica → se emite duda por cada meta sin número |
| Technology goals & drivers | NFR de integración y estandarización del ecosistema |
| Business standards & policies | Restricciones de proyecto (p.ej. uso exclusivo de software open-source o académico) |
| Technology standards & policies | `plan.md` § Contexto técnico dado; en `spec.md` **solo lo observable** (p.ej. "autenticación mediante el sistema institucional", sin nombre de producto) |
| Situational constraints | **§Restricciones**; una imposibilidad externa es la causa raíz de un FR compensatorio (R7) |
| Business principles | `constitution.md` § Principios |
| Technical principles | `constitution.md` § Principios técnicos |

## Reglas específicas de este skill

- **Regla de cuantificación (R-Q).** Todo post-it que empiece con un verbo de mejora
  ("reducir", "mejorar", "facilitar") es una **meta**, no un requisito. Se convierte en
  criterio de éxito CE-n y se adjunta la duda de métrica
  `[NEEDS CLARIFICATION: ¿medido cómo? ¿métrica y línea base?]`. **Nunca inventar un
  porcentaje.**
- **Regla de causa raíz (R-C).** Una restricción situacional se traduce en requisito solo
  si implica comportamiento observable. Ese FR compensatorio reaparecerá en el Functional
  Canvas del bundle correspondiente: ahí **se une por trazabilidad, no se duplica**
  (citar la restricción como causa: `causa: ACC/R-n`).
- **Regla de anonimización tecnológica (R-T).** En `spec.md` escribir la capacidad
  ("sistema institucional de identidad"); el nombre del producto queda en `plan.md`.
  Así la especificación sigue siendo válida si la organización cambia de proveedor.

## Formato de salida

```markdown
 /speckit.constitution
P1 {principio}: {enunciado}. [ACC/{sección}]
P2 ...

 /speckit.specify · Criterios de éxito
CE-1 {meta}. [NEEDS CLARIFICATION: ¿medido cómo?]
...

 /speckit.specify · Restricciones
R-1 {restricción observable}.
...

 contexto para /speckit.plan (dado por la organización)
{tecnologías citadas literalmente, con su traza}
```

Cerrar con el balance del canvas: n principios, n criterios de éxito, n restricciones,
n dudas · {post-it} post-it en {secciones} secciones, {trazas} trazas.
