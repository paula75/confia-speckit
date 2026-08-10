# Data Model: Bundle Backend/Frontend Web (BW), solo Backend

**Feature**: Gestión Integral de Reservas | **Bundle**: Backend/Frontend Web (componente backend)

**Alcance y proveniencia**: modela únicamente las entidades que el backend de BW usa según
`spec.md` §Key Entities y §Requirements (FR-BW-001 a FR-BW-044). Para las 4 entidades que
`spec.md` §Clarifications diferió explícitamente a esta etapa (Ficha clientes, Disponibilidad
Agenda, Catálogo de servicios, Profesionales y especialidades), los campos siguientes son una
**inferencia de diseño** basada en cómo cada FR-BW usa la entidad — no son texto literal de ningún
canvas. Ningún campo se agregó sin que un FR-BW lo motive; donde la evidencia es insuficiente para
un campo razonable, se deja como `// TBD`.

**Re-sincronización (2026-08-09)**: esta ejecución declara PostgreSQL como base de datos propia de
`bw-backend` (`research.md` §"Persistencia propia de BW"), reemplazando la decisión anterior de
tratar estas 4 entidades como "DTOs de lectura desde un contrato externo, sin tabla propia". Los
campos inferidos por FR-BW no cambian de fondo — solo su mecanismo de persistencia (ahora tablas
SQLAlchemy/PostgreSQL, antes esquemas Pydantic de solo lectura).

## Entidades propias de BW (tablas PostgreSQL)

### Profesionales y especialidades

Usada por: FR-BW-003 (input "Datos de profesionales"), FR-BW-005 (crear/modificar), FR-BW-011
(import — ver nota), FR-BW-025 (mostrar "Ficha Profesionales"), FR-BW-031 (servida como
"Profesionales Query API" — ver `contracts/bw-shared-internal-api.md`), FR-BW-037 (export).

| Campo | Tipo (PostgreSQL / SQLAlchemy) | Motivado por |
|---|---|---|
| `id` | `UUID` / `Integer` identity, PK | Requerido para "Crear/Modificar profesional" (FR-BW-005) |
| `nombre` | `VARCHAR` | "Datos de profesionales" (FR-BW-003) |
| `especialidades` | `ARRAY(VARCHAR)` (texto libre, `list[str]`) | El nombre de la entidad exige el campo; resuelto como texto libre, no referencia a `Catálogo de servicios` — ver `research.md` §"Tipo del campo especialidades" |

**Nota sobre FR-BW-011** ("leer el dato importado 'Profesionales y especialidades'"): con
persistencia propia en PostgreSQL, esta lectura es una consulta directa a la tabla local de BW, no
una importación desde un sistema externo — el nombre del requisito ("dato importado") proviene del
Functional Canvas original, que asumía un origen externo; esta ejecución lo satisface como lectura
local porque BW es ahora dueño del dato (ver `research.md` §"Persistencia propia de BW").

### Ficha clientes

Usada por: FR-BW-004 (input "Datos de clientes"), FR-BW-008 (modificar), FR-BW-010 (import — ver
nota igual que arriba), FR-BW-024 (mostrar), FR-BW-036 (export).

| Campo | Tipo | Motivado por |
|---|---|---|
| `id` | `UUID`/`Integer` identity, PK | Requerido para "Modificar datos Clientes" (FR-BW-008) |
| `nombre` | `VARCHAR` | "Datos de clientes" (FR-BW-004) |
| `datos_contacto` | `VARCHAR`/`JSONB` | `// TBD` en cuanto a estructura exacta (¿teléfono, email, ambos?) — ningún canvas lo especifica |
| `preferencias` | referencia externa | La entidad de negocio "Preferencias del cliente" no está declarada como parte de "Ficha clientes"; se deja como referencia externa, no se fusiona sin evidencia |

### Catálogo de servicios

Usada por: FR-BW-001 (input "Datos de servicios"), FR-BW-006 (crear/modificar), FR-BW-012 (import —
ver nota igual que arriba), FR-BW-039 (export).

| Campo | Tipo | Motivado por |
|---|---|---|
| `id` | `UUID`/`Integer` identity, PK | Requerido para "Crear/Modificar Servicios" (FR-BW-006) |
| `nombre` | `VARCHAR` | "Datos de servicios" (FR-BW-001) |
| `descripcion` | `TEXT` | `// TBD` — mínimo razonable de un catálogo, no declarado explícitamente |
| `duracion` | `INTERVAL` | `// TBD` — necesario para calcular disponibilidad contra un servicio, pero ningún FR lo declara explícitamente |

### Disponibilidad Agenda

Usada por: FR-BW-002 (input "Disponibilidad de agenda"), FR-BW-007 (modificar agenda), FR-BW-009
(import — ver nota igual que arriba), FR-BW-023 (mostrar "Agenda horaria"), FR-BW-035 (export),
FR-BW-044 (sincronización en tiempo real desde Backend Agendamiento).

| Campo | Tipo | Motivado por |
|---|---|---|
| `id` | `UUID`/`Integer` identity, PK | Requerido para identificar el bloque modificado por FR-BW-007 |
| `profesional_id` | `FK → profesionales.id` | La agenda se administra por profesional (FR-BW-025 coexiste con la agenda) |
| `fecha` | `DATE` | "Agenda horaria" (FR-BW-023) implica una dimensión temporal |
| `hora_inicio` / `hora_fin` | `TIME` | Sin esto no hay "disponibilidad horaria" que mostrar |
| `estado` | `ENUM('disponible','reservado','bloqueado')` | FR-BW-044 sincroniza en tiempo real "el cambio" emitido por Backend Agendamiento; requiere un estado que cambie |
| `origen_ultimo_cambio` | `ENUM('bw','backend_agendamiento')` | `// TBD, campo técnico añadido en esta ejecución` para poder distinguir, ante auditoría, si el último cambio vino de una edición manual en BW (FR-BW-007) o de un evento de sincronización (FR-BW-044) — no cambia el comportamiento funcional, solo trazabilidad interna; ningún FR-BW lo exige explícitamente, se marca como decisión de implementación menor, no de negocio |

**Nota de fuente de verdad (P13)**: esta tabla es una copia sincronizada, no la fuente autoritativa
de reservas. BW la escribe en dos casos: (a) edición manual vía FR-BW-007, y (b) aplicación del
evento de FR-BW-044 emitido por Backend Agendamiento. Ante evento perdido o fuera de orden, BW
sobrescribe el rango afectado reconsultando directamente a Backend Agendamiento (`research.md`
§"Política de reintento y resincronización de FR-BW-044"), nunca al revés.

### Multimedia Web

Declarada en `spec.md` §Key Entities. Aclarado (Clarifications, Sesión 2026-08-08): su gestión
(carga/consulta/eliminación) queda fuera de alcance de esta iteración — **ningún FR-BW la requiere
todavía**. Se documenta su forma mínima únicamente para no perder la entidad, sin implementarla:

| Campo | Tipo | Notas |
|---|---|---|
| `id` | `UUID` | — |
| `tipo` | `// TBD` | Ningún FR-BW especifica qué tipos admite |
| `referencia_almacenamiento` | `// TBD` | Mecanismo de almacenamiento no decidido en esta ejecución — ningún FR lo requiere aún (podría ser una tabla PostgreSQL de metadatos + Object Storage para el binario, u otra combinación; se difiere hasta que exista un requisito) |
| `entidad_asociada` | `// TBD` | No se declara a qué entidad se asocia |

## Entidades externas consumidas (no propiedad de BW — esquema no se define aquí)

| Entidad | Uso en BW | Mecanismo |
|---|---|---|
| Reserva | FR-BW-032..034 (crear/actualizar/cancelar) | Consumida vía adaptador hacia Backend Agendamiento (`contracts/bw-shared-internal-api.md` §Operaciones consumidas). **No** se persiste en el PostgreSQL de BW — ver `plan.md` §Constitution Check, P13. |
| Reglas de negocio | FR-BW-014 | Import — esquema fuera del alcance de `bundle-scope.md` (pertenece a AC/BA) |
| Historial Conversación | FR-BW-013 | Import — idem |
| Configuración conversacional | FR-BW-015 | Import — idem |

## Relaciones

```text
Profesionales y especialidades (1) ──< (N) Disponibilidad Agenda   // FK profesional_id
Catálogo de servicios (1) ──< (N)? Disponibilidad Agenda   // TBD: ¿un bloque de agenda referencia un servicio? ningún FR-BW lo declara
Ficha clientes (1) ──< (N) Reserva   // Reserva es externa, no modelada en el PostgreSQL de BW
Multimedia Web (N) ──> (1) entidad_asociada   // TBD: destino de la asociación no declarado; sin implementar
```

## Validaciones derivadas de requisitos

- Ninguna acción de creación/modificación (FR-BW-005 a FR-BW-008) puede ejecutarse sin el rol
  "Administrador de la operación" (aclarado en `spec.md` §Clarifications) — regla de autorización, no
  de forma del dato; se aplica en la capa de servicio antes de llegar a la capa `db/`.
- La entidad "Reserva" nunca se escribe en el PostgreSQL de BW — invariante de arquitectura derivada
  del Principio de constitution P13, no un campo de validación de forma.
- No se derivan reglas de validación de formato/rango para ningún campo `// TBD`: inventarlas
  excedería la instrucción de no introducir decisiones de diseño no respaldadas por la Specification.
