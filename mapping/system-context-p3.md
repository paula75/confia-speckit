# Mapping — System Context Canvas

Fuente COM: `com/arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-system_context-p3.json`

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

## Integraciones (frontera del sistema)

INT-1 Integración de entrada desde “WhatsApp”; contrato exacto por confirmar.
INT-2 Integración de entrada desde “LLM”; contrato exacto por confirmar.
INT-3 Integración de entrada desde “Proveedor de Mapas”; contrato exacto por confirmar.
INT-4 Integración de salida hacia “WhatsApp”; contrato exacto por confirmar.
INT-5 Integración de salida hacia “LLM”; contrato exacto por confirmar.

## Requisitos funcionales (de frontera)

FR-SCC-001 El sistema DEBE recibir información mediante “WhatsApp”.
  ← SCC / User data input interfaces “WhatsApp”
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema recibir la información mediante la interfaz declarada.
  [NEEDS CLARIFICATION: contrato, esquema y comportamiento de error no declarados]

FR-SCC-002 El sistema DEBE emitir información mediante “WhatsApp”.
  ← SCC / User data output interfaces “WhatsApp”
  Escenario: Dado que la contraparte está disponible, cuando ocurre el intercambio, entonces el sistema emitir la información mediante la interfaz declarada.
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

## Fuera de alcance (por complemento)

- Intercambios con sistemas, repositorios o dispositivos que no aparecen en la retícula.
- Escrituras hacia contrapartes declaradas solo como origen y lecturas desde contrapartes declaradas solo como destino.
- Software instalado en dispositivos y contratos de repositorio, porque no están declarados.

Balance: 31 post-it, 5 integraciones, 18 FR de frontera, 14 dudas, 4 celdas vacías reportadas.

## Trazas

| sticky_id | sección | target_id |
|---|---|---|
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3SU-01` | Source users | `spec:Alcance/Actores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3SU-02` | Source users | `spec:Alcance/Actores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3SU-03` | Source users | `spec:Alcance/Actores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3SU-04` | Source users | `spec:Alcance/Actores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3TU-01` | Target users | `spec:Alcance/Actores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3TU-02` | Target users | `spec:Alcance/Actores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3TU-03` | Target users | `spec:Alcance/Actores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3TU-04` | Target users | `spec:Alcance/Actores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3SS-01` | Source systems | `spec:INT-1` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3SS-02` | Source systems | `spec:INT-2` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3SS-03` | Source systems | `spec:INT-3` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3TS-01` | Target systems | `spec:INT-4` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3TS-02` | Target systems | `spec:INT-5` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3UDII-01` | User data input interfaces | `spec:FR-SCC-001` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3UDOI-01` | User data output interfaces | `spec:FR-SCC-002` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3UDOI-02` | User data output interfaces | `spec:FR-SCC-003` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3UDOI-03` | User data output interfaces | `spec:FR-SCC-004` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3UDOI-04` | User data output interfaces | `spec:FR-SCC-005` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3SDII-01` | System data input interfaces | `spec:FR-SCC-006` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3SDII-02` | System data input interfaces | `spec:FR-SCC-007` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3SDOI-01` | System data output interfaces | `spec:FR-SCC-008` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3DDII-01` | Device data input interfaces | `spec:FR-SCC-009` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3DDII-02` | Device data input interfaces | `spec:FR-SCC-010` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3DDOI-01` | Device data output interfaces | `spec:FR-SCC-011` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3DDOI-02` | Device data output interfaces | `spec:FR-SCC-012` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3SD-01` | Source devices | `spec:FR-SCC-013` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3SD-02` | Source devices | `spec:FR-SCC-014` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3SD-03` | Source devices | `spec:FR-SCC-015` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3TD-01` | Target devices | `spec:FR-SCC-016` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3TD-02` | Target devices | `spec:FR-SCC-017` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P3TD-03` | Target devices | `spec:FR-SCC-018` |

## Clarifications

- [NEEDS CLARIFICATION: correspondencia uno-a-uno entre sistemas, interfaces de entrada/salida y destinos no declarada]
- [NEEDS CLARIFICATION: FR-SCC-001, contrato, esquema y error]
- [NEEDS CLARIFICATION: FR-SCC-002, contrato, esquema y error]
- [NEEDS CLARIFICATION: FR-SCC-003, contrato, esquema y error]
- [NEEDS CLARIFICATION: FR-SCC-004, contrato, esquema y error]
- [NEEDS CLARIFICATION: FR-SCC-005, contrato, esquema y error]
- [NEEDS CLARIFICATION: FR-SCC-006, contrato, esquema y error]
- [NEEDS CLARIFICATION: FR-SCC-007, contrato, esquema y error]
- [NEEDS CLARIFICATION: FR-SCC-008, contrato, esquema y error]
- [NEEDS CLARIFICATION: FR-SCC-009, contrato, esquema y error]
- [NEEDS CLARIFICATION: FR-SCC-010, contrato, esquema y error]
- [NEEDS CLARIFICATION: FR-SCC-011, contrato, esquema y error]
- [NEEDS CLARIFICATION: FR-SCC-012, contrato, esquema y error]
- [NEEDS CLARIFICATION: fila de repositorios vacía; confirmar que no existen integraciones externas de persistencia]
