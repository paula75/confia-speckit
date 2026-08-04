# Mapping — Functional Canvas p5

Fuente COM: `com/arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-functional-p5.json`

### Bundle: Agente conversacional (Functional, p. 5)

## Entidades clave

- “Conversación”: atributos por confirmar.
- “Mensaje”: atributos por confirmar.
- “Contexto”: atributos por confirmar.
- “Intención”: atributos por confirmar.
- “Prompt”: atributos por confirmar.
- “Estado Conversacional”: atributos por confirmar.

## Requisitos funcionales

FR-AC-001 El sistema DEBE aceptar la interacción humana “Mensaje WhatsApp”.
  ← Functional / User inputs “Mensaje WhatsApp”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Mensaje WhatsApp” y deja un resultado observable.

FR-AC-002 El sistema DEBE aceptar la interacción humana “Audio WhatsApp”.
  ← Functional / User inputs “Audio WhatsApp”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Audio WhatsApp” y deja un resultado observable.

FR-AC-003 El sistema DEBE aceptar la interacción humana “Imagen WhatsApp”.
  ← Functional / User inputs “Imagen WhatsApp”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Imagen WhatsApp” y deja un resultado observable.

FR-AC-004 El sistema DEBE aceptar la interacción humana “Ubicación WhatsApp”.
  ← Functional / User inputs “Ubicación WhatsApp”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Ubicación WhatsApp” y deja un resultado observable.

FR-AC-005 El sistema DEBE aceptar la interacción humana “Documento WhatsApp”.
  ← Functional / User inputs “Documento WhatsApp”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Documento WhatsApp” y deja un resultado observable.

FR-AC-006 El sistema DEBE aceptar la interacción humana “Confirmar Cita”.
  ← Functional / UI-processing inputs “Confirmar Cita”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Confirmar Cita” y deja un resultado observable.

FR-AC-007 El sistema DEBE aceptar la interacción humana “Cancelar Cita”.
  ← Functional / UI-processing inputs “Cancelar Cita”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Cancelar Cita” y deja un resultado observable.

FR-AC-008 El sistema DEBE aceptar la interacción humana “Entregar disponibilidad horaria”.
  ← Functional / UI-processing inputs “Entregar disponibilidad horaria”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Entregar disponibilidad horaria” y deja un resultado observable.

FR-AC-009 El sistema DEBE recibir la solicitud de contrato “Webhook: mensaje de WhatsApp”.
  ← Functional / API inputs “Webhook: mensaje de WhatsApp”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Webhook: mensaje de WhatsApp” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-AC-010 El sistema DEBE recibir la solicitud de contrato “Webhook: estado de mensaje”.
  ← Functional / API inputs “Webhook: estado de mensaje”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Webhook: estado de mensaje” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-AC-011 El sistema DEBE leer el dato importado “Ficha del cliente”.
  ← Functional / Data imports “Ficha del cliente”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Ficha del cliente” y deja un resultado observable.

FR-AC-012 El sistema DEBE leer el dato importado “Configuración conversacional”.
  ← Functional / Data imports “Configuración conversacional”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Configuración conversacional” y deja un resultado observable.

FR-AC-013 El sistema DEBE leer el dato importado “Historial de Conversación”.
  ← Functional / Data imports “Historial de Conversación”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Historial de Conversación” y deja un resultado observable.

FR-AC-014 El sistema DEBE leer el dato importado “Catalogo de servicios”.
  ← Functional / Data imports “Catalogo de servicios”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Catalogo de servicios” y deja un resultado observable.

FR-AC-015 El sistema DEBE leer el dato importado “Disponibilidad de Agenda”.
  ← Functional / Data imports “Disponibilidad de Agenda”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Disponibilidad de Agenda” y deja un resultado observable.

FR-AC-016 El sistema DEBE leer el dato importado “Reglas de negocio”.
  ← Functional / Data imports “Reglas de negocio”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Reglas de negocio” y deja un resultado observable.

FR-AC-017 El sistema DEBE reaccionar al evento recibido “Mensaje recibido”.
  ← Functional / Event handlers “Mensaje recibido”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Mensaje recibido” y deja un resultado observable.

FR-AC-018 El sistema DEBE reaccionar al evento recibido “Multimedia recibida”.
  ← Functional / Event handlers “Multimedia recibida”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Multimedia recibida” y deja un resultado observable.

FR-AC-019 El sistema DEBE reaccionar al evento recibido “Recordatorio de cita”.
  ← Functional / Event handlers “Recordatorio de cita”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Recordatorio de cita” y deja un resultado observable.

FR-AC-020 El sistema DEBE reaccionar al evento recibido “Error de interpretacion (derivar)”.
  ← Functional / Event handlers “Error de interpretacion (derivar)”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Error de interpretacion (derivar)” y deja un resultado observable.

FR-AC-021 El sistema DEBE reaccionar al evento recibido “Hora liberada”.
  ← Functional / Event handlers “Hora liberada”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Hora liberada” y deja un resultado observable.

FR-AC-022 El sistema DEBE reaccionar al evento recibido “Conversación reanudada”.
  ← Functional / Event handlers “Conversación reanudada”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Conversación reanudada” y deja un resultado observable.

FR-AC-023 El sistema DEBE aplicar la regla auxiliar “Constructor de Prompt”.
  ← Functional / Helpers “Constructor de Prompt”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Constructor de Prompt” y deja un resultado observable.

FR-AC-024 El sistema DEBE aplicar la regla auxiliar “Gestor de Contexto”.
  ← Functional / Helpers “Gestor de Contexto”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Gestor de Contexto” y deja un resultado observable.

FR-AC-025 El sistema DEBE aplicar la regla auxiliar “Depurar historial conversacional”.
  ← Functional / Helpers “Depurar historial conversacional”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Depurar historial conversacional” y deja un resultado observable.

FR-AC-026 El sistema DEBE aplicar la regla auxiliar “Recomendación de servicios”.
  ← Functional / Helpers “Recomendación de servicios”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Recomendación de servicios” y deja un resultado observable.

FR-AC-027 El sistema DEBE aplicar la regla auxiliar “Moderación de Contenido”.
  ← Functional / Helpers “Moderación de Contenido”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Moderación de Contenido” y deja un resultado observable.

FR-AC-028 El sistema DEBE aplicar la regla auxiliar “Clasificador de intención”.
  ← Functional / Helpers “Clasificador de intención”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Clasificador de intención” y deja un resultado observable.

FR-AC-029 El sistema DEBE aplicar la regla auxiliar “Detección de intención”.
  ← Functional / Helpers “Detección de intención”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Detección de intención” y deja un resultado observable.

FR-AC-030 El sistema DEBE mostrar o notificar “Respuesta conversacional”.
  ← Functional / User visualizations, reports & notifications “Respuesta conversacional”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Respuesta conversacional” y deja un resultado observable.

FR-AC-031 El sistema DEBE mostrar o notificar “Confirmación de reserva”.
  ← Functional / User visualizations, reports & notifications “Confirmación de reserva”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Confirmación de reserva” y deja un resultado observable.

FR-AC-032 El sistema DEBE mostrar o notificar “Propuesta de horarios”.
  ← Functional / User visualizations, reports & notifications “Propuesta de horarios”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Propuesta de horarios” y deja un resultado observable.

FR-AC-033 El sistema DEBE mostrar o notificar “Recordatorio”.
  ← Functional / User visualizations, reports & notifications “Recordatorio”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Recordatorio” y deja un resultado observable.

FR-AC-034 El sistema DEBE presentar el resultado de interfaz “Respuesta Confirmacion de cita”.
  ← Functional / UI-processing outputs “Respuesta Confirmacion de cita”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Respuesta Confirmacion de cita” y deja un resultado observable.

FR-AC-035 El sistema DEBE presentar el resultado de interfaz “Respuesta Cancelacion de cita”.
  ← Functional / UI-processing outputs “Respuesta Cancelacion de cita”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Respuesta Cancelacion de cita” y deja un resultado observable.

FR-AC-036 El sistema DEBE presentar el resultado de interfaz “Disponibilidad horaria entregada”.
  ← Functional / UI-processing outputs “Disponibilidad horaria entregada”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Disponibilidad horaria entregada” y deja un resultado observable.

FR-AC-037 El sistema DEBE emitir la respuesta de contrato “Disponibilidad Query API”.
  ← Functional / API outputs “Disponibilidad Query API”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Disponibilidad Query API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-AC-038 El sistema DEBE emitir la respuesta de contrato “Servicios Query API”.
  ← Functional / API outputs “Servicios Query API”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Servicios Query API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-AC-039 El sistema DEBE emitir la respuesta de contrato “Profesionale s Query API”.
  ← Functional / API outputs “Profesionale s Query API”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Profesionale s Query API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-AC-040 El sistema DEBE emitir la respuesta de contrato “Historial de conversacion Query”.
  ← Functional / API outputs “Historial de conversacion Query”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Historial de conversacion Query” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-AC-041 El sistema DEBE emitir la respuesta de contrato “Crear Reserva Command API”.
  ← Functional / API outputs “Crear Reserva Command API”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Crear Reserva Command API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-AC-042 El sistema DEBE emitir la respuesta de contrato “Actualizar Reserva Command API”.
  ← Functional / API outputs “Actualizar Reserva Command API”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Actualizar Reserva Command API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-AC-043 El sistema DEBE emitir la respuesta de contrato “Cancelar Reserva Command API”.
  ← Functional / API outputs “Cancelar Reserva Command API”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Cancelar Reserva Command API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-AC-044 El sistema DEBE emitir la respuesta de contrato “LLM Conversation”.
  ← Functional / API outputs “LLM Conversation”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “LLM Conversation” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-AC-045 El sistema DEBE persistir o entregar el dato exportado “Historial de Conversación”.
  ← Functional / Data exports “Historial de Conversación”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Historial de Conversación” y deja un resultado observable.

FR-AC-046 El sistema DEBE emitir el evento “Mensaje IN or OUT”.
  ← Functional / Event triggers “Mensaje IN or OUT”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Mensaje IN or OUT” y deja un resultado observable.

FR-AC-047 El sistema DEBE ejecutar la tarea programada “Registrar conversación”.
  ← Functional / Jobs “Registrar conversación”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Registrar conversación” y deja un resultado observable.
  [NEEDS CLARIFICATION: periodicidad, ventana de ejecución y comportamiento ante fallo no declarados]

FR-AC-048 El sistema DEBE ejecutar la tarea programada “Actualizar contexto conversacional”.
  ← Functional / Jobs “Actualizar contexto conversacional”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Actualizar contexto conversacional” y deja un resultado observable.
  [NEEDS CLARIFICATION: periodicidad, ventana de ejecución y comportamiento ante fallo no declarados]

FR-AC-049 El sistema DEBE ejecutar la tarea programada “Limpiar contexto expirado”.
  ← Functional / Jobs “Limpiar contexto expirado”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Limpiar contexto expirado” y deja un resultado observable.
  [NEEDS CLARIFICATION: periodicidad, ventana de ejecución y comportamiento ante fallo no declarados]

FR-AC-050 El sistema DEBE ejecutar la tarea programada “Resumir conversación”.
  ← Functional / Jobs “Resumir conversación”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Resumir conversación” y deja un resultado observable.
  [NEEDS CLARIFICATION: periodicidad, ventana de ejecución y comportamiento ante fallo no declarados]

## Contexto para /speckit.plan

Bundle: “Agente conversacional”.

### Stack declarado
- “WhatsApp Business API”.
- “Meta Business Suite”.
- “LLM API”.

### Constraints locales
- “Mantener contexto conversacional”.
- “Ejecutar acciones únicamente autorizadas por las reglas de negocio”.
- “Trazabilidad de las conversaciones”.
- “Baja latencia en las respuestas”.
- “Permitir derivación a atención humana”.

Balance p5: 65 post-it, 50 FR-AC, 6 entidades, 16 dudas, 65 trazas.

## Trazas

| sticky_id | sección | target_id |
|---|---|---|
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5BC-01` | Bundles & components | `spec:Bundle AC` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5DO-01` | Data objects | `spec:AC/Entidades` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5DO-02` | Data objects | `spec:AC/Entidades` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5DO-03` | Data objects | `spec:AC/Entidades` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5DO-04` | Data objects | `spec:AC/Entidades` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5DO-05` | Data objects | `spec:AC/Entidades` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5DO-06` | Data objects | `spec:AC/Entidades` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5UI-01` | User inputs | `spec:FR-AC-001` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5UI-02` | User inputs | `spec:FR-AC-002` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5UI-03` | User inputs | `spec:FR-AC-003` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5UI-04` | User inputs | `spec:FR-AC-004` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5UI-05` | User inputs | `spec:FR-AC-005` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5UIPIN-01` | UI-processing inputs | `spec:FR-AC-006` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5UIPIN-02` | UI-processing inputs | `spec:FR-AC-007` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5UIPIN-03` | UI-processing inputs | `spec:FR-AC-008` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5APIIN-01` | API inputs | `spec:FR-AC-009` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5APIIN-02` | API inputs | `spec:FR-AC-010` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5DI-01` | Data imports | `spec:FR-AC-011` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5DI-02` | Data imports | `spec:FR-AC-012` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5DI-03` | Data imports | `spec:FR-AC-013` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5DI-04` | Data imports | `spec:FR-AC-014` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5DI-05` | Data imports | `spec:FR-AC-015` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5DI-06` | Data imports | `spec:FR-AC-016` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5EH-01` | Event handlers | `spec:FR-AC-017` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5EH-02` | Event handlers | `spec:FR-AC-018` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5EH-03` | Event handlers | `spec:FR-AC-019` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5EH-04` | Event handlers | `spec:FR-AC-020` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5EH-05` | Event handlers | `spec:FR-AC-021` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5EH-06` | Event handlers | `spec:FR-AC-022` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5H-01` | Helpers | `spec:FR-AC-023` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5H-02` | Helpers | `spec:FR-AC-024` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5H-03` | Helpers | `spec:FR-AC-025` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5H-04` | Helpers | `spec:FR-AC-026` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5H-05` | Helpers | `spec:FR-AC-027` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5H-06` | Helpers | `spec:FR-AC-028` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5H-07` | Helpers | `spec:FR-AC-029` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5UVRN-01` | User visualizations, reports & notifications | `spec:FR-AC-030` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5UVRN-02` | User visualizations, reports & notifications | `spec:FR-AC-031` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5UVRN-03` | User visualizations, reports & notifications | `spec:FR-AC-032` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5UVRN-04` | User visualizations, reports & notifications | `spec:FR-AC-033` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5UIPOUT-01` | UI-processing outputs | `spec:FR-AC-034` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5UIPOUT-02` | UI-processing outputs | `spec:FR-AC-035` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5UIPOUT-03` | UI-processing outputs | `spec:FR-AC-036` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5APIOUT-01` | API outputs | `spec:FR-AC-037` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5APIOUT-02` | API outputs | `spec:FR-AC-038` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5APIOUT-03` | API outputs | `spec:FR-AC-039` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5APIOUT-04` | API outputs | `spec:FR-AC-040` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5APIOUT-05` | API outputs | `spec:FR-AC-041` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5APIOUT-06` | API outputs | `spec:FR-AC-042` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5APIOUT-07` | API outputs | `spec:FR-AC-043` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5APIOUT-08` | API outputs | `spec:FR-AC-044` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5DE-01` | Data exports | `spec:FR-AC-045` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5ET-01` | Event triggers | `spec:FR-AC-046` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5J-01` | Jobs | `spec:FR-AC-047` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5J-02` | Jobs | `spec:FR-AC-048` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5J-03` | Jobs | `spec:FR-AC-049` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5J-04` | Jobs | `spec:FR-AC-050` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5TS-01` | Technology stack | `plan:AC/Stack` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5TS-02` | Technology stack | `plan:AC/Stack` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5TS-03` | Technology stack | `plan:AC/Stack` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5C-01` | Constraints | `plan:AC/Constraints` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5C-02` | Constraints | `plan:AC/Constraints` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5C-03` | Constraints | `plan:AC/Constraints` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5C-04` | Constraints | `plan:AC/Constraints` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P5C-05` | Constraints | `plan:AC/Constraints` |

## Clarifications

- [NEEDS CLARIFICATION: atributos de las entidades del bundle “Agente conversacional” no declarados]
- [NEEDS CLARIFICATION: FR-AC-009, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-AC-010, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-AC-037, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-AC-038, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-AC-039, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-AC-040, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-AC-041, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-AC-042, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-AC-043, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-AC-044, esquema, contraparte y error del contrato]
- [NEEDS CLARIFICATION: FR-AC-047, periodicidad, ventana y fallo]
- [NEEDS CLARIFICATION: FR-AC-048, periodicidad, ventana y fallo]
- [NEEDS CLARIFICATION: FR-AC-049, periodicidad, ventana y fallo]
- [NEEDS CLARIFICATION: FR-AC-050, periodicidad, ventana y fallo]
- [NEEDS CLARIFICATION: Organization, Canvas, Version y Date están vacíos en la cabecera]
