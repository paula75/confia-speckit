# Auditoría arquitectura-para-sistema-de-reservas-inteligente

| Canvas | Post-it | Trazas | Dudas inline |
|---|---:|---:|---:|
| `business_context` | 51 | 51 | 0 |
| `architectural_context` | 59 | 59 | 13 |
| `system_context` | 31 | 31 | 17 |
| `structural` | 30 | 30 | 0 |
| `functional` | 170 | 170 | 39 |
| `deployment` | 22 | 22 | 3 |
| **Total** | **363** | **363** | **72** |

C = 363/363 = 1,000 → ok
A = 72/177 = 0,407
T = 0 (lista negra desde COM: `WhatsApp Business`, `WhatsApp`, `PostgreSQL`, `MongoDB`, `Docker`, `LLM`, `Meta Business Suite`, `Python`, `Javascript`, `Nginx`, `Node.js`, `cPython`, `Linux`, `GCP`, `Cloud run`, `Cloud Sql`, `Cloud Function`, `Object Storage`) → ok
V = 149/149 = 1,000

## Veredicto

**VÁLIDA** — C = 1,000 y T = 0.

## Motivos y hallazgos

- Contaminación técnica: no se detectaron términos de la lista negra en `prompt_specify`; el cambio del Delivery ID eliminó la detección anterior de `LLM`.
- Cobertura atómica recuperada: 363 post-it con exactamente una traza coincidente y destino no vacío; huérfanos=0, duplicados=0, IDs desconocidos=0 y discrepancias literales=0.
- Inconsistencia de encabezados: `prompt_specify` y `prompt_constitution` declaran `arquitectura-para-sistema-de-reservas-inteligente`; `trace_annex` y los IDs de los COM conservan `arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm`. Los `post_it_id` originales son correctos y no se modifican.
- Verificabilidad: 149/149 FR contienen escenario con Dado/Cuando/Entonces.
- Trazas inline faltantes: 0 FR y 13 NFR/CE/R. Afectados: CE-1, CE-2, CE-3, CE-4, CE-5, CE-6, CE-7, NFR-TEC-1, NFR-TEC-2, NFR-TEC-3, NFR-TEC-4, NFR-TEC-5, NFR-TEC-6.
- Consistencia anexo→prompt recuperada: los 29 identificadores anteriormente ausentes existen nuevamente; destinos `id_req` ausentes=0.
- Censo cruzado: Structural=10, Functional=3, Deployment=5; las correspondencias literales están incompletas.
- Structural sin correspondencia literal en Functional: Pagina web admin locales; Backend / Agente conversacional y de reservas; Backend agendamiento (multi-tenant); Backend / Pagina web admin locales (multi-tenant); PostgreSQL; Storage; MongoDB; Docker; Servicio LLM; whatsapp business.
- Functional sin correspondencia literal en Structural: Agente conversacional; Backend Agendamiento; Backend/Frontend Web.
- Structural sin correspondencia literal en Deployment: Pagina web admin locales; Backend / Agente conversacional y de reservas; Backend agendamiento (multi-tenant); Backend / Pagina web admin locales (multi-tenant); PostgreSQL; MongoDB; Docker; Servicio LLM; whatsapp business.
- Deployment sin correspondencia literal en Structural: Portal web pymes; Backend/ Sitio web; Backend/ Agendamiento; Base de Datos (PostgreSQL).
- Ausencias esperables detectadas: respaldo, accesibilidad.
- Prueba de sanidad del auditor: PASÓ; al retirar una fila de la composición actual en memoria C=362/363=0,997 y la corrida fue rechazada.

## Lectura del resultado

La composición recuperó cobertura total, mantiene contaminación técnica cero y ya no tiene destinos del anexo ausentes. Los FR conservan sus escenarios. Permanecen dudas de métricas, umbrales, contratos y periodicidades, además de 13 fallos de trazas inline; la auditoría no los corrige ni los resuelve.
