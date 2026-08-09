# Tasks: Gestión Integral de Reservas — Feature "Gestión de profesionales" (Bundle Backend/Frontend Web)

**Input**: Design documents from `specs/001-gestion-integral-reservas/`
**Prerequisites**: `plan.md` (required), `spec.md` (required), `data-model.md`, `contracts/bw-shared-internal-api.md`, `research.md`, `quickstart.md`

## Alcance de esta ejecución

Fuente de requisitos: `spec.md` (Specification oficial) y `bundle-scope.md` (restringe el diseño
al bundle Backend/Frontend Web, BW). Dentro de ese alcance, esta ejecución de `/speckit-tasks`
genera tareas **únicamente** para el área funcional "Gestión de profesionales" (`spec.md`
§Contexto → Índice de requisitos, punto 2), por instrucción explícita de
`prompts/etapa-j-tasks.md`. No se generan tareas para "Gestión de agenda", "Gestión de servicios",
"Ejecución de servicio", "Seguimiento de servicio agendado" ni "Gestión de conversacional" — quedan
para ejecuciones futuras de `/speckit-tasks`.

**Requisitos funcionales de BW en el alcance de "Gestión de profesionales"** (identificados por
mencionar explícitamente "profesional"/"profesionales" en `spec.md` §Requirements — Bundle BW):

| FR-BW | Descripción (spec.md) |
|---|---|
| FR-BW-003 | Aceptar la interacción humana "Datos de profesionales" |
| FR-BW-005 | Aceptar la interacción humana "Crear/Modificar profesional" (rol restringido a "Administrador de la operación"; UI oculta la acción a otros roles — Clarifications 2026-08-05/2026-08-08) |
| FR-BW-011 | Leer el dato importado "Profesionales y especialidades" |
| FR-BW-025 | Mostrar o notificar "Ficha Profesionales" |
| FR-BW-031 | Emitir la respuesta de contrato "Profesionales Query API" (`GET /internal/profesionales`, contrato compartido con AC/BA; reintento automático ante fallo — Clarifications 2026-08-08) |
| FR-BW-037 | Persistir o entregar el dato exportado "Profesionales y especialidades" |

No se incluyen aquí los requisitos genéricos de confirmación de UI (FR-BW-026/027/028) ni de
dashboard (FR-BW-022): no nombran a "profesionales" específicamente y son compartidos con otras
áreas funcionales de BW fuera del alcance de esta ejecución.

## Convención de AC-ID

`prompts/etapa-j-tasks.md` exige etiquetar cada tarea de historia con `[AC:<AC-IDs>]`. `spec.md` no
declara un catálogo separado de identificadores "AC-nnn"; cada `FR-BW-nnn` ya trae exactamente un
escenario Dado/Cuando/Entonces (su criterio de aceptación). Por lo tanto, **AC-ID = FR-BW-ID** en
este documento. No confundir con el prefijo de bundle "FR-AC-" (Agente Conversacional): ese bundle
está fuera del alcance de `bundle-scope.md` y no aparece en ninguna tarea de este archivo.

**Tests**: incluidos solo para backend (`bw-backend/tests/unit/`, pytest) — declarado explícitamente
como requisito para esta ejecución (`prompts/etapa-i-plan.md` §Stack: "Se incluyen test unitarios en
backend"). No se incluyen tareas de test de frontend: ningún canvas, `spec.md` ni el stack de esta
ejecución declaran un framework de pruebas de frontend (ver `research.md` §"Framework de pruebas");
inventar una obligación de test de frontend violaría la restricción de no inventar decisiones no
respaldadas.

**Organización**: Setup → Foundational → US-001 (P1, MVP) → US-002 (P2) → US-003 (P3) → US-004 (P4)
→ Validación final. El orden de prioridad P1–P4 (Crear → Consultar → Modificar → Exportar) es una
decisión de secuenciación de esta ejecución (`spec.md` no declara prioridad para "Gestión de
profesionales" — todas las "Por qué esta prioridad" de las historias de negocio EN-01..EN-08 están
marcadas `[NEEDS CLARIFICATION]`); no reordena ni inventa ningún requisito, solo secuencia los 6
FR-BW ya declarados en incrementos independientemente entregables.

## Format: `- [ ] Tnnn [P?] [USn] [AC:<AC-IDs>] Descripción con ruta exacta — Commit: "<asunto esperado>"`

- **[P]**: paralelizable (archivos distintos, sin dependencia de una tarea incompleta)
- **[USn]**: historia de usuario a la que pertenece (solo en fases de historia; Setup/Foundational/
  Validación final no llevan `[USn]` ni `[AC:...]`)
- **[AC:<AC-IDs>]**: FR-BW-ID(s) de `spec.md` que la tarea satisface (ver "Convención de AC-ID")
- **Commit**: asunto de commit esperado para esa tarea, en formato Conventional Commits

## Path Conventions

Según `plan.md` §Project Structure: `bw-backend/src/{models,services,adapters,api}`,
`bw-backend/tests/unit/`, `bw-frontend/src/{pages,components,types,services}`.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: inicialización del proyecto y del verificador de trazabilidad.

- [ ] T001 Crear el verificador de trazabilidad en
  `specs/001-gestion-integral-reservas/scripts/verify_traceability.py` (valida que cada AC-ID de la
  tabla "Coverage Audit" de este archivo tiene ≥1 tarea `Tnnn` asociada, y que
  `specs/001-gestion-integral-reservas/traceability.md` tiene una fila por tarea con SHA de commit
  no vacío una vez completada la implementación) y crear el esqueleto de
  `specs/001-gestion-integral-reservas/traceability.md` (tabla con columnas Tnnn | AC-ID(s) | Ruta |
  SHA — SHA vacío hasta T036) — Commit: `"chore(tasks): add traceability verifier and skeleton for Gestión de profesionales"`
- [ ] T002 [P] Inicializar `bw-backend` (FastAPI): estructura `src/{models,services,adapters,api}/`,
  `tests/unit/`, `requirements.txt`/`pyproject.toml`, configuración de lint/format (ruff + black), y
  entrypoint `bw-backend/src/main.py` — Commit: `"chore(bw-backend): scaffold FastAPI project structure"`
- [ ] T003 [P] Inicializar `bw-frontend` (React + TypeScript estricto): estructura
  `src/{pages,components,types,services}/`, `package.json`, `tsconfig.json` (`"strict": true`),
  configuración de ESLint/Prettier — Commit: `"chore(bw-frontend): scaffold React+TS strict project structure"`

**Nota de orden**: T001 debe completarse primero (instrucción explícita de esta ejecución); T002 y
T003 no dependen técnicamente de T001, pero se secuencian después de él por esa misma instrucción.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: infraestructura que las 4 historias de "Gestión de profesionales" necesitan en común.

**⚠️ CRITICAL**: ninguna historia de usuario puede comenzar hasta completar esta fase.

- [ ] T004 [P] Definir el modelo Pydantic base `Profesional` (`id`, `nombre`, `especialidades` — ver
  `data-model.md` §Profesionales y especialidades) en `bw-backend/src/models/profesional.py`
  (depende de T002) — Commit: `"feat(bw-backend): add Profesional pydantic model"`
- [ ] T005 [P] Definir la interfaz TypeScript `Profesional` (`id`, `nombre`, `especialidades`) en
  `bw-frontend/src/types/profesional.ts` (depende de T003) — Commit: `"feat(bw-frontend): add Profesional TS interface"`
- [ ] T006 Implementar el adaptador del contrato de API interna compartido
  (`contracts/bw-shared-internal-api.md`) con reintento automático ante fallo o indisponibilidad
  (Clarifications, Sesión 2026-08-08) en `bw-backend/src/adapters/internal_api_client.py` (depende
  de T002, T004; Principio de constitution P21 "Integración mediante adapters") — Commit:
  `"feat(bw-backend): add shared internal API adapter with auto-retry"`
- [ ] T007 [P] Implementar el control de autorización que restringe crear/modificar profesional al
  rol "Administrador de la operación" (actor organizacional "Administrador del centro" — aclarado en
  Clarifications, Sesión 2026-08-08) en `bw-backend/src/services/auth.py` (depende de T002) —
  Commit: `"feat(bw-backend): add role authorization guard for Administrador de la operación"`
- [ ] T008 Registrar el router base `profesionales` (sin endpoints aún) en
  `bw-backend/src/api/profesionales.py` y montarlo en `bw-backend/src/main.py` (depende de T002) —
  Commit: `"chore(bw-backend): register profesionales router skeleton"`
- [ ] T009 [P] Crear el layout de administración y la ruta base `/profesionales` en
  `bw-frontend/src/App.tsx` (depende de T003) — Commit: `"chore(bw-frontend): add profesionales route skeleton"`

**Checkpoint**: fundación lista — las historias US-001 a US-004 pueden comenzar.

---

## Phase 3: User Story 1 — Crear un profesional nuevo (Priority: P1) 🎯 MVP

**Goal**: el rol "Administrador de la operación" (actor "Administrador del centro") completa el
formulario "Datos de profesionales" y crea un nuevo registro de profesional.

**Independent Test**: autenticado como "Administrador del centro", enviar un payload válido de
"Datos de profesionales" a la acción "Crear profesional"; verificar que el sistema persiste el
registro y deja un resultado observable (FR-BW-005). Repetir con un rol distinto y verificar que la
acción no está disponible en la interfaz (Clarifications, Sesión 2026-08-08).

**AC-IDs cubiertos**: FR-BW-003, FR-BW-005

### Tests for User Story 1

- [ ] T010 [P] [US1] [AC:FR-BW-003] Unit test: el schema Pydantic de "Datos de profesionales" rechaza
  payloads sin `nombre` y acepta uno válido, en `bw-backend/tests/unit/test_profesional_schema.py` —
  Commit: `"test(bw-backend): add schema validation tests for crear profesional (US1)"`
- [ ] T011 [P] [US1] [AC:FR-BW-005] Unit test: `ProfesionalService.crear()` persiste el registro solo
  cuando el rol es "Administrador de la operación" y lo rechaza para cualquier otro rol, en
  `bw-backend/tests/unit/test_profesional_create_service.py` — Commit:
  `"test(bw-backend): add authorization + create tests for crear profesional (US1)"`

### Implementation for User Story 1

- [ ] T012 [US1] [AC:FR-BW-003] Extender `bw-backend/src/models/profesional.py` con el schema de
  entrada `ProfesionalCreateInput` (campo requerido `nombre` — motivado por FR-BW-004/§data-model.md)
  (depende de T004, T010) — Commit: `"feat(bw-backend): add ProfesionalCreateInput schema (US1)"`
- [ ] T013 [US1] [AC:FR-BW-005] Implementar `ProfesionalService.crear()` (valida rol vía T007,
  persiste a través del adaptador T006 hacia el contrato compartido) en
  `bw-backend/src/services/profesional_service.py` (depende de T006, T007, T011, T012) — Commit:
  `"feat(bw-backend): implement crear profesional service (US1)"`
- [ ] T014 [US1] [AC:FR-BW-005] Implementar el endpoint `POST /profesionales` en
  `bw-backend/src/api/profesionales.py` (depende de T008, T013) — Commit:
  `"feat(bw-backend): add POST /profesionales endpoint (US1)"`
- [ ] T015 [P] [US1] [AC:FR-BW-003] Implementar el formulario "Datos de profesionales" en
  `bw-frontend/src/components/ProfesionalForm.tsx` (depende de T005, T009) — Commit:
  `"feat(bw-frontend): add ProfesionalForm component (US1)"`
- [ ] T016 [P] [US1] [AC:FR-BW-005] Implementar el cliente HTTP (método `crear`) en
  `bw-frontend/src/services/profesionalesApi.ts` (depende de T005) — Commit:
  `"feat(bw-frontend): add profesionalesApi client with crear method (US1)"`
- [ ] T017 [US1] [AC:FR-BW-005] Implementar la página "Crear profesional"
  (`bw-frontend/src/pages/CrearProfesional.tsx`), integrando T015 y T016 y ocultando la acción para
  roles distintos de "Administrador de la operación" (Clarifications, Sesión 2026-08-08) (depende de
  T014, T015, T016) — Commit: `"feat(bw-frontend): add CrearProfesional page with role-gated action (US1)"`

**Checkpoint**: US-001 completo y testeable de forma independiente (MVP).

---

## Phase 4: User Story 2 — Consultar la ficha de profesionales (Priority: P2)

**Goal**: mostrar el listado/ficha de profesionales (FR-BW-025), obtenidos mediante el contrato
compartido "Profesionales Query API" (FR-BW-031 / FR-BW-011).

**Independent Test**: con datos de profesionales servidos por el doble de prueba del contrato
compartido (`quickstart.md`), abrir la vista "Profesionales" y verificar que se muestra el listado y
la ficha esperados, sin depender de que US-001 se haya ejecutado antes.

**AC-IDs cubiertos**: FR-BW-011, FR-BW-025, FR-BW-031

### Tests for User Story 2

- [ ] T018 [P] [US2] [AC:FR-BW-031] Unit test: `ProfesionalService.listar()` invoca el adaptador hacia
  `GET /internal/profesionales` y propaga el reintento automático ante fallo (Clarifications, Sesión
  2026-08-08), en `bw-backend/tests/unit/test_profesional_query_service.py` — Commit:
  `"test(bw-backend): add profesionales query + retry tests (US2)"`

### Implementation for User Story 2

- [ ] T019 [US2] [AC:FR-BW-011,FR-BW-031] Implementar `ProfesionalService.listar()` (consume el
  adaptador T006 hacia la Profesionales Query API) en `bw-backend/src/services/profesional_service.py`
  (depende de T006, T018; mismo archivo que T013 → secuencial) — Commit:
  `"feat(bw-backend): implement listar profesionales via shared query API (US2)"`
- [ ] T020 [US2] [AC:FR-BW-025] Implementar los endpoints `GET /profesionales` (lista) y
  `GET /profesionales/{id}` (ficha) en `bw-backend/src/api/profesionales.py` (depende de T008, T019;
  mismo archivo que T014 → secuencial) — Commit: `"feat(bw-backend): add GET /profesionales endpoints (US2)"`
- [ ] T021 [P] [US2] [AC:FR-BW-025] Agregar los métodos `listar`/`obtener` al cliente HTTP en
  `bw-frontend/src/services/profesionalesApi.ts` (depende de T016; mismo archivo, fase posterior →
  sin conflicto de ejecución simultánea) — Commit: `"feat(bw-frontend): add listar/obtener client methods (US2)"`
- [ ] T022 [P] [US2] [AC:FR-BW-025] Implementar el componente "Ficha Profesionales" (listado +
  detalle) en `bw-frontend/src/components/FichaProfesionales.tsx` (depende de T005) — Commit:
  `"feat(bw-frontend): add FichaProfesionales component (US2)"`
- [ ] T023 [US2] [AC:FR-BW-025] Implementar la página "Profesionales"
  (`bw-frontend/src/pages/Profesionales.tsx`), integrando T021 y T022 (depende de T020, T021, T022) —
  Commit: `"feat(bw-frontend): add Profesionales listing page (US2)"`

**Checkpoint**: US-001 y US-002 funcionan de forma independiente.

---

## Phase 5: User Story 3 — Modificar un profesional existente (Priority: P3)

**Goal**: el rol "Administrador de la operación" modifica los datos de un profesional existente
(variante "Modificar" de FR-BW-005).

**Independent Test**: autenticado como "Administrador del centro", con un `profesional_id` existente
(servido por el doble de prueba del contrato compartido), enviar una modificación y verificar que el
sistema la persiste y deja un resultado observable; repetir con un rol no autorizado y verificar que
la acción está oculta en la interfaz (Clarifications, Sesión 2026-08-08). No depende de haber
ejecutado US-001 o US-002 primero (usa un `profesional_id` provisto directamente por el doble de
prueba).

**AC-IDs cubiertos**: FR-BW-005

### Tests for User Story 3

- [ ] T024 [P] [US3] [AC:FR-BW-005] Unit test: `ProfesionalService.modificar()` persiste el cambio
  solo para el rol "Administrador de la operación" y lo rechaza para cualquier otro, en
  `bw-backend/tests/unit/test_profesional_update_service.py` — Commit:
  `"test(bw-backend): add modificar profesional authorization tests (US3)"`

### Implementation for User Story 3

- [ ] T025 [US3] [AC:FR-BW-005] Implementar `ProfesionalService.modificar()` (reutiliza el schema de
  T012 para los campos editables) en `bw-backend/src/services/profesional_service.py` (depende de
  T007, T012, T024; mismo archivo que T013/T019 → secuencial) — Commit:
  `"feat(bw-backend): implement modificar profesional service (US3)"`
- [ ] T026 [US3] [AC:FR-BW-005] Implementar el endpoint `PUT /profesionales/{id}` en
  `bw-backend/src/api/profesionales.py` (depende de T020, T025; mismo archivo que T014/T020 →
  secuencial) — Commit: `"feat(bw-backend): add PUT /profesionales/{id} endpoint (US3)"`
- [ ] T027 [P] [US3] [AC:FR-BW-005] Agregar el método `modificar` al cliente HTTP en
  `bw-frontend/src/services/profesionalesApi.ts` (depende de T021; mismo archivo, fase posterior →
  sin conflicto de ejecución simultánea) — Commit: `"feat(bw-frontend): add modificar client method (US3)"`
- [ ] T028 [US3] [AC:FR-BW-005] Implementar la página "Modificar profesional"
  (`bw-frontend/src/pages/ModificarProfesional.tsx`), reutilizando `ProfesionalForm` (T015) y
  precargando datos vía T023, ocultando la acción para roles no autorizados (Clarifications, Sesión
  2026-08-08) (depende de T015, T023, T026, T027) — Commit:
  `"feat(bw-frontend): add ModificarProfesional page with role-gated action (US3)"`

**Checkpoint**: US-001, US-002 y US-003 funcionan de forma independiente.

---

## Phase 6: User Story 4 — Exportar datos de profesionales (Priority: P4)

**Goal**: BW persiste/entrega el dato exportado "Profesionales y especialidades" (FR-BW-037).
`spec.md` no detalla el formato/mecanismo de entrega más allá de "persistir o entregar"; esta fase
lo resuelve como una decisión de implementación mínima (endpoint de exportación), sin inventar
alcance de negocio adicional.

**Independent Test**: invocar la exportación de profesionales directamente (sin pasar por US-002) y
verificar que el sistema entrega el conjunto completo de datos de "Profesionales y especialidades".

**AC-IDs cubiertos**: FR-BW-037

### Tests for User Story 4

- [ ] T029 [P] [US4] [AC:FR-BW-037] Unit test: `ProfesionalService.exportar()` serializa la lista
  completa de profesionales, en `bw-backend/tests/unit/test_profesional_export_service.py` — Commit:
  `"test(bw-backend): add exportar profesionales tests (US4)"`

### Implementation for User Story 4

- [ ] T030 [US4] [AC:FR-BW-037] Implementar `ProfesionalService.exportar()` en
  `bw-backend/src/services/profesional_service.py` (depende de T019, T029; mismo archivo que
  T013/T019/T025 → secuencial) — Commit: `"feat(bw-backend): implement exportar profesionales service (US4)"`
- [ ] T031 [US4] [AC:FR-BW-037] Implementar el endpoint `GET /profesionales/export` en
  `bw-backend/src/api/profesionales.py` (depende de T026, T030; mismo archivo que
  T014/T020/T026 → secuencial) — Commit: `"feat(bw-backend): add GET /profesionales/export endpoint (US4)"`
- [ ] T032 [P] [US4] [AC:FR-BW-037] Agregar la acción "Exportar" a
  `bw-frontend/src/pages/Profesionales.tsx` (depende de T023, T031; mismo archivo que T023, fase
  posterior → sin conflicto de ejecución simultánea) — Commit:
  `"feat(bw-frontend): add exportar action to Profesionales page (US4)"`

**Checkpoint**: las 4 historias de "Gestión de profesionales" funcionan de forma independiente.

---

## Phase 7: Validación final

- [ ] T033 [P] Ejecutar `pytest bw-backend/tests/unit/` y corregir cualquier falla antes de continuar
  — Commit: `"test(bw-backend): green unit suite for Gestión de profesionales"`
- [ ] T034 Ejecutar manualmente el Escenario 1 de `quickstart.md` ("Crear/modificar un profesional",
  FR-BW-005) contra `bw-backend` + `bw-frontend` corriendo localmente con el doble de prueba del
  contrato compartido, y registrar el resultado en
  `specs/001-gestion-integral-reservas/validation-log.md` — Commit:
  `"docs(specs): record Gestión de profesionales quickstart validation"`
- [ ] T035 Ejecutar el Coverage Audit: correr
  `specs/001-gestion-integral-reservas/scripts/verify_traceability.py` (T001) contra este archivo y
  confirmar que los 6 AC-IDs de la tabla "Coverage Audit" tienen ≥1 tarea asociada — Commit:
  `"chore(tasks): run coverage audit for Gestión de profesionales"`
- [ ] T036 (FINAL) Registrar los SHA de commit reales de T001–T035 en
  `specs/001-gestion-integral-reservas/traceability.md` (una fila por tarea: Tnnn, AC-ID(s), ruta,
  SHA), usando `verify_traceability.py` — Commit:
  `"docs(specs): record real commit SHAs in traceability.md for Gestión de profesionales"`

---

## Coverage Audit

Todos los AC-IDs (FR-BW-ID) en el alcance de "Gestión de profesionales" y sus tareas:

| AC-ID | Descripción (spec.md) | Tareas |
|---|---|---|
| FR-BW-003 | Aceptar "Datos de profesionales" | T010, T012, T015 |
| FR-BW-005 | Crear/Modificar profesional (rol restringido; UI oculta acción a otros roles) | T011, T013, T014, T016, T017, T024, T025, T026, T027, T028 |
| FR-BW-011 | Leer el dato importado "Profesionales y especialidades" | T019 |
| FR-BW-025 | Mostrar "Ficha Profesionales" | T018 (indirecto vía query), T020, T021, T022, T023 |
| FR-BW-031 | "Profesionales Query API" (reintento automático) | T018, T019, T020 |
| FR-BW-037 | Exportar "Profesionales y especialidades" | T029, T030, T031, T032 |

Sin AC-ID huérfano: los 6 requisitos en el alcance de esta ejecución tienen al menos una tarea.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: sin dependencias — T001 primero por instrucción explícita, luego T002/T003.
- **Foundational (Phase 2)**: depende de Setup — bloquea las 4 historias.
- **User Stories (Phase 3–6)**: dependen todas de Foundational.
  - US-001 (P1): sin dependencia de otras historias.
  - US-002 (P2): sin dependencia de otras historias (usa el doble de prueba del contrato compartido).
  - US-003 (P3): reutiliza componentes de US-001 (`ProfesionalForm`) y US-002 (página de listado
    para prefill), pero es testeable de forma independiente vía `profesional_id` directo.
  - US-004 (P4): reutiliza la página de US-002 para exponer la acción "Exportar", pero es testeable
    de forma independiente invocando el endpoint de exportación directamente.
- **Validación final (Phase 7)**: depende de que todas las historias deseadas estén completas.

### Parallel Opportunities

- T002 y T003 (Setup) en paralelo tras T001.
- T004, T005, T007, T009 (Foundational) en paralelo entre sí (archivos distintos).
- Dentro de US-001: T010 y T011 (tests) en paralelo; T015 y T016 (frontend) en paralelo.
- Dentro de US-002: T021 y T022 (frontend) en paralelo.
- Dentro de US-003: T024 (test) en paralelo con el resto de Foundational/otras historias ya cerradas.
- Dentro de US-004: T029 (test) y T032 (UI) en paralelo con tareas de otras historias.
- Ningún par de tareas marcadas `[P]` modifica el mismo archivo dentro de la misma fase.

---

## Parallel Example: User Story 1

```bash
# Tests de US-001 en paralelo:
Task: "Unit test schema Datos de profesionales en bw-backend/tests/unit/test_profesional_schema.py"
Task: "Unit test autorización + creación en bw-backend/tests/unit/test_profesional_create_service.py"

# Frontend de US-001 en paralelo:
Task: "ProfesionalForm.tsx en bw-frontend/src/components/"
Task: "profesionalesApi.ts (método crear) en bw-frontend/src/services/"
```

---

## Implementation Strategy

### MVP First (User Story 1 únicamente)

1. Completar Phase 1: Setup (T001–T003).
2. Completar Phase 2: Foundational (T004–T009) — bloqueante.
3. Completar Phase 3: User Story 1 (T010–T017).
4. **Detener y validar**: probar "Crear un profesional nuevo" de forma independiente.
5. Desplegar/demo si está listo — esto ya entrega valor de "Gestión de profesionales".

### Entrega incremental

1. Setup + Foundational → base lista.
2. US-001 (Crear) → probar de forma independiente → demo (MVP).
3. US-002 (Consultar) → probar de forma independiente → demo.
4. US-003 (Modificar) → probar de forma independiente → demo.
5. US-004 (Exportar) → probar de forma independiente → demo.
6. Validación final (Phase 7) → Coverage Audit y `traceability.md` con SHA reales.

---

## Notes

- `[P]` = archivos distintos, sin dependencia de una tarea incompleta.
- `[USn]` mapea la tarea a su historia de usuario para trazabilidad.
- `[AC:<AC-IDs>]` mapea la tarea a su(s) FR-BW de `spec.md` (ver "Convención de AC-ID").
- Cada historia es completable y testeable de forma independiente.
- Verificar que las pruebas fallan antes de implementar (T010/T011/T018/T024/T029 antes que su
  implementación correspondiente).
- Confirmar (commit) después de cada tarea o grupo lógico, usando el asunto indicado.
- Detenerse en cada checkpoint para validar la historia de forma independiente.
- Evitar: tareas vagas, conflictos de archivo entre tareas `[P]`, dependencias entre historias que
  rompan su independencia de prueba.
