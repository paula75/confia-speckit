# Phase 0 Research: Bundle Backend/Frontend Web (BW)

**Feature**: Gestión Integral de Reservas | **Bundle**: Backend/Frontend Web (alcance por
`bundle-scope.md`) | **Fecha**: 2026-08-08

Alcance de esta investigación: únicamente las decisiones de diseño que `spec.md` difirió
explícitamente a `/speckit.plan` (esquema técnico de los contratos compartidos FR-BW-029..034,
atributos de 4 entidades, y "contexto técnico" en general — ver pie de página de `spec.md`), más
las decisiones de stack/testing que ningún requisito respalda y que por tanto no constituyen
ambigüedad de negocio sino elección de implementación. Los `[NEEDS CLARIFICATION]` que `spec.md`
deja abiertos sin remitirlos a esta etapa (umbrales de NFR-TEC/NFR-OP, metas de desempeño, permisos
de los roles fuera de BW) **no se resuelven aquí** — se listan en "Fuera de alcance de esta
investigación" al final, en vez de inventarse.

**Re-sincronización (2026-08-08)**: una sesión adicional de `/speckit.clarify` (bundle BW, misma
fecha) resolvió el comportamiento general ante fallo del contrato compartido (FR-BW-029..034,
reintento automático) y de FR-BW-044 (reintento + resincronización por reconsulta) — ver `spec.md`
§Clarifications, Sesión 2026-08-08. Este documento no se había actualizado con esas decisiones hasta
ahora (brecha detectada por `/speckit.analyze`, hallazgos I1/U1/U2); las secciones siguientes
definen los parámetros concretos (número de reintentos, backoff) que `spec.md` remite explícitamente
a esta etapa, y resuelven el tipo del campo `especialidades` (marcado `// TBD` en `data-model.md`).

## Decisión: Framework de frontend

- **Decision**: React con TypeScript en modo estricto sobre JavaScript.
- **Rationale**: `composed/plan_input.md` declara "Javascript" como stack de BW; el framework
  concreto (React) y el modo de tipado (TypeScript estricto) están declarados explícitamente como
  entrada de esta ejecución de `/speckit.plan` (`prompts/etapa-i-plan.md` §Stack: "Frontend usa
  React con typescript estricto"), por lo que dejan de ser una decisión abierta de implementación.
  Se requiere una capa de componentes para las 5 vistas administrativas de FR-BW-022 a FR-BW-028
  (dashboard, agenda, fichas de cliente/profesional, confirmaciones) más los 4 formularios de
  FR-BW-005 a FR-BW-008; React cubre ese requisito.
- **Alternatives considered**: no aplica — el framework y el modo de tipado están fijados
  explícitamente para esta ejecución, no son una elección abierta entre alternativas.

## Decisión: Framework de backend

- **Decision**: FastAPI sobre Python.
- **Rationale**: "Python" está declarado como stack de BW en `composed/plan_input.md`; el
  framework concreto (FastAPI) está declarado explícitamente como entrada de esta ejecución de
  `/speckit.plan` (`prompts/etapa-i-plan.md` §Stack: "Backend usa python con el framework
  FastAPI"), por lo que deja de ser una decisión abierta de implementación. BW expone endpoints
  propios hacia `bw-frontend` y consume el contrato compartido con AC/BA (FR-BW-029 a FR-BW-034) —
  FastAPI, orientado a APIs REST tipadas, encaja directamente.
- **Alternatives considered**: no aplica — el framework está fijado explícitamente para esta
  ejecución, no es una elección abierta entre alternativas.

## Decisión: Modo de tipado estricto en frontend (TypeScript)

- **Decision**: `tsconfig.json` de `bw-frontend` con `"strict": true` (habilita, entre otras,
  `strictNullChecks`, `noImplicitAny`).
- **Rationale**: Declarado explícitamente como entrada de esta ejecución de `/speckit.plan`
  (`prompts/etapa-i-plan.md` §Stack: "Frontend usa React con typescript estricto"). Los tipos de
  las entidades diferidas por `spec.md` §Clarifications (ver `data-model.md`, varios campos
  `// TBD`) deben modelarse en TS de forma explícita en vez de con `any`, para que el modo estricto
  sea consistente con el resto del código.
- **Alternatives considered**: no aplica — el modo estricto está fijado explícitamente para esta
  ejecución.

## Decisión: Framework de pruebas

- **Decision**: Backend: pytest para `bw-backend/tests/unit/`. Frontend: `bw-backend` tiene
  pruebas unitarias declaradas explícitamente para esta ejecución (`prompts/etapa-i-plan.md`
  §Stack: "Se incluyen test unitarios en backend"); `bw-frontend` no tiene un framework de pruebas
  declarado explícitamente por ninguna fuente — se deja como decisión abierta de implementación:
  un runner de pruebas de componentes estándar de TypeScript/React (p. ej. Vitest/Jest) sería
  compatible con el stack, pero no se fija aquí como requisito.
- **Rationale**: Para el backend, pytest resuelve directamente la exigencia explícita de pruebas
  unitarias. Para el frontend, ni el canvas, ni `spec.md`, ni el stack de esta ejecución declaran
  una herramienta de pruebas — no se inventa una obligación de pruebas de frontend que nadie pidió.
- **Alternatives considered**: unittest (Python) — se prefiere pytest por convención de mercado y
  por ser el runner estándar para proyectos FastAPI; sin impacto en requisitos.

## Decisión: Esquema del contrato de API interna compartido (FR-BW-029 a FR-BW-034)

- **Decision**: Ver `contracts/bw-shared-internal-api.md`. Se define como una API REST con 6
  operaciones (3 queries + 3 commands), consumida por `bw-backend` mediante un adaptador dedicado
  (Principio de constitution P21).
- **Rationale**: `spec.md` §Clarifications aclaró explícitamente que estos 6 requisitos comparten
  la misma API interna con Agente Conversacional y Backend Agendamiento, y diferió el "esquema
  técnico y el formato de respuesta de error" a esta etapa. Definir el esquema es exactamente lo
  que esta etapa debe resolver.
- **Alternatives considered**: acceso directo a la base de datos de Backend Agendamiento desde BW
  (rechazado: violaría el Principio P9 "integración desacoplada" y P13 "única fuente de
  información", y contradiría la aclaración de "API compartida" ya registrada en `spec.md`).

## Decisión: Política de reintento del contrato compartido (FR-BW-029 a FR-BW-034)

- **Decision**: máximo 3 reintentos con backoff exponencial (1s, 2s, 4s) por llamada al contrato
  compartido. Si los 3 intentos fallan, BW propaga el `error.code` recibido al llamador (frontend o
  servicio interno de BW) sin más reintentos automáticos.
- **Rationale**: `spec.md` §Clarifications, Sesión 2026-08-08 aclaró explícitamente el reintento
  automático y difirió "número de reintentos y backoff" a esta etapa (ver `contracts/bw-shared-internal-api.md`).
  3 intentos con backoff corto es un valor de mercado estándar para una llamada interna entre
  bundles del mismo sistema (no una API externa de terceros con latencia impredecible); acota la
  espera percibida por "Administrador de la operación" sin renunciar a tolerar fallos transitorios.
- **Alternatives considered**: reintento indefinido (rechazado: podría colgar la UI indefinidamente
  ante una falla persistente, sin ningún requisito que lo exija); un único reintento (rechazado:
  insuficiente para fallas transitorias breves típicas de red/proceso).

## Decisión: Política de reintento y resincronización de FR-BW-044

- **Decision**: al recibir un evento de cambio de agenda, si su procesamiento falla, BW reintenta
  hasta 3 veces (mismo backoff que arriba: 1s, 2s, 4s). Si tras 3 intentos el evento sigue fallando,
  o si BW detecta que un evento llegó fuera de secuencia (marca de tiempo/secuencia menor a la del
  último evento aplicado), BW dispara una resincronización completa invocando
  `GET /internal/disponibilidad` (Disponibilidad Query API, FR-BW-029) para el rango afectado, en
  vez de seguir esperando el evento perdido.
- **Rationale**: `spec.md` §Clarifications, Sesión 2026-08-08 aclaró el mecanismo (reintentar y
  resincronizar por reconsulta) pero no fijó el número de reintentos ni el criterio exacto de "fuera
  de orden". Ningún requisito de negocio depende de un valor numérico específico, por lo que se
  resuelve aquí como decisión de implementación pura (mismo tratamiento que "Decisión: Framework de
  pruebas" arriba), reutilizando el backoff del resto del adaptador por consistencia.
- **Alternatives considered**: resincronizar en cada evento fallido sin reintentar primero
  (rechazado: generaría carga innecesaria en la Disponibilidad Query API ante fallas transitorias de
  un solo evento).

## Decisión: Tipo del campo `especialidades` (Profesionales y especialidades)

- **Decision**: `especialidades` es una lista de cadenas de texto libre (`list[str]`), no una
  referencia a `Catálogo de servicios`.
- **Rationale**: `data-model.md` dejó el campo como `// TBD` porque ningún FR-BW declara si es texto
  libre o referencia. Ninguno de los FR-BW que usan la entidad (003, 005, 011, 025, 037) describe una
  relación explícita entre "especialidad" y una entrada del catálogo de servicios (p. ej. FR-BW-006
  "Crear/Modificar Servicios" no menciona asociarlo a un profesional); forzar una referencia
  inventaría una relación de negocio no respaldada. Texto libre es la opción mínima consistente con
  la evidencia disponible. Se resuelve aquí (no en `spec.md`) porque `spec.md` §Clarifications,
  Sesión 2026-08-05 difirió explícitamente a esta etapa la definición de atributos de esta entidad.
- **Alternatives considered**: referencia a `Catálogo de servicios` (rechazada: ningún FR-BW la
  respalda; puede revisarse si una futura sesión de negocio confirma esa relación).

## Decisión: Atributos de las 4 entidades diferidas (Ficha clientes, Disponibilidad Agenda,
## Catálogo de servicios, Profesionales y especialidades)

- **Decision**: Ver `data-model.md`. Los atributos se derivan únicamente de cómo cada entidad es
  usada por los FR-BW que la importan/exportan/muestran — no se agregó ningún atributo sin un FR
  que lo motive.
- **Rationale**: `spec.md` §Clarifications diferió explícitamente esta definición a `/speckit.plan`
  ("no se inventan atributos en esta especificación").
- **Alternatives considered**: dejar los atributos sin definir hasta `/speckit.tasks` (rechazado:
  contradice la instrucción explícita de esta etapa de "resolver mediante decisiones de diseño
  únicamente aquellos aspectos que la Specification haya diferido explícitamente a esta etapa" —
  este es exactamente uno de esos aspectos).

## Fuera de alcance de esta investigación (no resuelto, no inventado)

Estos ítems permanecen como `[NEEDS CLARIFICATION]` en `spec.md` y **no** fueron diferidos
explícitamente a `/speckit.plan`; por lo tanto no se resuelven en este plan, consistente con la
restricción de esta etapa de no inventar decisiones de negocio:

- Umbral/criterio verificable de `NFR-TEC-1` a `NFR-TEC-6` y objetivo/ventana de `NFR-OP-1` a
  `NFR-OP-3` (no hay evidencia de que estos NFR sean específicos de BW; ver `plan.md` §Technical
  Context → Performance Goals).
- Observabilidad (Principio de constitution P22): ningún FR ni NFR de BW declara un requisito de
  logging/monitoreo; ver `plan.md` §Complexity Tracking para la justificación formal de este vacío.
- Permisos de "Coordinador de agenda", "Prestador del servicio" y "Solicitante de reserva" fuera
  de las 4 acciones ya aclaradas de BW.
- Cuantificación de "GUI amigable" (constraint declarada para BW sin métrica).
- Metas de desempeño y escala (usuarios concurrentes, volumen de datos) propias de BW.

Estos puntos deben resolverse por el cliente/negocio (vía una sesión de `/speckit.clarify`
adicional o una decisión explícita de producto), no por este plan.
