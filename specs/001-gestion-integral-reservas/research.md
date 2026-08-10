# Phase 0 Research: Bundle Backend/Frontend Web (BW), solo Backend

**Feature**: Gestión Integral de Reservas | **Bundle**: Backend/Frontend Web, componente backend
(alcance por `bundle-scope.md` + restricción explícita de esta ejecución a solo backend,
`prompts/etapa-i-plan.md`) | **Fecha**: 2026-08-09

Alcance de esta investigación: las decisiones de diseño que `spec.md` difirió explícitamente a
`/speckit.plan` (esquema técnico de los contratos compartidos, atributos de 4 entidades, "contexto
técnico" en general), más las decisiones de implementación (ORM, migraciones, dockerización) que
ningún requisito respalda directamente y que por tanto no constituyen ambigüedad de negocio. Los
`[NEEDS CLARIFICATION]` que `spec.md` deja abiertos sin remitirlos a esta etapa (umbrales de
NFR-TEC/NFR-OP, metas de desempeño, permisos de roles fuera de BW) **no se resuelven aquí**.

**Re-sincronización (2026-08-09)**: esta ejecución reemplaza las decisiones de la versión anterior
(2026-08-08) relativas a (a) frontend — eliminadas, fuera de alcance de esta ejecución — y (b)
persistencia de BW — revisadas de raíz porque el stack de esta ejecución declara explícitamente
PostgreSQL y dockerización, información que no existía en la ejecución anterior.

**Re-sincronización (2026-08-09b)**: `prompts/etapa-i-plan.md` precisó el requisito de testing ("Se
incluyen test unitarios en backend que usan una sesion aislada de DB"), no declarado en la
ejecución anterior. Se agrega la decisión "Estrategia de aislamiento de base de datos en pruebas"
más abajo, que resuelve el hallazgo HIGH (U1) de la sesión de `/speckit-analyze` inmediatamente
posterior a esa ejecución: ningún artefacto anterior definía cómo las pruebas unitarias obtenían una
base de datos utilizable sin contaminarse entre tests.

## Decisión: Framework de backend

- **Decision**: FastAPI sobre Python.
- **Rationale**: Declarado explícitamente en `prompts/etapa-i-plan.md` §Stack: "Backend usa python
  con el framework FastAPI". Sin cambios respecto a la ejecución anterior.
- **Alternatives considered**: no aplica — framework fijado explícitamente.

## Decisión: Persistencia propia de BW (PostgreSQL)

- **Decision**: `bw-backend` persiste directamente en PostgreSQL las 4 entidades que `spec.md`
  §Clarifications (Sesión 2026-08-05, respuesta a la pregunta sobre falta de esquema) identifica como
  "entidades que BW administra por CRUD": Ficha clientes, Disponibilidad Agenda, Catálogo de
  servicios, Profesionales y especialidades. La entidad "Reserva" **no** se persiste aquí — sigue
  siendo propiedad de Backend Agendamiento, consumida vía el contrato compartido (ver siguiente
  decisión).
- **Rationale**: La ejecución anterior de este plan (2026-08-08) había decidido "BW no declara una
  base de datos relacional propia" explícitamente **porque** "ningún canvas ni la entrada de plan
  declaró una base de datos" en ese momento. `prompts/etapa-i-plan.md` de esta ejecución declara
  explícitamente "Base de datos postgresql a través de una imagen de docker" — la premisa de la
  decisión anterior ya no es cierta, por lo que esta ejecución la reemplaza en vez de mantenerla por
  inercia. Esto también resuelve, con evidencia de stack (no por invención), la brecha crítica que
  `/speckit-analyze` (sesión 2026-08-09, hallazgo I1) detectó en la ejecución anterior: el contrato
  compartido documentado no tenía ninguna operación de escritura para Profesionales (ni para
  Servicios, Agenda o Clientes), por lo que no había ningún mecanismo autorizado para que
  `ProfesionalService.crear()`/`modificar()` (FR-BW-005) persistiera algo. Con PostgreSQL propio, BW
  persiste sus propias escrituras administrativas sin necesitar extender un contrato compartido con
  otros dos bundles (AC, BA) fuera del alcance de esta ejecución.
- **Alternatives considered**: extender el contrato compartido con operaciones de escritura para
  Profesionales/Servicios/Agenda/Clientes (opción registrada en
  `clarify/clarify-log.md`, sin sesión formal de `/speckit.clarify` que la cerrara; rechazada aquí
  porque exigiría modificar el contrato de dos bundles fuera de este alcance, y porque el stack de
  esta ejecución ya provee una alternativa sin esa dependencia cruzada); repositorio en memoria
  (rechazado: no sobrevive un reinicio del servicio, y el stack ya declara un motor de BD real).

## Decisión: Motor de base de datos y herramientas de acceso a datos

- **Decision**: SQLAlchemy como ORM sobre PostgreSQL, con Alembic para migraciones, y `psycopg`
  como driver.
- **Rationale**: `prompts/etapa-i-plan.md` declara PostgreSQL explícitamente pero no declara ORM ni
  herramienta de migraciones — decisión de implementación abierta, no de negocio. SQLAlchemy es el
  ORM estándar de mercado para FastAPI + PostgreSQL, y Alembic es su herramienta de migraciones
  complementaria estándar; ambos evitan escribir SQL crudo disperso por el código, consistente con
  P17 "alta cohesión". Sin este par de decisiones no se puede completar el diseño de `data-model.md`
  con un mecanismo de persistencia concreto.
- **Alternatives considered**: SQL crudo con un driver mínimo (`psycopg` directo, sin ORM) —
  rechazado: dispersaría el esquema de las 4 entidades por el código sin un punto único de
  definición, contra P17; SQLModel (capa sobre SQLAlchemy + Pydantic) — considerado, pero SQLAlchemy
  + Pydantic por separado es la combinación más consolidada para FastAPI y no introduce una
  dependencia adicional sin necesidad clara.

## Decisión: Dockerización del backend

- **Decision**: `bw-backend/Dockerfile` para el servicio FastAPI, `bw-backend/docker-compose.yml`
  que orquesta el contenedor del backend junto con un contenedor de la imagen oficial `postgres`.
- **Rationale**: Declarado explícitamente en `prompts/etapa-i-plan.md` §Stack: "Backend se
  dockeriza" y "Base de datos postgresql a través de una imagen de docker". `docker-compose.yml` es
  el mecanismo estándar de mercado para levantar juntos un servicio y su base de datos en desarrollo
  local, sin inventar una topología de despliegue que ningún requisito exige (el despliegue en
  Production sigue diferido a `NFR-OP-2` "Deploy manual coordinado por Área de Sistemas", sin detalle
  adicional aquí).
- **Alternatives considered**: no aplica para el hecho de dockerizar (declarado explícitamente); para
  la orquestación local, se prefiere `docker-compose` sobre instrucciones manuales de `docker run`
  por ser el estándar de mercado y no requerir una decisión adicional no respaldada.

## Decisión: Framework de pruebas

- **Decision**: pytest para `bw-backend/tests/unit/`.
- **Rationale**: Declarado explícitamente en `prompts/etapa-i-plan.md` §Stack: "Se incluyen test
  unitarios en backend". Sin alcance de frontend en esta ejecución, no aplica ninguna decisión de
  testing de frontend.
- **Alternatives considered**: unittest (Python) — se prefiere pytest por convención de mercado para
  proyectos FastAPI.

## Decisión: Estrategia de aislamiento de base de datos en pruebas

- **Decision**: cada test que ejercita `ProfesionalService` contra PostgreSQL corre dentro de una
  **transacción SQLAlchemy propia**, abierta en un fixture de pytest (`bw-backend/tests/conftest.py`)
  al inicio del test y revertida (`rollback()`) al finalizar, sobre el mismo PostgreSQL de
  `docker-compose.yml` (no una base de datos física separada por test). El `Session` que recibe
  `ProfesionalService` en cada test se vincula (`bind=`) a esa transacción, de modo que ningún test
  deja datos residuales para el siguiente.
- **Rationale**: `prompts/etapa-i-plan.md` declara explícitamente "test unitarios en backend que usan
  una sesion aislada de DB" — el sustantivo es "sesión", no "base de datos"; se resuelve con el
  patrón estándar de mercado para aislar tests con SQLAlchemy (transacción por test con rollback),
  sin necesitar levantar un contenedor PostgreSQL adicional solo para pruebas. Esto resuelve el
  hallazgo HIGH (U1) de `/speckit-analyze` (sesión previa a esta re-sincronización): ninguna tarea
  definía cómo `bw-backend/tests/unit/` obtenía una base de datos utilizable sin contaminarse entre
  tests.
- **Alternatives considered**: base de datos PostgreSQL de prueba separada (contenedor o esquema
  adicional en `docker-compose.yml`) — rechazada por ser más pesada que lo que pide la literalidad
  de "sesión aislada", y por requerir gestionar dos ciclos de vida de base de datos (dev y test) sin
  que ningún requisito lo exija; SQLite en memoria — rechazada porque no es PostgreSQL real y podría
  ocultar comportamiento específico del motor (p. ej. la columna `especialidades` como `ARRAY`, sin
  equivalente nativo en SQLite).

## Decisión: Dirección del contrato de API interna compartido (FR-BW-029 a FR-BW-034)

- **Decision**: se separa el contrato único de la ejecución anterior en dos direcciones, según el
  verbo que cada FR-BW usa:
  - **BW consume** (Backend Agendamiento sirve): Crear/Actualizar/Cancelar Reserva Command API
    (FR-BW-032, FR-BW-033, FR-BW-034 — texto "El sistema DEBE **emitir la respuesta** de contrato...";
    ver nota más abajo) y el evento de sincronización de agenda (FR-BW-044). Se mantiene sin cambios
    respecto a la ejecución anterior: "Reserva" no es una de las 4 entidades que BW administra por
    CRUD (ver decisión de persistencia arriba), por lo que su fuente de verdad sigue siendo Backend
    Agendamiento.
  - **BW sirve** (BW es el proveedor): Disponibilidad Query API, Servicios Query API, Profesionales
    Query API (FR-BW-029, FR-BW-030, FR-BW-031). Con PostgreSQL propio para estas 3 entidades, BW
    puede responder estas consultas directamente desde su propia base de datos, consistente con la
    lectura literal de esos tres FR-BW ("El sistema DEBE **emitir la respuesta** de contrato...":
    BW es quien responde, no quien pregunta).
  - **Nota sobre el texto literal**: los 6 FR-BW-029..034 comparten el mismo verbo ("emitir la
    respuesta"); la ejecución anterior los trató como 6 operaciones consumidas por BW, apoyándose en
    la aclaración de `spec.md` §Clarifications ("es la misma API interna compartida por los tres
    bundles") sin especificar dirección. Esta ejecución solo reinterpreta la dirección de las 3
    operaciones de **consulta** (Disponibilidad/Servicios/Profesionales), porque ahora BW tiene una
    base de datos propia que las respalda — no reinterpreta las 3 de **Reserva**, porque BW sigue sin
    persistir esa entidad. Las 6 siguen siendo, en conjunto, "la misma API compartida" en el sentido
    de compartir esquema/formato de error entre los tres bundles (aclarado en `spec.md`
    §Clarifications, Sesión 2026-08-05); lo que cambia es cuál bundle implementa cada dirección.
- **Rationale**: la decisión previa ("BW consume las 6") dependía de que BW no tuviera datos propios
  para las 3 consultas; esa premisa cambió con PostgreSQL. Mantener las 3 operaciones de Reserva como
  consumidas es necesario para no crear una segunda fuente de verdad de reservas (P13).
- **Alternatives considered**: mantener las 6 como consumidas por BW, ignorando que ahora BW tiene
  datos propios para 3 de ellas (rechazado: dejaría sin usar la nueva base de datos para el propósito
  que la motivó — resolver la brecha de persistencia de escritura de FR-BW-005 — y contradiría la
  lectura literal "emite la respuesta" para esas 3 operaciones); tratar las 6 como servidas por BW,
  incluida Reserva (rechazado: violaría P13, "Reserva" no es una entidad que `spec.md` §Clarifications
  atribuya a BW).

## Decisión: Política de reintento del contrato consumido (Reserva Command API, FR-BW-032 a FR-BW-034)

- **Decision**: máximo 3 reintentos con backoff exponencial (1s, 2s, 4s) por llamada. Si los 3
  intentos fallan, BW propaga el `error.code` recibido al llamador sin más reintentos automáticos.
- **Rationale**: Sin cambios de fondo respecto a la ejecución anterior (`spec.md` §Clarifications,
  Sesión 2026-08-08); se reduce el alcance de esta política a las 3 operaciones que BW sigue
  consumiendo (antes eran 6), porque las 3 de consulta ahora las sirve BW mismo y no requieren
  política de reintento de cliente.
- **Alternatives considered**: igual que la ejecución anterior — reintento indefinido (rechazado);
  un único reintento (rechazado, insuficiente para fallas transitorias breves).

## Decisión: Política de reintento y resincronización de FR-BW-044

- **Decision**: al recibir un evento de cambio de agenda desde Backend Agendamiento, si su
  procesamiento falla, BW reintenta hasta 3 veces (mismo backoff: 1s, 2s, 4s). Si tras 3 intentos el
  evento sigue fallando, o llega fuera de secuencia, BW dispara una resincronización completa
  reconsultando el estado de disponibilidad del rango afectado **directamente a Backend Agendamiento**
  (no a su propio endpoint de Disponibilidad Query API, que ahora es el que BW sirve a terceros — ver
  decisión de dirección del contrato arriba), y sobrescribe su copia local en PostgreSQL con la
  respuesta.
- **Rationale**: `spec.md` §Clarifications, Sesión 2026-08-08 aclaró el mecanismo (reintentar y
  resincronizar por reconsulta) sin fijar el número de reintentos. Se actualiza el destino de la
  reconsulta respecto a la ejecución anterior porque, con la nueva dirección del contrato, BW ya no
  tiene sentido "reconsultándose a sí mismo" — el origen autoritativo del cambio de agenda sigue
  siendo Backend Agendamiento (P13).
- **Alternatives considered**: resincronizar contra la propia copia en PostgreSQL de BW (rechazado:
  circular — esa copia es precisamente la que quedó desactualizada); resincronizar en cada evento
  fallido sin reintentar primero (rechazado: carga innecesaria ante fallas transitorias de un solo
  evento).

## Decisión: Tipo del campo `especialidades` (Profesionales y especialidades)

- **Decision**: `especialidades` es una columna de tipo lista de texto (`ARRAY(String)` en
  PostgreSQL vía SQLAlchemy, equivalente a `list[str]`), no una referencia a `Catálogo de servicios`.
- **Rationale**: Sin cambios respecto a la ejecución anterior — ningún FR-BW declara una relación
  explícita entre "especialidad" y una entrada del catálogo de servicios; se actualiza únicamente el
  tipo concreto de columna PostgreSQL para reflejar la persistencia real definida en esta ejecución.
- **Alternatives considered**: tabla de unión N:M hacia `Catálogo de servicios` (rechazada: ningún
  FR-BW respalda esa relación).

## Decisión: Atributos de las 4 entidades ahora persistidas (Ficha clientes, Disponibilidad Agenda,
## Catálogo de servicios, Profesionales y especialidades)

- **Decision**: ver `data-model.md`. Los atributos se derivan únicamente de cómo cada FR-BW usa la
  entidad — sin cambios de fondo respecto a la ejecución anterior; se actualiza su representación de
  "DTO de lectura desde un contrato externo" a "columna de tabla PostgreSQL propia".
- **Rationale**: `spec.md` §Clarifications diferió esta definición a `/speckit.plan`; esta ejecución
  la resuelve con el mismo nivel de evidencia que la anterior, solo cambia el mecanismo de
  persistencia subyacente.
- **Alternatives considered**: igual que la ejecución anterior.

## Fuera de alcance de esta investigación (no resuelto, no inventado)

- Umbral/criterio verificable de `NFR-TEC-1` a `NFR-TEC-6` y objetivo/ventana de `NFR-OP-1` a
  `NFR-OP-3` — no hay evidencia de que sean específicos de BW; no se infiere.
- Observabilidad (Principio P22): ningún FR ni NFR de BW declara un requisito de logging/monitoreo;
  ver `plan.md` §Complexity Tracking.
- Permisos de "Coordinador de agenda", "Prestador del servicio" y "Solicitante de reserva" fuera de
  las 4 acciones ya aclaradas de BW.
- Diseño de `bw-frontend` (React + TypeScript): excluido explícitamente de esta ejecución
  (`prompts/etapa-i-plan.md`: "diseñar unicamente el bundle de backend"); no se decide aquí ningún
  aspecto de interfaz de usuario, incluida la cuantificación de "GUI amigable".
- Metas de desempeño y escala (usuarios concurrentes, volumen de datos) propias de BW.
- Alta disponibilidad / clustering de PostgreSQL: ningún NFR de esta ejecución lo exige; se usa una
  única instancia vía Docker, sin decidir una topología de réplicas.

Estos puntos deben resolverse por el cliente/negocio o por una futura ejecución de `/speckit-plan`
con la entrada correspondiente, no por este plan.
