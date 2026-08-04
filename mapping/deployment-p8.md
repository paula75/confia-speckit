# Mapping — Deployment Canvas

Fuente COM: `com/arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-deployment-p8.json`

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

Balance: 22 post-it, 19 a plan.md, 3 NFR en spec.md, 8 dudas, 22 trazas.

## Trazas

| sticky_id | sección | target_id |
|---|---|---|
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8E-01` | Environments | `spec:NFR-OP-1` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8I-01` | Installation | `spec:NFR-OP-2` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8C-01` | Constraints | `spec:NFR-OP-3` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8B-01` | Bundles | `plan:Bundles` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8B-02` | Bundles | `plan:Bundles` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8B-03` | Bundles | `plan:Bundles` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8B-04` | Bundles | `plan:Bundles` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8B-05` | Bundles | `plan:Bundles` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8M-01` | Middleware | `plan:Middleware` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8R-01` | Runtime | `plan:Runtime` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8R-02` | Runtime | `plan:Runtime` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8CR-01` | Container runtimes | `plan:Container runtimes` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8OPS-01` | Operating systems | `plan:Operating systems` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8VE-01` | Virtualization engines | `plan:Virtualization engines` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8CA-01` | Cloud abstractions | `plan:Cloud abstractions` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8CA-02` | Cloud abstractions | `plan:Cloud abstractions` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8CA-03` | Cloud abstractions | `plan:Cloud abstractions` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8CA-04` | Cloud abstractions | `plan:Cloud abstractions` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8L-01` | Locations | `plan:Locations` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8N-01` | Networks | `plan:Networks` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8N-02` | Networks | `plan:Networks` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P8N-03` | Networks | `plan:Networks` |

## Clarifications

- [NEEDS CLARIFICATION: entornos de prueba, integración o preproducción no declarados]
- [NEEDS CLARIFICATION: NFR-OP-2, procedimiento, reversión y evidencias]
- [NEEDS CLARIFICATION: NFR-OP-3, objetivo de disponibilidad y ventana]
- [NEEDS CLARIFICATION: inconsistencia Structural↔Deployment; bundles Structural ausentes en Deployment: “Pagina web admin locales”; “Backend / Agente conversacional y de reservas”; “Backend agendamiento (multi-tenant)”; “Backend / Pagina web admin locales (multi-tenant)”; “PostgreSQL”; “MongoDB”; “Docker”; “Servicio LLM”; “whatsapp business”]
- [NEEDS CLARIFICATION: inconsistencia Structural↔Deployment; unidades Deployment no idénticas al censo: “Portal web pymes”; “Backend/ Sitio web”; “Backend/ Agendamiento”; “Base de Datos (PostgreSQL)”]
- [NEEDS CLARIFICATION: sección Operation vacía; responsable y procedimiento operativo no declarados]
- [NEEDS CLARIFICATION: respaldo y monitoreo no declarados]
- [NEEDS CLARIFICATION: Organization, Canvas, Version y Date están vacíos en la cabecera]
