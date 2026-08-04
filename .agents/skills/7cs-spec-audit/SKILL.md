---
name: 7cs-spec-audit
description: Etapa C del pipeline 7Cs→Spec Kit (verificación). Recalcula las métricas C (cobertura), A (ambigüedad), T (contaminación técnica) y V (verificabilidad) sobre el prompt compuesto y su anexo de trazas, exige una traza por post-it y FALLA la corrida si la cobertura es menor que 1,00 o hay contaminación técnica mayor que cero. Alimenta /speckit.clarify, /speckit.checklist y /speckit.analyze. Usar después de 7cs-spec-compose, o cuando el usuario pida "auditar la especificación", "calcular cobertura", "validar las trazas" o verificar una corrida del pipeline 7Cs.
---

# 7cs-spec-audit — Etapa C · Auditoría

Este skill hace **científico** el pipeline: sin sus métricas no hay medición ni
refutación. Recalcula cobertura desde cero (no confía en los reportes de los skills de
mapeo), exige trazas y **declara inválida la corrida** si queda un post-it sin destino.

## Contrato

```yaml
name: 7cs-spec-audit
when_to_use: >
  Existe un prompt compuesto por 7cs-spec-compose con su anexo de trazabilidad.
  Ejecutar antes de pegar nada en Spec Kit; reejecutar tras /speckit.tasks
  para alimentar /speckit.analyze.
inputs:
  prompt_specify: markdown
  prompt_constitution: markdown
  trace_annex: tabla
  coms: [CanvasObjectModel]     # para recontar post-it de forma independiente
outputs:
  audit_report: markdown        # métricas C, A, T, V + veredicto
  clarify_input: markdown       # dudas ordenadas por impacto, para /speckit.clarify
  checklist_input: markdown     # verificaciones para /speckit.checklist
  verdict: "valida" | "invalida"
guardrails:
  - Prohibido corregir la especificación: la auditoría reporta, no arregla.
  - Prohibido cerrar una duda por cuenta propia.
acceptance:
  - la corrida se declara inválida si C < 1.00 o T > 0
  - la auditoría falla a propósito en una prueba con un post-it borrado
    (prueba de sanidad del propio auditor)
```

## Las cuatro métricas

**C · Cobertura** = trazas / post-it. **Meta: 1,00.** Es una igualdad, no una estimación:
recontar los post-it directamente desde los COM y verificar que cada `post_it_id` aparece
exactamente en una fila del anexo con destino no vacío. Si C < 1, **rechazar la corrida**
y listar los post-it huérfanos.

**A · Índice de ambigüedad** = dudas / requisitos emitidos. Un valor alto **no es un
fracaso del pipeline**: es una medición honesta de cuánto le falta al canvas para ser
desarrollable. Reportarlo sin maquillarlo.

**T · Contaminación técnica** = menciones de producto o framework en la parte de spec.
**Meta estricta: 0.** Verificar con una **lista negra construida desde los propios
canvas**: extraer de los COM de Structural, Deployment, Technology standards y Technology
stack todos los nombres de producto/framework/runtime, y buscar cada uno en
`prompt_specify` y en los fragmentos destinados a `spec.md`. Cualquier aparición → T > 0
→ corrida inválida (la mención debe moverse a `plan.md`).

**V · Verificabilidad** = FR con al menos un escenario Dado/Cuando/Entonces / total de FR.
**Meta: 1,00 para los FR de comportamiento.** Los FR de integración sin escenario
derivable quedan marcados como duda, no se les inventa escenario.

## Verificaciones adicionales (checklist_input)

- Forma canónica en todo FR: sujeto + DEBE + verbo observable + objeto + condición.
  Detectar verbos prohibidos sin objeto: "gestionar", "manejar", "soportar".
- Traza `←` presente en todo FR, NFR, CE y R.
- Prefijo de bundle en todos los FR de bundle; sin colisiones de identificadores.
- Idempotencia: si hay una corrida previa, comparar identificadores FR-nnn (deben
  coincidir para el mismo COM).
- Chequeos cruzados reportados: censo de bundles Structural↔Deployment↔Functional.
- Ausencias esperables señaladas (respaldo, monitoreo, disponibilidad, seguridad,
  accesibilidad si no aparecen en los canvas) — se reportan para que se pregunten
  explícitamente, nunca se completan.

## Salida para /speckit.clarify

Lista de todas las `[NEEDS CLARIFICATION]` **ordenadas por impacto en el plan**
(primero las que bloquean decisiones de `/speckit.plan`: periodicidades de jobs,
esquemas de archivos, permisos por rol, métricas de metas; después las de menor
impacto). Las dudas se numeran, no se resuelven: son preguntas para el cliente, y sin
respuesta la especificación queda incompleta **por diseño**.

## Formato del reporte

```markdown
# Auditoría {delivery_id}

| Canvas | Post-it | Trazas | Dudas |
|---|---|---|---|
| ... | n | n | n |
| **Total** | N | N | D |

C = {trazas}/{post-it} = {valor}   → {ok | RECHAZO: post-it huérfanos: ...}
A = {dudas}/{requisitos} ≈ {valor}
T = {menciones} (lista negra: {términos detectados})  → {ok | RECHAZO}
V = {FR con escenario}/{FR} = {valor}

Veredicto: {VÁLIDA | INVÁLIDA — motivos}

Lectura del resultado: {qué cubre bien el canvas (el "qué existe") y qué cubre mal
(el "cuánto y cuándo")}. El pipeline no lo arregla: lo hace visible antes de escribir
código.
```

## Criterio de detención del pipeline

El pipeline se declara insuficiente si, con dudas cerradas por el equipo,
`/speckit.analyze` reporta inconsistencias que se explican por el mapeo y no por el
canvas. Ese caso es un **defecto de regla** y se corrige en la tabla del skill de mapeo
correspondiente, no improvisando en el prompt.
