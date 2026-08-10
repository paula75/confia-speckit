# Contract: API interna compartida con Backend Agendamiento

**Alcance**: describe, en dos direcciones, el contrato que `spec.md` §Clarifications (Sesión
2026-08-05) aclaró como "la misma API interna compartida" entre Backend/Frontend Web (BW), Agente
Conversacional (AC) y Backend Agendamiento (BA). Diseñar la implementación de AC o BA queda fuera
del alcance de esta etapa (`bundle-scope.md`).

**Re-sincronización (2026-08-09)**: esta ejecución declara PostgreSQL como base de datos propia de
BW (`research.md` §"Persistencia propia de BW"). Con esa base, BW deja de necesitar consumir las 3
operaciones de **consulta** (Disponibilidad/Servicios/Profesionales Query API) — ahora las **sirve**
él mismo, respaldadas por su propio PostgreSQL. Las 3 operaciones de **Reserva** (crear/actualizar/
cancelar) se mantienen sin cambios: BW sigue **consumiéndolas**, porque "Reserva" no es una entidad
que `spec.md` §Clarifications atribuya a BW (ver `research.md` §"Decisión: Dirección del contrato de
API interna compartido"). Este cambio de dirección para las 3 consultas es una decisión de esta
ejecución, no un requisito nuevo de `spec.md`.

**Requisitos cubiertos**: FR-BW-029, FR-BW-030, FR-BW-031 (servidas por BW), FR-BW-032, FR-BW-033,
FR-BW-034 (consumidas por BW), FR-BW-044 (evento consumido por BW).

## Parte 1 — Operaciones que BW sirve (BW es el proveedor)

Respaldadas por las tablas PostgreSQL propias de BW (ver `data-model.md`). Cualquier bundle
(incluido AC o BA) puede consumirlas; su implementación es responsabilidad de `bw-backend/src/api/`.

### `GET /profesionales/query` — FR-BW-031 "Profesionales Query API"

- **Request**: sin parámetros obligatorios (listado completo) o `id` (consulta puntual).
- **Response 200**: lista o registro de `Profesionales y especialidades` (ver `data-model.md`).
- **Response de error**: ver "Formato de error" abajo.

### `GET /servicios/query` — FR-BW-030 "Servicios Query API"

- **Request**: sin parámetros obligatorios o `id`.
- **Response 200**: lista o registro de `Catálogo de servicios`.

### `GET /agenda/query` — FR-BW-029 "Disponibilidad Query API"

- **Request**: `profesional_id` (opcional), `fecha_desde`, `fecha_hasta`.
- **Response 200**: lista de bloques de `Disponibilidad Agenda`.

**Nota de nomenclatura**: se usan rutas propias (`/profesionales/query`, etc.) en vez de
`/internal/...` (usado en la ejecución anterior para las operaciones consumidas) para distinguir
visualmente, en el código, qué expone `bw-backend` de qué consume — no hay ningún requisito que fije
el nombre exacto de ruta; es una decisión de implementación menor.

## Parte 2 — Operaciones que BW consume (Backend Agendamiento es el proveedor)

**Adaptador**: BW accede a estas 3 operaciones exclusivamente a través de `bw-backend/src/adapters/`
(Principio de constitution P21), con reintento automático (ver "Comportamiento ante fallo" abajo).

### `POST /internal/reservas` — FR-BW-032 "Crear Reserva Command API"

- **Request**: `cliente_id`, `profesional_id`, `servicio_id`, `fecha`, `hora_inicio`. `// TBD`:
  ningún FR-BW declara si BW puede crear una reserva directamente o solo visualizarla; se incluye la
  operación porque `spec.md` la lista como requisito de BW, no se amplía su alcance de negocio.
- **Response 200**: `reserva_id`, `estado`.
- **Response de error**: ver "Formato de error" abajo.

### `PUT /internal/reservas/{reserva_id}` — FR-BW-033 "Actualizar Reserva Command API"

- **Request**: `reserva_id`, campos a modificar (subconjunto de los de creación).
- **Response 200**: `reserva_id`, `estado`.

### `DELETE /internal/reservas/{reserva_id}` — FR-BW-034 "Cancelar Reserva Command API"

- **Request**: `reserva_id`.
- **Response 200**: `reserva_id`, `estado: "cancelada"`.

### Evento consumido: cambio de agenda — FR-BW-044

- **Origen**: Backend Agendamiento emite el evento cuando una reserva afecta la disponibilidad.
- **Efecto en BW**: se aplica de inmediato a la tabla `Disponibilidad Agenda` de BW (tiempo real,
  Clarifications Sesión 2026-08-05).
- **Ante fallo/pérdida/desorden**: BW reintenta hasta 3 veces (mismo backoff que abajo); si falla
  definitivamente, BW resincroniza reconsultando el rango afectado **directamente a Backend
  Agendamiento** (no a su propio endpoint de Parte 1, que es lo que BW sirve a terceros) — ver
  `research.md` §"Política de reintento y resincronización de FR-BW-044".

## Formato de error (aplica a las operaciones consumidas de la Parte 2)

```json
{
  "error": {
    "code": "string",
    "message": "string",
    "contrato": "crear_reserva|actualizar_reserva|cancelar_reserva"
  }
}
```

- **Comportamiento ante fallo** (Clarifications, Sesión 2026-08-08 + `research.md` §"Política de
  reintento del contrato consumido"): ante timeout o error, BW reintenta automáticamente hasta 3
  veces con backoff exponencial (1s, 2s, 4s). Si los 3 intentos fallan, BW propaga el `error.code`
  recibido al llamador sin más reintentos automáticos.
- Las 3 operaciones que BW **sirve** (Parte 1) usan el mismo formato de error por consistencia,
  aunque no tienen política de reintento de cliente (BW es el servidor, no el cliente, para esas 3).

## Trazabilidad

| Operación | Dirección | FR-BW | Aclaración de origen |
|---|---|---|---|
| Disponibilidad Query API | BW sirve | FR-BW-029 | `spec.md` §Clarifications, Sesión 2026-08-05; dirección revisada esta ejecución (`research.md`) |
| Servicios Query API | BW sirve | FR-BW-030 | idem |
| Profesionales Query API | BW sirve | FR-BW-031 | idem |
| Crear Reserva Command API | BW consume | FR-BW-032 | `spec.md` §Clarifications, Sesión 2026-08-05 |
| Actualizar Reserva Command API | BW consume | FR-BW-033 | idem |
| Cancelar Reserva Command API | BW consume | FR-BW-034 | idem |
| Evento de cambio de agenda | BW consume | FR-BW-044 | idem + Sesión 2026-08-08 (reintento/resincronización) |
