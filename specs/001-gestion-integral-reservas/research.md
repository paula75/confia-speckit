# Phase 0 Research: Bundle Backend/Frontend Web (BW)

**Feature**: Gestión Integral de Reservas | **Bundle**: Backend/Frontend Web (alcance por
`bundle-scope.md`) | **Fecha**: 2026-08-05

Alcance de esta investigación: únicamente las decisiones de diseño que `spec.md` difirió
explícitamente a `/speckit.plan` (esquema técnico de los contratos compartidos FR-BW-029..034,
atributos de 4 entidades, y "contexto técnico" en general — ver pie de página de `spec.md`), más
las decisiones de stack/testing que ningún requisito respalda y que por tanto no constituyen
ambigüedad de negocio sino elección de implementación. Los `[NEEDS CLARIFICATION]` que `spec.md`
deja abiertos sin remitirlos a esta etapa (umbrales de NFR-TEC/NFR-OP, comportamiento ante fallo de
FR-BW-044, metas de desempeño, permisos de los roles fuera de BW) **no se resuelven aquí** — se
listan en "Fuera de alcance de esta investigación" al final, en vez de inventarse.

## Decisión: Framework de frontend

- **Decision**: React (o un framework de componentes equivalente) sobre JavaScript.
- **Rationale**: `composed/plan_input.md` declara "Javascript" como stack de BW pero no un
  framework específico. Se requiere una capa de componentes para las 5 vistas administrativas de
  FR-BW-022 a FR-BW-028 (dashboard, agenda, fichas de cliente/profesional, confirmaciones) más los
  4 formularios de FR-BW-005 a FR-BW-008. Un framework de componentes de mercado reduce trabajo
  respecto de JavaScript sin librería, sin contradecir ningún requisito (la elección exacta de
  framework no está respaldada por ningún FR, así que es una decisión de implementación, no de
  negocio).
- **Alternatives considered**: JavaScript "vanilla" con plantillas server-side (se descartó por
  no aportar valor frente a un framework de componentes estándar para un panel administrativo con
  varias vistas con estado); otro framework de componentes (intercambiable sin impacto en
  `spec.md` — no se fija una única opción como requisito, ver `plan.md` §Technical Context).

## Decisión: Framework de backend

- **Decision**: Un framework web de Python orientado a APIs REST (p. ej. FastAPI o equivalente).
- **Rationale**: "Python" está declarado como stack de BW en `composed/plan_input.md`. BW expone
  endpoints propios hacia `bw-frontend` y consume el contrato compartido con AC/BA (FR-BW-029 a
  FR-BW-034) — un framework de APIs REST encaja directamente sin decisiones adicionales no
  respaldadas.
- **Alternatives considered**: Framework full-stack con renderizado server-side (se descartó
  porque el frontend ya está separado por decisión de Structural Canvas — "Pagina web admin
  locales" como bundle de frontend distinto del backend).

## Decisión: Framework de pruebas

- **Decision**: pytest para `bw-backend`; un runner de pruebas de componentes estándar de
  JavaScript (p. ej. Vitest/Jest) para `bw-frontend`.
- **Rationale**: Ningún canvas ni `spec.md` declara herramienta de pruebas (`Testing: NEEDS
  CLARIFICATION` en el template de plan). Es una decisión de implementación pura, sin impacto en
  ningún requisito funcional — se resuelve aquí en vez de dejarla abierta, porque bloquearía
  cualquier verificación de las tareas de implementación futuras.
- **Alternatives considered**: unittest (Python) — se prefiere pytest por convención de mercado;
  sin impacto en requisitos.

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
- Comportamiento ante fallo de `FR-BW-044` (reintentos, orden de eventos, eventos perdidos).
- Permisos de "Coordinador de agenda", "Prestador del servicio" y "Solicitante de reserva" fuera
  de las 4 acciones ya aclaradas de BW.
- Cuantificación de "GUI amigable" (constraint declarada para BW sin métrica).
- Metas de desempeño y escala (usuarios concurrentes, volumen de datos) propias de BW.

Estos puntos deben resolverse por el cliente/negocio (vía una sesión de `/speckit.clarify`
adicional o una decisión explícita de producto), no por este plan.
