---
name: 7cs-business-context
description: Skill de mapeo del pipeline 7Cs→Spec Kit. Convierte el COM de un Business Context Canvas en fragmentos para /speckit.constitution (misión) y /speckit.specify (§Contexto, §Perfiles, §Key Entities, índice de requisitos), con trazas post-it→destino y dudas [NEEDS CLARIFICATION]. Usar cuando exista un COM con canvas == "business_context" dentro del pipeline 7Cs, o cuando el usuario pida mapear el Business Context Canvas a una especificación Spec Kit. Se ejecuta antes que cualquier otro skill de mapeo.
---

# 7cs-business-context — Mapeo · Business Context Canvas

**Regla de oro de este canvas:** describe el negocio, no el software. Sus post-it **no son
requisitos**; solo *System's functional areas* declara alcance del sistema. Este skill NO
produce ningún requisito funcional numerado: los FR nacen del Functional Canvas.

Leer `references/reglas-reescritura.md` (R1–R7 y forma canónica) y
`references/com-schema.md` antes de emitir salida.

## Contrato

```yaml
name: 7cs-business-context
when_to_use: >
  El COM tiene canvas == "business_context".
  Se ejecuta antes que cualquier otro skill de mapeo.
inputs:
  com: CanvasObjectModel        # única fuente de verdad; prohibido volver al PDF
  delivery_id: string           # p.ej. "E1"
outputs:
  fragment: markdown            # texto para /speckit.specify
  constitution_lines: markdown  # texto para /speckit.constitution
  traces: [ {sticky_id, section, target_id} ]
  clarifications: [ string ]
procedure:
  1. Verificar secciones esperadas (9). Faltantes → clarification.
  2. Para cada sección aplicar SU regla de mapeo (tabla fija).
  3. Normalizar cada post-it a una frase verificable (R1–R7).
  4. Emitir traza por post-it. Sin traza no hay salida.
  5. Nunca fusionar dos post-it en un requisito.
guardrails:
  - Prohibido inventar actores, cifras o tecnologías.
  - Prohibido escribir stack en el fragmento de spec.
  - Texto literal del post-it siempre citado entre comillas.
acceptance:
  - traces.length == total_stickies
  - fragment sin nombres de productos ni frameworks
  - cero requisitos funcionales numerados en la salida
```

## Tabla de mapeo (una fila por sección; destino único)

El skill no puede escribir en un destino ausente de esta tabla, ni dejar una sección sin destino.

| Sección del canvas | Qué produce el skill |
|---|---|
| Business products & services | Enunciado de propósito en `constitution.md` y §Contexto de `spec.md` |
| Business units & actors | Lista de actores organizacionales; los agrupadores ("Público general") **se conservan como jerarquía**, no se aplanan |
| Business roles | Perfiles de usuario con permisos a especificar; si el canvas no declara permisos → `[NEEDS CLARIFICATION: permisos de cada perfil no declarados en el canvas]` |
| Business objects | §Key Entities: una entidad por post-it, **atributos abiertos** (el canvas da nombres, no esquemas; inventar campos es el error más caro porque el plan los convierte en tablas) |
| Business processes | Escenarios de usuario (uno por proceso) que luego generan FR verificables. **No** convertirlos en FR aquí: confundir procesos con requisitos funcionales duplica requisitos que reaparecen en el Functional Canvas y rompe el conteo de cobertura |
| Business functions | Agrupadores de requisitos (épicas): estructuran, no obligan |
| Business infrastructure & equipment | Canales y dispositivos de salida obligatorios (contexto, no FR) |
| Business locations / facilities | Contexto de uso; solo entra en `spec.md` si condiciona un requisito observable |
| System's functional areas | **Índice de §Requisitos**: cada área es una subsección obligatoria. El índice manda: todo FR posterior debe caer en una de ellas o justificar una nueva |

## Reglas específicas

- **La cabecera vacía también es un dato.** Si System/Organization/Version/Date están
  `null`, emitir una duda de identificación del artefacto (una sola, agrupada).
- Procesos y funciones se tratan distinto: los procesos generan escenarios; las funciones
  agrupan requisitos.
- El fragmento se estructura así (formato de salida):

```markdown
 fragmento para /speckit.constitution
Propósito: {enunciado citando entre comillas los post-it de Business products & services}
  ← BCC / Business products & services ({n} post-it)

 fragmento para /speckit.specify
## Contexto
{prosa con objetos de negocio y actores; agrupadores conservados como jerarquía}

## Perfiles de usuario
{lista de Business roles} [NEEDS CLARIFICATION: permisos de cada perfil...]

## Entidades clave
{una por post-it de Business objects} ← BCC / Business objects ({n} post-it, sin atributos declarados)

## Índice de requisitos (System's functional areas)
1..N {áreas} ← BCC / System's functional areas ({n} post-it)
```

- Cada bloque cierra con su flecha de traza `← BCC / {sección} ({n} post-it)`.
- La tabla `traces` acompaña la salida: `sticky_id | destino trazado`
  (p.ej. `E1-BPS-01 → constitution § Propósito`, `E1-BUA-06 → spec § Contexto (actor,
  hijo de "Público general")`).
