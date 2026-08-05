# Insumo para /speckit.checklist

Delivery ID: `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm`

Verificaciones de la metodología 7Cs→Spec Kit ejecutadas contra `composed/` y `com/`. Cada ítem indica
`OK` / `INCUMPLE` / `OBSERVACIÓN` y la evidencia exacta. No se corrigió nada: la auditoría reporta.

## 1. Cobertura y trazabilidad

- [x] **OK** — Cobertura completa de post-it: 363/363 post-it de los 8 COM tienen exactamente una fila en
  `trace_annex.md` con `destino` no vacío. C = 1.00.
- [x] **OK** — Exactamente una traza por post-it: 0 post-it con 2+ trazas, 0 post-it sin trazas.
- [x] **OK** — 0 filas del anexo referencian un `post_it_id` inexistente en los COM (0 trazas "fantasma").
- [x] **OK** — Los 182 identificadores de requisito (`FR-*`, `NFR-*`, `R-*`, `CE-*`, `INT-*`) de
  `prompt_specify.md` tienen exactamente una fila `id_req` correspondiente en `trace_annex.md`, y viceversa.

## 2. Ausencia de contaminación técnica

- [x] **OK** — 0 coincidencias en `prompt_specify.md` ni `prompt_constitution.md` contra la lista negra de 25
  términos de producto/framework/runtime extraída de Structural, Deployment, `Technology stack` y
  `Technology standards & policies`. T = 0.
- [x] **OK** — Las 5 integraciones de frontera (`INT-1`…`INT-5`) y sus FR equivalentes (`FR-SCC-001/002`) usan
  capacidades neutrales ("servicio externo de mensajería conversacional", "servicio externo de procesamiento",
  "servicio externo de geolocalización") en vez de nombrar WhatsApp/LLM/proveedor de mapas — confirmado también
  por `prompt_specify_reconstruction_report.md`.

## 3. Verificabilidad

- [x] **OK** — 149/149 FR tienen escenario Dado/Cuando/Entonces. V = 1.00.
- [x] **OK** — Los 5 INT de frontera también tienen escenario (5/5), aunque no son FR estrictos.
- [x] **OBSERVACIÓN** — NFR (0/9), R (0/12) y CE (0/7) no tienen escenario. Es el comportamiento esperado del
  skill (solo los FR de comportamiento requieren escenario), no un defecto.

## 4. Forma canónica de los requisitos

- [x] **OK** — 0 líneas de FR usan verbos prohibidos sin objeto ("gestionar", "manejar", "soportar").
- [x] **OK** — 0 identificadores FR duplicados/colisionados entre bundles (AC-001…050, BA-001…037,
  BW-001…044, SCC-001…018 son todos únicos).
- [x] **OK** — Todo FR sigue el patrón "El sistema DEBE + verbo observable + objeto"; los 12 R siguen "El
  proyecto DEBE/NO DEBE + verbo + objeto".
- [ ] **INCUMPLE** — Traza `←` inline presente en todo FR, NFR, CE y R: los 149 FR, los 3 NFR-OP y los 12 R sí
  la citan; los **7 CE (`CE-1`…`CE-7`) y los 6 NFR-TEC (`NFR-TEC-1`…`NFR-TEC-6`) no citan la línea `← Canvas /
  Sección`** en `prompt_specify.md`, aunque la traza sí existe en `trace_annex.md` (post-it `P2BGD-01`…`07` →
  `spec:CE-1`…`7`; post-it `P2TGD-01`…`06` → `spec:NFR-TEC-1`…`6`). 13 bloques afectados. No afecta la métrica
  C (calculada contra el anexo), pero rompe la trazabilidad legible dentro de `spec.md` mismo.

## 5. Chequeos cruzados de bundles

- [x] **OBSERVACIÓN** (heredada, no generada por esta auditoría) — Censo de bundles: Structural declara 10
  bundles, Deployment declara 5, Functional cubre 3 (Agente conversacional, Backend Agendamiento,
  Backend/Frontend Web). La discrepancia ya está señalada en `plan_input.md` §"Chequeo cruzado de bundles" y
  sigue sin resolverse. Se reafirma aquí porque el contrato de auditoría exige reportarla explícitamente.

## 6. Ausencias esperables

- [ ] **AUSENTE** — Respaldo/backup: 0 menciones en los 8 COM.
- [ ] **AUSENTE** — Monitoreo operativo observable: solo aparece como principio técnico ("Observabilidad
  mediante logging y monitoreo", `P2TP-07` → `constitution:P22`); no hay NFR de monitoreo en
  `prompt_specify.md`.
- [x] **PRESENTE** — Disponibilidad: `NFR-TEC-1` "Alta disponibilidad" y `NFR-OP-3` "Alta disponibilidad de
  servicio" (ambos con duda de umbral abierta, ver `clarify_input.md` Bloques 6–7).
- [x] **PRESENTE** — Seguridad: `NFR-TEC-3` (con duda de criterio/umbral abierta).
- [ ] **AUSENTE** — Accesibilidad: 0 menciones en los 8 COM, incluyendo el bundle con interfaz humana directa
  ("Backend/Frontend Web", constraints declaradas: "GUI amigable", "Recibir derivación de LLM para atención
  humana" — ninguna menciona accesibilidad).
- [ ] **AUSENTE** — Responsable/procedimiento de operación más allá de `NFR-OP-2` "Deploy manual coordinado por
  Área de Sistemas" (que a su vez tiene duda abierta sobre pasos, aprobaciones y reversión).

## 7. Ambigüedad no marcada formalmente

- [ ] **OBSERVACIÓN** — §Perfiles de usuario declara 4 roles con "permisos no declarados" en prosa, sin la
  marca `[NEEDS CLARIFICATION]`. Incluido en `clarify_input.md` Bloque 4 pese a la omisión de marca, porque el
  propio skill de auditoría nombra "permisos por rol" como categoría de alto impacto.
- [ ] **OBSERVACIÓN** — 21 entidades con "atributos abiertos" / "atributos por confirmar", sin marca formal.
- [ ] **OBSERVACIÓN** — 8 escenarios de negocio (`EN-01`…`EN-08`) con actor/precondición/resultado "por
  confirmar", sin marca formal y explícitamente excluidos del conteo de FR ("no son FR").
- [ ] **OBSERVACIÓN** — `compose_manifest.json` declara `"clarifications": 94`; el recuento real verificado en
  `composed/` es 78 (72 en `prompt_specify.md` + 6 en `plan_input.md`). El manifiesto quedó desactualizado tras
  la reconstrucción documentada en `prompt_specify_reconstruction_report.md` y no debe usarse como fuente de
  métricas.

## 8. Idempotencia

- [x] **N/A para esta corrida** — `audit/` estaba vacío antes de esta ejecución (sin auditoría previa con la
  cual comparar identificadores `FR-nnn`). Esta corrida es la línea base: toda reejecución futura debe comparar
  contra los identificadores aquí confirmados (149 FR únicos, sin colisiones, ver sección 4).
