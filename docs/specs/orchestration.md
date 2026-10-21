# Orquestación SDD de IoTArg

## Fuente confirmada

El usuario indicó [nicovon24/harness-nicovon24](https://github.com/nicovon24/harness-nicovon24) como referencia de su orquestación.

- Commit inspeccionado: `da43b1f00426606088de2b8afff59671a9c6f639`.
- Versión del paquete: `0.1.0-alpha.3`.
- Evidencia: `git ls-remote ... HEAD` y `git rev-parse HEAD` del clon temporal coinciden.
- Se leyó el código en una carpeta temporal; no se instaló el harness ni se ejecutaron sus workflows en IoTArg.

Referencias versionadas:

- [README e instalación](https://github.com/nicovon24/harness-nicovon24/blob/da43b1f00426606088de2b8afff59671a9c6f639/README.md).
- [Defaults](https://github.com/nicovon24/harness-nicovon24/blob/da43b1f00426606088de2b8afff59671a9c6f639/config/defaults.json).
- [Modelos Codex](https://github.com/nicovon24/harness-nicovon24/blob/da43b1f00426606088de2b8afff59671a9c6f639/adapters/codex/models.json).
- [Workflow builtin](https://github.com/nicovon24/harness-nicovon24/blob/da43b1f00426606088de2b8afff59671a9c6f639/workflows/builtin.md).
- [Compatibilidad declarada](https://github.com/nicovon24/harness-nicovon24/blob/da43b1f00426606088de2b8afff59671a9c6f639/docs/compatibility.md).

## Configuración declarada por el harness

| Rol | Perfil | Modelo solicitado por adaptador Codex | Esfuerzo por defecto |
| --- | --- | --- | --- |
| Coordinador | astra | `gpt-6-astra` | medium |
| Investigador | luna | `gpt-6-luna` | high |
| Implementador | sol | `gpt-6-sol` | medium |
| Reviewer | sol | `gpt-6-sol` | high |

Existen overrides por clasificación: inventario simple usa investigador medium, implementación compleja usa implementador high y arquitectura ambigua usa coordinador high. No hay fallback implícito permitido. La skill SDD invocada en esta entrega pide investigador high, que es lo solicitado a los perfiles nativos.

Política declarada: modo `auto`, máximo 2 subagentes, 2 rondas de corrección y 8 delegaciones; timeouts de 20 minutos por agente y 60 por run; testing `standard`, spec `proportional`, revisión `risk-based`; escritor exclusivo por checkout/feature, scope local al host y sin delegación recursiva.

Estos valores no demuestran enforcement en la conversación. El harness no controla herramientas que ignoren sus locks. Los perfiles del cliente y el modelo efectivo deben comprobarse por separado.

## Claude y Codex: estado comprobado

| Elemento | Observación |
| --- | --- |
| Configuración local Claude | `~/.claude/CLAUDE.md` contiene preferencia de idioma; no se encontraron agentes en `~/.claude/agents` ni `~/.claude/skills/sdd` |
| Preferencias de modelo Claude | Ajustes locales inspeccionados indican `opus`, esfuerzo global `medium` y una preferencia específica `high`; no constituyen roles SDD ni prueba de ejecución |
| Configuración de proyecto Claude | IoTArg no tiene `.claude/` |
| Instalador del harness | El código inspeccionado admite `--runtime codex` y copia recursos a `.agents/` con `--apply` |
| Soporte Claude del harness | Su tabla de compatibilidad lo registra pendiente; no hay adaptador Claude verificado en este checkout |
| Codex local | Skill SDD disponible y perfiles nativos usados por el runtime de esta conversación |
| Instalación de harness en IoTArg | No existen manifiesto, CLI instalada, runs o locks del harness |

Esto describe solo las fuentes inspeccionadas. No invalida una configuración de Claude existente en otro entorno ni certifica compatibilidad por similitud de archivos.

## Adaptación a `docs/specs/`

La skill SDD local sugiere `docs/features/<slug>/`. El harness `h-spec` prescribe `harness/features/<slug>/`. El usuario eligió `docs/specs/`; esa elección prevalece para los documentos de IoTArg.

Hay una incompatibilidad técnica concreta: [src/snapshot.mjs](https://github.com/nicovon24/harness-nicovon24/blob/da43b1f00426606088de2b8afff59671a9c6f639/src/snapshot.mjs), líneas 34 y 47, construye la ruta `harness/features/<feature>/requirements.md`. No basta cambiar instrucciones o `references.roadmap` del manifiesto: los snapshots y revisiones seguirían buscando esa aceptación.

Propuesta antes de activar la CLI:

1. Añadir al harness soporte explícito y validado para la ubicación canónica de aceptación, con pruebas de snapshot y vigencia de revisión.
2. Configurar IoTArg para que su aceptación resuelva a `docs/specs/requirements.md` y sus referencias a `docs/specs/tasks.md`.
3. Verificar que editar aceptación invalide la revisión y que un cambio de código invalide los checks pertinentes.
4. Mantener una sola fuente editable; no copiar requisitos a otra carpeta para aparentar compatibilidad.

Esta mejora del harness es trabajo futuro en otro repositorio. No se modificó ese repositorio en esta entrega ni se presenta una clave de configuración inventada como soportada.

## Flujo aplicado en esta entrega

Se utiliza la skill `$sdd` de Codex y sus herramientas de agentes reales:

1. El coordinador crea alcance, IDs y contratos compartidos.
2. Dos investigadores trabajan en lectura sobre fuentes independientes.
3. El coordinador integra y escribe los documentos.
4. Un reviewer en contexto nuevo contrasta aceptación, documentos y evidencia.
5. Se corrigen hallazgos y se registran checks y próximo paso.

En la entrega documental inicial, el coordinador fue el único escritor. En el primer corte visual posterior, un solo implementador recibió propiedad del HTML y `designs/map-data/`; el coordinador mantuvo documentos y fuentes. No hubo escritores simultáneos del HTML. No se atribuyen a esta ejecución locks, checkpoints o límites automáticos del harness externo.

## Registro de delegación de esta entrega

| Tarea / agente | Perfil solicitado | Modelo / esfuerzo pedidos | Evidencia del runtime |
| --- | --- | --- | --- |
| DOC-01 `/root/inventory` | `sdd_researcher` | `gpt-6-luna` / high | `spawn_agent` devolvió ese task path y se recibió entrega |
| DOC-02 `/root/orchestration` | `sdd_researcher` | `gpt-6-luna` / high | Creación, entrega inicial y entrega posterior a `followup_task` |
| DOC-04 `/root/spec_review` | `sdd_reviewer` | `gpt-6-sol` / high | Resultado y estado en `review.md` |

La definición nativa de los perfiles declara esos modelos/esfuerzos. Los recibos de creación usados aquí devuelven `task_name`, sin un campo independiente que certifique el modelo efectivo; por eso se registra como solicitado, no como comprobado mediante telemetría de ejecución. No se infiere el modelo del coordinador desde el archivo de defaults.

## Preferencia del usuario para Spec 01

El 2026-10-20 el usuario pidió **Astra xhigh para planificar y orquestar**, otros modelos para el resto y **Sol high para implementar**. Esta preferencia prevalece sobre los defaults anteriores para esta fase.

- Planificación: se creó `/root/astra_plan` con `model: gpt-6-astra`, `reasoning_effort: xhigh`, contexto nuevo. Se recibió su propuesta y aceptación.
- Assessment A: `/root/visual_review_a`, agente independiente con perfil heredado; no se atribuye un modelo efectivo no informado.
- Assessment B: `/root/orchestration`, perfil investigador Luna high, reutilizado para detector y navegador sin acceso a la valoración A; entregó después de finalizar A.
- Revisión del plan: `/root/plan_review`, perfil `sdd_reviewer` (Sol high), contexto nuevo y solo lectura; encontró dos ajustes menores sobre escritor de correcciones y aceptación 2D/3D, incorporados por el coordinador.
- Primer corte cartográfico: `/root/map_slice_plan` solicitó `gpt-6-astra` / xhigh para delimitar el mapa; `/root/map_implementer` solicitó `gpt-6-sol` / high como escritor exclusivo de `designs/IoTArg.html` y `designs/map-data/`. La investigación de fuente Georef usó `/root/orchestration` (Luna high). `/root/spec_review` releyó el primer corte y aprobó la corrección de sus tres hallazgos P1/P2 en una segunda pasada solo lectura. El coordinador ejecutó las pruebas de navegador y actualizó documentos.

Esto registra solicitudes y entregas reales de agentes. No cambia automáticamente el modelo del hilo principal ni instala el harness. Los recibos no incluyen telemetría independiente de modelo efectivo. La propuesta y el reparto están en [Spec 01](subspecs/01-initial-design.md).

## Procedimiento futuro de instalación

Pendiente de OPS-00 y OPS-01 en [tasks.md](tasks.md). Requiere Node.js 22+ según el harness y un proyecto versionado para verificar snapshots con Git.

Una vez resuelta la ruta de aceptación: preparar dependencias en un checkout del harness, inicializar el manifiesto de proyecto, validar, inspeccionar preview de instalación Codex y aplicar. Después ejecutar `doctor`, `config`, `runs --verify` y `memory-render` mediante la CLI instalada.

Un run implementado usa `begin`, `checkpoint`, `review-record`, `review-status` y `end`, con IDs y tokens devueltos realmente. No inventar esos valores. La independencia de un reviewer se demuestra con la sesión del runtime, además de lo declarado al harness.

## Continuidad

Hoy la continuidad durable está en `docs/specs/`. Al retomar, leer requisitos, tareas y [revisión del primer corte](review.md); comprobar el estado Git y si el harness fue activado después. Git local está inicializado, todavía sin commit; el harness sigue pendiente.

Si se instala el harness, `MEMORY.md` y `harness/.local/` son cache y registros locales excluidos de Git; las decisiones se guardan primero en documentos durables. El compositor limita la cache a cinco días activos, 150 líneas y 8192 bytes. Supermemory permanece como piloto opcional explícito y no fue utilizado aquí.

## Spec 02 — orquestación observada, 2026-10-20

El usuario pidió SDD y modelos por rol para el nuevo subspec. La sesión principal coordinó y escribió la documentación; el runtime no expuso al coordinador un identificador de variante/esfuerzo, así que **Astra medium no está verificado** para esta sesión. No se creó un subagente orquestador.

| Tarea / agente | Modelo y esfuerzo solicitados | Evidencia observada |
| --- | --- | --- |
| Investigación `/root/sdd_reference_audit` | Perfil `sdd_researcher`: `gpt-6-luna` high | `spawn_agent` devolvió task path; se recibió inventario y `FINAL_ANSWER` de lectura. |
| Revisión `/root/sdd_spec_review_02` | Perfil `sdd_reviewer`: `gpt-6-sol` high | `spawn_agent` devolvió task path; se recibió veredicto con tres hallazgos; `followup_task` pidió revalidación y llegó aprobación final. |

La respuesta de creación no incluye telemetría que pruebe el modelo efectivo. Sol medium/high para implementar OPA-A/B/C es una asignación futura en `tasks.md`, no un agente creado en esta entrega. [Detalle de hallazgos](review.md).

## Spec 02 — planificación revisión 2, 2026-10-20

El usuario aprobó implementar Spec 02 y pidió bajar la planificación de Astra de xhigh a medium. La ejecución se divide en cortes OPA-BASE → OPA-A1 → OPA-B → OPA-C → OPA-A2 → OPA-QA. Un único Sol high escribe `designs/IoTArg.html` por corte; el coordinador actualiza documentación y commits, con revisión Sol independiente antes de cerrar cada corte. La conexión ThingsBoard queda fuera de esta implementación.

| Agente | Perfil / modelo solicitado | Evidencia del runtime |
| --- | --- | --- |
| `/root/inventory_admin_gap_v2` | `sdd_researcher`, Luna high | `spawn_agent` devolvió task path; entrega y `FINAL_ANSWER` recibidos con riesgos del HTML y orden de normalización. |
| `/root/spec02_v2_plan_review` | `sdd_reviewer`, Sol high | `spawn_agent` con contexto nuevo devolvió task path; se recibió revisión con hallazgos, después `followup_task` y aprobación documental de correcciones. |
| `/root/astra_medium_execution_plan` | Astra medium | Secuencia, puertas de aceptación y riesgos de OPA-BASE entregados; sin cambios en archivos. |
| `/root/luna_prototype_inventory` | Luna high | Inventario de símbolos y acoplamientos en el HTML entregado; sin cambios en archivos. |
| `/root/sol_base_admin_implementation` | Sol high | Implementó OPA-BASE: catálogo/relaciones, lecturas, persistencia y compatibilidad del mapa. |
| `/root/review_opa_base` | Sol high, revisión independiente | Dos rondas estáticas; hallazgos resueltos y OPA-BASE aprobable. No ejecutó pruebas. |
| `/root/sol_base_admin_implementation` | Sol high | Implementó OPA-A1: cuatro tablas de Inventario, filtros, accesos contextuales y hash; corrigió hallazgos de revisión. |
| `/root/review_opa_base` | Sol high, revisión independiente | Revisión estática OPA-A1: dos hallazgos resueltos; corte aprobado. No ejecutó pruebas. |
| `/root/sol_base_admin_implementation` | Sol high | Implementó OPA-B: Administración con Estructura y Contenido, árbol, subárbol y estados vacíos. |
| `/root/review_opa_base` | Sol high, revisión independiente | Revisión estática OPA-B: sin hallazgos P1/P2; corte aprobado. |

Los modelos indicados reflejan las asignaciones solicitadas a `spawn_agent`; la herramienta no expone telemetría para verificar de forma independiente el modelo efectivo. No se cambia configuración del harness.

## Spec 02 — revisión 3, Administración y Soluciones, 2026-10-21

El usuario pidió planificar con Astra medium antes de continuar y priorizó Administración visual y Soluciones sobre formularios. `/root/astra_medium_admin_solutions_plan` recibió `gpt-6-astra` con esfuerzo `medium` y entregó la secuencia A2 → B2 → S0 → S1 → S2 → S3 → QA de lectura; no editó archivos. El coordinador contrastó [AirportIQ](https://senzary.com/solutions/airportiq/) y [RotaryIQ](https://senzary.com/solutions/rotaryiq/) en el sitio oficial de Senzary para usar su jerarquía informativa como inspiración, sin atribuir sus capacidades a los datos de IoTArg.

El coordinador actualiza Spec 02 revisión 3 y tareas antes de pedir cambios de HTML. Después asigna un único escritor Sol high por corte B2/S0–S3 y una revisión independiente de cada entrega. Cada corte se publica en un commit propio. OPA-C, QA de mutaciones y conexión ThingsBoard quedan pendientes por decisión del usuario.
