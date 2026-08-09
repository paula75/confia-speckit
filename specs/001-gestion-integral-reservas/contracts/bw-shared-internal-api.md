# Contract: API interna compartida (consumida por Backend/Frontend Web)

**Alcance**: describe el contrato desde la perspectiva de BW como **consumidor**. La API en sí es
compartida con Agente Conversacional y Backend Agendamiento (aclarado en `spec.md` §Clarifications,
Sesión 2026-08-05); diseñar la implementación de esos otros dos bundles queda fuera del alcance de
esta etapa (`bundle-scope.md`). El esquema y el formato de error que siguen son la decisión de
diseño que `spec.md` difirió explícitamente a `/speckit.plan` para FR-BW-029 a FR-BW-034.

**Requisitos cubiertos**: FR-BW-029, FR-BW-030, FR-BW-031, FR-BW-032, FR-BW-033, FR-BW-034.

**Adaptador**: BW accede a este contrato exclusivamente a través de una capa `adapters/` en
`bw-backend` (ver `plan.md` §Project Structure), consistente con el Principio de constitution P21
"Integración mediante adapters" — el resto del backend de BW no debe depender del formato exacto
del contrato.

## Operaciones (queries)

### `GET /internal/disponibilidad` — FR-BW-029 "Disponibilidad Query API"

- **Request**: `profesional_id` (opcional), `fecha_desde`, `fecha_hasta`.
- **Response 200**: lista de bloques de `Disponibilidad Agenda` (ver `data-model.md`).
- **Response de error**: ver "Formato de error" abajo.

### `GET /internal/servicios` — FR-BW-030 "Servicios Query API"

- **Request**: sin parámetros obligatorios (listado completo) o `id` (consulta puntual).
- **Response 200**: lista o registro de `Catálogo de servicios`.

### `GET /internal/profesionales` — FR-BW-031 "Profesionales Query API"

- **Request**: sin parámetros obligatorios o `id`.
- **Response 200**: lista o registro de `Profesionales y especialidades`.

## Operaciones (commands)

### `POST /internal/reservas` — FR-BW-032 "Crear Reserva Command API"

- **Request**: `cliente_id`, `profesional_id`, `servicio_id`, `fecha`, `hora_inicio`.
  `// TBD`: ningún FR-BW declara si BW puede crear una reserva directamente o solo visualizarla;
  se incluye la operación porque `spec.md` la lista como requisito de BW (FR-BW-032), no se amplía
  su alcance de negocio más allá de eso.
- **Response 200**: `reserva_id`, `estado`.
- **Response de error**: ver "Formato de error" abajo.

### `PUT /internal/reservas/{reserva_id}` — FR-BW-033 "Actualizar Reserva Command API"

- **Request**: `reserva_id`, campos a modificar (subconjunto de los de creación).
- **Response 200**: `reserva_id`, `estado`.

### `DELETE /internal/reservas/{reserva_id}` — FR-BW-034 "Cancelar Reserva Command API"

- **Request**: `reserva_id`.
- **Response 200**: `reserva_id`, `estado: "cancelada"`.

## Formato de error (aplica a las 6 operaciones)

```json
{
  "error": {
    "code": "string",
    "message": "string",
    "contrato": "disponibilidad|servicios|profesionales|crear_reserva|actualizar_reserva|cancelar_reserva"
  }
}
```

- **Decisión de diseño**: se estandariza un único formato de error para las 6 operaciones porque
  las 6 comparten la misma API (aclarado en `spec.md`); un formato distinto por operación
  introduciría inconsistencia sin ningún requisito que la exija.
- **Comportamiento ante fallo (timeouts, errores del contrato)**: resuelto (`spec.md`
  §Clarifications, Sesión 2026-08-08 + `research.md` §"Política de reintento del contrato
  compartido"). Ante timeout o respuesta de error, BW reintenta automáticamente hasta 3 veces con
  backoff exponencial (1s, 2s, 4s). Si los 3 intentos fallan, BW propaga el `error.code` recibido al
  llamador (frontend o servicio interno de BW) sin más reintentos automáticos.
- **Orden de eventos**: no aplica a las operaciones de este contrato — las 6 son query/command
  síncronas request-response, no eventos. El comportamiento ante eventos fuera de orden se define
  para FR-BW-044 en `research.md` §"Política de reintento y resincronización de FR-BW-044", no en
  este contrato.

## Trazabilidad

| Contrato | FR-BW | Aclaración de origen |
|---|---|---|
| Disponibilidad Query API | FR-BW-029 | `spec.md` §Clarifications, Sesión 2026-08-05 |
| Servicios Query API | FR-BW-030 | idem |
| Profesionales Query API | FR-BW-031 | idem |
| Crear Reserva Command API | FR-BW-032 | idem |
| Actualizar Reserva Command API | FR-BW-033 | idem |
| Cancelar Reserva Command API | FR-BW-034 | idem |
