# Mapping — Functional Canvas p6

Fuente COM: `com/arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-functional-p6.json`

### Bundle: Backend Agendamiento (Functional, p. 6)

## Entidades clave

- “Ficha clientes”: atributos por confirmar.
- “Disponibilidad Agenda”: atributos por confirmar.
- “Catálogo de servicios”: atributos por confirmar.
- “Profesionales y especialidades”: atributos por confirmar.
- “Historial Conversación”: atributos por confirmar.
- “Reglas de negocio”: atributos por confirmar.
- “Configuración conversacional”: atributos por confirmar.

## Requisitos funcionales

FR-BA-001 El sistema DEBE recibir la solicitud de contrato “Disponibilidad Query API”.
  ← Functional / API inputs “Disponibilidad Query API”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Disponibilidad Query API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BA-002 El sistema DEBE recibir la solicitud de contrato “Servicios Query API”.
  ← Functional / API inputs “Servicios Query API”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Servicios Query API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BA-003 El sistema DEBE recibir la solicitud de contrato “Profesionale s Query API”.
  ← Functional / API inputs “Profesionale s Query API”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Profesionale s Query API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BA-004 El sistema DEBE recibir la solicitud de contrato “Historial de conversacion Query”.
  ← Functional / API inputs “Historial de conversacion Query”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Historial de conversacion Query” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BA-005 El sistema DEBE recibir la solicitud de contrato “Crear Reserva Command API”.
  ← Functional / API inputs “Crear Reserva Command API”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Crear Reserva Command API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BA-006 El sistema DEBE recibir la solicitud de contrato “Actualizar Reserva Command API”.
  ← Functional / API inputs “Actualizar Reserva Command API”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Actualizar Reserva Command API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BA-007 El sistema DEBE recibir la solicitud de contrato “Cancelar Reserva Command API”.
  ← Functional / API inputs “Cancelar Reserva Command API”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Cancelar Reserva Command API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BA-008 El sistema DEBE recibir la solicitud de contrato “LLM Conversation”.
  ← Functional / API inputs “LLM Conversation”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “LLM Conversation” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BA-009 El sistema DEBE leer el dato importado “Historial de Conversación”.
  ← Functional / Data imports “Historial de Conversación”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Historial de Conversación” y deja un resultado observable.

FR-BA-010 El sistema DEBE leer el dato importado “Respuesta LLM”.
  ← Functional / Data imports “Respuesta LLM”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Respuesta LLM” y deja un resultado observable.

FR-BA-011 El sistema DEBE reaccionar al evento recibido “Mensaje recibido”.
  ← Functional / Event handlers “Mensaje recibido”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Mensaje recibido” y deja un resultado observable.

FR-BA-012 El sistema DEBE reaccionar al evento recibido “Error de interpretacion (derivar)”.
  ← Functional / Event handlers “Error de interpretacion (derivar)”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Error de interpretacion (derivar)” y deja un resultado observable.

FR-BA-013 El sistema DEBE aplicar la regla auxiliar “Recomendación de servicios”.
  ← Functional / Helpers “Recomendación de servicios”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Recomendación de servicios” y deja un resultado observable.

FR-BA-014 El sistema DEBE aplicar la regla auxiliar “Selección de horarios”.
  ← Functional / Helpers “Selección de horarios”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Selección de horarios” y deja un resultado observable.

FR-BA-015 El sistema DEBE aplicar la regla auxiliar “Validación de reservas”.
  ← Functional / Helpers “Validación de reservas”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Validación de reservas” y deja un resultado observable.

FR-BA-016 El sistema DEBE emitir la respuesta de contrato “Disponibilidad Query API”.
  ← Functional / API outputs “Disponibilidad Query API”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Disponibilidad Query API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BA-017 El sistema DEBE emitir la respuesta de contrato “Servicios Query API”.
  ← Functional / API outputs “Servicios Query API”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Servicios Query API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BA-018 El sistema DEBE emitir la respuesta de contrato “Profesionale s Query API”.
  ← Functional / API outputs “Profesionale s Query API”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Profesionale s Query API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BA-019 El sistema DEBE emitir la respuesta de contrato “Crear Reserva Command API”.
  ← Functional / API outputs “Crear Reserva Command API”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Crear Reserva Command API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BA-020 El sistema DEBE emitir la respuesta de contrato “Actualizar Reserva Command API”.
  ← Functional / API outputs “Actualizar Reserva Command API”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Actualizar Reserva Command API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BA-021 El sistema DEBE emitir la respuesta de contrato “Cancelar Reserva Command API”.
  ← Functional / API outputs “Cancelar Reserva Command API”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Cancelar Reserva Command API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BA-022 El sistema DEBE persistir o entregar el dato exportado “Disponibilidad Agenda”.
  ← Functional / Data exports “Disponibilidad Agenda”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Disponibilidad Agenda” y deja un resultado observable.

FR-BA-023 El sistema DEBE persistir o entregar el dato exportado “Ficha clientes”.
  ← Functional / Data exports “Ficha clientes”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Ficha clientes” y deja un resultado observable.

FR-BA-024 El sistema DEBE persistir o entregar el dato exportado “Profesionales y especialidades”.
  ← Functional / Data exports “Profesionales y especialidades”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Profesionales y especialidades” y deja un resultado observable.

FR-BA-025 El sistema DEBE persistir o entregar el dato exportado “Catálogo de servicios”.
  ← Functional / Data exports “Catálogo de servicios”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Catálogo de servicios” y deja un resultado observable.

FR-BA-026 El sistema DEBE persistir o entregar el dato exportado “Historial Conversación”.
  ← Functional / Data exports “Historial Conversación”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Historial Conversación” y deja un resultado observable.

FR-BA-027 El sistema DEBE persistir o entregar el dato exportado “Reglas de negocio”.
  ← Functional / Data exports “Reglas de negocio”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Reglas de negocio” y deja un resultado observable.

FR-BA-028 El sistema DEBE persistir o entregar el dato exportado “Configuración conversacional”.
  ← Functional / Data exports “Configuración conversacional”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Configuración conversacional” y deja un resultado observable.

FR-BA-029 El sistema DEBE emitir el evento “Escalamiento a humano por error de interpretación”.
  ← Functional / Event triggers “Escalamiento a humano por error de interpretación”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Escalamiento a humano por error de interpretación” y deja un resultado observable.

FR-BA-030 El sistema DEBE emitir el evento “Conversación finalizada”.
  ← Functional / Event triggers “Conversación finalizada”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Conversación finalizada” y deja un resultado observable.

FR-BA-031 El sistema DEBE emitir el evento “Cita creada”.
  ← Functional / Event triggers “Cita creada”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Cita creada” y deja un resultado observable.

FR-BA-032 El sistema DEBE emitir el evento “Cita cancelada”.
  ← Functional / Event triggers “Cita cancelada”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Cita cancelada” y deja un resultado observable.

FR-BA-033 El sistema DEBE emitir el evento “Cita actualizada”.
  ← Functional / Event triggers “Cita actualizada”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Cita actualizada” y deja un resultado observable.

FR-BA-034 El sistema DEBE ejecutar la tarea programada “Limpieza de sesiones expiradas LLM”.
  ← Functional / Jobs “Limpieza de sesiones expiradas LLM”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Limpieza de sesiones expiradas LLM” y deja un resultado observable.
  [NEEDS CLARIFICATION: periodicidad, ventana de ejecución y comportamiento ante fallo no declarados]

FR-BA-035 El sistema DEBE ejecutar la tarea programada “Detección de Alucinaciones”.
  ← Functional / Jobs “Detección de Alucinaciones”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Detección de Alucinaciones” y deja un resultado observable.
  [NEEDS CLARIFICATION: periodicidad, ventana de ejecución y comportamiento ante fallo no declarados]

FR-BA-036 El sistema DEBE ejecutar la tarea programada “Evaluador Score”.
  ← Functional / Jobs “Evaluador Score”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Evaluador Score” y deja un resultado observable.
  [NEEDS CLARIFICATION: periodicidad, ventana de ejecución y comportamiento ante fallo no declarados]

FR-BA-037 El sistema DEBE ejecutar la tarea programada “Liberador reservas sin confirmar”.
  ← Functional / Jobs “Liberador reservas sin confirmar”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Liberador reservas sin confirmar” y deja un resultado observable.
  [NEEDS CLARIFICATION: periodicidad, ventana de ejecución y comportamiento ante fallo no declarados]

## Contexto para /speckit.plan

Bundle: “Backend Agendamiento”.

### Stack declarado
- “Python”.
- “Docker”.
- “PostgreSQL”.

### Constraints locales
- “No generar reservas duplicadas”.
- “No ofrecer horarios no disponibles”.
- “Confirmar antes de modificar una cita”.
- “Mantener trazabilidad de las operaciones”.

Secciones vacías coherentes con un bundle sin interfaz humana: `User inputs`, `UI-processing inputs`. Las visualizaciones también están vacías.

Balance p6: 52 post-it, 37 FR-BA, 7 entidades, 21 dudas, 52 trazas.

## Trazas

| sticky_id | sección | target_id |
|---|---|---|
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6BC-01` | Bundles & components | `spec:Bundle BA` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6DO-01` | Data objects | `spec:BA/Entidades` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6DO-02` | Data objects | `spec:BA/Entidades` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6DO-03` | Data objects | `spec:BA/Entidades` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6DO-04` | Data objects | `spec:BA/Entidades` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6DO-05` | Data objects | `spec:BA/Entidades` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6DO-06` | Data objects | `spec:BA/Entidades` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6DO-07` | Data objects | `spec:BA/Entidades` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6APIIN-01` | API inputs | `spec:FR-BA-001` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6APIIN-02` | API inputs | `spec:FR-BA-002` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6APIIN-03` | API inputs | `spec:FR-BA-003` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6APIIN-04` | API inputs | `spec:FR-BA-004` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6APIIN-05` | API inputs | `spec:FR-BA-005` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6APIIN-06` | API inputs | `spec:FR-BA-006` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6APIIN-07` | API inputs | `spec:FR-BA-007` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6APIIN-08` | API inputs | `spec:FR-BA-008` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6DI-01` | Data imports | `spec:FR-BA-009` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6DI-02` | Data imports | `spec:FR-BA-010` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6EH-01` | Event handlers | `spec:FR-BA-011` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6EH-02` | Event handlers | `spec:FR-BA-012` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6H-01` | Helpers | `spec:FR-BA-013` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6H-02` | Helpers | `spec:FR-BA-014` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6H-03` | Helpers | `spec:FR-BA-015` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6APIOUT-01` | API outputs | `spec:FR-BA-016` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6APIOUT-02` | API outputs | `spec:FR-BA-017` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6APIOUT-03` | API outputs | `spec:FR-BA-018` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6APIOUT-04` | API outputs | `spec:FR-BA-019` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6APIOUT-05` | API outputs | `spec:FR-BA-020` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6APIOUT-06` | API outputs | `spec:FR-BA-021` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6DE-01` | Data exports | `spec:FR-BA-022` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6DE-02` | Data exports | `spec:FR-BA-023` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6DE-03` | Data exports | `spec:FR-BA-024` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6DE-04` | Data exports | `spec:FR-BA-025` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6DE-05` | Data exports | `spec:FR-BA-026` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6DE-06` | Data exports | `spec:FR-BA-027` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6DE-07` | Data exports | `spec:FR-BA-028` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6ET-01` | Event triggers | `spec:FR-BA-029` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6ET-02` | Event triggers | `spec:FR-BA-030` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6ET-03` | Event triggers | `spec:FR-BA-031` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6ET-04` | Event triggers | `spec:FR-BA-032` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6ET-05` | Event triggers | `spec:FR-BA-033` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6J-01` | Jobs | `spec:FR-BA-034` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6J-02` | Jobs | `spec:FR-BA-035` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6J-03` | Jobs | `spec:FR-BA-036` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6J-04` | Jobs | `spec:FR-BA-037` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6TS-01` | Technology stack | `plan:BA/Stack` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6TS-02` | Technology stack | `plan:BA/Stack` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6TS-03` | Technology stack | `plan:BA/Stack` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6C-01` | Constraints | `plan:BA/Constraints` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6C-02` | Constraints | `plan:BA/Constraints` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6C-03` | Constraints | `plan:BA/Constraints` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P6C-04` | Constraints | `plan:BA/Constraints` |

## Clarifications

- [NEEDS CLARIFICATION: atributos de las entidades del bundle “Backend Agendamiento” no declarados]
- [NEEDS CLARIFICATION: FR-BA-001, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-BA-002, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-BA-003, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-BA-004, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-BA-005, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-BA-006, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-BA-007, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-BA-008, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-BA-016, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-BA-017, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-BA-018, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-BA-019, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-BA-020, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-BA-021, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-BA-034, periodicidad, ventana y fallo]
- [NEEDS CLARIFICATION: FR-BA-035, periodicidad, ventana y fallo]
- [NEEDS CLARIFICATION: FR-BA-036, periodicidad, ventana y fallo]
- [NEEDS CLARIFICATION: FR-BA-037, periodicidad, ventana y fallo]
- [NEEDS CLARIFICATION: System, Organization, Canvas, Version y Date están vacíos en la cabecera]
- [NEEDS CLARIFICATION: confirmar que el bundle Backend Agendamiento no expone visualizaciones ni salidas de UI]
