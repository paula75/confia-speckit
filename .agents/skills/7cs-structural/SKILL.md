---
name: 7cs-structural
description: Skill de mapeo del pipeline 7Cs→Spec Kit. Convierte el COM de un Structural Canvas en contexto de arquitectura para /speckit.plan (capas, bundles, contratos de entrada/salida) — NUNCA en spec.md — más el censo de bundles que gobierna los Functional Canvas. Usar cuando exista un COM con canvas == "structural" dentro del pipeline 7Cs, o cuando el usuario pida mapear el Structural Canvas (bundles, componentes, interfaces entre capas) hacia Spec Kit.
---

# 7cs-structural — Mapeo · Structural Canvas (destino: `plan.md`)

**Decisión metodológica:** Spec Kit pide describir *qué* y *por qué* sin fijar el stack en
la especificación. Este canvas habla de tecnología: **no se vuelca en `spec.md`**, se
reserva para `/speckit.plan`. Volcarlo antes contamina la especificación y bloquea
alternativas de diseño. "PostgreSQL (Local)", "Docker CLI" o "Nginx" son decisiones de
solución: si se escriben como requisitos, cualquier `/speckit.analyze` posterior las
tratará como obligaciones del negocio. El skill las guarda para `/speckit.plan` con la
etiqueta **"dado por la organización"**.

Leer `references/reglas-reescritura.md` y `references/com-schema.md` antes de emitir salida.

## Contrato

```yaml
name: 7cs-structural
when_to_use: >
  El COM tiene canvas == "structural".
inputs:
  com: CanvasObjectModel        # única fuente de verdad; prohibido volver al PDF
  delivery_id: string
outputs:
  plan_fragment: markdown       # arquitectura en capas para /speckit.plan
  bundle_census: [ string ]     # lista de bundles declarados (índice del Functional)
  traces: [ {sticky_id, section, target_id} ]
  clarifications: [ string ]
procedure:
  1. Verificar las filas esperadas (5 capas × entrada/bundle/salida + Constraints).
  2. Para cada fila aplicar SU regla de mapeo (tabla fija).
  3. Levantar el censo de bundles: número e identidad exactos.
  4. Cotejar restricciones con las del Architectural Context.
  5. Emitir traza por post-it; secciones vacías → registro explícito.
guardrails:
  - Prohibido escribir NADA de este canvas en spec.md.
  - Prohibido inventar bundles, interfaces o configuraciones.
  - Texto literal del post-it siempre citado entre comillas.
acceptance:
  - traces.length == total_stickies
  - bundle_census emitido con conteo exacto
  - cero contenido de este canvas en el fragmento de spec
```

## Tabla de mapeo (una fila por sección; destino único)

| Fila del canvas | Qué produce el skill |
|---|---|
| Frontend bundles | Componentes de presentación en `plan.md` + qué perfil de usuario atiende cada uno |
| Backend bundles | Servicios y sus contratos |
| Repository bundles | Almacenes de datos y de archivos, con su modo de acceso |
| Platform & infrastructure | Piezas de plataforma (reverse proxy, contenedores) y su configuración declarada |
| Device bundles | Si está vacía → se reporta como "sin software desplegado en dispositivo", **una decisión, no un olvido** |
| Data input/output interfaces (por capa) | Contrato de entrada y de salida de cada capa |
| Constraints | Restricciones de arquitectura (despliegue, licenciamiento, límites de integración) |

## Reglas específicas de este skill

- **Censo de bundles.** El número de bundles declarados es el índice del Functional
  Canvas: **debe existir un Functional por bundle**, y este skill lo verifica. Si la
  entrega trae menos Functional que bundles, emitir
  `[NEEDS CLARIFICATION: falta detalle funcional de los bundles {nombres}]` **en lugar de
  imaginar pantallas o comportamientos**. Este es el hallazgo automático del chequeo
  cruzado.
- **Restricciones cruzadas.** Las restricciones de esta capa se cotejan con las del
  Architectural Context: si se contradicen, **prevalece la del Architectural Context** y
  la contradicción se reporta.
- **El vacío es evidencia.** Secciones sin post-it se registran en `empty_sections` y se
  declaran como decisión explícita del equipo, distinguiéndolas de un olvido. Dudas
  agrupadas por causa (tres celdas vacías del mismo bloque = 1 duda).

## Formato de salida

```markdown
 /speckit.plan (contexto dado, no elegido)
Arquitectura en capas:

Presentación   {bundles} · entrada: {…} · salida: {…}
Servicios      {bundles} · entrada: {…} · salida: {…}
Persistencia   {bundles} · entrada: {…} · salida: {…}
Plataforma     {bundles} · entrada: {…} · salida: {…}
Dispositivo    {bundles o "(sin bundles declarados)"}

Restricciones de arquitectura: {lista}

Censo de bundles ({n}): {lista exacta}
```

Cada línea con su traza. Cerrar con el balance del canvas y las dudas emitidas.
