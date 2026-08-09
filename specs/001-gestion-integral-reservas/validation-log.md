# Validation Log: Gestión de profesionales (Bundle Backend/Frontend Web, solo Backend)

**Tarea**: T027 | **Fecha**: 2026-08-09 | **Entorno**: `bw-backend` + PostgreSQL vía
`docker compose up --build` (`bw-backend/docker-compose.yml`), sin `bw-frontend` (excluido de
esta ejecución). Validación manual contra `http://localhost:8000` con `curl`.

## Escenario 1 — Crear/modificar un profesional (FR-BW-005)

Referencia: `quickstart.md` §Escenario 1.

1. `POST /profesionales` con `{"nombre": "Escenario1 QA"}`, header
   `X-Rol: administrador-operacion` → **201**, respuesta
   `{"id": "67dafc70-...", "nombre": "Escenario1 QA", "especialidades": []}`.
2. `GET /profesionales/{id}` → **200**, devuelve el mismo registro (FR-BW-025, "Ficha
   Profesionales" refleja el resultado observable de FR-BW-005).
3. `PUT /profesionales/{id}` con `{"nombre": "Escenario1 QA Modificado"}`, mismo rol → **200**,
   `nombre` actualizado — confirma la variante "modificar" de FR-BW-005.

**Resultado**: ✅ el sistema persiste el registro en su PostgreSQL propio y deja un resultado
observable, tanto para crear como para modificar.

## Escenario 5 — Autorización (aclaración de Etapa G)

Referencia: `quickstart.md` §Escenario 5.

- `POST /profesionales` con header `X-Rol: coordinador-agenda` (rol NO autorizado) → **403**,
  `{"detail": "El rol 'coordinador-agenda' no está autorizado para esta acción; se requiere
  'Administrador de la operación'."}`.

**Resultado**: ✅ la acción se rechaza para un rol distinto de "Administrador de la operación"
(Clarifications, Sesión 2026-08-05/2026-08-08). El ocultamiento de la acción en una interfaz de
usuario queda fuera de esta ejecución (sin `bw-frontend` — ver `tasks.md` §"Nota de alcance:
backend sin frontend").

## Notas

- Se detectó y corrigió un defecto real durante esta validación: el `CMD` original de
  `bw-backend/Dockerfile` ejecutaba `uvicorn src.main:app`, lo que trataba `src` como paquete
  Python y rompía las importaciones absolutas del código (`from api.profesionales import ...`,
  escritas para `src/` en el `sys.path`, consistente con `pyproject.toml`'s
  `[tool.pytest.ini_options] pythonpath = ["src"]`). Corregido a
  `uvicorn main:app --app-dir src ...`, que aplica la misma convención de import que usan los
  tests con pytest. Verificado: el contenedor arranca y sirve `/docs` con 200.
- Los datos de prueba insertados durante esta validación se eliminaron de la tabla `profesionales`
  al finalizar (`DELETE FROM profesionales WHERE nombre LIKE 'Escenario1%'`), dejando la base de
  datos en el mismo estado (vacía) en que estaba antes de esta ejecución.
- No se validaron los Escenarios 2, 3 y 4 de `quickstart.md`: pertenecen a "Gestión de servicios",
  "Gestión de agenda" y "Gestión de clientes", fuera del alcance de "Gestión de profesionales"
  (`tasks.md` §Alcance de esta ejecución).
