# Auditoría arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm

Etapa D · 7cs-spec-audit. Insumos auditados: `composed/prompt_specify.md`, `composed/prompt_constitution.md`,
`composed/trace_annex.md` y los 8 COM de `com/`. `composed/plan_input.md` y `composed/compose_manifest.json`
se usaron solo como referencia cruzada (no son insumos normativos del contrato de auditoría).
Todas las métricas fueron recalculadas desde cero; no se confió en ningún reporte previo del compositor.

## Cobertura por canvas

| Canvas | Post-it (COM) | Trazas (anexo) | Dudas (FR/NFR/CE con `[NEEDS CLARIFICATION]`) |
|---|---|---|---|
| architectural_context | 59 | 59 | 13 |
| business_context | 51 | 51 | 0 |
| deployment | 22 | 22 | 3 |
| functional | 170 | 170 | 39 |
| structural | 30 | 30 | 0 |
| system_context | 31 | 31 | 17 |
| **Total** | **363** | **363** | **72** |

Post-it recontados directamente desde los 8 archivos de `com/` (suma de `stickies` por `section`), no desde el
manifiesto. `363 = 363`: cada `post_it_id` aparece en el anexo **exactamente una vez** (0 post-it con 2+ trazas,
0 post-it sin trazas, 0 filas del anexo que citen un `post_it_id` inexistente en los COM, 0 filas con `destino`
vacío o placeholder).

## Métricas

**C = 363/363 = 1.00 → OK.** Cobertura perfecta e igualdad exacta (no estimación). No hay post-it huérfanos.

**A = 72/182 ≈ 0.40.** Denominador = todos los identificadores de requisito emitidos en `prompt_specify.md`
(149 FR + 9 NFR + 12 R + 7 CE + 5 INT = 182). Un valor de 0.40 no es un fracaso del pipeline: refleja que casi
la mitad de lo emitido —sobre todo contratos de integración, jobs programados y métricas de éxito— depende de
información que el canvas no declaró. Ver `clarify_input.md` para el detalle numerado.

**T = 0 (lista negra: 0 coincidencias) → OK.** Lista negra construida desde los propios COM de Structural,
Deployment, `Technology stack` (functional) y `Technology standards & policies` (architectural_context): 25
términos de producto/framework/runtime (PostgreSQL, MongoDB, Docker, Node.js, cPython, Python, Javascript,
Nginx, GCP, Cloud Run, Cloud SQL, Cloud Function, Bucket, Linux, Object Storage, WhatsApp Business API,
WhatsApp, Meta Business Suite, LLM API, LLM, whatsapp business, Red GCP, Red docker, entre otros). Ninguno
aparece en `prompt_specify.md` ni en `prompt_constitution.md`. El reporte de reconstrucción
(`prompt_specify_reconstruction_report.md`) confirma que las menciones a WhatsApp/LLM/geolocalización fueron
sustituidas deliberadamente por capacidades neutrales ("canal de mensajería conversacional", "capacidad externa
de procesamiento", etc.) y trasladadas a `plan_input.md`.

**V = 149/149 = 1.00 → OK** (FR verificables, es decir, todos los FR). Los 5 INT de frontera también incluyen
escenario (5/5). NFR (0/9), R (0/12) y CE (0/7) no tienen escenario Dado/Cuando/Entonces — correcto por diseño:
son cualidades, reglas y metas, no comportamientos, y el skill exige escenario solo para FR de comportamiento.

Veredicto: **VÁLIDA** — C ≥ 1.00 y T = 0, únicas dos condiciones de rechazo automático definidas por el
contrato del skill. La corrida puede avanzar a `/speckit.clarify`, `/speckit.checklist` y `/speckit.plan`, con
las 72 dudas de `clarify_input.md` pendientes de resolución por el cliente y las observaciones de
`checklist_input.md` pendientes de revisión.

## Verificaciones adicionales (detalle en `checklist_input.md`)

- **Forma canónica de FR:** sin verbos prohibidos sin objeto ("gestionar", "manejar", "soportar") en los 149 FR. OK.
- **Colisiones de identificador:** 0 identificadores FR duplicados entre bundles (AC/BA/BW/SCC). OK.
- **Traza `←` inline en todo FR/NFR/CE/R:** **INCUMPLE parcialmente.** Los 149 FR, los 12 R y los 3 NFR-OP
  citan su traza inline (`← Canvas / Sección "texto"`). Los **7 CE y los 6 NFR-TEC (13 bloques) no citan traza
  inline**, aunque la traza existe en `trace_annex.md` (post-it `P2BGD-*` → `spec:CE-*`; post-it `P2TGD-*` →
  `spec:NFR-TEC-*`). Es un defecto de formato en `prompt_specify.md`, no de cobertura: C sigue en 1.00 porque se
  calculó contra el anexo, pero un lector de `spec.md` sin el anexo abierto no puede verificar de dónde salieron
  esas 13 líneas.
- **Idempotencia:** `audit/` estaba vacío al iniciar esta corrida (sin auditoría previa contra la cual comparar
  IDs FR-nnn). Esta corrida queda como línea base para la próxima reejecución.
- **Censo de bundles (Structural↔Deployment↔Functional):** discrepancia ya señalada por el compositor en
  `plan_input.md` (Structural declara 10 bundles; Deployment declara 5; Functional cubre 3 de los 10). Se
  reporta aquí de nuevo porque sigue sin resolverse; la auditoría no la corrige.
- **Metadato desactualizado:** `compose_manifest.json` declara `"clarifications": 94`, pero el recuento real en
  `composed/` es 78 (72 en `prompt_specify.md` + 6 en `plan_input.md`, estos últimos duplicados de los mismos
  requisitos con nombre de tecnología). El manifiesto no refleja la reconstrucción posterior documentada en
  `prompt_specify_reconstruction_report.md`. No bloquea el veredicto, pero es evidencia de que el manifiesto no
  debe tomarse como fuente de métricas — motivo por el cual esta auditoría recalculó todo desde cero.

## Lectura del resultado

El canvas cubre bien el **qué existe**: los 6 bundles/canales, sus 149 interacciones funcionales y las 12
restricciones de negocio tienen post-it, traza y (donde aplica) escenario Dado/Cuando/Entonces completos, sin
una sola mención de producto o proveedor filtrada hacia la especificación. Lo que el canvas cubre mal es el
**cuánto y cuándo**: 47 de las 72 dudas son contratos de integración (esquema, contraparte, error) sin
declarar, 9 son tareas programadas sin periodicidad ni comportamiento ante fallo, y las 13 métricas de éxito y
calidad (CE + NFR-TEC) no tienen línea base ni umbral. El pipeline no inventa esos valores: los deja visibles
como preguntas numeradas en `clarify_input.md` antes de que alguien los decida escribiendo código.
