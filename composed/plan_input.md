# /speckit.plan

Delivery ID: `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm`  
Template: `7Cs v1.1 June 2026`

## Contexto técnico dado por la organización (ACC)

## Contexto para /speckit.plan (dado por la organización)

- “Arquitectura desacoplada mediante adapters”.
- “Arquitectura SaaS Multi- tenant”.
- “Integración mediante APIs”.
- “Diseño modular”.
- “Protección de datos personales”.
- “API REST para integración interna”.

## Arquitectura estructural (Structural)

## /speckit.plan (contexto dado, no elegido)

Arquitectura en capas:

- **Presentación:** “Pagina web admin locales” · entrada: “Formulario carga de servicio”, “Formulario carga de agenda”, “Formulario carga de profesional” · salida: “Notificación web local”.
- **Servicios:** “Backend / Agente conversacional y de reservas”, “Backend agendamiento (multi-tenant)”, “Backend / Pagina web admin locales (multi-tenant)” · entrada: “command request (whatsapp business)- Conversacion”, “command request - Ubicación”, “command request (servicio llm)- Conversacion” · salida: “Respuesta WhatsApp”, “Crear Reserva Command Gmail - Outlook”, “Actualizar Reserva Command Gmail - Outlook”, “Cancelar Reserva Command Gmail - Outlook”, “Notificación WhatsApp”.
- **Persistencia:** “PostgreSQL”, “Storage”, “MongoDB” · entrada: (sin entradas declaradas) · salida: (sin salidas declaradas).
- **Plataforma:** “Docker”, “Servicio LLM”, “whatsapp business” · entrada: “Imágenes / contenedores Docker” · salida: “Entorno de ejecución”.
- **Dispositivo:** (sin bundles declarados) · entrada: (sin entradas declaradas) · salida: (sin salidas declaradas).

### Restricciones de arquitectura

- “deploy nube”.
- “Agendamiento exclusivo por outlook y gmail”.
- “Persistencia exclusiva de datos propios de ConfIA”.
- “Operación exclusiva mediante WhatsApp”.
- “Integración desacoplada mediante APIs”.
- “Arquitectura SaaS Multitenant”.

### Censo de bundles (10)

1. “Pagina web admin locales”
2. “Backend / Agente conversacional y de reservas”
3. “Backend agendamiento (multi-tenant)”
4. “Backend / Pagina web admin locales (multi-tenant)”
5. “PostgreSQL”
6. “Storage”
7. “MongoDB”
8. “Docker”
9. “Servicio LLM”
10. “whatsapp business”

### Chequeo de Functional Canvas

- Functional encontrados: 3; bundles censados: 10.
- Nombres Functional: “Agente conversacional”, “Backend Agendamiento”, “Backend/Frontend Web”.
- Sin software desplegado en dispositivo: decisión indicada por la sección vacía `Device bundles`.

Balance: 30 post-it, 10 bundles, 30 trazas, 3 dudas.

## Contexto por bundle (Functional)

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

## Contexto para /speckit.plan

Bundle: “Backend/Frontend Web”.

### Stack declarado
- “Javascript”.
- “Python”.
- “Docker”.
- “Object Storage”.
- “Nginx”.

### Constraints locales
- “GUI amigable”.
- “Recibir derivacion de LLM para atencion humana”.

## Infraestructura y operación (Deployment)

## Fragmento para /speckit.plan

### Infra y operación

#### Bundles
- “Portal web pymes”.
- “Backend/ Sitio web”.
- “Backend/ Agendamiento”.
- “Base de Datos (PostgreSQL)”.
- “Storage”.

#### Middleware
- “PostgreSQL”.

#### Runtime
- “Node.js”.
- “cPython”.

#### Orchestration & scheduling
- (sin elementos declarados)

#### Container runtimes
- “Docker”.

#### Operating systems
- “Linux”.

#### Virtualization engines
- “GCP”.

#### Cloud abstractions
- “Cloud run”.
- “Cloud Sql”.
- “Bucket”.
- “Cloud Function”.

#### Hardware
- (sin elementos declarados)

#### Locations
- “Chile”.

#### Networks
- “Red GCP”.
- “Internet / WAN”.
- “Red docker”.

### Chequeo cruzado de bundles

- Censo Structural (10): “Pagina web admin locales”; “Backend / Agente conversacional y de reservas”; “Backend agendamiento (multi-tenant)”; “Backend / Pagina web admin locales (multi-tenant)”; “PostgreSQL”; “Storage”; “MongoDB”; “Docker”; “Servicio LLM”; “whatsapp business”.
- Deployment (5): “Portal web pymes”; “Backend/ Sitio web”; “Backend/ Agendamiento”; “Base de Datos (PostgreSQL)”; “Storage”.
- La discrepancia se reporta; no se corrigió ni fusionó.

Ausencias esperables reportadas: respaldo, monitoreo y responsable/procedimiento de operación.

## Bloques trasladados íntegramente desde /speckit.specify por contener tecnología nombrada

INT-1 Integración de entrada desde “WhatsApp”; contrato exacto por confirmar.
INT-2 Integración de entrada desde “LLM”; contrato exacto por confirmar.
INT-3 Integración de entrada desde “Proveedor de Mapas”; contrato exacto por confirmar.
INT-4 Integración de salida hacia “WhatsApp”; contrato exacto por confirmar.
INT-5 Integración de salida hacia “LLM”; contrato exacto por confirmar.

FR-SCC-001 El sistema DEBE recibir información mediante “WhatsApp”.
  ← SCC / User data input interfaces “WhatsApp”
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema recibir la información mediante la interfaz declarada.
  [NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]

FR-SCC-002 El sistema DEBE emitir información mediante “WhatsApp”.
  ← SCC / User data output interfaces “WhatsApp”
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema emitir la información mediante la interfaz declarada.
  [NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]

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

FR-AC-009 El sistema DEBE recibir la solicitud de contrato “Webhook: mensaje de WhatsApp”.
  ← Functional / API inputs “Webhook: mensaje de WhatsApp”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Webhook: mensaje de WhatsApp” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-AC-044 El sistema DEBE emitir la respuesta de contrato “LLM Conversation”.
  ← Functional / API outputs “LLM Conversation”
  Escenario: Dado que el bundle “Agente conversacional” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “LLM Conversation” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BA-008 El sistema DEBE recibir la solicitud de contrato “LLM Conversation”.
  ← Functional / API inputs “LLM Conversation”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “LLM Conversation” y deja un resultado observable.
  [NEEDS CLARIFICATION: esquema, contraparte y respuesta de error del contrato no declarados]

FR-BA-010 El sistema DEBE leer el dato importado “Respuesta LLM”.
  ← Functional / Data imports “Respuesta LLM”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Respuesta LLM” y deja un resultado observable.

FR-BA-034 El sistema DEBE ejecutar la tarea programada “Limpieza de sesiones expiradas LLM”.
  ← Functional / Jobs “Limpieza de sesiones expiradas LLM”
  Escenario: Dado que el bundle “Backend Agendamiento” está disponible, cuando ocurre el disparador declarado, entonces el sistema completa “Limpieza de sesiones expiradas LLM” y deja un resultado observable.
  [NEEDS CLARIFICATION: periodicidad, ventana de ejecución y comportamiento ante fallo no declarados]

- “Cliente”.
- “Profesional del Centro”.
- “Administrador del centro”.
- “Sistema de Agenda / ERP del centro”.
- “WhatsApp Business”.
- “Equipo de Operación ConfIA”.

R-1 El proyecto DEBE respetar “Política de confirmación de reservas”.
R-2 El proyecto DEBE respetar “Política de cancelación y reprogramación”.
R-3 El proyecto DEBE respetar “Política de atención mediante WhatsApp”.
R-4 El proyecto DEBE respetar “Política de protección de datos del cliente”.
R-5 El proyecto DEBE respetar “Política de penalización por inasistencia”.
R-6 El proyecto DEBE respetar “Operar exclusivamente mediante WhatsApp”.
R-7 El proyecto DEBE respetar “Integrarse al sistema de gestión existente”.
R-8 El proyecto DEBE respetar “No reemplazar el sistema de gestión del centro”.
R-9 El proyecto DEBE respetar “Sincronizar disponibilidad y reservas en tiempo real”.
R-10 El proyecto DEBE respetar “Operar continuamente 24×7”.
R-11 El proyecto DEBE respetar “Integración con APIs de terceros”.
R-12 El proyecto DEBE respetar “Disponibilidad de internet”.
