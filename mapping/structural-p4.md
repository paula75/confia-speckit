# Mapping — Structural Canvas

Fuente COM: `com/arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-structural-p4.json`

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

## Trazas

| sticky_id | sección | target_id |
|---|---|---|
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4DIF-01` | Data input interfaces to frontend bundles | `plan:Capa Presentación` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4DIF-02` | Data input interfaces to frontend bundles | `plan:Capa Presentación` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4DIF-03` | Data input interfaces to frontend bundles | `plan:Capa Presentación` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4FB-01` | Frontend bundles | `plan:Capa Presentación` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4DOF-01` | Data output interfaces from frontend bundles | `plan:Capa Presentación` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4DIB-01` | Data input interfaces to backend bundles | `plan:Capa Servicios` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4DIB-02` | Data input interfaces to backend bundles | `plan:Capa Servicios` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4DIB-03` | Data input interfaces to backend bundles | `plan:Capa Servicios` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4BB-01` | Backend bundles | `plan:Capa Servicios` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4BB-02` | Backend bundles | `plan:Capa Servicios` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4BB-03` | Backend bundles | `plan:Capa Servicios` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4DOB-01` | Data output interfaces from backend bundles | `plan:Capa Servicios` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4DOB-02` | Data output interfaces from backend bundles | `plan:Capa Servicios` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4DOB-03` | Data output interfaces from backend bundles | `plan:Capa Servicios` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4DOB-04` | Data output interfaces from backend bundles | `plan:Capa Servicios` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4DOB-05` | Data output interfaces from backend bundles | `plan:Capa Servicios` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4RB-01` | Repository bundles | `plan:Capa Persistencia` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4RB-02` | Repository bundles | `plan:Capa Persistencia` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4RB-03` | Repository bundles | `plan:Capa Persistencia` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4DIPI-01` | Data input interfaces to platform & infrastructure bundles | `plan:Capa Plataforma` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4PIB-01` | Platform & Infrastructure bundles | `plan:Capa Plataforma` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4PIB-02` | Platform & Infrastructure bundles | `plan:Capa Plataforma` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4PIB-03` | Platform & Infrastructure bundles | `plan:Capa Plataforma` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4DOPI-01` | Data output interfaces from platform & infrastructure bundles | `plan:Capa Plataforma` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4C-01` | Constraints | `plan:Restricciones` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4C-02` | Constraints | `plan:Restricciones` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4C-03` | Constraints | `plan:Restricciones` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4C-04` | Constraints | `plan:Restricciones` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4C-05` | Constraints | `plan:Restricciones` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P4C-06` | Constraints | `plan:Restricciones` |

## Clarifications

- [NEEDS CLARIFICATION: falta detalle funcional de los bundles “Pagina web admin locales”; “Backend / Agente conversacional y de reservas”; “Backend agendamiento (multi-tenant)”; “Backend / Pagina web admin locales (multi-tenant)”; “PostgreSQL”; “Storage”; “MongoDB”; “Docker”; “Servicio LLM”; “whatsapp business”]
- [NEEDS CLARIFICATION: los nombres de Functional Canvas no coinciden literalmente con el censo: “Agente conversacional”; “Backend Agendamiento”; “Backend/Frontend Web”]
- [NEEDS CLARIFICATION: las celdas de repositorio y dispositivo sin interfaces deben confirmarse como decisión explícita]
