# Feature Specification: Gestión Integral de Reservas

**Feature Branch**: `001-gestion-integral-reservas` (nombre de directorio; no se creó rama git — no hay hook `before_specify` configurado en este proyecto)

**Created**: 2026-08-04

**Status**: Draft

**Input**: Artefactos auditados del pipeline 7Cs: `composed/prompt_specify.md` (fuente primaria de requisitos), `.specify/memory/constitution.md` (principios y gobernanza), `composed/trace_annex.md` (trazabilidad, consultado únicamente para verificar destino cuando corresponde)

**Auditoría de origen**: C = 1.000, T = 0, V = 1.000 — veredicto **VÁLIDA** (`audit/audit_report.md`, `audit/verdict.txt`)

**Delivery ID**: `arquitectura-para-sistema-de-reservas-inteligente` (según `prompt_specify.md`/constitution). Nota: `trace_annex.md` y los Canvas Object Models originales usan `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm`; la discrepancia ya fue señalada por la auditoría y no se corrige en este documento.

## Nota de generación de esta especificación

Este documento se generó por instrucción explícita del usuario a partir de artefactos ya auditados del pipeline 7Cs, no de una descripción de feature en lenguaje natural libre. Reglas aplicadas, con desviaciones respecto al flujo estándar de `/speckit-specify` documentadas explícitamente:

1. **No se inventaron requisitos nuevos y no se eliminó ningún requisito funcional**: los 149 FR de frontera y de bundle (18 `FR-SCC-*` + 50 `FR-AC-*` + 37 `FR-BA-*` + 44 `FR-BW-*` = 149, cifra que coincide con V = 149/149 de la auditoría) se preservan íntegros.
2. **Se preservaron los identificadores originales** (`FR-SCC-*`, `FR-AC-*`, `FR-BA-*`, `FR-BW-*`, `INT-*`, `CE-*`, `NFR-TEC-*`, `NFR-OP-*`, `R-*`) en lugar de renumerarlos como `FR-001, FR-002…`, para no romper la trazabilidad con `trace_annex.md`.
3. **No se aplicó el límite estándar de 3 marcadores `[NEEDS CLARIFICATION]`** del flujo genérico de `/speckit-specify`: el pipeline 7Cs ya catalogó 94 dudas auditadas en `composed/clarify_input.md` (CL-001–CL-094). Resolverlas es tarea de `/speckit.clarify`, no de este paso. Todas las marcas `[NEEDS CLARIFICATION]` del prompt de origen se preservan tal cual, sin resolver ni recortar.
4. **El checklist de calidad no se "arregló" inventando valores**: los ítems que fallan por falta de métrica, umbral o contrato quedan documentados como fallidos y pendientes de `/speckit.clarify`, en vez de completarse con supuestos no respaldados por evidencia.
5. **No se incluyó tecnología**: se mantiene la neutralidad técnica exigida por T=0; el contexto técnico (stack, runtime, despliegue) corresponde a `/speckit-plan`, no a este documento.
6. Las prioridades P1–P4 asignadas a las User Stories son una inferencia razonable (permitida por las reglas de generación de Spec Kit para completar vacíos no críticos) y se documentan en **Assumptions**, no una decisión provista por el pipeline 7Cs.

## User Scenarios & Testing *(mandatory)*

Las ocho escenarios de negocio (EN-01 a EN-08) declarados en el Business Context Canvas no traen actor, precondición ni resultado observable definidos ("por confirmar" en la fuente). Se agrupan aquí en User Stories por afinidad funcional; cada FR referenciado sí trae su propio escenario Dado/Cuando/Entonces (ver **Requirements**).

### User Story 1 - Atención y agendamiento por canal conversacional (Priority: P1)

Un cliente contacta al centro por el canal de mensajería conversacional soportado, expresa su necesidad y agenda o confirma una cita sin intervención humana, salvo derivación explícita.

**Cubre**: EN-08 "Identificar requerimiento del cliente", EN-02 "Agendar una cita", EN-03 "Confirmar una cita".
`[NEEDS CLARIFICATION: actor, precondición y resultado observable de EN-02, EN-03, EN-08 por confirmar — CL-083]`

**Why this priority**: Es el proceso central de la Constitution P1 ("automatizar la atención conversacional") y P6 ("mejorar la experiencia del cliente"); sin esto no hay producto mínimo viable.

**Independent Test**: Puede probarse enviando un mensaje por el canal soportado y verificando que el sistema identifica la necesidad, ofrece disponibilidad y confirma una reserva (bundle "Agente conversacional", ver FR-AC-001 a FR-AC-050).

**Acceptance Scenarios**: ver Requisitos funcionales `FR-AC-001`–`FR-AC-050` y de frontera `FR-SCC-001`, `FR-SCC-002` — cada uno trae su propio escenario Dado/Cuando/Entonces.

---

### User Story 2 - Gestión de cambios sobre una reserva existente (Priority: P2)

Un cliente o el sistema reprograma, cancela o confirma asistencia a una cita ya agendada.

**Cubre**: EN-04 "Reprogramar una cita", EN-05 "Cancelar una cita", EN-06 "Confirmar asistencia".
`[NEEDS CLARIFICATION: actor, precondición y resultado observable de EN-04, EN-05, EN-06 por confirmar — CL-083]`

**Why this priority**: Depende de que exista una reserva creada (User Story 1); es la segunda capa de valor sobre el mismo flujo conversacional y de agendamiento (bundles "Agente conversacional" y "Backend Agendamiento").

**Independent Test**: Con una reserva ya creada, solicitar cancelación o reprogramación por el canal soportado y verificar que el estado de la reserva cambia y se emite el evento correspondiente (`FR-BA-031` a `FR-BA-033`, `FR-BW-040` a `FR-BW-042`).

**Acceptance Scenarios**: ver `FR-AC-006`, `FR-AC-007`, `FR-BA-005` a `FR-BA-007`, `FR-BA-019` a `FR-BA-021`, `FR-BW-040` a `FR-BW-042`.

---

### User Story 3 - Seguimiento de servicio agendado (Priority: P2)

El sistema hace seguimiento de una reserva agendada (recordatorios, liberación de horas no confirmadas).

**Cubre**: EN-07 "Seguimiento de reservas".
`[NEEDS CLARIFICATION: actor, precondición y resultado observable de EN-07 por confirmar — CL-083]`

**Why this priority**: Sostiene los objetivos de negocio CE-4 ("reducir inasistencias") y CE-6 ("reducir los no-shows"); depende de que existan reservas creadas.

**Independent Test**: Verificar que ante una cita próxima se dispara un recordatorio (`FR-AC-019`, `FR-AC-033`) y que una reserva sin confirmar se libera según la tarea programada correspondiente (`FR-BA-037`).

**Acceptance Scenarios**: ver `FR-AC-019`, `FR-AC-033`, `FR-BA-037`, `FR-AC-047` a `FR-AC-050`, `FR-BA-034` a `FR-BA-036`.

---

### User Story 4 - Administración de catálogo, agenda y profesionales (Priority: P3)

El administrador o recepcionista gestiona, mediante el sitio web administrativo, los servicios ofrecidos, los profesionales, la disponibilidad de agenda y los datos de clientes.

**Cubre**: EN-01 "Gestionar servicios disponibles".
`[NEEDS CLARIFICATION: actor, precondición y resultado observable de EN-01 por confirmar — CL-083]`

**Why this priority**: Es configuración de soporte para las User Stories 1-3, no atención directa al cliente final; puede desarrollarse de forma independiente (bundle "Backend/Frontend Web").

**Independent Test**: Crear o modificar un profesional, un servicio o la agenda desde la interfaz administrativa y verificar que el dato exportado queda disponible para los demás bundles (`FR-BW-005` a `FR-BW-008`, `FR-BW-035` a `FR-BW-039`).

**Acceptance Scenarios**: ver `FR-BW-001` a `FR-BW-044`.

---

### Edge Cases

El pipeline 7Cs auditado no declara casos límite explícitos (no hay post-it de "edge cases" en ningún canvas). No se inventan aquí. El comportamiento ante error queda abierto y marcado `[NEEDS CLARIFICATION]` en los puntos donde el pipeline sí detectó la ausencia:

- Comportamiento ante error de cada contrato de integración: `INT-1` a `INT-5`, `FR-AC-009`, `FR-AC-044`, `FR-BA-008`, y todos los contratos Query/Command API (`FR-AC-037`–`FR-AC-043`, `FR-BA-001`–`FR-BA-007`, `FR-BA-016`–`FR-BA-021`, `FR-BW-029`–`FR-BW-034`).
- Comportamiento ante fallo de las tareas programadas (jobs): `FR-AC-047`–`FR-AC-050`, `FR-BA-034`–`FR-BA-037`, `FR-BW-044`.

## Requirements *(mandatory)*

### Contexto (BCC/ACC)

**Actores organizacionales**: "Cliente", "Profesionales del Centro", "Administrador del centro", "Recepcionista".

**Productos y servicios**: "Gestión integral de Reservas".

**Business infrastructure & equipment**: "PC del Encargado del Local", "Dispositivos Móvil del Recepcionista", "PC del Recepcionista", "Dispositivo Móvil del Cliente", "PC del Cliente", "Dispositivo Móvil del Profesional", "PC del Profesional", "Servicio Cloud".

**Business locations**: "Región Metropolitana".

**Business facilities**: "Oficina Administracion", "Recepción", "Sala de espera", "Estación de trabajo".

### Perfiles de usuario

- "Administrador de la operación": permisos no declarados.
- "Coordinador de agenda": permisos no declarados.
- "Prestador del servicio": permisos no declarados.
- "Solicitante de reserva": permisos no declarados.

`[NEEDS CLARIFICATION: permisos de cada perfil no declarados en el canvas — CL-001]`

### Alcance

**Índice de requisitos** (System's functional areas):
1. "Gestión de agenda"
2. "Gestión de profesionales"
3. "Gestión de servicios"
4. "Ejecución de servicio"
5. "Seguimiento de servicio agendado"
6. "Gestión de conversacional"

**Source users**: "Profesionales del Centro", "Administrador del Centro", "Cliente", "Recepcionista del Centro".

**Target users**: "Profesionales del Centro", "Administrador del Centro", "Cliente", "Recepcionista del Centro".

**Fuera de alcance** (por complemento):
- Intercambios con sistemas, repositorios o dispositivos que no aparecen en la retícula.
- Escrituras hacia contrapartes declaradas solo como origen y lecturas desde contrapartes declaradas solo como destino.
- Software instalado en dispositivos y contratos de repositorio, porque no están declarados.

### Key Entities *(include if feature involves data)*

**Entidades clave (negocio)**: "Cliente", "Profesional", "Local", "Disponibilidad", "Historial de atención", "Servicio", "Agenda", "Reserva", "Preferencias del cliente" — atributos abiertos.

**Entidades clave (Agente conversacional)**: "Conversación", "Mensaje", "Contexto", "Intención", "Prompt", "Estado Conversacional" — atributos por confirmar.
`[NEEDS CLARIFICATION: atributos de las entidades del bundle "Agente conversacional" no declarados — CL-020]`

**Entidades clave (Backend Agendamiento)**: "Ficha clientes", "Disponibilidad Agenda", "Catálogo de servicios", "Profesionales y especialidades", "Historial Conversación", "Reglas de negocio", "Configuración conversacional" — atributos por confirmar.
`[NEEDS CLARIFICATION: atributos de las entidades del bundle "Backend Agendamiento" no declarados — CL-031]`

**Entidades clave (Backend/Frontend Web)**: "Multimedia Web" — atributos por confirmar.
`[NEEDS CLARIFICATION: atributos de las entidades del bundle "Backend/Frontend Web" no declarados — CL-047]`

`[NEEDS CLARIFICATION: atributos de las entidades de negocio no declarados en el canvas — CL-002]`

### Integraciones (frontera del sistema)

**INT-1** Integración de entrada desde un servicio externo de mensajería conversacional; contrato exacto por confirmar.
Escenario: Dado que el servicio externo de mensajería está disponible, cuando entrega un mensaje, entonces el sistema recibe la información mediante el contrato declarado.
`[NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]`

**INT-2** Integración de entrada desde un servicio externo de procesamiento conversacional; contrato exacto por confirmar.
Escenario: Dado que el servicio externo de procesamiento está disponible, cuando entrega un resultado conversacional, entonces el sistema recibe la información mediante el contrato declarado.
`[NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]`

**INT-3** Integración de entrada desde un servicio externo de geolocalización; contrato exacto por confirmar.
Escenario: Dado que el servicio externo de geolocalización está disponible, cuando se consulta una ubicación, entonces el sistema recibe el resultado mediante el contrato declarado.
`[NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]`

**INT-4** Integración de salida hacia un servicio externo de mensajería conversacional; contrato exacto por confirmar.
Escenario: Dado un mensaje de salida, cuando el sistema solicita su entrega, entonces lo emite hacia el servicio externo mediante el contrato declarado.
`[NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]`

**INT-5** Integración de salida hacia un servicio externo de procesamiento conversacional; contrato exacto por confirmar.
Escenario: Dada una solicitud de procesamiento conversacional, cuando el sistema requiere un resultado, entonces la emite hacia el servicio externo mediante el contrato declarado.
`[NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]`

### Functional Requirements

Se preservan los 149 FR auditados (V = 149/149), agrupados por bundle/frontera tal como en `prompt_specify.md`. Cada uno conserva su ID original, su traza a `trace_annex.md` y su escenario Dado/Cuando/Entonces.

#### Requisitos funcionales de frontera (SCC)

- **FR-SCC-001**: El sistema DEBE recibir información humana mediante el canal de mensajería conversacional soportado.
  Escenario: Dado que una persona utiliza el canal soportado, cuando envía información, entonces el sistema la recibe y deja un resultado observable.
  Equivalencia funcional: absorbido también por FR-AC-017.
  `[NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados — CL-004]`
- **FR-SCC-002**: El sistema DEBE emitir información visible mediante el canal de mensajería conversacional soportado.
  Escenario: Dado un resultado conversacional, cuando el sistema responde a una persona, entonces emite la información mediante el canal soportado.
  Equivalencia funcional: absorbido también por FR-AC-030 y FR-AC-046.
  `[NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados — CL-005]`
- **FR-SCC-003**: El sistema DEBE emitir información mediante "SMS".
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema emite la información mediante la interfaz declarada.
  `[NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados — CL-006]`
- **FR-SCC-004**: El sistema DEBE emitir información mediante "Email".
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema emite la información mediante la interfaz declarada.
  `[NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados — CL-007]`
- **FR-SCC-005**: El sistema DEBE emitir información mediante "falta interfaz web".
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema emite la información mediante la interfaz declarada.
  `[NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados — CL-008]`
- **FR-SCC-006**: El sistema DEBE recibir información mediante "Command Request".
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema recibe la información mediante la interfaz declarada.
  `[NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados — CL-009]`
- **FR-SCC-007**: El sistema DEBE recibir información mediante "Command Endpoints".
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema recibe la información mediante la interfaz declarada.
  `[NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados — CL-010]`
- **FR-SCC-008**: El sistema DEBE emitir información mediante "Command Request".
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema emite la información mediante la interfaz declarada.
  `[NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados — CL-011]`
- **FR-SCC-009**: El sistema DEBE recibir información mediante "File System".
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema recibe la información mediante la interfaz declarada.
  `[NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados — CL-012]`
- **FR-SCC-010**: El sistema DEBE recibir información mediante "Cámara del Dispositivo".
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema recibe la información mediante la interfaz declarada.
  `[NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados — CL-013]`
- **FR-SCC-011**: El sistema DEBE emitir información mediante "Pantalla del dispositivo".
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema emite la información mediante la interfaz declarada.
  `[NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados — CL-014]`
- **FR-SCC-012**: El sistema DEBE emitir información mediante "Monitor PC".
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema emite la información mediante la interfaz declarada.
  `[NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados — CL-015]`
- **FR-SCC-013**: El sistema DEBE permitir el canal de uso "PCs" (dispositivo origen).
  Escenario: Dado un dispositivo declarado, cuando una persona usa el sistema, entonces el canal permanece disponible.
- **FR-SCC-014**: El sistema DEBE permitir el canal de uso "Notebooks" (dispositivo origen).
  Escenario: Dado un dispositivo declarado, cuando una persona usa el sistema, entonces el canal permanece disponible.
- **FR-SCC-015**: El sistema DEBE permitir el canal de uso "Dispositivos Móviles" (dispositivo origen).
  Escenario: Dado un dispositivo declarado, cuando una persona usa el sistema, entonces el canal permanece disponible.
- **FR-SCC-016**: El sistema DEBE permitir el canal de uso "PCs" (dispositivo destino).
  Escenario: Dado un dispositivo declarado, cuando una persona usa el sistema, entonces el canal permanece disponible.
- **FR-SCC-017**: El sistema DEBE permitir el canal de uso "Notebooks" (dispositivo destino).
  Escenario: Dado un dispositivo declarado, cuando una persona usa el sistema, entonces el canal permanece disponible.
- **FR-SCC-018**: El sistema DEBE permitir el canal de uso "Dispositivos Móviles" (dispositivo destino).
  Escenario: Dado un dispositivo declarado, cuando una persona usa el sistema, entonces el canal permanece disponible.

#### Requisitos funcionales — Bundle "Agente conversacional" (AC)

- **FR-AC-001**: El sistema DEBE aceptar mensajes de texto enviados por una persona mediante el canal conversacional soportado.
  Escenario: Dado que el agente conversacional está disponible, cuando una persona envía un mensaje de texto, entonces el sistema lo recibe y deja un resultado observable.
  Equivalencia funcional: absorbido también por FR-AC-017 y FR-AC-046.
- **FR-AC-002**: El sistema DEBE aceptar mensajes de audio enviados por una persona mediante el canal conversacional soportado.
  Escenario: Dado que el agente conversacional está disponible, cuando una persona envía audio, entonces el sistema lo recibe como contenido multimedia y deja un resultado observable.
  Equivalencia funcional: absorbido también por FR-AC-018.
- **FR-AC-003**: El sistema DEBE aceptar imágenes enviadas por una persona mediante el canal conversacional soportado.
  Escenario: Dado que el agente conversacional está disponible, cuando una persona envía una imagen, entonces el sistema la recibe como contenido multimedia y deja un resultado observable.
  Equivalencia funcional: absorbido también por FR-AC-018.
- **FR-AC-004**: El sistema DEBE aceptar una ubicación enviada por una persona mediante el canal conversacional soportado.
  Escenario: Dado que el agente conversacional está disponible, cuando una persona comparte una ubicación, entonces el sistema la recibe y deja un resultado observable.
- **FR-AC-005**: El sistema DEBE aceptar documentos enviados por una persona mediante el canal conversacional soportado.
  Escenario: Dado que el agente conversacional está disponible, cuando una persona envía un documento, entonces el sistema lo recibe y deja un resultado observable.
- **FR-AC-006**: El sistema DEBE aceptar la interacción humana "Confirmar Cita".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Confirmar Cita" y deja un resultado observable.
- **FR-AC-007**: El sistema DEBE aceptar la interacción humana "Cancelar Cita".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Cancelar Cita" y deja un resultado observable.
- **FR-AC-008**: El sistema DEBE aceptar la interacción humana "Entregar disponibilidad horaria".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Entregar disponibilidad horaria" y deja un resultado observable.
- **FR-AC-009**: El sistema DEBE recibir notificaciones entrantes de mensajes mediante un contrato de integración.
  Escenario: Dado que el agente conversacional está disponible, cuando la contraparte notifica un mensaje, entonces el sistema recibe el contenido mediante el contrato declarado.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-021]`
- **FR-AC-010**: El sistema DEBE recibir la solicitud de contrato "Webhook: estado de mensaje".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Webhook: estado de mensaje" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-022]`
- **FR-AC-011**: El sistema DEBE leer el dato importado "Ficha del cliente".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Ficha del cliente" y deja un resultado observable.
- **FR-AC-012**: El sistema DEBE leer el dato importado "Configuración conversacional".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Configuración conversacional" y deja un resultado observable.
- **FR-AC-013**: El sistema DEBE leer el dato importado "Historial de Conversación".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Historial de Conversación" y deja un resultado observable.
- **FR-AC-014**: El sistema DEBE leer el dato importado "Catalogo de servicios".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Catalogo de servicios" y deja un resultado observable.
- **FR-AC-015**: El sistema DEBE leer el dato importado "Disponibilidad de Agenda".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Disponibilidad de Agenda" y deja un resultado observable.
- **FR-AC-016**: El sistema DEBE leer el dato importado "Reglas de negocio".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Reglas de negocio" y deja un resultado observable.
- **FR-AC-017**: El sistema DEBE reaccionar al evento recibido "Mensaje recibido".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Mensaje recibido" y deja un resultado observable.
- **FR-AC-018**: El sistema DEBE reaccionar al evento recibido "Multimedia recibida".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Multimedia recibida" y deja un resultado observable.
- **FR-AC-019**: El sistema DEBE reaccionar al evento recibido "Recordatorio de cita".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Recordatorio de cita" y deja un resultado observable.
- **FR-AC-020**: El sistema DEBE reaccionar al evento recibido "Error de interpretacion (derivar)".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Error de interpretacion (derivar)" y deja un resultado observable.
- **FR-AC-021**: El sistema DEBE reaccionar al evento recibido "Hora liberada".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Hora liberada" y deja un resultado observable.
- **FR-AC-022**: El sistema DEBE reaccionar al evento recibido "Conversación reanudada".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Conversación reanudada" y deja un resultado observable.
- **FR-AC-023**: El sistema DEBE aplicar la regla auxiliar "Constructor de Prompt".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Constructor de Prompt" y deja un resultado observable.
- **FR-AC-024**: El sistema DEBE aplicar la regla auxiliar "Gestor de Contexto".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Gestor de Contexto" y deja un resultado observable.
- **FR-AC-025**: El sistema DEBE aplicar la regla auxiliar "Depurar historial conversacional".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Depurar historial conversacional" y deja un resultado observable.
- **FR-AC-026**: El sistema DEBE aplicar la regla auxiliar "Recomendación de servicios".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Recomendación de servicios" y deja un resultado observable.
- **FR-AC-027**: El sistema DEBE aplicar la regla auxiliar "Moderación de Contenido".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Moderación de Contenido" y deja un resultado observable.
- **FR-AC-028**: El sistema DEBE aplicar la regla auxiliar "Clasificador de intención".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Clasificador de intención" y deja un resultado observable.
- **FR-AC-029**: El sistema DEBE aplicar la regla auxiliar "Detección de intención".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Detección de intención" y deja un resultado observable.
- **FR-AC-030**: El sistema DEBE mostrar o notificar "Respuesta conversacional".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Respuesta conversacional" y deja un resultado observable.
- **FR-AC-031**: El sistema DEBE mostrar o notificar "Confirmación de reserva".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Confirmación de reserva" y deja un resultado observable.
- **FR-AC-032**: El sistema DEBE mostrar o notificar "Propuesta de horarios".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Propuesta de horarios" y deja un resultado observable.
- **FR-AC-033**: El sistema DEBE mostrar o notificar "Recordatorio".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Recordatorio" y deja un resultado observable.
- **FR-AC-034**: El sistema DEBE presentar el resultado de interfaz "Respuesta Confirmacion de cita".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Respuesta Confirmacion de cita" y deja un resultado observable.
- **FR-AC-035**: El sistema DEBE presentar el resultado de interfaz "Respuesta Cancelacion de cita".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Respuesta Cancelacion de cita" y deja un resultado observable.
- **FR-AC-036**: El sistema DEBE presentar el resultado de interfaz "Disponibilidad horaria entregada".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Disponibilidad horaria entregada" y deja un resultado observable.
- **FR-AC-037**: El sistema DEBE emitir la respuesta de contrato "Disponibilidad Query API".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Disponibilidad Query API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-023]`
- **FR-AC-038**: El sistema DEBE emitir la respuesta de contrato "Servicios Query API".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Servicios Query API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-024]`
- **FR-AC-039**: El sistema DEBE emitir la respuesta de contrato "Profesionales Query API".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Profesionales Query API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-025]`
- **FR-AC-040**: El sistema DEBE emitir la respuesta de contrato "Historial de conversacion Query".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Historial de conversacion Query" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-026]`
- **FR-AC-041**: El sistema DEBE emitir la respuesta de contrato "Crear Reserva Command API".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Crear Reserva Command API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-027]`
- **FR-AC-042**: El sistema DEBE emitir la respuesta de contrato "Actualizar Reserva Command API".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Actualizar Reserva Command API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-028]`
- **FR-AC-043**: El sistema DEBE emitir la respuesta de contrato "Cancelar Reserva Command API".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Cancelar Reserva Command API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-029]`
- **FR-AC-044**: El sistema DEBE emitir solicitudes conversacionales hacia una capacidad externa de procesamiento mediante un contrato de integración.
  Escenario: Dado que existe una conversación que requiere procesamiento externo, cuando el agente solicita un resultado, entonces el sistema emite la solicitud mediante el contrato declarado.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-030]`
- **FR-AC-045**: El sistema DEBE persistir o entregar el dato exportado "Historial de Conversación".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Historial de Conversación" y deja un resultado observable.
- **FR-AC-046**: El sistema DEBE emitir el evento "Mensaje IN or OUT".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Mensaje IN or OUT" y deja un resultado observable.
- **FR-AC-047**: El sistema DEBE ejecutar la tarea programada "Registrar conversación".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Registrar conversación" y deja un resultado observable.
  `[NEEDS CLARIFICATION: periodicidad, ventana de ejecución y comportamiento ante fallo no declarados — CL-074]`
- **FR-AC-048**: El sistema DEBE ejecutar la tarea programada "Actualizar contexto conversacional".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Actualizar contexto conversacional" y deja un resultado observable.
  `[NEEDS CLARIFICATION: periodicidad, ventana de ejecución y comportamiento ante fallo no declarados — CL-075]`
- **FR-AC-049**: El sistema DEBE ejecutar la tarea programada "Limpiar contexto expirado".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Limpiar contexto expirado" y deja un resultado observable.
  `[NEEDS CLARIFICATION: periodicidad, ventana de ejecución y comportamiento ante fallo no declarados — CL-076]`
- **FR-AC-050**: El sistema DEBE ejecutar la tarea programada "Resumir conversación".
  Escenario: Dado que el bundle "Agente conversacional" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Resumir conversación" y deja un resultado observable.
  `[NEEDS CLARIFICATION: periodicidad, ventana de ejecución y comportamiento ante fallo no declarados — CL-077]`

#### Requisitos funcionales — Bundle "Backend Agendamiento" (BA)

- **FR-BA-001**: El sistema DEBE recibir la solicitud de contrato "Disponibilidad Query API".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Disponibilidad Query API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-032]`
- **FR-BA-002**: El sistema DEBE recibir la solicitud de contrato "Servicios Query API".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Servicios Query API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-033]`
- **FR-BA-003**: El sistema DEBE recibir la solicitud de contrato "Profesionales Query API".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Profesionales Query API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-034]`
- **FR-BA-004**: El sistema DEBE recibir la solicitud de contrato "Historial de conversacion Query".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Historial de conversacion Query" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-035]`
- **FR-BA-005**: El sistema DEBE recibir la solicitud de contrato "Crear Reserva Command API".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Crear Reserva Command API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-036]`
- **FR-BA-006**: El sistema DEBE recibir la solicitud de contrato "Actualizar Reserva Command API".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Actualizar Reserva Command API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-037]`
- **FR-BA-007**: El sistema DEBE recibir la solicitud de contrato "Cancelar Reserva Command API".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Cancelar Reserva Command API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-038]`
- **FR-BA-008**: El sistema DEBE recibir resultados conversacionales desde una capacidad externa de procesamiento mediante un contrato de integración.
  Escenario: Dado que el backend de agendamiento está disponible, cuando la contraparte entrega un resultado conversacional, entonces el sistema lo recibe mediante el contrato declarado.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-039]`
- **FR-BA-009**: El sistema DEBE leer el dato importado "Historial de Conversación".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Historial de Conversación" y deja un resultado observable.
- **FR-BA-010**: El sistema DEBE leer una respuesta conversacional importada para continuar el procesamiento del agendamiento.
  Escenario: Dado que existe una respuesta conversacional disponible, cuando el backend continúa el agendamiento, entonces el sistema lee la respuesta y deja un resultado observable.
- **FR-BA-011**: El sistema DEBE reaccionar al evento recibido "Mensaje recibido".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Mensaje recibido" y deja un resultado observable.
- **FR-BA-012**: El sistema DEBE reaccionar al evento recibido "Error de interpretacion (derivar)".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Error de interpretacion (derivar)" y deja un resultado observable.
- **FR-BA-013**: El sistema DEBE aplicar la regla auxiliar "Recomendación de servicios".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Recomendación de servicios" y deja un resultado observable.
- **FR-BA-014**: El sistema DEBE aplicar la regla auxiliar "Selección de horarios".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Selección de horarios" y deja un resultado observable.
- **FR-BA-015**: El sistema DEBE aplicar la regla auxiliar "Validación de reservas".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Validación de reservas" y deja un resultado observable.
- **FR-BA-016**: El sistema DEBE emitir la respuesta de contrato "Disponibilidad Query API".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Disponibilidad Query API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-040]`
- **FR-BA-017**: El sistema DEBE emitir la respuesta de contrato "Servicios Query API".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Servicios Query API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-041]`
- **FR-BA-018**: El sistema DEBE emitir la respuesta de contrato "Profesionales Query API".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Profesionales Query API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-042]`
- **FR-BA-019**: El sistema DEBE emitir la respuesta de contrato "Crear Reserva Command API".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Crear Reserva Command API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-043]`
- **FR-BA-020**: El sistema DEBE emitir la respuesta de contrato "Actualizar Reserva Command API".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Actualizar Reserva Command API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-044]`
- **FR-BA-021**: El sistema DEBE emitir la respuesta de contrato "Cancelar Reserva Command API".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Cancelar Reserva Command API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-045]`
- **FR-BA-022**: El sistema DEBE persistir o entregar el dato exportado "Disponibilidad Agenda".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Disponibilidad Agenda" y deja un resultado observable.
- **FR-BA-023**: El sistema DEBE persistir o entregar el dato exportado "Ficha clientes".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Ficha clientes" y deja un resultado observable.
- **FR-BA-024**: El sistema DEBE persistir o entregar el dato exportado "Profesionales y especialidades".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Profesionales y especialidades" y deja un resultado observable.
- **FR-BA-025**: El sistema DEBE persistir o entregar el dato exportado "Catálogo de servicios".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Catálogo de servicios" y deja un resultado observable.
- **FR-BA-026**: El sistema DEBE persistir o entregar el dato exportado "Historial Conversación".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Historial Conversación" y deja un resultado observable.
- **FR-BA-027**: El sistema DEBE persistir o entregar el dato exportado "Reglas de negocio".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Reglas de negocio" y deja un resultado observable.
- **FR-BA-028**: El sistema DEBE persistir o entregar el dato exportado "Configuración conversacional".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Configuración conversacional" y deja un resultado observable.
- **FR-BA-029**: El sistema DEBE emitir el evento "Escalamiento a humano por error de interpretación".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Escalamiento a humano por error de interpretación" y deja un resultado observable.
- **FR-BA-030**: El sistema DEBE emitir el evento "Conversación finalizada".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Conversación finalizada" y deja un resultado observable.
- **FR-BA-031**: El sistema DEBE emitir el evento "Cita creada".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Cita creada" y deja un resultado observable.
- **FR-BA-032**: El sistema DEBE emitir el evento "Cita cancelada".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Cita cancelada" y deja un resultado observable.
- **FR-BA-033**: El sistema DEBE emitir el evento "Cita actualizada".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Cita actualizada" y deja un resultado observable.
- **FR-BA-034**: El sistema DEBE ejecutar la limpieza de sesiones conversacionales expiradas.
  Escenario: Dado que existen sesiones conversacionales expiradas, cuando se dispara la tarea de limpieza, entonces el sistema elimina su estado expirado y registra el resultado.
  Equivalencia funcional: absorbido también por FR-AC-049.
  `[NEEDS CLARIFICATION: periodicidad, ventana de ejecución y comportamiento ante fallo no declarados — CL-078]`
- **FR-BA-035**: El sistema DEBE ejecutar la tarea programada "Detección de Alucinaciones".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Detección de Alucinaciones" y deja un resultado observable.
  `[NEEDS CLARIFICATION: periodicidad, ventana de ejecución y comportamiento ante fallo no declarados — CL-079]`
- **FR-BA-036**: El sistema DEBE ejecutar la tarea programada "Evaluador Score".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Evaluador Score" y deja un resultado observable.
  `[NEEDS CLARIFICATION: periodicidad, ventana de ejecución y comportamiento ante fallo no declarados — CL-080]`
- **FR-BA-037**: El sistema DEBE ejecutar la tarea programada "Liberador reservas sin confirmar".
  Escenario: Dado que el bundle "Backend Agendamiento" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Liberador reservas sin confirmar" y deja un resultado observable.
  `[NEEDS CLARIFICATION: periodicidad, ventana de ejecución y comportamiento ante fallo no declarados — CL-081]`

#### Requisitos funcionales — Bundle "Backend/Frontend Web" (BW)

- **FR-BW-001**: El sistema DEBE aceptar la interacción humana "Datos de servicios".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Datos de servicios" y deja un resultado observable.
- **FR-BW-002**: El sistema DEBE aceptar la interacción humana "Disponibilidad de agenda".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Disponibilidad de agenda" y deja un resultado observable.
- **FR-BW-003**: El sistema DEBE aceptar la interacción humana "Datos de profesionales".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Datos de profesionales" y deja un resultado observable.
- **FR-BW-004**: El sistema DEBE aceptar la interacción humana "Datos de clientes".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Datos de clientes" y deja un resultado observable.
- **FR-BW-005**: El sistema DEBE aceptar la interacción humana "Crear/Modificar profesional".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Crear/Modificar profesional" y deja un resultado observable.
- **FR-BW-006**: El sistema DEBE aceptar la interacción humana "Crear/Modificar Servicios".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Crear/Modificar Servicios" y deja un resultado observable.
- **FR-BW-007**: El sistema DEBE aceptar la interacción humana "Modificar Agenda".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Modificar Agenda" y deja un resultado observable.
- **FR-BW-008**: El sistema DEBE aceptar la interacción humana "Modificar datos Clientes".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Modificar datos Clientes" y deja un resultado observable.
- **FR-BW-009**: El sistema DEBE leer el dato importado "Disponibilidad Agenda".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Disponibilidad Agenda" y deja un resultado observable.
- **FR-BW-010**: El sistema DEBE leer el dato importado "Ficha clientes".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Ficha clientes" y deja un resultado observable.
- **FR-BW-011**: El sistema DEBE leer el dato importado "Profesionales y especialidades".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Profesionales y especialidades" y deja un resultado observable.
- **FR-BW-012**: El sistema DEBE leer el dato importado "Catálogo de servicios".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Catálogo de servicios" y deja un resultado observable.
- **FR-BW-013**: El sistema DEBE leer el dato importado "Historial Conversación".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Historial Conversación" y deja un resultado observable.
- **FR-BW-014**: El sistema DEBE leer el dato importado "Reglas de negocio".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Reglas de negocio" y deja un resultado observable.
- **FR-BW-015**: El sistema DEBE leer el dato importado "Configuración conversacional".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Configuración conversacional" y deja un resultado observable.
- **FR-BW-016**: El sistema DEBE reaccionar al evento recibido "Mensaje recibido".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Mensaje recibido" y deja un resultado observable.
- **FR-BW-017**: El sistema DEBE reaccionar al evento recibido "Estado de mensaje recibido".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Estado de mensaje recibido" y deja un resultado observable.
- **FR-BW-018**: El sistema DEBE reaccionar al evento recibido "Error de interpretacion (derivar)".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Error de interpretacion (derivar)" y deja un resultado observable.
- **FR-BW-019**: El sistema DEBE aplicar la regla auxiliar "Gestión de conversación".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Gestión de conversación" y deja un resultado observable.
- **FR-BW-020**: El sistema DEBE aplicar la regla auxiliar "Selección de horarios".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Selección de horarios" y deja un resultado observable.
- **FR-BW-021**: El sistema DEBE aplicar la regla auxiliar "Validación de reservas".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Validación de reservas" y deja un resultado observable.
- **FR-BW-022**: El sistema DEBE mostrar o notificar "Dashboard resumen".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Dashboard resumen" y deja un resultado observable.
- **FR-BW-023**: El sistema DEBE mostrar o notificar "Agenda horaria".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Agenda horaria" y deja un resultado observable.
- **FR-BW-024**: El sistema DEBE mostrar o notificar "Ficha clientes".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Ficha clientes" y deja un resultado observable.
- **FR-BW-025**: El sistema DEBE mostrar o notificar "Ficha Profesionales".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Ficha Profesionales" y deja un resultado observable.
- **FR-BW-026**: El sistema DEBE presentar el resultado de interfaz "Respuesta Confirmacion de modificación".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Respuesta Confirmacion de modificación" y deja un resultado observable.
- **FR-BW-027**: El sistema DEBE presentar el resultado de interfaz "Respuesta Confirmacion de Creacion".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Respuesta Confirmacion de Creacion" y deja un resultado observable.
- **FR-BW-028**: El sistema DEBE presentar el resultado de interfaz "Respuesta Confirmacion de Eliminacion".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Respuesta Confirmacion de Eliminacion" y deja un resultado observable.
- **FR-BW-029**: El sistema DEBE emitir la respuesta de contrato "Disponibilidad Query API".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Disponibilidad Query API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-048]`
- **FR-BW-030**: El sistema DEBE emitir la respuesta de contrato "Servicios Query API".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Servicios Query API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-049]`
- **FR-BW-031**: El sistema DEBE emitir la respuesta de contrato "Profesionales Query API".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Profesionales Query API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-050]`
- **FR-BW-032**: El sistema DEBE emitir la respuesta de contrato "Crear Reserva Command API".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Crear Reserva Command API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-051]`
- **FR-BW-033**: El sistema DEBE emitir la respuesta de contrato "Actualizar Reserva Command API".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Actualizar Reserva Command API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-052]`
- **FR-BW-034**: El sistema DEBE emitir la respuesta de contrato "Cancelar Reserva Command API".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Cancelar Reserva Command API" y deja un resultado observable.
  `[NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados — CL-053]`
- **FR-BW-035**: El sistema DEBE persistir o entregar el dato exportado "Disponibilidad Agenda".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Disponibilidad Agenda" y deja un resultado observable.
- **FR-BW-036**: El sistema DEBE persistir o entregar el dato exportado "Ficha clientes".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Ficha clientes" y deja un resultado observable.
- **FR-BW-037**: El sistema DEBE persistir o entregar el dato exportado "Profesionales y especialidades".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Profesionales y especialidades" y deja un resultado observable.
- **FR-BW-038**: El sistema DEBE persistir o entregar el dato exportado "Reglas de negocio".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Reglas de negocio" y deja un resultado observable.
- **FR-BW-039**: El sistema DEBE persistir o entregar el dato exportado "Catálogo de servicios".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Catálogo de servicios" y deja un resultado observable.
- **FR-BW-040**: El sistema DEBE emitir el evento "Cita cancelada".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Cita cancelada" y deja un resultado observable.
- **FR-BW-041**: El sistema DEBE emitir el evento "Cita Modificada".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Cita Modificada" y deja un resultado observable.
- **FR-BW-042**: El sistema DEBE emitir el evento "Cita Creada".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Cita Creada" y deja un resultado observable.
- **FR-BW-043**: El sistema DEBE emitir el evento "Derivación a atención humana".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Derivación a atención humana" y deja un resultado observable.
- **FR-BW-044**: El sistema DEBE ejecutar la tarea programada "Actualizacion de agenda proveniente de Backend Agendamiento".
  Escenario: Dado que el bundle "Backend/Frontend Web" está disponible, cuando ocurre el disparador declarado, entonces el sistema completa "Actualizacion de agenda proveniente de Backend Agendamiento" y deja un resultado observable.
  `[NEEDS CLARIFICATION: periodicidad, ventana de ejecución y comportamiento ante fallo no declarados — CL-082]`

### Restricciones (R-1 a R-12)

- **R-1**: El proyecto DEBE respetar la política de confirmación de reservas.
- **R-2**: El proyecto DEBE respetar la política de cancelación y reprogramación.
- **R-3**: El proyecto DEBE respetar la política de atención mediante el canal de mensajería conversacional designado.
- **R-4**: El proyecto DEBE respetar la política de protección de datos del cliente.
- **R-5**: El proyecto DEBE respetar la política de penalización por inasistencia.
- **R-6**: El proyecto DEBE operar exclusivamente mediante el canal de mensajería conversacional designado.
- **R-7**: El proyecto DEBE integrarse con el sistema de gestión existente.
- **R-8**: El proyecto NO DEBE reemplazar el sistema de gestión del centro.
- **R-9**: El proyecto DEBE sincronizar la disponibilidad y las reservas en tiempo real.
- **R-10**: El proyecto DEBE operar continuamente 24×7.
- **R-11**: El proyecto DEBE integrarse con servicios externos mediante contratos declarados.
- **R-12**: El proyecto DEBE operar cuando la conectividad externa declarada esté disponible.

(Todas trazan a ACC / Business standards & policies o Situational constraints, disponible en `trace_annex.md`.)

### Escenarios de negocio (EN-01 a EN-08, no son FR)

- **EN-01**: "Gestionar servicios disponibles" — cubierto por User Story 4.
- **EN-02**: "Agendar una cita" — cubierto por User Story 1.
- **EN-03**: "Confirmar una cita" — cubierto por User Story 1.
- **EN-04**: "Reprogramar una cita" — cubierto por User Story 2.
- **EN-05**: "Cancelar una cita" — cubierto por User Story 2.
- **EN-06**: "Confirmar asistencia" — cubierto por User Story 2.
- **EN-07**: "Seguimiento de reservas" — cubierto por User Story 3.
- **EN-08**: "Identificar requerimiento del cliente" — cubierto por User Story 1.

`[NEEDS CLARIFICATION: actor, precondición y resultado observable de EN-01 a EN-08 por confirmar — CL-083]`

### Agrupadores de requisitos (informativo)

"Gestión de servicios", "Gestión de agendas y disponibilidad", "Gestión de clientes", "Gestión de profesionales", "Gestión de conversaciones", "Gestión de reservas".

## Success Criteria *(mandatory)*

### Criterios de éxito (CE) — objetivos de negocio

- **CE-1**: Lograr "Reducir tiempo de respuesta al cliente". `[NEEDS CLARIFICATION: ¿medido cómo? ¿métrica y línea base? — CL-058]`
- **CE-2**: Lograr "Incrementar conversión de consultas en reservas". `[NEEDS CLARIFICATION: ¿medido cómo? ¿métrica y línea base? — CL-059]`
- **CE-3**: Lograr "Recuperar automáticamente horas canceladas". `[NEEDS CLARIFICATION: ¿medido cómo? ¿métrica y línea base? — CL-060]`
- **CE-4**: Lograr "Reducir inasistencias mediante recordatorios automáticos". `[NEEDS CLARIFICATION: ¿medido cómo? ¿métrica y línea base? — CL-061]`
- **CE-5**: Lograr "Mantener sincronizada la agenda del centro". `[NEEDS CLARIFICATION: ¿medido cómo? ¿métrica y línea base? — CL-062]`
- **CE-6**: Lograr "Reducir los no-shows". `[NEEDS CLARIFICATION: ¿medido cómo? ¿métrica y línea base? — CL-063]`
- **CE-7**: Lograr "Centralizar la gestión de reservas". `[NEEDS CLARIFICATION: ¿medido cómo? ¿métrica y línea base? — CL-064]`

### NFR tecnológicos observables

- **NFR-TEC-1**: El sistema DEBE satisfacer la cualidad "Alta disponibilidad". `[NEEDS CLARIFICATION: criterio verificable y umbral no declarados — CL-065]`
- **NFR-TEC-2**: El sistema DEBE satisfacer la cualidad "Escalabilidad". `[NEEDS CLARIFICATION: criterio verificable y umbral no declarados — CL-066]`
- **NFR-TEC-3**: El sistema DEBE satisfacer la cualidad "Seguridad". `[NEEDS CLARIFICATION: criterio verificable y umbral no declarados — CL-067]`
- **NFR-TEC-4**: El sistema DEBE satisfacer la cualidad "Integrabilidad". `[NEEDS CLARIFICATION: criterio verificable y umbral no declarados — CL-068]`
- **NFR-TEC-5**: El sistema DEBE satisfacer la cualidad "Baja latencia conversacional". `[NEEDS CLARIFICATION: criterio verificable y umbral no declarados — CL-069]`
- **NFR-TEC-6**: El sistema DEBE satisfacer la cualidad "Mantenibilidad". `[NEEDS CLARIFICATION: criterio verificable y umbral no declarados — CL-070]`

### NFR de operación (deployment)

- **NFR-OP-1**: El sistema DEBE poder operar en el entorno "Production". `[NEEDS CLARIFICATION: entornos de prueba, integración o preproducción no declarados — CL-071]`
- **NFR-OP-2**: La instalación DEBE ser ejecutable mediante el procedimiento "Deploy manual coordinado por Área de Sistemas". `[NEEDS CLARIFICATION: pasos documentados, aprobaciones, reversión y evidencias de instalación no declarados — CL-089]`
- **NFR-OP-3**: El servicio DEBE satisfacer "Alta disponibilidad de servicio". `[NEEDS CLARIFICATION: objetivo, ventana de medición y exclusiones no declarados — CL-072]`

## Assumptions

- Las prioridades P1–P4 asignadas a las 4 User Stories no están declaradas en el pipeline 7Cs; se infirieron ordenando los 8 escenarios de negocio (EN-01 a EN-08) por afinidad con las prioridades de Constitution P1 ("automatizar la atención conversacional") y P6 ("mejorar la experiencia del cliente"), dejando la administración de catálogo (EN-01) como la de menor prioridad relativa por no ser atención directa al cliente. Es una decisión de secuenciación, no un requisito nuevo.
- No se asumió ningún otro valor no declarado: todo dato faltante (contratos, esquemas, métricas, umbrales, periodicidades, permisos, atributos de entidades, actores de escenarios de negocio) se dejó como `[NEEDS CLARIFICATION]`, replicando exactamente lo detectado por la auditoría del pipeline 7Cs (72 dudas inline + 94 en `clarify_input.md`).
- No se incluyó tecnología: nombres de producto (canal de mensajería, proveedor de procesamiento conversacional, bases de datos, runtime, nube) fueron neutralizados por el propio pipeline antes de esta especificación (ver `composed/prompt_specify_reconstruction_report.md`) y no se reintrodujeron aquí.
