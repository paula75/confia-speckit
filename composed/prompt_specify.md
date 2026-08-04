# /speckit.specify

Delivery ID: `arquitectura-para-sistema-de-reservas-inteligente`  
Template: `7Cs v1.1 June 2026`

Enunciado raíz (BCC):

Propósito: Proveer “Gestión integral de Reservas”.

## Contexto

### Actores organizacionales
- “Cliente”.
- “Profesionales del Centro”.
- “Administrador del centro”.
- “Recepcionista”.

### Productos y servicios

- “Gestión integral de Reservas”.

### Business infrastructure & equipment

- “PC del Encargado del Local”.
- “Dispositivos Móvil del Recepcionista”.
- “PC del Recepcionista”.
- “Dispositivo Móvil del Cliente”.
- “PC del Cliente”.
- “Dispositivo Móvil del Profesional”.
- “PC del Profesional”.
- “Servicio Cloud”.

### Business locations

- “Región Metropolitana”.

### Business facilities

- “Oficina Administracion”.
- “Recepción”.
- “Sala de espera”.
- “Estación de trabajo”.

## Perfiles de usuario

- “Administrador de la operación”: permisos no declarados.
- “Coordinador de agenda”: permisos no declarados.
- “Prestador del servicio”: permisos no declarados.
- “Solicitante de reserva”: permisos no declarados.

## ALCANCE (BCC/SCC)

## Índice de requisitos (System’s functional areas)

1. “Gestión de agenda”
2. “Gestión de profesionales”
3. “Gestión de servicios”
4. “Ejecución de servicio”
5. “Seguimiento de servicio agendado”
6. “Gestión de conversacional”

## Alcance

### Source users
- “Profesionales del Centro”.
- “Administrador del Centro”.
- “Cliente”.
- “Recepcionista del Centro”.
### Target users
- “Profesionales del Centro”.
- “Administrador del Centro”.
- “Cliente”.
- “Recepcionista del Centro”.

## Fuera de alcance (por complemento)

- Intercambios con sistemas, repositorios o dispositivos que no aparecen en la retícula.
- Escrituras hacia contrapartes declaradas solo como origen y lecturas desde contrapartes declaradas solo como destino.
- Software instalado en dispositivos y contratos de repositorio, porque no están declarados.

## ENTIDADES (BCC/Functional)

## Entidades clave

- “Cliente”: atributos abiertos.
- “Profesional”: atributos abiertos.
- “Local”: atributos abiertos.
- “Disponibilidad”: atributos abiertos.
- “Historial de atención”: atributos abiertos.
- “Servicio”: atributos abiertos.
- “Agenda”: atributos abiertos.
- “Reserva”: atributos abiertos.
- “Preferencias del cliente”: atributos abiertos.

## Entidades clave

- “Conversación”: atributos por confirmar.
- “Mensaje”: atributos por confirmar.
- “Contexto”: atributos por confirmar.
- “Intención”: atributos por confirmar.
- “Prompt”: atributos por confirmar.
- “Estado Conversacional”: atributos por confirmar.

## Entidades clave

- “Ficha clientes”: atributos por confirmar.
- “Disponibilidad Agenda”: atributos por confirmar.
- “Catálogo de servicios”: atributos por confirmar.
- “Profesionales y especialidades”: atributos por confirmar.
- “Historial Conversación”: atributos por confirmar.
- “Reglas de negocio”: atributos por confirmar.
- “Configuración conversacional”: atributos por confirmar.

## Entidades clave

- “Multimedia Web”: atributos por confirmar.

## Integraciones (frontera del sistema)

INT-1 Integración de entrada desde un servicio externo de mensajería conversacional; contrato exacto por confirmar.
  ← SCC / Source systems / traza atómica disponible en `trace_annex`
  Escenario: Dado que el servicio externo de mensajería está disponible, cuando entrega un mensaje, entonces el sistema recibe la información mediante el contrato declarado.
  [NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]

INT-2 Integración de entrada desde un servicio externo de procesamiento conversacional; contrato exacto por confirmar.
  ← SCC / Source systems / traza atómica disponible en `trace_annex`
  Escenario: Dado que el servicio externo de procesamiento está disponible, cuando entrega un resultado conversacional, entonces el sistema recibe la información mediante el contrato declarado.
  [NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]

INT-3 Integración de entrada desde un servicio externo de geolocalización; contrato exacto por confirmar.
  ← SCC / Source systems / traza atómica disponible en `trace_annex`
  Escenario: Dado que el servicio externo de geolocalización está disponible, cuando se consulta una ubicación, entonces el sistema recibe el resultado mediante el contrato declarado.
  [NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]

INT-4 Integración de salida hacia un servicio externo de mensajería conversacional; contrato exacto por confirmar.
  ← SCC / Target systems / traza atómica disponible en `trace_annex`
  Escenario: Dado un mensaje de salida, cuando el sistema solicita su entrega, entonces lo emite hacia el servicio externo mediante el contrato declarado.
  [NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]

INT-5 Integración de salida hacia un servicio externo de procesamiento conversacional; contrato exacto por confirmar.
  ← SCC / Target systems / traza atómica disponible en `trace_annex`
  Escenario: Dada una solicitud de procesamiento conversacional, cuando el sistema requiere un resultado, entonces la emite hacia el servicio externo mediante el contrato declarado.
  [NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]

## REQUISITOS (SCC/Functional)

## Requisitos funcionales (de frontera)

FR-SCC-001 El sistema DEBE recibir información humana mediante el canal de mensajería conversacional soportado.
  ← SCC / User data input interfaces / traza atómica disponible en `trace_annex`
  Escenario: Dado que una persona utiliza el canal soportado, cuando envía información, entonces el sistema la recibe y deja un resultado observable.
  Equivalencia funcional: absorbido también por FR-AC-017.
  [NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]

FR-SCC-002 El sistema DEBE emitir información visible mediante el canal de mensajería conversacional soportado.
  ← SCC / User data output interfaces / traza atómica disponible en `trace_annex`
  Escenario: Dado un resultado conversacional, cuando el sistema responde a una persona, entonces emite la información mediante el canal soportado.
  Equivalencia funcional: absorbido también por FR-AC-030 y FR-AC-046.
  [NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]

FR-SCC-003 El sistema DEBE emitir información mediante “SMS”.
  ← SCC / User data output interfaces “SMS”
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema emitir la información mediante la interfaz declarada.
  [NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]

FR-SCC-004 El sistema DEBE emitir información mediante “Email”.
  ← SCC / User data output interfaces “Email”
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema emitir la información mediante la interfaz declarada.
  [NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]

FR-SCC-005 El sistema DEBE emitir información mediante “falta interfaz web”.
  ← SCC / User data output interfaces “falta interfaz web”
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema emitir la información mediante la interfaz declarada.
  [NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]

FR-SCC-006 El sistema DEBE recibir información mediante “Command Request”.
  ← SCC / System data input interfaces “Command Request”
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema recibir la información mediante la interfaz declarada.
  [NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]

FR-SCC-007 El sistema DEBE recibir información mediante “Command Endpoints”.
  ← SCC / System data input interfaces “Command Endpoints”
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema recibir la información mediante la interfaz declarada.
  [NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]

FR-SCC-008 El sistema DEBE emitir información mediante “Command Request”.
  ← SCC / System data output interfaces “Command Request”
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema emitir la información mediante la interfaz declarada.
  [NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]

FR-SCC-009 El sistema DEBE recibir información mediante “File System”.
  ← SCC / Device data input interfaces “File System”
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema recibir la información mediante la interfaz declarada.
  [NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]

FR-SCC-010 El sistema DEBE recibir información mediante “Cámara del Dispositivo”.
  ← SCC / Device data input interfaces “Cámara del Dispositivo”
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema recibir la información mediante la interfaz declarada.
  [NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]

FR-SCC-011 El sistema DEBE emitir información mediante “Pantalla del dispositivo”.
  ← SCC / Device data output interfaces “Pantalla del dispositivo”
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema emitir la información mediante la interfaz declarada.
  [NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]

FR-SCC-012 El sistema DEBE emitir información mediante “Monitor PC”.
  ← SCC / Device data output interfaces “Monitor PC”
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema emitir la información mediante la interfaz declarada.
  [NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]

FR-SCC-013 El sistema DEBE permitir el canal de uso “PCs”.
  ← SCC / Source devices “PCs”
  Escenario: Dado un dispositivo declarado, cuando una persona usa el sistema, entonces el canal permanece disponible.

FR-SCC-014 El sistema DEBE permitir el canal de uso “Notebooks”.
  ← SCC / Source devices “Notebooks”
  Escenario: Dado un dispositivo declarado, cuando una persona usa el sistema, entonces el canal permanece disponible.

FR-SCC-015 El sistema DEBE permitir el canal de uso “Dispositivos Móviles”.
  ← SCC / Source devices “Dispositivos Móviles”
  Escenario: Dado un dispositivo declarado, cuando una persona usa el sistema, entonces el canal permanece disponible.

FR-SCC-016 El sistema DEBE permitir el canal de uso “PCs”.
  ← SCC / Target devices “PCs”
  Escenario: Dado un dispositivo declarado, cuando una persona usa el sistema, entonces el canal permanece disponible.

FR-SCC-017 El sistema DEBE permitir el canal de uso “Notebooks”.
  ← SCC / Target devices “Notebooks”
  Escenario: Dado un dispositivo declarado, cuando una persona usa el sistema, entonces el canal permanece disponible.

FR-SCC-018 El sistema DEBE permitir el canal de uso “Dispositivos Móviles”.
  ← SCC / Target devices “Dispositivos Móviles”
  Escenario: Dado un dispositivo declarado, cuando una persona usa el sistema, entonces el canal permanece disponible.

## Requisitos funcionales

FR-AC-001 El sistema DEBE aceptar mensajes de texto enviados por una persona mediante el canal conversacional soportado.
  ← Functional / User inputs / traza atómica disponible en `trace_annex`
  Escenario: Dado que el agente conversacional está disponible, cuando una persona envía un mensaje de texto, entonces el sistema lo recibe y deja un resultado observable.
  Equivalencia funcional: absorbido también por FR-AC-017 y FR-AC-046.

FR-AC-002 El sistema DEBE aceptar mensajes de audio enviados por una persona mediante el canal conversacional soportado.
  ← Functional / User inputs / traza atómica disponible en `trace_annex`
  Escenario: Dado que el agente conversacional está disponible, cuando una persona envía audio, entonces el sistema lo recibe como contenido multimedia y deja un resultado observable.
  Equivalencia funcional: absorbido también por FR-AC-018.

FR-AC-003 El sistema DEBE aceptar imágenes enviadas por una persona mediante el canal conversacional soportado.
  ← Functional / User inputs / traza atómica disponible en `trace_annex`
  Escenario: Dado que el agente conversacional está disponible, cuando una persona envía una imagen, entonces el sistema la recibe como contenido multimedia y deja un resultado observable.
  Equivalencia funcional: absorbido también por FR-AC-018.

FR-AC-004 El sistema DEBE aceptar una ubicación enviada por una persona mediante el canal conversacional soportado.
  ← Functional / User inputs / traza atómica disponible en `trace_annex`
  Escenario: Dado que el agente conversacional está disponible, cuando una persona comparte una ubicación, entonces el sistema la recibe y deja un resultado observable.

FR-AC-005 El sistema DEBE aceptar documentos enviados por una persona mediante el canal conversacional soportado.
  ← Functional / User inputs / traza atómica disponible en `trace_annex`
  Escenario: Dado que el agente conversacional está disponible, cuando una persona envía un documento, entonces el sistema lo recibe y deja un resultado observable.

FR-AC-009 El sistema DEBE recibir notificaciones entrantes de mensajes mediante un contrato de integración.
  ← Functional / API inputs / traza atómica disponible en `trace_annex`
  Escenario: Dado que el agente conversacional está disponible, cuando la contraparte notifica un mensaje, entonces el sistema recibe el contenido mediante el contrato declarado.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-AC-044 El sistema DEBE emitir solicitudes conversacionales hacia una capacidad externa de procesamiento mediante un contrato de integración.
  ← Functional / API outputs / traza atómica disponible en `trace_annex`
  Escenario: Dado que existe una conversación que requiere procesamiento externo, cuando el agente solicita un resultado, entonces el sistema emite la solicitud mediante el contrato declarado.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-AC-006 El sistema DEBE aceptar la interacción humana “Confirmar Cita”.
  ← Functional / UI-processing inputs “Confirmar Cita”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Confirmar Cita” y deja un resultado observable.

FR-AC-007 El sistema DEBE aceptar la interacción humana “Cancelar Cita”.
  ← Functional / UI-processing inputs “Cancelar Cita”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Cancelar Cita” y deja un resultado observable.

FR-AC-008 El sistema DEBE aceptar la interacción humana “Entregar disponibilidad horaria”.
  ← Functional / UI-processing inputs “Entregar disponibilidad horaria”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Entregar disponibilidad horaria” y deja un resultado observable.

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

## Requisitos funcionales

FR-BA-008 El sistema DEBE recibir resultados conversacionales desde una capacidad externa de procesamiento mediante un contrato de integración.
  ← Functional / API inputs / traza atómica disponible en `trace_annex`
  Escenario: Dado que el backend de agendamiento está disponible, cuando la contraparte entrega un resultado conversacional, entonces el sistema lo recibe mediante el contrato declarado.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BA-010 El sistema DEBE leer una respuesta conversacional importada para continuar el procesamiento del agendamiento.
  ← Functional / Data imports / traza atómica disponible en `trace_annex`
  Escenario: Dado que existe una respuesta conversacional disponible, cuando el backend continúa el agendamiento, entonces el sistema lee la respuesta y deja un resultado observable.

FR-BA-034 El sistema DEBE ejecutar la limpieza de sesiones conversacionales expiradas.
  ← Functional / Jobs / traza atómica disponible en `trace_annex`
  Escenario: Dado que existen sesiones conversacionales expiradas, cuando se dispara la tarea de limpieza, entonces el sistema elimina su estado expirado y registra el resultado.
  Equivalencia funcional: absorbido también por FR-AC-049.
  [NEEDS CLARIFICATION: periodicidad, ventana de ejecución y comportamiento ante fallo no declarados]

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

FR-BA-009 El sistema DEBE leer el dato importado “Historial de Conversación”.
  ← Functional / Data imports “Historial de Conversación”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Historial de Conversación” y deja un resultado observable.

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

## Requisitos funcionales

FR-BW-001 El sistema DEBE aceptar la interacción humana “Datos de servicios”.
  ← Functional / User inputs “Datos de servicios”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Datos de servicios” y deja un resultado observable.

FR-BW-002 El sistema DEBE aceptar la interacción humana “Disponibilidad de agenda”.
  ← Functional / User inputs “Disponibilidad de agenda”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Disponibilidad de agenda” y deja un resultado observable.

FR-BW-003 El sistema DEBE aceptar la interacción humana “Datos de profesionales”.
  ← Functional / User inputs “Datos de profesionales”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Datos de profesionales” y deja un resultado observable.

FR-BW-004 El sistema DEBE aceptar la interacción humana “Datos de clientes”.
  ← Functional / User inputs “Datos de clientes”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Datos de clientes” y deja un resultado observable.

FR-BW-005 El sistema DEBE aceptar la interacción humana “Crear/Modificar profesional”.
  ← Functional / UI-processing inputs “Crear/Modificar profesional”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Crear/Modificar profesional” y deja un resultado observable.

FR-BW-006 El sistema DEBE aceptar la interacción humana “Crear/Modificar Servicios”.
  ← Functional / UI-processing inputs “Crear/Modificar Servicios”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Crear/Modificar Servicios” y deja un resultado observable.

FR-BW-007 El sistema DEBE aceptar la interacción humana “Modificar Agenda”.
  ← Functional / UI-processing inputs “Modificar Agenda”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Modificar Agenda” y deja un resultado observable.

FR-BW-008 El sistema DEBE aceptar la interacción humana “Modificar datos Clientes”.
  ← Functional / UI-processing inputs “Modificar datos Clientes”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Modificar datos Clientes” y deja un resultado observable.

FR-BW-009 El sistema DEBE leer el dato importado “Disponibilidad Agenda”.
  ← Functional / Data imports “Disponibilidad Agenda”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Disponibilidad Agenda” y deja un resultado observable.

FR-BW-010 El sistema DEBE leer el dato importado “Ficha clientes”.
  ← Functional / Data imports “Ficha clientes”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Ficha clientes” y deja un resultado observable.

FR-BW-011 El sistema DEBE leer el dato importado “Profesionales y especialidades”.
  ← Functional / Data imports “Profesionales y especialidades”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Profesionales y especialidades” y deja un resultado observable.

FR-BW-012 El sistema DEBE leer el dato importado “Catálogo de servicios”.
  ← Functional / Data imports “Catálogo de servicios”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Catálogo de servicios” y deja un resultado observable.

FR-BW-013 El sistema DEBE leer el dato importado “Historial Conversación”.
  ← Functional / Data imports “Historial Conversación”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Historial Conversación” y deja un resultado observable.

FR-BW-014 El sistema DEBE leer el dato importado “Reglas de negocio”.
  ← Functional / Data imports “Reglas de negocio”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Reglas de negocio” y deja un resultado observable.

FR-BW-015 El sistema DEBE leer el dato importado “Configuración conversacional”.
  ← Functional / Data imports “Configuración conversacional”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Configuración conversacional” y deja un resultado observable.

FR-BW-016 El sistema DEBE reaccionar al evento recibido “Mensaje recibido”.
  ← Functional / Event handlers “Mensaje recibido”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Mensaje recibido” y deja un resultado observable.

FR-BW-017 El sistema DEBE reaccionar al evento recibido “Estado de mensaje recibido”.
  ← Functional / Event handlers “Estado de mensaje recibido”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Estado de mensaje recibido” y deja un resultado observable.

FR-BW-018 El sistema DEBE reaccionar al evento recibido “Error de interpretacion (derivar)”.
  ← Functional / Event handlers “Error de interpretacion (derivar)”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Error de interpretacion (derivar)” y deja un resultado observable.

FR-BW-019 El sistema DEBE aplicar la regla auxiliar “Gestión de conversación”.
  ← Functional / Helpers “Gestión de conversación”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Gestión de conversación” y deja un resultado observable.

FR-BW-020 El sistema DEBE aplicar la regla auxiliar “Selección de horarios”.
  ← Functional / Helpers “Selección de horarios”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Selección de horarios” y deja un resultado observable.

FR-BW-021 El sistema DEBE aplicar la regla auxiliar “Validación de reservas”.
  ← Functional / Helpers “Validación de reservas”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Validación de reservas” y deja un resultado observable.

FR-BW-022 El sistema DEBE mostrar o notificar “Dashboard resumen”.
  ← Functional / User visualizations, reports & notifications “Dashboard resumen”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Dashboard resumen” y deja un resultado observable.

FR-BW-023 El sistema DEBE mostrar o notificar “Agenda horaria”.
  ← Functional / User visualizations, reports & notifications “Agenda horaria”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Agenda horaria” y deja un resultado observable.

FR-BW-024 El sistema DEBE mostrar o notificar “Ficha clientes”.
  ← Functional / User visualizations, reports & notifications “Ficha clientes”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Ficha clientes” y deja un resultado observable.

FR-BW-025 El sistema DEBE mostrar o notificar “Ficha Profesionales”.
  ← Functional / User visualizations, reports & notifications “Ficha Profesionales”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Ficha Profesionales” y deja un resultado observable.

FR-BW-026 El sistema DEBE presentar el resultado de interfaz “Respuesta Confirmacion de modificación”.
  ← Functional / UI-processing outputs “Respuesta Confirmacion de modificación”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Respuesta Confirmacion de modificación” y deja un resultado observable.

FR-BW-027 El sistema DEBE presentar el resultado de interfaz “Respuesta Confirmacion de Creacion”.
  ← Functional / UI-processing outputs “Respuesta Confirmacion de Creacion”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Respuesta Confirmacion de Creacion” y deja un resultado observable.

FR-BW-028 El sistema DEBE presentar el resultado de interfaz “Respuesta Confirmacion de Eliminacion”.
  ← Functional / UI-processing outputs “Respuesta Confirmacion de Eliminacion”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Respuesta Confirmacion de Eliminacion” y deja un resultado observable.

FR-BW-029 El sistema DEBE emitir la respuesta de contrato “Disponibilidad Query API”.
  ← Functional / API outputs “Disponibilidad Query API”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Disponibilidad Query API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BW-030 El sistema DEBE emitir la respuesta de contrato “Servicios Query API”.
  ← Functional / API outputs “Servicios Query API”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Servicios Query API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BW-031 El sistema DEBE emitir la respuesta de contrato “Profesionale s Query API”.
  ← Functional / API outputs “Profesionale s Query API”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Profesionale s Query API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BW-032 El sistema DEBE emitir la respuesta de contrato “Crear Reserva Command API”.
  ← Functional / API outputs “Crear Reserva Command API”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Crear Reserva Command API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BW-033 El sistema DEBE emitir la respuesta de contrato “Actualizar Reserva Command API”.
  ← Functional / API outputs “Actualizar Reserva Command API”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Actualizar Reserva Command API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BW-034 El sistema DEBE emitir la respuesta de contrato “Cancelar Reserva Command API”.
  ← Functional / API outputs “Cancelar Reserva Command API”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Cancelar Reserva Command API” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BW-035 El sistema DEBE persistir o entregar el dato exportado “Disponibilidad Agenda”.
  ← Functional / Data exports “Disponibilidad Agenda”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Disponibilidad Agenda” y deja un resultado observable.

FR-BW-036 El sistema DEBE persistir o entregar el dato exportado “Ficha clientes”.
  ← Functional / Data exports “Ficha clientes”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Ficha clientes” y deja un resultado observable.

FR-BW-037 El sistema DEBE persistir o entregar el dato exportado “Profesionales y especialidades”.
  ← Functional / Data exports “Profesionales y especialidades”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Profesionales y especialidades” y deja un resultado observable.

FR-BW-038 El sistema DEBE persistir o entregar el dato exportado “Reglas de negocio”.
  ← Functional / Data exports “Reglas de negocio”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Reglas de negocio” y deja un resultado observable.

FR-BW-039 El sistema DEBE persistir o entregar el dato exportado “Catálogo de servicios”.
  ← Functional / Data exports “Catálogo de servicios”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Catálogo de servicios” y deja un resultado observable.

FR-BW-040 El sistema DEBE emitir el evento “Cita cancelada”.
  ← Functional / Event triggers “Cita cancelada”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Cita cancelada” y deja un resultado observable.

FR-BW-041 El sistema DEBE emitir el evento “Cita Modificada”.
  ← Functional / Event triggers “Cita Modificada”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Cita Modificada” y deja un resultado observable.

FR-BW-042 El sistema DEBE emitir el evento “Cita Creada”.
  ← Functional / Event triggers “Cita Creada”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Cita Creada” y deja un resultado observable.

FR-BW-043 El sistema DEBE emitir el evento “Derivación a atención humana”.
  ← Functional / Event triggers “Derivación a atención humana”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Derivación a atención humana” y deja un resultado observable.

FR-BW-044 El sistema DEBE ejecutar la tarea programada “Actualizacion de agenda proveniente de Backend Agendamiento”.
  ← Functional / Jobs “Actualizacion de agenda proveniente de Backend Agendamiento”
  Escenario: Dado que el bundle “Backend/Frontend Web” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Actualizacion de agenda proveniente de Backend Agendamiento” y deja un resultado observable.
  [NEEDS CLARIFICATION: periodicidad, ventana de ejecución y comportamiento ante fallo no declarados]

## CRITERIOS DE ÉXITO (ACC)

## /speckit.specify · Validadores de aceptación

## /speckit.specify · Criterios de éxito

CE-1 Lograr “Reducir tiempo de respuesta al cliente”. [NEEDS CLARIFICATION: ¿medido cómo? ¿métrica y línea base?]
CE-2 Lograr “Incrementar conversión de consultas en reservas”. [NEEDS CLARIFICATION: ¿medido cómo? ¿métrica y línea base?]
CE-3 Lograr “Recuperar automáticamente horas canceladas”. [NEEDS CLARIFICATION: ¿medido cómo? ¿métrica y línea base?]
CE-4 Lograr “Reducir inasistencias mediante recordatorios automáticos”. [NEEDS CLARIFICATION: ¿medido cómo? ¿métrica y línea base?]
CE-5 Lograr “Mantener sincronizada la agenda del centro”. [NEEDS CLARIFICATION: ¿medido cómo? ¿métrica y línea base?]
CE-6 Lograr “Reducir los no-shows”. [NEEDS CLARIFICATION: ¿medido cómo? ¿métrica y línea base?]
CE-7 Lograr “Centralizar la gestión de reservas”. [NEEDS CLARIFICATION: ¿medido cómo? ¿métrica y línea base?]

## /speckit.specify · NFR tecnológicos observables

NFR-TEC-1 El sistema DEBE satisfacer la cualidad “Alta disponibilidad”. [NEEDS CLARIFICATION: criterio verificable y umbral no declarados]
NFR-TEC-2 El sistema DEBE satisfacer la cualidad “Escalabilidad”. [NEEDS CLARIFICATION: criterio verificable y umbral no declarados]
NFR-TEC-3 El sistema DEBE satisfacer la cualidad “Seguridad”. [NEEDS CLARIFICATION: criterio verificable y umbral no declarados]
NFR-TEC-4 El sistema DEBE satisfacer la cualidad “Integrabilidad”. [NEEDS CLARIFICATION: criterio verificable y umbral no declarados]
NFR-TEC-5 El sistema DEBE satisfacer la cualidad “Baja latencia conversacional”. [NEEDS CLARIFICATION: criterio verificable y umbral no declarados]
NFR-TEC-6 El sistema DEBE satisfacer la cualidad “Mantenibilidad”. [NEEDS CLARIFICATION: criterio verificable y umbral no declarados]

## /speckit.specify · Restricciones

R-1 El proyecto DEBE respetar la política de confirmación de reservas.
  ← ACC / Business standards & policies / traza atómica disponible en `trace_annex`

R-2 El proyecto DEBE respetar la política de cancelación y reprogramación.
  ← ACC / Business standards & policies / traza atómica disponible en `trace_annex`

R-3 El proyecto DEBE respetar la política de atención mediante el canal de mensajería conversacional designado.
  ← ACC / Business standards & policies / traza atómica disponible en `trace_annex`

R-4 El proyecto DEBE respetar la política de protección de datos del cliente.
  ← ACC / Business standards & policies / traza atómica disponible en `trace_annex`

R-5 El proyecto DEBE respetar la política de penalización por inasistencia.
  ← ACC / Business standards & policies / traza atómica disponible en `trace_annex`

R-6 El proyecto DEBE operar exclusivamente mediante el canal de mensajería conversacional designado.
  ← ACC / Situational constraints / traza atómica disponible en `trace_annex`

R-7 El proyecto DEBE integrarse con el sistema de gestión existente.
  ← ACC / Situational constraints / traza atómica disponible en `trace_annex`

R-8 El proyecto NO DEBE reemplazar el sistema de gestión del centro.
  ← ACC / Situational constraints / traza atómica disponible en `trace_annex`

R-9 El proyecto DEBE sincronizar la disponibilidad y las reservas en tiempo real.
  ← ACC / Situational constraints / traza atómica disponible en `trace_annex`

R-10 El proyecto DEBE operar continuamente 24×7.
  ← ACC / Situational constraints / traza atómica disponible en `trace_annex`

R-11 El proyecto DEBE integrarse con servicios externos mediante contratos declarados.
  ← ACC / Situational constraints / traza atómica disponible en `trace_annex`

R-12 El proyecto DEBE operar cuando la conectividad externa declarada esté disponible.
  ← ACC / Situational constraints / traza atómica disponible en `trace_annex`

## CONTEXTO ADICIONAL (BCC)

## Escenarios de negocio (no son FR)

- EN-01: “Gestionar servicios disponibles”; actor, precondición y resultado observable por confirmar.
- EN-02: “Agendar una cita”; actor, precondición y resultado observable por confirmar.
- EN-03: “Confirmar una cita”; actor, precondición y resultado observable por confirmar.
- EN-04: “Reprogramar una cita”; actor, precondición y resultado observable por confirmar.
- EN-05: “Cancelar una cita”; actor, precondición y resultado observable por confirmar.
- EN-06: “Confirmar asistencia”; actor, precondición y resultado observable por confirmar.
- EN-07: “Seguimiento de reservas”; actor, precondición y resultado observable por confirmar.
- EN-08: “Identificar requerimiento del cliente”; actor, precondición y resultado observable por confirmar.

## Agrupadores de requisitos

- “Gestión de servicios”.
- “Gestión de agendas y disponibilidad”.
- “Gestión de clientes”.
- “Gestión de profesionales”.
- “Gestión de conversaciones”.
- “Gestión de reservas”.

## Fragmento para /speckit.specify

NFR-OP-1 El sistema DEBE poder operar en el entorno “Production”.
  ← Deployment / Environments “Production”
  [NEEDS CLARIFICATION: entornos de prueba, integración o preproducción no declarados]

NFR-OP-2 La instalación DEBE ser ejecutable mediante el procedimiento “Deploy manual coordinado por Área de Sistemas”.
  ← Deployment / Installation “Deploy manual coordinado por Área de Sistemas”
  [NEEDS CLARIFICATION: pasos documentados, aprobaciones, reversión y evidencias de instalación no declarados]

NFR-OP-3 El servicio DEBE satisfacer “Alta disponibilidad de servicio”.
  ← Deployment / Constraints “Alta disponibilidad de servicio”
  [NEEDS CLARIFICATION: objetivo, ventana de medición y exclusiones no declarados]

NO incluir decisiones de tecnología en esta especificación: el contexto técnico se entrega por separado en /speckit.plan.
