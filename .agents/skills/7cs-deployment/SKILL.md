---
name: 7cs-deployment
description: Skill de mapeo del pipeline 7Cs→Spec Kit. Convierte el COM de un Deployment Canvas en contexto de infraestructura y operación para /speckit.plan y en los pocos NFR de operación observables que sí ascienden a /speckit.specify, con chequeo cruzado contra el censo de bundles. Usar cuando exista un COM con canvas == "deployment" dentro del pipeline 7Cs, o cuando el usuario pida mapear el Deployment Canvas (entornos, runtime, redes, instalación, operación) hacia Spec Kit.
---

# 7cs-deployment — Mapeo · Deployment Canvas

**Reparto típico del canvas:** la gran mayoría de los post-it van a `plan.md`. Solo unos
pocos ascienden a la especificación, como NFR de operación.

**Criterio para ascender un post-it a `spec.md`:** sube solo si describe algo
**observable por la organización**: instalar, operar, soportar. Todo lo demás — proxy,
contenedores, hardware, redes — es solución y se queda en `plan.md`.

Leer `references/reglas-reescritura.md` y `references/com-schema.md` antes de emitir salida.

## Contrato

```yaml
name: 7cs-deployment
when_to_use: >
  El COM tiene canvas == "deployment".
inputs:
  com: CanvasObjectModel        # única fuente de verdad; prohibido volver al PDF
  delivery_id: string
  bundle_census: [ string ]     # del skill 7cs-structural, para el chequeo cruzado
outputs:
  fragment: markdown            # NFR-OP-n para /speckit.specify
  plan_fragment: markdown       # §Infra, topología, empaquetado, operación para /speckit.plan
  traces: [ {sticky_id, section, target_id} ]
  clarifications: [ string ]
procedure:
  1. Verificar las 15 secciones esperadas. Faltantes/vacías → registro con causa.
  2. Para cada sección aplicar SU regla de mapeo (tabla fija).
  3. Aplicar el criterio de ascenso: solo lo observable sube a spec.md.
  4. Chequeo cruzado con el censo de bundles del Structural.
  5. Emitir traza por post-it; reportar ausencias esperables.
guardrails:
  - Prohibido inventar objetivos de disponibilidad, respaldo o monitoreo no declarados.
  - Prohibido escribir nombres de producto en el fragmento de spec.
  - Texto literal del post-it siempre citado entre comillas.
acceptance:
  - traces.length == total_stickies
  - fragment (spec) contiene solo NFR observables por la organización
  - chequeo cruzado bundle_census ejecutado y reportado
```

## Tabla de mapeo (una fila por sección; destino único)

| Sección | Qué produce el skill |
|---|---|
| Environments | **NFR de operación en `spec.md`**: qué entornos deben existir y qué se promueve entre ellos. Un solo entorno declarado → `[NEEDS CLARIFICATION: entornos de prueba]` |
| Bundles | Unidades desplegables; **se cotejan con el censo del Structural (deben coincidir)** |
| Middleware · Runtime | `plan.md` § Contexto técnico: proxy, base de datos, runtimes por bundle |
| Orchestration · Container runtimes | `plan.md` § Empaquetado y orquestación |
| Operating systems · Virtualization | `plan.md`; conservar verificaciones declaradas (p.ej. "verificación en variantes de Linux") como criterio de prueba |
| Cloud abstractions | Si está vacía y existe restricción on-premise → se reporta como **coherente**, no como omisión |
| Hardware · Locations · Networks | `plan.md` § Topología |
| Installation · Operation | **NFR de operación**: instalación automatizada, verificación por variantes, quién opera |
| Constraints | Restricciones (autenticación institucional, licenciamiento, reutilización de plataforma, gobierno de la operación) |

## Reglas específicas de este skill

- **Chequeo cruzado con el Structural.** Las unidades desplegables deben coincidir con el
  censo de bundles; cualquier bundle que aparezca aquí y no allí (o al revés) es una
  **inconsistencia reportable**, nunca corregida en silencio.
- **Quién opera importa.** El responsable de operación ("Área de Sistemas") es un
  **requisito de operación**, no un dato administrativo: produce un NFR-OP.
- **Nótese la ausencia.** Si el canvas no declara respaldo, monitoreo ni disponibilidad,
  el hallazgo se reporta como **ausencia esperable** para que se pregunte, en vez de
  inventar un objetivo de disponibilidad.

## Formato de salida

```markdown
 fragmento para /speckit.specify
NFR-OP-1 La instalación DEBE ser reproducible y automatizada, sin pasos manuales
  no documentados.
  ← Deployment / Installation "{texto literal}"
NFR-OP-2 La operación DEBE poder ejecutarla {responsable declarado}, sin dependencia
  del equipo de desarrollo.
  ← Deployment / Operation "{texto literal}" [+ traza ACC si refuerza]
NFR-OP-3 El sistema DEBE funcionar en {condición de entorno declarada}.
  ← Deployment / Installation "{texto literal}"
  [NEEDS CLARIFICATION: {lista de variantes/versiones soportadas}]

 fragmento para /speckit.plan
§ Infra y operación: entornos, empaquetado, topología, instalación, operación.
Ausencias esperables reportadas: respaldo, monitoreo, disponibilidad (si aplica).
```

Cerrar con el balance: n post-it, n a `plan.md`, n NFR en `spec.md`, n dudas.
