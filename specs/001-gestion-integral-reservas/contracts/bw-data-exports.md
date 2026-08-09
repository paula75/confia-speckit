# Contract: Exportación de datos de BW (FR-BW-035, FR-BW-036, FR-BW-037, FR-BW-038, FR-BW-039)

**Alcance**: describe el mecanismo genérico que comparten los 5 requisitos "El sistema DEBE
persistir o entregar el dato exportado X" (mismo patrón textual en `spec.md`, un requisito por
entidad). No redefine el esquema de cada entidad exportada — ver `data-model.md` — solo el
mecanismo de entrega.

**Requisitos cubiertos**: FR-BW-035 (Disponibilidad Agenda), FR-BW-036 (Ficha clientes), FR-BW-037
(Profesionales y especialidades), FR-BW-038 (Reglas de negocio — entidad externa consumida, ver
`data-model.md` §Entidades externas consumidas), FR-BW-039 (Catálogo de servicios).

**Decisión de diseño**: `spec.md` no detalla el formato ni el mecanismo de entrega más allá de
"persistir o entregar" — ningún canvas ni Clarifications lo aclaran, y no fue diferido
explícitamente a esta etapa. Se resuelve aquí como decisión de implementación mínima, consistente
con la instrucción de no inventar alcance de negocio no respaldado: un endpoint HTTP de solo
lectura por entidad, sin mecanismo de notificación/"push" (ningún FR-BW lo exige).

**Nota**: este contrato se agregó en la re-sincronización de esta etapa (`/speckit.analyze`,
hallazgo G1); no existía en la primera pasada de `/speckit.plan`.

## Operación (mismo patrón, 5 endpoints)

- **Request**: sin parámetros (exporta el conjunto completo actual de la entidad).
- **Response 200**: lista completa de la entidad correspondiente, en el esquema de `data-model.md`.
- **Response de error**: mismo formato que `contracts/bw-shared-internal-api.md` §"Formato de
  error" (reutilizado por consistencia; ningún requisito exige uno distinto).

## Trazabilidad

| Endpoint | FR-BW | Entidad |
|---|---|---|
| `GET /profesionales/export` | FR-BW-037 | Profesionales y especialidades |
| `GET /clientes/export` | FR-BW-036 | Ficha clientes |
| `GET /servicios/export` | FR-BW-039 | Catálogo de servicios |
| `GET /agenda/export` | FR-BW-035 | Disponibilidad Agenda |
| `GET /reglas-negocio/export` | FR-BW-038 | Reglas de negocio (entidad externa, ver `data-model.md`) |

Cada ruta se implementa en el router de su entidad correspondiente en `bw-backend/src/api/` (ver
`plan.md` §Project Structure), no en un router de exportación centralizado — no hay ningún
requisito que exija centralizarlas.
