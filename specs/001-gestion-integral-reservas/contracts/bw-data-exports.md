# Contract: Exportación de datos de BW (FR-BW-035, FR-BW-036, FR-BW-037, FR-BW-038, FR-BW-039)

**Alcance**: describe el mecanismo genérico que comparten los 5 requisitos "El sistema DEBE
persistir o entregar el dato exportado X". No redefine el esquema de cada entidad exportada — ver
`data-model.md` — solo el mecanismo de entrega.

**Requisitos cubiertos**: FR-BW-035 (Disponibilidad Agenda), FR-BW-036 (Ficha clientes), FR-BW-037
(Profesionales y especialidades), FR-BW-038 (Reglas de negocio — entidad externa consumida, ver
`data-model.md` §Entidades externas consumidas), FR-BW-039 (Catálogo de servicios).

**Re-sincronización (2026-08-09)**: 4 de las 5 entidades exportadas (todas salvo "Reglas de
negocio") ahora se leen directamente de las tablas PostgreSQL propias de BW (ver `data-model.md`),
en vez de un origen sin persistencia propia como en la ejecución anterior. El mecanismo de entrega
(endpoint HTTP de solo lectura) no cambia.

**Decisión de diseño**: `spec.md` no detalla el formato ni el mecanismo de entrega más allá de
"persistir o entregar". Se resuelve como un endpoint HTTP de solo lectura por entidad, sin mecanismo
de notificación/"push" (ningún FR-BW lo exige).

## Operación (mismo patrón, 5 endpoints)

- **Request**: sin parámetros (exporta el conjunto completo actual de la entidad).
- **Response 200**: lista completa de la entidad correspondiente, en el esquema de `data-model.md`.
- **Response de error**: mismo formato que `contracts/bw-shared-internal-api.md` §"Formato de
  error" (reutilizado por consistencia).

## Trazabilidad

| Endpoint | FR-BW | Entidad | Fuente de datos |
|---|---|---|---|
| `GET /profesionales/export` | FR-BW-037 | Profesionales y especialidades | Tabla PostgreSQL propia |
| `GET /clientes/export` | FR-BW-036 | Ficha clientes | Tabla PostgreSQL propia |
| `GET /servicios/export` | FR-BW-039 | Catálogo de servicios | Tabla PostgreSQL propia |
| `GET /agenda/export` | FR-BW-035 | Disponibilidad Agenda | Tabla PostgreSQL propia (copia sincronizada, ver `data-model.md` §Nota de fuente de verdad) |
| `GET /reglas-negocio/export` | FR-BW-038 | Reglas de negocio | Entidad externa (ver `data-model.md`), no tiene tabla propia en BW — `// TBD`: mecanismo de entrega para un dato que BW no persiste no está resuelto por ningún FR-BW |

Cada ruta se implementa en el router de su entidad correspondiente en `bw-backend/src/api/` (ver
`plan.md` §Project Structure), no en un router de exportación centralizado.
