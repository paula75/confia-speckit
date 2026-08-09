# Traceability: Gestión de profesionales (Bundle Backend/Frontend Web, solo Backend)

Una fila por tarea de `tasks.md` (T001–T029). La columna `SHA` permanece vacía hasta T029, que la
completa con los SHA de commit reales (nunca inventados) — ver `scripts/verify_traceability.py`.

| Tnnn | AC-ID(s) | Ruta | SHA |
|---|---|---|---|
| T001 | — | specs/001-gestion-integral-reservas/scripts/verify_traceability.py, specs/001-gestion-integral-reservas/traceability.md | |
| T002 | — | bw-backend/src/{models,services,adapters,api,db}/, bw-backend/tests/unit/, bw-backend/pyproject.toml, bw-backend/src/main.py | |
| T003 | — | bw-backend/Dockerfile, bw-backend/docker-compose.yml | |
| T004 | — | bw-backend/src/db/session.py, bw-backend/src/db/base.py | |
| T005 | — | bw-backend/alembic/, bw-backend/alembic.ini | |
| T006 | — | bw-backend/src/models/profesional.py | |
| T007 | — | bw-backend/alembic/versions/ | |
| T008 | — | bw-backend/src/services/auth.py | |
| T009 | — | bw-backend/src/api/profesionales.py, bw-backend/src/main.py | |
| T010 | — | bw-backend/tests/conftest.py | |
| T011 | FR-BW-003 | bw-backend/tests/unit/test_profesional_schema.py | |
| T012 | FR-BW-005 | bw-backend/tests/unit/test_profesional_create_service.py | |
| T013 | FR-BW-003 | bw-backend/src/models/profesional.py | |
| T014 | FR-BW-005 | bw-backend/src/services/profesional_service.py | |
| T015 | FR-BW-005 | bw-backend/src/api/profesionales.py | |
| T016 | FR-BW-011,FR-BW-031 | bw-backend/tests/unit/test_profesional_query_service.py | |
| T017 | FR-BW-011,FR-BW-031 | bw-backend/src/services/profesional_service.py | |
| T018 | FR-BW-031 | bw-backend/src/api/profesionales.py | |
| T019 | FR-BW-025 | bw-backend/src/api/profesionales.py | |
| T020 | FR-BW-005 | bw-backend/tests/unit/test_profesional_update_service.py | |
| T021 | FR-BW-005 | bw-backend/src/services/profesional_service.py | |
| T022 | FR-BW-005 | bw-backend/src/api/profesionales.py | |
| T023 | FR-BW-037 | bw-backend/tests/unit/test_profesional_export_service.py | |
| T024 | FR-BW-037 | bw-backend/src/services/profesional_service.py | |
| T025 | FR-BW-037 | bw-backend/src/api/profesionales.py | |
| T026 | — | bw-backend/tests/unit/ (pytest run, sin cambio de archivo) | |
| T027 | — | specs/001-gestion-integral-reservas/validation-log.md | |
| T028 | — | specs/001-gestion-integral-reservas/scripts/verify_traceability.py (ejecución) | |
| T029 | — | specs/001-gestion-integral-reservas/traceability.md | |
