# Tasks: Gestión Integral de Reservas — Feature "Gestión de profesionales" (Bundle Backend/Frontend Web, solo Backend)

**Input**: Design documents from `specs/001-gestion-integral-reservas/`
**Prerequisites**: `plan.md` (required), `spec.md` (required), `data-model.md`, `contracts/bw-shared-internal-api.md`, `contracts/bw-data-exports.md`, `research.md`, `quickstart.md`

## Re-sincronización (2026-08-09b)

Esta ejecución reemplaza por completo la versión anterior de `tasks.md`, generada contra un
`plan.md` que no precisaba cómo las pruebas unitarias obtenían una base de datos aislada. El
`plan.md` vigente (re-sincronizado 2026-08-09b) agrega, a partir de `prompts/etapa-i-plan.md` §Stack
("Se incluyen test unitarios en backend que usan una sesion aislada de DB"), la decisión concreta de
`research.md` §"Estrategia de aislamiento de base de datos en pruebas": una transacción SQLAlchemy
por test, con rollback automático, sobre el mismo PostgreSQL de `docker-compose.yml`. Esto agrega
una tarea Foundational nueva (T010, fixture `conftest.py`) que no existía en la versión anterior de
este archivo — resuelve el hallazgo HIGH (U1) de la sesión de `/speckit-analyze` que siguió a esa
versión. De paso, T007 (migración) ahora también **aplica** la migración generada (antes solo la
generaba) — resuelve el hallazgo MEDIUM (I1) de esa misma sesión de análisis.

## Alcance de esta ejecución

Fuente de requisitos: `spec.md` (Specification oficial) y `bundle-scope.md` (restringe el diseño
al bundle Backend/Frontend Web, BW). Dentro de ese alcance, esta ejecución de `/speckit-tasks`
genera tareas **únicamente** para el área funcional "Gestión de profesionales" (`spec.md`
§Contexto → Índice de requisitos, punto 2) **y únicamente para el backend** (`bw-backend`), por
instrucción explícita de `prompts/etapa-j-tasks.md` ("Genera tareas únicamente para el feature de
'Gestión de profesionales' de backend" / "No incluyas el proyecto de frontend"). No se generan
tareas para "Gestión de agenda", "Gestión de servicios", "Ejecución de servicio", "Seguimiento de
servicio agendado" ni "Gestión de conversacional", ni ninguna tarea sobre `bw-frontend/` — quedan
para ejecuciones futuras de `/speckit-tasks`.

**Requisitos funcionales de BW en el alcance de "Gestión de profesionales"** (identificados por
mencionar explícitamente "profesional"/"profesionales" en `spec.md` §Requirements — Bundle BW):

| FR-BW | Descripción (spec.md) | Mecanismo (plan.md re-sincronizado 2026-08-09b) |
|---|---|---|
| FR-BW-003 | Aceptar la interacción humana "Datos de profesionales" | Aceptado a nivel de API (schema de entrada) |
| FR-BW-005 | Aceptar la interacción humana "Crear/Modificar profesional" (rol restringido a "Administrador de la operación"; UI oculta la acción a otros roles — Clarifications 2026-08-05/2026-08-08) | Persistido directamente en PostgreSQL propio de BW |
| FR-BW-011 | Leer el dato importado "Profesionales y especialidades" | Lectura local a PostgreSQL (ya no es importación externa) |
| FR-BW-025 | Mostrar o notificar "Ficha Profesionales" | Endpoints administrativos de solo lectura sobre PostgreSQL |
| FR-BW-031 | Emitir la respuesta de contrato "Profesionales Query API" | Servida por BW (`GET /profesionales/query`), respaldada por PostgreSQL propio |
| FR-BW-037 | Persistir o entregar el dato exportado "Profesionales y especialidades" | Export de solo lectura sobre PostgreSQL |

No se incluyen aquí los requisitos genéricos de confirmación de UI (FR-BW-026/027/028) ni de
dashboard (FR-BW-022): no nombran a "profesionales" específicamente y son compartidos con otras
áreas funcionales de BW fuera del alcance de esta ejecución.

## Nota de alcance: backend sin frontend

`prompts/etapa-j-tasks.md` excluye explícitamente el proyecto `bw-frontend`. Dos FR-BW de esta
área tienen, según `spec.md`, un componente de interfaz de usuario que un backend por sí solo no
puede completar; esta ejecución cubre exclusivamente su porción de backend:

- **FR-BW-005** — Aclarado (Clarifications, Sesión 2026-08-08): "para cualquier otro rol, la
  interfaz oculta esta acción". El backend cubre la porción exigible sin UI: el endpoint rechaza
  (autorización, T008) la acción para cualquier rol distinto de "Administrador de la operación".
  Ocultar la opción en la interfaz es responsabilidad de `bw-frontend` y queda fuera de esta
  ejecución.
- **FR-BW-025** — "El sistema DEBE mostrar o notificar 'Ficha Profesionales'". El backend cubre la
  porción que provee el dato a mostrar (endpoints `GET /profesionales`, `GET /profesionales/{id}`,
  T019); el renderizado en pantalla es responsabilidad de `bw-frontend` y queda fuera de esta
  ejecución.

## Convención de AC-ID

`prompts/etapa-j-tasks.md` exige etiquetar cada tarea de historia con `[AC:<AC-IDs>]`. `spec.md` no
declara un catálogo separado de identificadores "AC-nnn"; cada `FR-BW-nnn` ya trae exactamente un
escenario Dado/Cuando/Entonces (su criterio de aceptación). Por lo tanto, **AC-ID = FR-BW-ID** en
este documento. No confundir con el prefijo de bundle "FR-AC-" (Agente Conversacional): ese bundle
está fuera del alcance de `bundle-scope.md` y no aparece en ninguna tarea de este archivo.

**Tests**: incluidos solo para backend (`bw-backend/tests/unit/`, pytest) — declarado explícitamente
como requisito para esta ejecución (`prompts/etapa-i-plan.md` §Stack: "Se incluyen test unitarios en
backend que usan una sesion aislada de DB"). Cada test que ejercita `ProfesionalService` usa el
fixture de sesión aislada de T010 (transacción + rollback sobre el PostgreSQL de
`docker-compose.yml`, `research.md` §"Estrategia de aislamiento de base de datos en pruebas") — no
una base de datos física separada por test.

**Organización**: Setup → Foundational → US-001 (P1, MVP) → US-002 (P2) → US-003 (P3) → US-004 (P4)
→ Validación final. El orden de prioridad P1–P4 (Crear → Consultar → Modificar → Exportar) es una
decisión de secuenciación de esta ejecución (`spec.md` no declara prioridad para "Gestión de
profesionales"); no reordena ni inventa ningún requisito, solo secuencia los 6 FR-BW ya declarados
en incrementos independientemente entregables.

## Format: `- [ ] Tnnn [P?] [USn] [AC:<AC-IDs>] Descripción con ruta exacta — Commit: "<asunto esperado>"`

- **[P]**: paralelizable (archivos distintos, sin dependencia de una tarea incompleta)
- **[USn]**: historia de usuario a la que pertenece (solo en fases de historia; Setup/Foundational/
  Validación final no llevan `[USn]` ni `[AC:...]`)
- **[AC:<AC-IDs>]**: FR-BW-ID(s) de `spec.md` que la tarea satisface (ver "Convención de AC-ID")
- **Commit**: asunto de commit esperado para esa tarea, en formato Conventional Commits

## Path Conventions

Según `plan.md` §Project Structure (re-sincronizado 2026-08-09b): `bw-backend/src/{models,services,api,db}`,
`bw-backend/tests/{conftest.py,unit/}`, `bw-backend/alembic/`, `bw-backend/Dockerfile`,
`bw-backend/docker-compose.yml`. `bw-backend/src/adapters/` se crea vacío en el scaffold (T002) pero
**ninguna tarea de esta ejecución lo implementa**: las 6 FR-BW en el alcance de "Gestión de
profesionales" no requieren consumir el contrato compartido con Backend Agendamiento (ver
`contracts/bw-shared-internal-api.md` §Parte 1). Ninguna tarea toca `bw-frontend/` (excluido por
instrucción explícita de `prompts/etapa-j-tasks.md`).

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: inicialización del proyecto backend, su dockerización y el verificador de trazabilidad.

- [X] T001 Crear el verificador de trazabilidad en
  `specs/001-gestion-integral-reservas/scripts/verify_traceability.py` (valida que cada AC-ID de la
  tabla "Coverage Audit" de este archivo tiene ≥1 tarea `Tnnn` asociada, y que
  `specs/001-gestion-integral-reservas/traceability.md` tiene una fila por tarea con SHA de commit
  no vacío una vez completada la implementación) y crear el esqueleto de
  `specs/001-gestion-integral-reservas/traceability.md` (tabla con columnas Tnnn | AC-ID(s) | Ruta |
  SHA — SHA vacío hasta T029) — Commit: `"chore(tasks): add traceability verifier and skeleton for Gestión de profesionales (backend)"`
- [X] T002 Inicializar `bw-backend` (FastAPI): estructura `src/{models,services,adapters,api,db}/`,
  `tests/unit/`, `requirements.txt`/`pyproject.toml`, configuración de lint/format (ruff + black), y
  entrypoint `bw-backend/src/main.py` (depende de T001, por instrucción explícita de esta ejecución
  de completar primero el verificador de trazabilidad) — Commit: `"chore(bw-backend): scaffold FastAPI project structure"`
- [X] T003 [P] Dockerizar el backend: `bw-backend/Dockerfile` (imagen del servicio FastAPI) y
  `bw-backend/docker-compose.yml` (orquesta `bw-backend` + contenedor PostgreSQL con la imagen
  oficial `postgres`, ambos declarados explícitamente en `prompts/etapa-i-plan.md` §Stack) (depende
  de T002) — Commit: `"chore(bw-backend): add Dockerfile and docker-compose with postgres service"`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: infraestructura de backend (conexión a PostgreSQL, migraciones, aislamiento de tests,
autorización, router base) que las 4 historias de "Gestión de profesionales" necesitan en común.

**⚠️ CRITICAL**: ninguna historia de usuario puede comenzar hasta completar esta fase.

- [X] T004 Configurar la conexión a PostgreSQL: engine y sesión de SQLAlchemy en
  `bw-backend/src/db/session.py` y la clase `Base` declarativa en `bw-backend/src/db/base.py`
  (`research.md` §"Motor de base de datos y herramientas de acceso a datos") (depende de T002, T003) —
  Commit: `"feat(bw-backend): add SQLAlchemy engine, session and declarative base"`
- [X] T005 [P] Inicializar Alembic (migraciones) en `bw-backend/alembic/` (`env.py`,
  `script.py.mako`) y `bw-backend/alembic.ini`, apuntando a la `Base` de T004 (depende de T004) —
  Commit: `"chore(bw-backend): initialize Alembic migrations"`
- [X] T006 [P] Definir el modelo SQLAlchemy `Profesional` (tabla `profesionales`: `id`, `nombre`,
  `especialidades` — ver `data-model.md` §Profesionales y especialidades) y el schema Pydantic de
  salida `Profesional` en `bw-backend/src/models/profesional.py` (depende de T004) — Commit:
  `"feat(bw-backend): add Profesional SQLAlchemy model and output schema"`
- [X] T007 Generar la migración inicial de Alembic para la tabla `profesionales` en
  `bw-backend/alembic/versions/`, y aplicarla contra el PostgreSQL de `docker-compose.yml`
  (`alembic upgrade head`), verificando que la tabla `profesionales` existe (depende de T003, T005,
  T006) — Commit: `"chore(bw-backend): add and apply initial alembic migration for profesionales table"`
- [X] T008 [P] Implementar el control de autorización que restringe crear/modificar profesional al
  rol "Administrador de la operación" (actor organizacional "Administrador del centro" — aclarado en
  Clarifications, Sesión 2026-08-08) en `bw-backend/src/services/auth.py` (depende de T002) —
  Commit: `"feat(bw-backend): add role authorization guard for Administrador de la operación"`
- [X] T009 [P] Registrar el router base `profesionales` (sin endpoints aún) en
  `bw-backend/src/api/profesionales.py` y montarlo en `bw-backend/src/main.py` (depende de T002) —
  Commit: `"chore(bw-backend): register profesionales router skeleton"`
- [X] T010 Implementar el fixture de pytest de sesión aislada de base de datos en
  `bw-backend/tests/conftest.py`: abre una transacción SQLAlchemy sobre el PostgreSQL de
  `docker-compose.yml`, vincula (`bind=`) el `Session` de cada test a esa transacción, y la revierte
  (`rollback()`) al finalizar el test, de modo que ningún test deja datos residuales para el
  siguiente (`prompts/etapa-i-plan.md` §Stack: "test unitarios en backend que usan una sesion
  aislada de DB"; `research.md` §"Estrategia de aislamiento de base de datos en pruebas") (depende
  de T004, T007 — requiere que la tabla `profesionales` ya exista) — Commit:
  `"test(bw-backend): add isolated-session pytest fixture over postgres"`

**Checkpoint**: fundación lista — las historias US-001 a US-004 pueden comenzar.

---

## Phase 3: User Story 1 — Crear un profesional nuevo (Priority: P1) 🎯 MVP

**Goal**: el rol "Administrador de la operación" (actor "Administrador del centro") envía el
payload "Datos de profesionales" a la API y el backend crea un nuevo registro de profesional en su
PostgreSQL propio.

**Independent Test**: con `bw-backend` + PostgreSQL corriendo vía `docker compose up`, autenticado
como "Administrador del centro", enviar `POST /profesionales` con un payload válido de "Datos de
profesionales" y verificar que el sistema persiste el registro en la tabla `profesionales` y
responde con un resultado observable (FR-BW-005). Repetir la llamada con un rol distinto y verificar
que la API rechaza la solicitud (autorización de backend; el ocultamiento en interfaz queda fuera de
esta ejecución — ver "Nota de alcance: backend sin frontend").

**AC-IDs cubiertos**: FR-BW-003, FR-BW-005

### Tests for User Story 1

- [X] T011 [P] [US1] [AC:FR-BW-003] Unit test: el schema Pydantic de "Datos de profesionales" rechaza
  payloads sin `nombre` y acepta uno válido, en `bw-backend/tests/unit/test_profesional_schema.py`
  (no requiere el fixture de T010 — no toca la base de datos) — Commit:
  `"test(bw-backend): add schema validation tests for crear profesional (US1)"`
- [X] T012 [P] [US1] [AC:FR-BW-005] Unit test: `ProfesionalService.crear()` persiste el registro en
  PostgreSQL solo cuando el rol es "Administrador de la operación" y lo rechaza para cualquier otro
  rol, en `bw-backend/tests/unit/test_profesional_create_service.py` (usa el fixture de sesión
  aislada de T010) — Commit:
  `"test(bw-backend): add authorization + create tests for crear profesional (US1)"`

### Implementation for User Story 1

- [X] T013 [US1] [AC:FR-BW-003] Extender `bw-backend/src/models/profesional.py` con el schema de
  entrada `ProfesionalCreateInput` (campo requerido `nombre` — motivado por FR-BW-004/§data-model.md)
  (depende de T006, T011; mismo archivo que T006 → secuencial) — Commit:
  `"feat(bw-backend): add ProfesionalCreateInput schema (US1)"`
- [X] T014 [US1] [AC:FR-BW-005] Implementar `ProfesionalService.crear()` (valida rol vía T008,
  persiste la fila en PostgreSQL usando la sesión de T004/T010) en
  `bw-backend/src/services/profesional_service.py` (depende de T004, T008, T012, T013) — Commit:
  `"feat(bw-backend): implement crear profesional service (US1)"`
- [X] T015 [US1] [AC:FR-BW-005] Implementar el endpoint `POST /profesionales` en
  `bw-backend/src/api/profesionales.py` (depende de T009, T014; mismo archivo que T009 →
  secuencial) — Commit: `"feat(bw-backend): add POST /profesionales endpoint (US1)"`

**Checkpoint**: US-001 completo y testeable de forma independiente (MVP).

---

## Phase 4: User Story 2 — Consultar la ficha de profesionales (Priority: P2)

**Goal**: exponer los datos de "Ficha Profesionales" (FR-BW-025) desde la tabla PostgreSQL de BW,
tanto para uso administrativo interno como para el contrato "Profesionales Query API" que BW ahora
**sirve** a otros bundles (FR-BW-031 — `contracts/bw-shared-internal-api.md` §Parte 1). El
renderizado en pantalla es responsabilidad de `bw-frontend` y queda fuera de esta ejecución.

**Independent Test**: con datos de profesionales ya insertados en PostgreSQL (vía el fixture de
T010), invocar `GET /profesionales/query` (contrato servido) y `GET /profesionales`,
`GET /profesionales/{id}` (endpoints administrativos) y verificar que el backend devuelve el listado
y la ficha esperados, sin depender de que US-001 se haya ejecutado antes.

**AC-IDs cubiertos**: FR-BW-011, FR-BW-025, FR-BW-031

### Tests for User Story 2

- [X] T016 [P] [US2] [AC:FR-BW-011,FR-BW-031] Unit test: `ProfesionalService.listar()` consulta
  directamente la tabla `profesionales` en PostgreSQL y devuelve el listado completo, en
  `bw-backend/tests/unit/test_profesional_query_service.py` (usa el fixture de sesión aislada de
  T010) — Commit: `"test(bw-backend): add profesionales query tests against postgres (US2)"`

### Implementation for User Story 2

- [X] T017 [US2] [AC:FR-BW-011,FR-BW-031] Implementar `ProfesionalService.listar()` (lectura directa
  a PostgreSQL vía la sesión de T004 — ya no requiere adaptador externo, ver
  `contracts/bw-shared-internal-api.md` §Parte 1) en `bw-backend/src/services/profesional_service.py`
  (depende de T004, T016; mismo archivo que T014 → secuencial) — Commit:
  `"feat(bw-backend): implement listar profesionales from postgres (US2)"`
- [X] T018 [US2] [AC:FR-BW-031] Implementar el endpoint servido `GET /profesionales/query`
  (`contracts/bw-shared-internal-api.md` §Parte 1, contrato consumible por otros bundles) en
  `bw-backend/src/api/profesionales.py` (depende de T009, T017; mismo archivo que T015 →
  secuencial) — Commit: `"feat(bw-backend): serve GET /profesionales/query per shared contract (US2)"`
- [X] T019 [US2] [AC:FR-BW-025] Implementar los endpoints administrativos `GET /profesionales`
  (lista) y `GET /profesionales/{id}` (ficha) en `bw-backend/src/api/profesionales.py` (depende de
  T018; mismo archivo → secuencial) — Commit: `"feat(bw-backend): add GET /profesionales admin endpoints (US2)"`

**Checkpoint**: US-001 y US-002 funcionan de forma independiente.

---

## Phase 5: User Story 3 — Modificar un profesional existente (Priority: P3)

**Goal**: el rol "Administrador de la operación" modifica los datos de un profesional existente
(variante "Modificar" de FR-BW-005) mediante la API, persistiendo el cambio en PostgreSQL.

**Independent Test**: con un `profesional_id` existente en PostgreSQL (vía el fixture de T010),
autenticado como "Administrador del centro", enviar `PUT /profesionales/{id}` y verificar que el
sistema persiste el cambio en la tabla `profesionales` y deja un resultado observable; repetir con
un rol no autorizado y verificar que la API rechaza la solicitud (autorización de backend; el
ocultamiento en interfaz queda fuera de esta ejecución). No depende de haber ejecutado US-001 o
US-002 primero.

**AC-IDs cubiertos**: FR-BW-005

### Tests for User Story 3

- [X] T020 [P] [US3] [AC:FR-BW-005] Unit test: `ProfesionalService.modificar()` persiste el cambio en
  PostgreSQL solo para el rol "Administrador de la operación" y lo rechaza para cualquier otro, en
  `bw-backend/tests/unit/test_profesional_update_service.py` (usa el fixture de sesión aislada de
  T010) — Commit: `"test(bw-backend): add modificar profesional authorization tests (US3)"`

### Implementation for User Story 3

- [X] T021 [US3] [AC:FR-BW-005] Implementar `ProfesionalService.modificar()` (reutiliza el schema de
  T013, actualiza la fila en PostgreSQL vía la sesión de T004) en
  `bw-backend/src/services/profesional_service.py` (depende de T008, T013, T020; mismo archivo que
  T014/T017 → secuencial) — Commit: `"feat(bw-backend): implement modificar profesional service (US3)"`
- [ ] T022 [US3] [AC:FR-BW-005] Implementar el endpoint `PUT /profesionales/{id}` en
  `bw-backend/src/api/profesionales.py` (depende de T019, T021; mismo archivo que T015/T018/T019 →
  secuencial) — Commit: `"feat(bw-backend): add PUT /profesionales/{id} endpoint (US3)"`

**Checkpoint**: US-001, US-002 y US-003 funcionan de forma independiente.

---

## Phase 6: User Story 4 — Exportar datos de profesionales (Priority: P4)

**Goal**: BW persiste/entrega el dato exportado "Profesionales y especialidades" (FR-BW-037) —
mecanismo definido en `contracts/bw-data-exports.md` (`GET /profesionales/export`, endpoint de solo
lectura sobre PostgreSQL, sin notificación push).

**Independent Test**: con datos ya insertados en PostgreSQL (vía el fixture de T010), invocar
`GET /profesionales/export` directamente (sin pasar por US-002) y verificar que el sistema entrega
el conjunto completo de datos de "Profesionales y especialidades".

**AC-IDs cubiertos**: FR-BW-037

### Tests for User Story 4

- [ ] T023 [P] [US4] [AC:FR-BW-037] Unit test: `ProfesionalService.exportar()` serializa la lista
  completa de profesionales leída de PostgreSQL, en
  `bw-backend/tests/unit/test_profesional_export_service.py` (usa el fixture de sesión aislada de
  T010) — Commit: `"test(bw-backend): add exportar profesionales tests (US4)"`

### Implementation for User Story 4

- [ ] T024 [US4] [AC:FR-BW-037] Implementar `ProfesionalService.exportar()` en
  `bw-backend/src/services/profesional_service.py` (depende de T017, T023; mismo archivo que
  T014/T017/T021 → secuencial) — Commit: `"feat(bw-backend): implement exportar profesionales service (US4)"`
- [ ] T025 [US4] [AC:FR-BW-037] Implementar el endpoint `GET /profesionales/export` en
  `bw-backend/src/api/profesionales.py` (depende de T022, T024; mismo archivo que
  T015/T018/T019/T022 → secuencial) — Commit: `"feat(bw-backend): add GET /profesionales/export endpoint (US4)"`

**Checkpoint**: las 4 historias de "Gestión de profesionales" (backend) funcionan de forma
independiente.

---

## Phase 7: Validación final

- [ ] T026 [P] Ejecutar `pytest bw-backend/tests/unit/` (cada test usa el fixture de sesión aislada
  de T010) y corregir cualquier falla antes de continuar — Commit:
  `"test(bw-backend): green unit suite for Gestión de profesionales"`
- [ ] T027 Levantar `docker compose up` (`bw-backend` + PostgreSQL) y ejecutar manualmente el
  Escenario 1 de `quickstart.md` ("Crear/modificar un profesional", FR-BW-005) invocando
  `bw-backend` directamente (p. ej. `httpx`/`TestClient` de FastAPI o `curl`, sin `bw-frontend` por
  estar excluido de esta ejecución), y registrar el resultado en
  `specs/001-gestion-integral-reservas/validation-log.md` — Commit:
  `"docs(specs): record Gestión de profesionales (backend) quickstart validation"`
- [ ] T028 Ejecutar el Coverage Audit: correr
  `specs/001-gestion-integral-reservas/scripts/verify_traceability.py` (T001) contra este archivo y
  confirmar que los 6 AC-IDs de la tabla "Coverage Audit" tienen ≥1 tarea asociada — Commit:
  `"chore(tasks): run coverage audit for Gestión de profesionales (backend)"`
- [ ] T029 (FINAL) Registrar los SHA de commit reales de T001–T028 en
  `specs/001-gestion-integral-reservas/traceability.md` (una fila por tarea: Tnnn, AC-ID(s), ruta,
  SHA), usando `verify_traceability.py` — Commit:
  `"docs(specs): record real commit SHAs in traceability.md for Gestión de profesionales (backend)"`

---

## Coverage Audit

Todos los AC-IDs (FR-BW-ID) en el alcance de "Gestión de profesionales" (backend) y sus tareas:

| AC-ID | Descripción (spec.md) | Tareas |
|---|---|---|
| FR-BW-003 | Aceptar "Datos de profesionales" | T011, T013 |
| FR-BW-005 | Crear/Modificar profesional (autorización de backend; ocultamiento de UI fuera de esta ejecución) | T012, T014, T015, T020, T021, T022 |
| FR-BW-011 | Leer el dato importado "Profesionales y especialidades" (lectura local a PostgreSQL) | T016, T017 |
| FR-BW-025 | Mostrar "Ficha Profesionales" (backend: provisión de datos vía endpoints; renderizado fuera de esta ejecución) | T019 |
| FR-BW-031 | "Profesionales Query API" (servida por BW desde PostgreSQL propio) | T016, T017, T018 |
| FR-BW-037 | Exportar "Profesionales y especialidades" | T023, T024, T025 |

Sin AC-ID huérfano: los 6 requisitos en el alcance de esta ejecución tienen al menos una tarea.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: T001 primero por instrucción explícita, luego T002, luego T003.
- **Foundational (Phase 2)**: depende de Setup — bloquea las 4 historias. T004 (conexión DB) es el
  prerrequisito central: T005, T006 dependen de T004; T007 (migración, generar + aplicar) depende de
  T003, T005, T006; T008 y T009 solo dependen de T002 (paralelos entre sí y con la cadena T004-T007);
  T010 (fixture de sesión aislada) depende de T004 y T007 — necesita que la tabla `profesionales` ya
  exista para poder usarla en los tests.
- **User Stories (Phase 3–6)**: dependen todas de Foundational (incluido T010, ya que todas las
  pruebas de servicio usan su fixture).
  - US-001 (P1): sin dependencia de otras historias.
  - US-002 (P2): sin dependencia de otras historias (usa datos insertados directamente en PostgreSQL
    vía el fixture de T010, no requiere haber ejecutado US-001).
  - US-003 (P3): reutiliza el schema de US-001 (`ProfesionalCreateInput`, T013) y el router de
    US-002 (T019, mismo archivo → secuencial), pero es testeable de forma independiente vía
    `profesional_id` directo.
  - US-004 (P4): reutiliza `ProfesionalService.listar()` de US-002 (T017) y el router de US-003
    (T022, mismo archivo → secuencial), pero es testeable de forma independiente invocando el
    endpoint de exportación directamente.
- **Validación final (Phase 7)**: depende de que todas las historias deseadas estén completas.

### Parallel Opportunities

- T003 (Setup) en paralelo tras T002.
- T005 y T006 (Foundational) en paralelo entre sí (archivos distintos, ambos dependen solo de T004);
  T008 y T009 en paralelo entre sí y con la cadena T004→T005/T006→T007 (archivos distintos, ambos
  dependen solo de T002); T010 no es paralelo — depende de que T007 haya terminado.
- Dentro de US-001: T011 y T012 (tests) en paralelo.
- Dentro de US-002: ninguna tarea de implementación es paralela entre sí (todas tocan
  `profesional_service.py`/`profesionales.py`, ya secuenciadas); T016 (test) es independiente.
- Dentro de US-003: T020 (test) en paralelo con el resto de Foundational/otras historias ya cerradas.
- Dentro de US-004: T023 (test) en paralelo con tareas de otras historias.
- Ningún par de tareas marcadas `[P]` modifica el mismo archivo dentro de la misma fase.

---

## Parallel Example: User Story 1

```bash
# Tests de US-001 en paralelo:
Task: "Unit test schema Datos de profesionales en bw-backend/tests/unit/test_profesional_schema.py"
Task: "Unit test autorización + creación en bw-backend/tests/unit/test_profesional_create_service.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 únicamente)

1. Completar Phase 1: Setup (T001–T003).
2. Completar Phase 2: Foundational (T004–T010) — bloqueante.
3. Completar Phase 3: User Story 1 (T011–T015).
4. **Detener y validar**: probar "Crear un profesional nuevo" de forma independiente (vía API, con
   PostgreSQL corriendo en Docker).
5. Desplegar/demo si está listo — esto ya entrega valor de "Gestión de profesionales" (backend).

### Entrega incremental

1. Setup + Foundational → base lista (incluye PostgreSQL vía Docker y el fixture de sesión aislada
   de tests).
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
- Verificar que las pruebas fallan antes de implementar (T011/T012/T016/T020/T023 antes que su
  implementación correspondiente).
- Confirmar (commit) después de cada tarea o grupo lógico, usando el asunto indicado.
- Detenerse en cada checkpoint para validar la historia de forma independiente.
- Evitar: tareas vagas, conflictos de archivo entre tareas `[P]`, dependencias entre historias que
  rompan su independencia de prueba, tareas sobre `bw-frontend/` (excluido de esta ejecución), y
  tareas sobre `bw-backend/src/adapters/` (sin uso en el alcance de "Gestión de profesionales").
