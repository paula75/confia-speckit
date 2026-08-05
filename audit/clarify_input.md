# Insumo para /speckit.clarify

Delivery ID: `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm`

72 dudas `[NEEDS CLARIFICATION]` recuperadas de `composed/prompt_specify.md`, más 4 ambigüedades que el
compositor dejó en prosa sin la marca formal. Ninguna se resuelve aquí: se numeran y se ordenan por impacto en
las decisiones de `/speckit.plan` (primero lo que bloquea diseño de jobs, contratos y permisos; después lo de
menor impacto), tal como exige el contrato del skill de auditoría. Son preguntas para el cliente.

## Bloque 1 — Periodicidad y comportamiento ante fallo de tareas programadas (bloquea diseño de scheduling en `/speckit.plan`)

1. `FR-AC-047` "Registrar conversación": ¿periodicidad, ventana de ejecución y comportamiento ante fallo?
2. `FR-AC-048` "Actualizar contexto conversacional": ídem.
3. `FR-AC-049` / `FR-BA-034` "Limpiar contexto expirado" (equivalencia funcional documentada): ídem.
4. `FR-AC-050` "Resumir conversación": ídem.
5. `FR-BA-035` "Detección de Alucinaciones": ídem.
6. `FR-BA-036` "Evaluador Score": ídem.
7. `FR-BA-037` "Liberador reservas sin confirmar": ídem.
8. `FR-BW-044` "Actualizacion de agenda proveniente de Backend Agendamiento": ídem.

## Bloque 2 — Esquema, contraparte y comportamiento de error de contratos de integración internos (bloquea diseño de contratos API en `/speckit.plan`)

9. `FR-AC-009` "Webhook: notificación de mensaje entrante".
10. `FR-AC-010` "Webhook: estado de mensaje".
11. `FR-AC-037`…`FR-AC-043` (7 contratos: Disponibilidad Query, Servicios Query, Profesionales Query, Historial
    de conversación Query, Crear/Actualizar/Cancelar Reserva Command).
12. `FR-AC-044` "solicitud de procesamiento conversacional externo".
13. `FR-BA-001`…`FR-BA-008` (8 contratos de entrada equivalentes a los del bloque anterior, vistos desde
    Backend Agendamiento).
14. `FR-BA-016`…`FR-BA-021` (6 contratos de salida, mismos nombres).
15. `FR-BW-029`…`FR-BW-034` (6 contratos de salida, mismos nombres, vistos desde Backend/Frontend Web).

   → Los tres bundles (AC, BA, BW) repiten los mismos 7 nombres de contrato (Disponibilidad Query API,
   Servicios Query API, Profesionales Query API, Historial de conversación Query, Crear/Actualizar/Cancelar
   Reserva Command API) sin que el canvas declare si es **un solo contrato compartido** o **tres implementaciones
   independientes**. Esa decisión de diseño no puede tomarse en `/speckit.plan` sin resolver esta duda primero.

## Bloque 3 — Contrato, esquema y comportamiento de error de las integraciones de frontera (bloquea diseño de adapters en `/speckit.plan`)

16. `INT-1` entrada desde mensajería conversacional externa.
17. `INT-2` entrada desde procesamiento conversacional externo.
18. `INT-3` entrada desde geolocalización externa.
19. `INT-4` salida hacia mensajería conversacional externa.
20. `INT-5` salida hacia procesamiento conversacional externo.
21. `FR-SCC-001` / `FR-SCC-002` (equivalentes a INT-1/INT-4 en la frontera de usuario).
22. `FR-SCC-003` "SMS".
23. `FR-SCC-004` "Email".
24. `FR-SCC-005` "interfaz web" (el propio post-it original dice "falta interfaz web": ni siquiera hay nombre
    de interfaz declarado).
25. `FR-SCC-006` "Command Request" (entrada de sistema).
26. `FR-SCC-007` "Command Endpoints" (entrada de sistema).
27. `FR-SCC-008` "Command Request" (salida de sistema).
28. `FR-SCC-009` "File System" (entrada de dispositivo).
29. `FR-SCC-010` "Cámara del Dispositivo".
30. `FR-SCC-011` "Pantalla del dispositivo".
31. `FR-SCC-012` "Monitor PC".

## Bloque 4 — Permisos por rol (bloquea el modelo de autorización en `/speckit.plan`; ambigüedad presente en el texto pero SIN la marca `[NEEDS CLARIFICATION]`)

32. Perfil "Administrador de la operación": permisos no declarados.
33. Perfil "Coordinador de agenda": permisos no declarados.
34. Perfil "Prestador del servicio": permisos no declarados.
35. Perfil "Solicitante de reserva": permisos no declarados.

   → `composed/prompt_specify.md` §Perfiles de usuario declara los 4 roles y dice literalmente "permisos no
   declarados" para cada uno, pero el compositor no les puso la marca `[NEEDS CLARIFICATION]`. Se incluyen aquí
   porque el propio contrato del skill de auditoría nombra "permisos por rol" como categoría de alto impacto, y
   dejarlos fuera de este insumo los volvería invisibles para `/speckit.clarify`.

## Bloque 5 — Métricas de éxito (bloquea la definición de "hecho" antes de `/speckit.plan`)

36. `CE-1` "Reducir tiempo de respuesta al cliente": ¿medido cómo? ¿métrica y línea base?
37. `CE-2` "Incrementar conversión de consultas en reservas": ídem.
38. `CE-3` "Recuperar automáticamente horas canceladas": ídem.
39. `CE-4` "Reducir inasistencias mediante recordatorios automáticos": ídem.
40. `CE-5` "Mantener sincronizada la agenda del centro": ídem.
41. `CE-6` "Reducir los no-shows": ídem.
42. `CE-7` "Centralizar la gestión de reservas": ídem.

## Bloque 6 — Umbral y criterio verificable de calidad técnica (impacto medio: informa presupuestos de NFR en `/speckit.plan`, pero no bloquea la estructura del plan)

43. `NFR-TEC-1` "Alta disponibilidad": criterio verificable y umbral no declarados.
44. `NFR-TEC-2` "Escalabilidad": ídem.
45. `NFR-TEC-3` "Seguridad": ídem.
46. `NFR-TEC-4` "Integrabilidad": ídem.
47. `NFR-TEC-5` "Baja latencia conversacional": ídem.
48. `NFR-TEC-6` "Mantenibilidad": ídem.

## Bloque 7 — Operación y despliegue (impacto medio-bajo: afecta runbook, no arquitectura)

49. `NFR-OP-1` "Production": entornos de prueba, integración o preproducción no declarados.
50. `NFR-OP-2` "Deploy manual coordinado por Área de Sistemas": pasos documentados, aprobaciones, reversión y
    evidencias de instalación no declarados.
51. `NFR-OP-3` "Alta disponibilidad de servicio": objetivo, ventana de medición y exclusiones no declarados.

## Bloque 8 — Ambigüedades adicionales sin marca formal (impacto bajo; informativas, no bloquean `/speckit.plan` de inmediato)

52. Entidades con "atributos abiertos" (Cliente, Profesional, Local, Disponibilidad, Historial de atención,
    Servicio, Agenda, Reserva, Preferencias del cliente) y "atributos por confirmar" (Conversación, Mensaje,
    Contexto, Intención, Prompt, Estado Conversacional, Ficha clientes, Disponibilidad Agenda, Catálogo de
    servicios, Profesionales y especialidades, Historial Conversación, Reglas de negocio, Configuración
    conversacional, Multimedia Web): ningún atributo concreto está declarado para ninguna de las 21 entidades.
53. Escenarios de negocio `EN-01`…`EN-08` (explícitamente marcados "no son FR"): actor, precondición y resultado
    observable "por confirmar" en los 8 casos.
54. Discrepancia de censo de bundles entre Structural (10), Deployment (5) y Functional (3 canvases
    documentados) — ya señalada por el compositor en `plan_input.md`, no resuelta.
55. Ausencia total de: procedimiento de respaldo/backup, monitoreo operativo (solo aparece como principio
    técnico "Observabilidad mediante logging y monitoreo", sin NFR observable), responsable/procedimiento de
    operación más allá del deploy manual, y accesibilidad — ninguno de los 4 aparece en ningún canvas.

---

Total de preguntas numeradas: **55** (agrupan las 72 marcas `[NEEDS CLARIFICATION]` de `prompt_specify.md`,
ya que varias comparten exactamente el mismo texto de duda y bloque temático, más 4 preguntas del Bloque 4 y 4
observaciones agregadas del Bloque 8).
