# Insumo para /speckit.checklist

| ID | Verificación | Estado | Evidencia |
|---|---|---|---|
| CHK-01 | Cobertura C=1,00 | **PASS** | 363/363 |
| CHK-02 | Exactamente una traza por post-it | **PASS** | huérfanos=0, duplicados=0 |
| CHK-03 | Destino no vacío en toda traza | **PASS** | cubiertas=363 |
| CHK-04 | Texto, canvas y sección del anexo coinciden con COM | **PASS** | discrepancias=0 |
| CHK-05 | Contaminación técnica T=0 | **PASS** | T=0 |
| CHK-06 | Forma canónica en todos los FR | **PASS** | fallos=0 |
| CHK-07 | Sin gestionar/manejar/soportar sin objeto | **PASS** | fallos=0 |
| CHK-08 | Escenario Dado/Cuando/Entonces en todo FR | **PASS** | 149/149 |
| CHK-09 | Traza ← inline en todo FR | **PASS** | fallos=0 |
| CHK-10 | Traza ← inline en todo NFR, CE y R | **FAIL** | fallos=13 |
| CHK-11 | Prefijo de bundle en FR funcionales | **PASS** | FR funcionales=131 |
| CHK-12 | Sin colisiones de identificadores de requisito | **PASS** | IDs=177 |
| CHK-13 | Destinos id_req del anexo existen en los prompts | **PASS** | ausentes=0 |
| CHK-14 | Chequeo Structural↔Functional reportado | **PASS** | Structural=10, Functional=3 |
| CHK-15 | Chequeo Structural↔Deployment reportado | **PASS** | Structural=10, Deployment=5 |
| CHK-16 | Ausencias esperables señaladas | **PASS** | respaldo, accesibilidad |
| CHK-17 | Idempotencia contra auditoría previa | **N/A** | La corrida anterior no persistió una lista completa de FR para comparación exacta |
| CHK-18 | Prueba de sanidad: borrar una traza causa rechazo | **PASS** | C_sanidad=0,997 |
| CHK-19 | Delivery ID consistente entre composición y COM | **FAIL** | specify/constitution=`arquitectura-para-sistema-de-reservas-inteligente`; trace_annex/IDs COM=`arquitectura-para-sistema-de-reservas-con-agente-inteligente-llm` |

## Detalle de fallos

- CHK-10: CE-1, CE-2, CE-3, CE-4, CE-5, CE-6, CE-7, NFR-TEC-1, NFR-TEC-2, NFR-TEC-3, NFR-TEC-4, NFR-TEC-5, NFR-TEC-6.
- CHK-19: `prompt_specify` y `prompt_constitution` usan el ID actualizado, mientras `trace_annex` y los COM preservan el ID original de evidencia.
- El chequeo de idempotencia queda N/A porque la corrida anterior no persistió una lista completa de FR; no se infiere un resultado a partir del conteo.
