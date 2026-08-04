---
name: 7cs-functional
description: Skill de mapeo del pipeline 7Cs→Spec Kit. Convierte cada COM de un Functional Canvas (uno por bundle; puede haber varios por entrega) en requisitos funcionales FR con prefijo de bundle, entidades, escenarios Dado/Cuando/Entonces y dudas para /speckit.specify, más stack por bundle para /speckit.plan. Usar cuando exista un COM con canvas == "functional" dentro del pipeline 7Cs, o cuando el usuario pida derivar requisitos funcionales desde Functional Canvas.
---

# 7cs-functional — Mapeo · Functional Canvas (×N bundles)

**El skill itera, no promedia.** Se ejecuta **una vez por cada Functional Canvas** y
prefija los identificadores con el bundle (`FR-ETL-001`, `FR-CMS-001`, `FR-INT-001`).
Sin ese prefijo, dos bundles que leen la misma entidad producen requisitos
indistinguibles y `/speckit.tasks` genera trabajo duplicado. Los prefijos vienen del
censo del Structural Canvas.

**Geometría del canvas = forma del requisito.** Cada sección genera un requisito
funcional de una naturaleza particular (ver tabla).

Leer `references/reglas-reescritura.md` y `references/com-schema.md` antes de emitir salida.

## Contrato

```yaml
name: 7cs-functional
when_to_use: >
  El COM tiene canvas == "functional". Ejecutar una vez por instancia
  (una por bundle), con el censo del Structural como referencia de prefijos.
inputs:
  com: CanvasObjectModel        # única fuente de verdad; prohibido volver al PDF
  delivery_id: string
  bundle_census: [ string ]     # del skill 7cs-structural, para prefijos y chequeo
outputs:
  fragment: markdown            # §FR del bundle, §Key Entities, escenarios
  plan_context: markdown        # Technology stack + constraints locales, para /speckit.plan
  traces: [ {sticky_id, section, target_id} ]
  clarifications: [ string ]
procedure:
  1. Identificar el bundle (Bundles & components) y su prefijo desde el censo.
  2. Verificar secciones esperadas. Vacías → registrar (pueden ser coherentes).
  3. Para cada sección aplicar SU regla de mapeo (tabla fija).
  4. Normalizar cada post-it a la forma canónica (R1–R7); escenario por FR.
  5. Emitir traza por post-it. Nunca fusionar, salvo la excepción de calidad.
guardrails:
  - Prohibido inventar atributos de entidades, periodicidades o esquemas.
  - Prohibido escribir stack en el fragmento de spec (va a plan_context).
  - Texto literal del post-it siempre citado entre comillas.
acceptance:
  - traces.length == total_stickies
  - todo FR de comportamiento tiene al menos un escenario Dado/Cuando/Entonces
  - todos los FR llevan el prefijo del bundle
```

## Tabla de mapeo (una fila por sección; destino único)

| Sección | Qué produce el skill |
|---|---|
| Bundles & components | Agrupador del bloque de FR; se enlaza con el censo del Structural |
| Data objects | **§Key Entities** con atributos por confirmar |
| User inputs · UI-processing inputs | FR iniciados por persona; si están vacíos y el bundle no tiene interfaz humana, se reportan como **coherentes, no como omisión** |
| API inputs | FR de recepción por contrato (query requests, command endpoints, callback) |
| Data imports · exports | FR de lectura y de persistencia observables |
| Jobs | **FR con disparador temporal**: un FR por job + duda de periodicidad si no está declarada |
| Event handlers · Event triggers | FR reactivos y notificaciones |
| Helpers | Reglas de validación y cálculo → FR de calidad de datos |
| User visualizations / reports | FR de visualización; si está vacío → duda de alcance de UI |
| Technology stack · Constraints | `plan.md` por bundle + restricciones locales. Fuera de `spec.md` |

## Reglas específicas de este skill

- **Fusión permitida, con regla.** Se permite combinar dos post-it en un FR **solo**
  cuando uno es condición de calidad del otro (p.ej. un import de datos + su validador),
  y **ambas trazas quedan citadas**. Fuera de ese caso: un post-it → un requisito.
- **Los jobs son la mina de NFR.** Todo job implica periodicidad, ventana de ejecución y
  comportamiento ante fallo. El canvas casi nunca los declara: emitir
  `[NEEDS CLARIFICATION: periodicidad no declarada en el canvas]` por cada uno.
  **Nunca** escribir una frecuencia inventada.
- **Entidades sin atributos.** Un nombre no es un esquema. Declarar la entidad y dejar
  los atributos abiertos: inventarlos es el modo de falla más costoso, porque
  `/speckit.plan` los convierte en tablas.
- **Secciones vacías con sentido.** Evaluar coherencia: un bundle sin interfaz humana con
  *User inputs* vacío es coherente; un bundle de UI con *User visualizations* vacío es una
  duda de alcance.

## Formato de salida

```markdown
### Bundle: {nombre} (Functional, p. {n})

Entidades: {lista} ← Data objects ({n} post-it, atributos por confirmar)

FR-{PREFIJO}-001 El sistema DEBE {verbo observable} {objeto} {condición}.
  ← {sección} "{texto literal}" [+ "{segundo post-it}" si fusión de calidad]
  Escenario: Dado ..., cuando ..., entonces ...
  [NEEDS CLARIFICATION: ...]
...

 contexto para /speckit.plan (bundle {nombre})
Stack declarado: {tecnologías literales} · Constraints locales: {lista}
```

Cerrar con el balance de los Functional de la entrega: post-it, FR con prefijo,
entidades, dudas; y si el censo del Structural indica bundles sin canvas, repetir la
duda de alcance correspondiente.
