# Data Model: Bundle Backend/Frontend Web (BW)

**Feature**: Gestión Integral de Reservas | **Bundle**: Backend/Frontend Web

**Alcance y proveniencia**: modela únicamente las entidades que el bundle BW usa según
`spec.md` §Key Entities y §Requirements (FR-BW-001 a FR-BW-044). Para las 4 entidades que
`spec.md` §Clarifications diferió explícitamente a esta etapa (Ficha clientes, Disponibilidad
Agenda, Catálogo de servicios, Profesionales y especialidades), los campos siguientes son una
**inferencia de diseño** basada en cómo cada FR-BW usa la entidad (qué se ingresa, qué se muestra,
qué se modifica) — no son texto literal de ningún canvas, porque ningún canvas declaró atributos.
Ningún campo se agregó sin que un FR-BW lo motive; donde la evidencia es insuficiente para un campo
razonable, se deja como `// TBD` en vez de inventarse.

## Entidades propias de BW

### Multimedia Web

Declarada en `spec.md` §Key Entities como objeto de datos propio de BW (Object Storage, ver
`plan.md` §Technical Context → Storage). **Ningún FR-BW describe cómo se crea, lee, actualiza o
elimina este objeto** — es una brecha ya señalada en `checklists/bw-requirements.md` CHK003; el
modelo de datos siguiente cubre solo su forma mínima para no bloquear el diseño de las otras
entidades, no resuelve esa brecha.

| Campo | Tipo | Notas |
|---|---|---|
| `id` | identificador | — |
| `tipo` | enum | `// TBD` — ningún FR-BW especifica qué tipos de multimedia admite BW |
| `referencia_almacenamiento` | string | Ruta/clave en Object Storage |
| `entidad_asociada` | referencia | `// TBD` — no se declara a qué entidad se asocia (¿Servicio? ¿Profesional?) |

## Entidades diferidas por `spec.md` §Clarifications (atributos inferidos, no literales)

### Ficha clientes

Usada por: FR-BW-004 (input "Datos de clientes"), FR-BW-008 (modificar), FR-BW-010 (import),
FR-BW-024 (mostrar), FR-BW-036 (export).

| Campo | Tipo | Motivado por |
|---|---|---|
| `id` | identificador | Requerido para "Modificar datos Clientes" (FR-BW-008) — no se puede modificar sin identificar el registro |
| `nombre` | string | "Datos de clientes" (FR-BW-004) — dato mínimo de identificación humana |
| `datos_contacto` | string/objeto | "Datos de clientes" (FR-BW-004) — ningún canvas especifica si es teléfono, email o ambos; `// TBD` en cuanto a estructura exacta |
| `preferencias` | referencia | La entidad de negocio "Preferencias del cliente" (BCC, P1BO-09) existe en el sistema pero no está declarada como parte de "Ficha clientes"; se deja como referencia externa, no se fusiona sin evidencia |

### Disponibilidad Agenda

Usada por: FR-BW-002 (input "Disponibilidad de agenda"), FR-BW-007 (modificar agenda),
FR-BW-009 (import), FR-BW-023 (mostrar "Agenda horaria"), FR-BW-035 (export), FR-BW-044
(sincronización en tiempo real desde Backend Agendamiento, aclarado en Clarifications).

| Campo | Tipo | Motivado por |
|---|---|---|
| `id` | identificador | Requerido para identificar el bloque modificado por FR-BW-007 |
| `profesional_id` | referencia a Profesionales y especialidades | La agenda es "del Centro" y se administra por profesional (FR-BW-025 "Ficha Profesionales" coexiste con la agenda) |
| `fecha` | fecha | "Agenda horaria" (FR-BW-023) implica una dimensión temporal |
| `hora_inicio` / `hora_fin` | hora | Igual que arriba — sin esto no hay "disponibilidad horaria" que mostrar |
| `estado` | enum (`disponible`/`reservado`/`bloqueado`) | FR-BW-044 sincroniza en tiempo real "el cambio" emitido por Backend Agendamiento; requiere un estado que cambie |

### Catálogo de servicios

Usada por: FR-BW-001 (input "Datos de servicios"), FR-BW-006 (crear/modificar), FR-BW-012
(import), FR-BW-039 (export).

| Campo | Tipo | Motivado por |
|---|---|---|
| `id` | identificador | Requerido para "Crear/Modificar Servicios" (FR-BW-006) |
| `nombre` | string | "Datos de servicios" (FR-BW-001) |
| `descripcion` | string | `// TBD` — no declarado explícitamente; incluido como mínimo razonable de un catálogo, marcar para validar con negocio |
| `duracion` | duración | Necesario para calcular "Disponibilidad Agenda" contra un servicio, pero ningún FR lo declara explícitamente — `// TBD`, no se asume un valor |

### Profesionales y especialidades

Usada por: FR-BW-003 (input "Datos de profesionales"), FR-BW-005 (crear/modificar), FR-BW-011
(import), FR-BW-025 (mostrar "Ficha Profesionales"), FR-BW-037 (export).

| Campo | Tipo | Motivado por |
|---|---|---|
| `id` | identificador | Requerido para "Crear/Modificar profesional" (FR-BW-005) |
| `nombre` | string | "Datos de profesionales" (FR-BW-003) |
| `especialidades` | `list[str]` (texto libre) | El nombre de la entidad ("Profesionales **y especialidades**") exige el campo. Resuelto como texto libre, no referencia a `Catálogo de servicios` — ver `research.md` §"Tipo del campo especialidades" (re-sincronización 2026-08-08); ningún FR-BW declara esa relación. |

## Entidades externas consumidas (no propiedad de BW — esquema no se define aquí)

Estas entidades entran a BW por importación (Data imports) desde otro bundle. Definir su esquema
excede el alcance de `bundle-scope.md` (pertenecen a AC/BA); BW solo las consume.

| Entidad | Importada en | Propietario probable (referencia informativa) |
|---|---|---|
| Reglas de negocio | FR-BW-014 | Compartida con AC (FR-AC-016) y BA (FR-BA-006 exporta) |
| Historial Conversación | FR-BW-013 | Compartida con AC (FR-AC-013/045) y BA (FR-BA-009) |
| Configuración conversacional | FR-BW-015 | Compartida con AC (FR-AC-012) y BA (FR-BA-028 exporta) |

## Relaciones

```text
Profesionales y especialidades (1) ──< (N) Disponibilidad Agenda
Catálogo de servicios (1) ──< (N)? Disponibilidad Agenda   // TBD: ¿un bloque de agenda referencia un servicio?
Ficha clientes (1) ──< (N) Reserva   // "Reserva" es una entidad de negocio (BCC) fuera del alcance de datos propios de BW; BW la consume vía el contrato compartido, no la modela aquí
Multimedia Web (N) ──> (1) entidad_asociada   // TBD: destino de la asociación no declarado
```

## Validaciones derivadas de requisitos

- Ninguna acción de creación/modificación (FR-BW-005 a FR-BW-008) puede ejecutarse sin el rol
  "Administrador de la operación" (aclarado en `spec.md` §Clarifications) — regla de autorización,
  no de forma del dato; se referencia aquí para trazabilidad hacia `contracts/`.
- No se derivan reglas de validación de formato/rango para ningún campo `// TBD`: inventarlas
  excedería la instrucción de no introducir decisiones de diseño no respaldadas por la
  Specification.
