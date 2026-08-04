# Mapping — Architectural Context Canvas

Fuente COM: `com/arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-architectural_context-p2.json`

## /speckit.constitution

P1 “Automatizar la atención conversacional”. [ACC/Business strategy]
P2 “Incrementar la ocupación efectiva de las agendas”. [ACC/Business strategy]
P3 “Reducir la carga administrativa del centro”. [ACC/Business strategy]
P4 “Escalar el servicio para múltiples centros de belleza”. [ACC/Business strategy]
P5 “Brindar atención permanente mediante canales digitales 24/7.”. [ACC/Business strategy]
P6 “Mejorar la experiencia del cliente”. [ACC/Business strategy]
P7 “Plataforma SaaS”. [ACC/IT strategy]
P8 “Cloud Native”. [ACC/IT strategy]
P9 “Integración desacoplada con sistemas existentes”. [ACC/IT strategy]
P10 “Configuración centralizada para múltiples centros”. [ACC/IT strategy]
P11 “La experiencia del cliente tiene prioridad”. [ACC/Business principles]
P12 “Automatizar sin modificar la operación del centro”. [ACC/Business principles]
P13 “Mantener una única fuente de información para las reservas”. [ACC/Business principles]
P14 “Facilitar la autogestión del cliente”. [ACC/Business principles]
P15 “Minimizar el impacto sobre los procesos actuales”. [ACC/Business principles]
P16 “Bajo acoplamiento”. [ACC/Technical principles]
P17 “Alta cohesión”. [ACC/Technical principles]
P18 “Configuración antes que personalización”. [ACC/Technical principles]
P19 “Componentes reutilizables”. [ACC/Technical principles]
P20 “Escalabilidad horizontal”. [ACC/Technical principles]
P21 “Integración mediante adapters”. [ACC/Technical principles]
P22 “Observabilidad mediante logging y monitoreo”. [ACC/Technical principles]

## /speckit.specify · Validadores de aceptación

- “Cliente”.
- “Profesional del Centro”.
- “Administrador del centro”.
- “Sistema de Agenda / ERP del centro”.
- “WhatsApp Business”.
- “Equipo de Operación ConfIA”.

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

## Contexto para /speckit.plan (dado por la organización)

- “Arquitectura desacoplada mediante adapters”.
- “Arquitectura SaaS Multi- tenant”.
- “Integración mediante APIs”.
- “Diseño modular”.
- “Protección de datos personales”.
- “API REST para integración interna”.

Balance: 22 principios, 7 criterios de éxito, 12 restricciones, 14 dudas · 59 post-it, 10 secciones, 59 trazas.

## Trazas

| sticky_id | sección | target_id |
|---|---|---|
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BS-01` | Business strategy | `constitution:P1` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BS-02` | Business strategy | `constitution:P2` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BS-03` | Business strategy | `constitution:P3` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BS-04` | Business strategy | `constitution:P4` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BS-05` | Business strategy | `constitution:P5` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BS-06` | Business strategy | `constitution:P6` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2ITS-01` | IT strategy | `constitution:P7` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2ITS-02` | IT strategy | `constitution:P8` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2ITS-03` | IT strategy | `constitution:P9` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2ITS-04` | IT strategy | `constitution:P10` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BPR-01` | Business principles | `constitution:P11` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BPR-02` | Business principles | `constitution:P12` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BPR-03` | Business principles | `constitution:P13` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BPR-04` | Business principles | `constitution:P14` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BPR-05` | Business principles | `constitution:P15` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2TP-01` | Technical principles | `constitution:P16` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2TP-02` | Technical principles | `constitution:P17` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2TP-03` | Technical principles | `constitution:P18` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2TP-04` | Technical principles | `constitution:P19` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2TP-05` | Technical principles | `constitution:P20` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2TP-06` | Technical principles | `constitution:P21` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2TP-07` | Technical principles | `constitution:P22` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2ST-01` | Stakeholders | `spec:Validadores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2ST-02` | Stakeholders | `spec:Validadores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2ST-03` | Stakeholders | `spec:Validadores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2ST-04` | Stakeholders | `spec:Validadores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2ST-05` | Stakeholders | `spec:Validadores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2ST-06` | Stakeholders | `spec:Validadores` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BGD-01` | Business goals & drivers | `spec:CE-1` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BGD-02` | Business goals & drivers | `spec:CE-2` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BGD-03` | Business goals & drivers | `spec:CE-3` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BGD-04` | Business goals & drivers | `spec:CE-4` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BGD-05` | Business goals & drivers | `spec:CE-5` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BGD-06` | Business goals & drivers | `spec:CE-6` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BGD-07` | Business goals & drivers | `spec:CE-7` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2TGD-01` | Technology goals & drivers | `spec:NFR-TEC-1` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2TGD-02` | Technology goals & drivers | `spec:NFR-TEC-2` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2TGD-03` | Technology goals & drivers | `spec:NFR-TEC-3` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2TGD-04` | Technology goals & drivers | `spec:NFR-TEC-4` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2TGD-05` | Technology goals & drivers | `spec:NFR-TEC-5` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2TGD-06` | Technology goals & drivers | `spec:NFR-TEC-6` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BSP-01` | Business standards & policies | `spec:R-1` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BSP-02` | Business standards & policies | `spec:R-2` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BSP-03` | Business standards & policies | `spec:R-3` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BSP-04` | Business standards & policies | `spec:R-4` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2BSP-05` | Business standards & policies | `spec:R-5` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2SC-01` | Situational constraints | `spec:R-6` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2SC-02` | Situational constraints | `spec:R-7` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2SC-03` | Situational constraints | `spec:R-8` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2SC-04` | Situational constraints | `spec:R-9` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2SC-05` | Situational constraints | `spec:R-10` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2SC-06` | Situational constraints | `spec:R-11` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2SC-07` | Situational constraints | `spec:R-12` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2TSP-01` | Technology standards & policies | `plan:Contexto técnico` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2TSP-02` | Technology standards & policies | `plan:Contexto técnico` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2TSP-03` | Technology standards & policies | `plan:Contexto técnico` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2TSP-04` | Technology standards & policies | `plan:Contexto técnico` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2TSP-05` | Technology standards & policies | `plan:Contexto técnico` |
| `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm-P2TSP-06` | Technology standards & policies | `plan:Contexto técnico` |

## Clarifications

- [NEEDS CLARIFICATION: CE-1, métrica y línea base para “Reducir tiempo de respuesta al cliente”]
- [NEEDS CLARIFICATION: CE-2, métrica y línea base para “Incrementar conversión de consultas en reservas”]
- [NEEDS CLARIFICATION: CE-3, métrica y línea base para “Recuperar automáticamente horas canceladas”]
- [NEEDS CLARIFICATION: CE-4, métrica y línea base para “Reducir inasistencias mediante recordatorios automáticos”]
- [NEEDS CLARIFICATION: CE-5, métrica y línea base para “Mantener sincronizada la agenda del centro”]
- [NEEDS CLARIFICATION: CE-6, métrica y línea base para “Reducir los no-shows”]
- [NEEDS CLARIFICATION: CE-7, métrica y línea base para “Centralizar la gestión de reservas”]
- [NEEDS CLARIFICATION: NFR-TEC-1, umbral verificable no declarado]
- [NEEDS CLARIFICATION: NFR-TEC-2, umbral verificable no declarado]
- [NEEDS CLARIFICATION: NFR-TEC-3, umbral verificable no declarado]
- [NEEDS CLARIFICATION: NFR-TEC-4, umbral verificable no declarado]
- [NEEDS CLARIFICATION: NFR-TEC-5, umbral verificable no declarado]
- [NEEDS CLARIFICATION: NFR-TEC-6, umbral verificable no declarado]
- [NEEDS CLARIFICATION: Organization, Canvas, Version y Date están vacíos en la cabecera]
