# Traceability: Gestión de profesionales (Bundle Backend/Frontend Web, solo Backend)

Una fila por tarea de `tasks.md` (T001–T029). SHA reales de commit registrados por T029 (FINAL),
verificados contra `git cat-file -e` antes de escribirse — ninguno inventado. T029 no puede
registrar su propio SHA (no existe hasta que este archivo se confirma), consistente con el alcance
de T029 declarado en `tasks.md` ("T001–T028").

| Tnnn | AC-ID(s) | Ruta | SHA |
|---|---|---|---|
| T001 | — | specs/001-gestion-integral-reservas/scripts/verify_traceability.py, specs/001-gestion-integral-reservas/traceability.md | 4a1e0359a20450079b6c61225497b6375de892ba |
| T002 | — | bw-backend/src/{models,services,adapters,api,db}/, bw-backend/tests/unit/, bw-backend/pyproject.toml, bw-backend/src/main.py | 1efd5b2092c3dfe1d4cb8f7ae1651ff301e47656 |
| T003 | — | bw-backend/Dockerfile, bw-backend/docker-compose.yml | 613d25de97c8e8e591ba588f96b426252b46cdda |
| T004 | — | bw-backend/src/db/session.py, bw-backend/src/db/base.py | 6ca25c8d282b2deb581d77c3c0fbeeaa3cf93240 |
| T005 | — | bw-backend/alembic/, bw-backend/alembic.ini | 9ef174bbfaa2e72835bd2f75747ac39d8af5b771 |
| T006 | — | bw-backend/src/models/profesional.py | 2e7ab1d4cbd161f45676b2e235040be9c7a28183 |
| T007 | — | bw-backend/alembic/versions/ | 91ce53565a3b425737a2dd5d28791c7a23b29b36 |
| T008 | — | bw-backend/src/services/auth.py | 20047c89c79d4f3bede8968779dd6254cf74eabe |
| T009 | — | bw-backend/src/api/profesionales.py, bw-backend/src/main.py | 6ba36658182066948241e0693744ec6fcea6831c |
| T010 | — | bw-backend/tests/conftest.py | f8796dcdc7940b98bdc2be90cb5f5e4d6a25f7a4 |
| T011 | FR-BW-003 | bw-backend/tests/unit/test_profesional_schema.py | 3ab742fbaed42d7e996eb48040c3a5c9e3f33354 |
| T012 | FR-BW-005 | bw-backend/tests/unit/test_profesional_create_service.py | b4cad4c667106c4d47b5b85df9d9633f2b3abd51 |
| T013 | FR-BW-003 | bw-backend/src/models/profesional.py | 754773b7543eaf4161b6b05692f26ca2a4fe4372 |
| T014 | FR-BW-005 | bw-backend/src/services/profesional_service.py | 570768c39b7c9d08cdaeede548fd22897f4cddf1 |
| T015 | FR-BW-005 | bw-backend/src/api/profesionales.py | e860808e978463ea2043f18bb1ae804d81359855 |
| T016 | FR-BW-011,FR-BW-031 | bw-backend/tests/unit/test_profesional_query_service.py | c127e8f6603c2440e15273292d698184e9e7db1f |
| T017 | FR-BW-011,FR-BW-031 | bw-backend/src/services/profesional_service.py | 332c4223a1424dce868d1add23714437d61ac74c |
| T018 | FR-BW-031 | bw-backend/src/api/profesionales.py | ded176225d8a1835fe310a29bc863b9dcb4e770d |
| T019 | FR-BW-025 | bw-backend/src/api/profesionales.py | 62de2eedfd485dfef57ddc90bf3fd953171bad76 |
| T020 | FR-BW-005 | bw-backend/tests/unit/test_profesional_update_service.py | b434570529e79a71806d8b0158f5320d2b34d8d7 |
| T021 | FR-BW-005 | bw-backend/src/services/profesional_service.py | f129209103f0ce6431bdf7258b60455b4f4ef969 |
| T022 | FR-BW-005 | bw-backend/src/api/profesionales.py | 842c72db66cfeaa98f4e34adab4d570a345ec095 |
| T023 | FR-BW-037 | bw-backend/tests/unit/test_profesional_export_service.py | 390f3bc6642a44ba39fefc08853af614704b90c8 |
| T024 | FR-BW-037 | bw-backend/src/services/profesional_service.py | 8a2af54814f693df54e94edd386ac814038f8296 |
| T025 | FR-BW-037 | bw-backend/src/api/profesionales.py | 159bb14c5b64a5a1037aef3179c0a2add72fdc3c |
| T026 | — | bw-backend/tests/unit/ (pytest run, sin cambio de archivo) | 39efa855cb11509e98633665055ddd06b9f22fa5 |
| T027 | — | specs/001-gestion-integral-reservas/validation-log.md, bw-backend/Dockerfile | b77a317abdedd35e187317e3deadab97c1928d89 |
| T028 | — | specs/001-gestion-integral-reservas/scripts/verify_traceability.py (ejecución) | 1124401f3d819310e9b4369b51d23ede5fbfea36 |
| T029 | — | specs/001-gestion-integral-reservas/traceability.md | (este commit) |
