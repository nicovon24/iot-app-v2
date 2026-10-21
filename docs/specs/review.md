# Revisión de la especificación

## Alcance

Aceptación: REQ-001 a REQ-008 en [requirements.md](requirements.md).

Archivos: `README.md`, `PRODUCT.md`, `DESIGN.md` y `docs/specs/*.md`.

Fuentes: HTML original y harness `da43b1f00426606088de2b8afff59671a9c6f639`. La carpeta IoTArg no es un repositorio Git; no se declara diff, rama ni commit local.

## Revisión independiente

- Agente creado: `/root/spec_review`, perfil nativo `sdd_reviewer`, contexto nuevo.
- Modelo/esfuerzo solicitados: `gpt-6-sol` / high.
- Datos reportados: `spawn_agent` devolvió `task_name: /root/spec_review`; se recibió entrega y veredicto. No se reportó modelo efectivo como campo separado.
- Veredicto inicial: requiere cambios menores. Veredicto final tras ronda 1: **aprobado**, sin hallazgos pendientes en las partes afectadas.
- Hallazgo R-01, precisión factual: README decía que los reconocimientos duraban la sesión; además `data.md` generalizaba el borrado a todo cambio de escenario. Se aclaró memoria hasta recarga y diferencia entre botón y `popstate`; se agregó OBS-08 y pendiente en IMP-05.
- Hallazgo R-02, precisión factual: README afirmaba que la serie offline terminaba en la última lectura disponible, pese al límite inclusivo en minuto 12 y etiqueta calculada actual. Se corrigió la descripción del README; DATA-004 conserva la corrección funcional pendiente.
- El reviewer confirmó las correcciones en lectura y aclaró que su revisión fue exclusivamente estática, sin navegador ni pruebas dinámicas. Las dos entregas constan en la conversación de `/root/spec_review`.

## Comprobaciones

- Inspección estática del prototipo y configuración/harness por investigadores.
- Integración verificó el botón estático Metodología, descartando un falso positivo.
- Hash inicial HTML: `D55DCCA186D0B159A8A074B6E56ECB591203932C4E031D51D58C010AFCC47C8E`.
- Comprobación ejecutada mediante Python estándar (`py -3 -`, script inline): leyó 12 Markdown, resolvió 32 enlaces locales, comprobó 37 IDs de requisito definidos y comparó SHA-256 del HTML. Resultado: `errors: []`, exit code 0.
- Repetida después de las correcciones R-01/R-02: 12 archivos, 32 enlaces, 37 IDs, `html_unchanged: true`, `errors: []`, exit code 0.
- Hash del HTML después de redactar: coincide con el inicial; contenido preservado.
- En la entrega documental inicial no se ejecutaron pruebas visuales, de navegador ni de aplicación. La revisión posterior de Spec 01 se registra abajo.
- No se ejecutaron instalación, tests ni workflows del harness. Su compatibilidad se documenta como evidencia de código y de su propia tabla.

## Vigencia

Cualquier cambio posterior de aceptación o contenido técnico pertinente exige revisar de nuevo la parte afectada. Actualizar estados y registrar resultados de la revisión no cambia el contrato de producto.

## Cierre

REQ-001 a REQ-008 cubiertos en la entrega documental inicial. Esa revisión aprueba la documentación y su evidencia, no certifica el funcionamiento de la maqueta ni instala el harness.

## Revisión visual posterior — 2026-10-20

- Target: HTML en raíz, antes de traslado o rediseño.
- Assessment A: `/root/visual_review_a`, criterio visual independiente, capturas de overview/ubicación/sensor en escritorio y móvil; ambos temas muestreados. Evaluación 23/40.
- Assessment B: `/root/orchestration`, detector estático ejecutado una vez, overlay y navegación en sesión aislada. El coordinador recibió sus hallazgos después de cerrar A.
- Coordinador: inspección overview claro/oscuro, capturas y verificación de `THREE.REVISION === "160"` y mapa inicializado en navegador.
- Entorno: Chromium headless; escritorio 1440×900 y móvil 390×844. No certifica rendimiento en GPU física ni completa V-01 a V-07.
- Se observó bloqueo del click de Córdoba por superposición, contradicción de estado por activo, falta de umbral crítico visible y problemas de lectura/controles móviles.
- Detector: 24 coincidencias estáticas con `line: 0`; overlay: 72 coincidencias del DOM. No se suman ni sustituyen inspección humana.
- Recarga de localhost con modo offline falló con error de red; no se considera prueba del HTML local ni del fallback sin WebGL.
- [Crítica y capturas](../../designs/evidence/critique-2026-10-20.md), [informe B](../../designs/evidence/review-b/assessment-b.md), [Spec 01](subspecs/01-initial-design.md).
- Astra xhigh fue solicitado para planificar; recibida propuesta e integrada en Spec 01. La implementación queda pendiente.
- Preferencias confirmadas por el usuario: mapa estilizado con instalación industrial esquemática, y condición destacada para investigar.
- Comprobación documental posterior: 15 Markdown, 68 enlaces locales, `errors: []`; SHA-256 del HTML idéntico al inicial. No se modificaron el HTML ni el README raíz en esta revisión.
- Sesiones de navegador cerradas; B detuvo su servidor de overlay de puerto 8400 y el coordinador detuvo el servidor local 8766 al finalizar la inspección.
- Crítica persistida en `.impeccable/critique/2026-10-20T17-46-37Z__iotarg-html.md`, con huella del HTML. Primera ejecución del target: 23/40, sin tendencia histórica. Archivo temporal eliminado.
- Revisión documental de Spec 01 por `/root/plan_review`, perfil `sdd_reviewer` (Sol high), contexto nuevo: aprobada con dos ajustes menores. P2: asignar las correcciones del HTML al implementador y posterior revalidación; P3: concretar aceptación de 2D cenital/plano frente a 3D inclinado/volumétrico. Ambos ajustes incorporados y su resolución confirmada por el reviewer en relectura. Este señaló además una atribución ambigua de elección de 2D al usuario; el coordinador sustituyó la frase por «El modo 2D puede usar el renderer existente». Revisión exclusivamente documental.

IMP-03 cubre el diagnóstico inicial; el siguiente trabajo de implementación empieza por IMP-01/IMP-02. La aprobación documental inicial no se extiende automáticamente a la propuesta nueva ni a la maqueta.

## Comparación cartográfica posterior — capturas aportadas por el usuario

- Se inspeccionaron dos capturas de [Municipios Argentinos](../../designs/evidence/reference/README.md) y la captura de [IoTArg actual](../../designs/evidence/review-a/overview-desktop.png).
- Diferencias comprobables en esas imágenes: visor territorial casi a pantalla completa frente a mapa en tarjeta bajo KPI; extrusiones, laterales y límites muy visibles frente a relieve tenue; provincias y subdivisiones al acercarse frente a países únicamente; etiquetas de punto frente a pines rectangulares superpuestos; leyenda de altura explícita frente a relieve sin escala de dato.
- La referencia no demuestra su tecnología, rendimiento, comportamiento móvil o animaciones. La similitud futura se validará con capturas de IoTArg en el mismo tamaño y dos niveles de zoom.
- Spec 01 agrega VIS-011 a VIS-015 e IMP-10 para geodatos. La cartografía provincial, foco URL y visualización de altura están **propuestos**, aún no implementados.
- Relectura independiente por `/root/plan_review` (Sol high, solo lectura) encontró una contradicción menor entre VIS-012 («volumen») y VIS-008 (2D plano). VIS-012 ahora exige límites/selección en ambos modos y volumen únicamente en 3D. No se observaron otros conflictos en foco, capas o dependencias.

## Primer corte implementado del mapa mundial — 2026-10-20

- Archivo editable: [designs/IoTArg.html](../../designs/IoTArg.html), con [cartografía mundial](cartography.md) y los assets de `designs/map-data/`. Git local inicializado; no hay commit ni publicación.
- Las fuentes descargadas se validaron como `FeatureCollection` WGS84: Natural Earth 50m países (242 entidades), Natural Earth 10m admin 1 (4.596 divisiones fuente) y Georef Argentina (24). El asset de entrega contiene 4.556 divisiones Natural Earth para 239 países y la maqueta agrega 24 de Argentina: 240 países con detalle administrativo.
- QA del coordinador en Chrome headless: [Mundo 1440×900](../../designs/evidence/implementation-map/world-1440.png), [Argentina 1440×900](../../designs/evidence/implementation-map/argentina-1440.png), [Argentina móvil 390×844](../../designs/evidence/implementation-map/argentina-mobile-final.png). Se observó mapa visible, condición crítica, controles y lista; móvil sin scroll horizontal. Mundo y Argentina se recorrieron por selectores. Se probó apertura directa `file://` con el asset local cargado; consola sin errores de aplicación, con aviso de depreciación de Three r160.
- El primer parche de resize dejaba canvas vacío al cambiar viewport. Se reprodujo a 1264×768, se aisló con contexto WebGL válido y `renderer.render(scene,camera)` manual, y el implementador añadió render posterior al resize. Repetición 1264→1440 sin recargar: [mapa visible](../../designs/evidence/implementation-map/resize-fixed-1440.png).
- Fallback SVG comprobado al forzar `HTMLCanvasElement.getContext` a devolver `null` para WebGL. El primer intento no enfocaba Argentina porque una referencia al canvas eliminado abortaba `renderOverview`. Tras el parche, [Argentina y provincias se muestran centradas](../../designs/evidence/implementation-map/fallback-argentina-fixed.png). El error de creación de contexto en la consola es esperado bajo esa prueba; no hubo una excepción posterior de la aplicación.
- Revisión independiente solo lectura por `/root/spec_review` (perfil `sdd_reviewer`, Sol high solicitado): estructura de 242 países con IDs únicos, 4.556 admin 1 de 239 países sin IDs duplicados y Georef AR24 confirmada. Veredicto inicial: **requiere correcciones**. P1: cambiar de país por canvas/SVG con provincia seleccionada podía renderizar `state.geo` obsoleto. P2: tooltip de país omitía filtro de solución. P2: atribución Georef oculta en móvil.
- El implementador corrigió los tres hallazgos y probó Córdoba provincia → Chile por raycast y SVG, el tooltip con filtro Assets sin ubicaciones y el crédito móvil. El reviewer releyó el código y dio **aprobado** a los tres: el foco provincial se limpia antes de renderizar y también se valida defensivamente, el tooltip usa `scopedLocations()`, y la leyenda móvil muestra Natural Earth + Servicio Georef/IGN + CC BY 4.0. La [captura móvil final](../../designs/evidence/implementation-map/mobile-credit-final.png) muestra el crédito en `file://`; el coordinador verificó visualmente la leyenda y ausencia de error de carga local. La revalidación del reviewer fue estática.

La QA anterior comprueba el primer corte cartográfico, no el resto de VIS-001 a VIS-016, DATA-001 a DATA-007 ni V-01 a V-07. No se recorrieron visualmente los 240 países con admin 1 ni se midió rendimiento en dispositivos físicos. La exactitud de límites políticos corresponde a las fuentes declaradas; la simplificación por anillo es para demostración.

## Corte sudamericano y mapa protagonista — 2026-10-20

- [Spec 01](subspecs/01-initial-design.md) actualiza las sedes simuladas a Córdoba/AR, Santiago/CL, Lima/PE y Montevideo/UY, conservando 4 clientes, 4 ubicaciones, 8 activos y 16 sensores. El mundo sigue navegable; EE. UU. y México no tienen sensores. El selector País contiene solo Vista general + AR/CL/PE/UY.
- La Vista global usa un visor amplio, riel lateral compacto y controles operativos superpuestos. [Escritorio final 1440×900](../../designs/evidence/implementation-south-america/overview-1440-final.png): panel x80/y66, 1348×818 px según QA del coordinador. [Móvil final 390×844](../../designs/evidence/implementation-south-america/overview-390-final.png): cuatro pines visibles, `scrollWidth=390`, mapa antes del listado.
- Sol high implementó el orden de arranque: antes de revelar el panel dibuja el primer fotograma de Sudamérica centrado y cenital; después la cámara se inclina a la derecha en unos 1,3 s sin cambiar centro ni zoom. El estado de preparación ocupa el mismo panel. El implementador registró 82 cuadros: centro `{x:38,y:-33}` y zoom `2.1` estables en escritorio; cámara inicial `(38,-33,185)` y final `(73,-94,185)`. Un deep link a país/provincia abre su foco sin la entrada regional; el SVG alternativo se revela ya centrado.
- QA del coordinador en Chrome `file://`: a 390×844, `matchMedia('(prefers-reduced-motion: reduce)').matches=true` dio `introActive=false`, cámara final `(73,-94,185)` y panel listo. Tras ampliar el fit móvil, zoom regional `1.856`, cuatro centros pulsables, sin scroll horizontal. A 1440×900 y movimiento normal, panel listo, `introActive=false` tras completar la transición y 4/4 centros pulsables. El selector conservó `['', 'AR', 'CL', 'PE', 'UY']`.
- Revisión independiente Sol high, solo lectura: hallazgo inicial **P1** en móvil, Montevideo tapaba el centro pulsable de Córdoba tras carga limpia. El implementador corrigió el algoritmo de colisión y mantuvo posiciones estables durante la cámara. Revalidación independiente **aprobada**: 4/4 centros propios a 390×844 y 1440×900; sin intersecciones con controles ni entre pines, sin desplazamiento horizontal. La traza móvil de 152 fotogramas no mostró cambios de slot; Japón elegido desde el mundo conservó el selector de cuatro países, mostró su nombre en el alcance y cero ubicaciones.
- Sintaxis de los bloques JavaScript inline comprobada con `node --check` por el implementador. Checker de Markdown del coordinador tras registrar la revisión: 19 archivos, 119 enlaces locales, cero rutas faltantes.

La verificación cubre este corte y esos tamaños; no certifica rendimiento en GPU física, todos los países o los criterios pendientes de Spec 01 y del MVP posterior. La animación de la web de referencia no fue inspeccionada cuadro a cuadro: se implementó la secuencia descrita por el usuario.

## Entrada cenital con acercamiento — revisión posterior, 2026-10-20

El usuario sustituyó la inclinación inicial descrita arriba por un acercamiento con el mapa derecho. [Spec 01](subspecs/01-initial-design.md) y el HTML reflejan la decisión actual; la sección anterior conserva la evidencia del corte previo.

- Sol high implementó un primer fotograma centrado en Sudamérica con el 94 % del zoom final, un acercamiento de unos 900 ms, aparición de los cuatro marcadores en 280 ms y un pulso único de Córdoba de 700 ms. El botón 3D permite inclinar el mapa cuando se elige expresamente. El estado de preparación sigue dentro del mismo panel.
- [Escritorio 1440×900](../../designs/evidence/implementation-south-america/overview-1440-zoom-final.png) y [móvil 390×844](../../designs/evidence/implementation-south-america/overview-390-zoom-final.png) muestran el estado final derecho. QA del coordinador en Chrome `file://`: escritorio cámara `(38,-33,185)`, centro `{x:38,y:-33}`, zoom `2.1`, `is3D=false`; móvil la misma cámara, zoom `1.8559`, 4/4 centros de marcador pulsables y `scrollWidth=390`.
- Revisión independiente Sol high, solo lectura: **aprobado**. Una traza de escritorio de 142 muestras registró cámara X/Y constantes `(38,-33)`, zoom de `1.974` a `2.1` y 54 cuadros de entrada activa. En móvil el zoom fue de `1.7445` a `1.8559`; los cuatro marcadores siguieron pulsables. La cancelación por interacción llevó el zoom al estado final, reveló los marcadores y desactivó la entrada. El reviewer verificó por código que el pulso se aplica una vez a Córdoba y se retira.
- Movimiento reducido usa directamente el estado final, sin entrada ni animación CSS; los enlaces directos y el fallback SVG se abren en su propio foco. El implementador comprobó `node --check` de todos los scripts inline. El checker documental final resolvió 122 enlaces locales en 19 Markdown sin errores. La revisión independiente no filmó el pulso; su unicidad se sustenta en la secuencia de clases y temporizadores del código.

## Controles geográficos y resumen contextual — 2026-10-20

- **SA-12 a SA-15:** la barra ofrece Ver mundo, Ver Sudamérica, Centrar en mis datos y Quitar filtros junto a País/Provincia. Quitar limpia país y provincia y mantiene cliente, solución, capa y escenario. Centrar en mis datos calcula el encuadre de las ubicaciones del alcance y conserva `fit=data` en la URL; un alcance vacío conserva cámara y comunica que no hay sedes. El algoritmo busca el arco mínimo de longitudes y crea copias de país donde se necesita cruzar el antimeridiano.
- El tooltip de país, provincia y ubicación muestra nombre y datos del alcance. Salud separa sensores normales, en atención, críticos y sin señal; Dispositivos muestra total y conectividad; Cobertura muestra ubicaciones y sensores con datos. Los territorios vacíos indican Sin datos IoT. El contenido se construye como nodos de texto, sin interpolar nombres en HTML.
- QA del coordinador en Chrome `file://`: país Argentina → provincia Córdoba → Quitar filtros limpió ambos y dejó `#fit=data`; el visor encuadró las cuatro sedes. [Escritorio](../../designs/evidence/implementation-south-america/controls-fit-desktop.png) y [móvil final 390×844](../../designs/evidence/implementation-south-america/controls-fit-mobile-final.png) muestran los controles y cuatro marcadores. Córdoba en Salud reportó 4 sensores: 3 normales y 1 crítico en el minuto 28. Los cinco scripts inline pasaron `vm.Script`.
- La primera pasada detectó que el fit calculado en escritorio no se actualizaba al pasar a 390 px; el mapa dejaba Lima y Santiago fuera de vista. `resizeMap` ahora recalcula el fit y la repetición mostró los cuatro pines, `scrollWidth=390`. La revisión independiente encontró dos defectos del fallback SVG: Córdoba quedaba parcialmente tapada por Santiago y, tras resize, los pines retenían posiciones viejas. Se añadieron slots de etiquetas y recálculo SVG; a 390 px los cuatro centros quedaron pulsables y, al cambiar el panel de 368 a 498 px sin recarga, las posiciones coincidieron con sus puntos proyectados con error menor de 0,001 px.
- La misma revisión encontró que un país duplicado para el antimeridiano era enfocable pero no respondía a Enter/Espacio en SVG. Un manejador de teclado delegado lo corrigió. **Veredicto independiente: aprobado**, sin P1/P2 pendientes para SA-12 a SA-15. El cruce del antimeridiano se probó con sedes sintéticas en memoria y WebGL/SVG; el dataset persistido de la demo sigue limitado a cuatro países sudamericanos.

## Mapa derecho con relieve permanente — 2026-10-20

El usuario retiró la opción de inclinar o aplanar la vista. El botón 2D/3D y sus handlers se eliminaron; las mallas de países y provincias conservan extrusión con altura según Salud, Dispositivos y Cobertura. La cámara WebGL permanece perpendicular al mapa durante la carga, la entrada, el zoom y los cambios de encuadre. El SVG sigue siendo la alternativa automática sin WebGL.

- [Captura 1440×900](../../designs/evidence/implementation-south-america/upright-3d-1440.png): mapa derecho, cuatro marcadores y control de dimensión ausente. Implementador Sol high: Chrome escritorio/móvil, Mundo, Sudamérica, país, fit, enlace directo y SVG forzado; seis scripts pasaron comprobación de sintaxis. Móvil 390×844 sin scroll horizontal.
- Revisión independiente Sol high: **SA-16 aprobado**, sin P1/P2. En WebGL comprobó dirección de cámara perpendicular `[0,0,-1]` en carga, Mundo, Sudamérica, fit, Argentina, provincia y URL directa; las escalas de provincias cambiaron por capa. Con WebGL bloqueado verificó SVG y navegación. La QA dinámica del reviewer fue de escritorio; móvil y primer fotograma fueron inspección estática en esa ronda.
- La extrusión conserva datos y geometría, pero una vista estrictamente cenital muestra principalmente las caras superiores; no se inclina la cámara para hacer visibles los lados.

## Globo entre los controles del mapa — 2026-10-20

El usuario pidió un único botón Ver mundo con ícono de globo en el grupo inferior derecho y retiró los botones textuales Mundo/Sudamérica de la barra de País. El control de restablecer existente vuelve a Sudamérica. Centrar en mis datos, País/Provincia y Quitar filtros siguen en la barra geográfica.

- El implementador Sol high comprobó el click, el hash `extent=world`, `aria-pressed`, restablecer Sudamérica y la ausencia de superposición de los cuatro controles en escritorio y móvil. La sintaxis de los scripts inline pasó su comprobación.
- QA del coordinador a 390×844: [captura móvil](../../designs/evidence/implementation-south-america/globe-control-mobile-390.png), cuatro marcadores visibles, globo y restablecer pulsables, `scrollWidth=390`. El globo produjo `extent=world` y `aria-pressed=true`; restablecer limpió `extent`, devolvió `americas` y dejó `aria-pressed=false`. La barra ya no contiene botones Mundo/Sudamérica.

## Spec 02 — revisión documental, 2026-10-20

Aceptación examinada: OPA-001 a OPA-010 en [Spec 02](subspecs/02-operational-tables-admin.md), con índice, [tareas](tasks.md), [UX](ux.md) y [Spec 01](subspecs/01-initial-design.md). Código de referencia examinado en lectura: `designs/IoTArg.html` y `../iot_app`. No se evaluó implementación de OPA-A/B/C ni se ejecutó la maqueta en navegador para esta entrega.

- Investigador `/root/sdd_reference_audit`, perfil `sdd_researcher`, Luna high solicitado: confirmó que la maqueta usa datos estáticos y no tiene CRUD; en `iot_app` identificó ClientWizard, AdminAssetPanel, AdminDevicePanel, CreateUserDialog, DTOs, restricciones y diferencias de jerarquía. Entrega recibida en el runtime.
- Reviewer independiente `/root/sdd_spec_review_02`, perfil `sdd_reviewer`, Sol high solicitado: revisión solo lectura. Hallazgo P1: reproducción retirada pero VIS-009/010 y V-03 requerían controles/minutos. P2: diez secciones quedaba obsoleto con Administración. P2: desglose de accesos omitía «Sin datos».
- El coordinador corrigió los tres puntos: enlaces `scenario=offline&time=11/12/28` y textos de Escenarios como contrato, VIS-009/010 y UX-013, y desglose de entidades destino con «Sin datos» distinto de cero entidades. El mismo reviewer releyó las correcciones y devolvió **aprobado para OPA-DOC**. La revisión de implementación queda pendiente después de modificar el HTML.
- Comprobación local: script Python sobre los cinco documentos afectados, **0 enlaces locales rotos**. `git status --short --branch` reportó repositorio sin commits y archivos de proyecto sin seguimiento; no se hizo commit.

## Spec 02 — revisión 2: Estructura y Contenido, 2026-10-20

El usuario sustituyó la Administración como pendientes por dos tablas con CRUD y relaciones, agrupó las tablas operativas en Inventario y pidió revisar el plan antes de implementar. La aprobación anterior queda como evidencia de revisión 1; no cubre este nuevo alcance.

- Investigación solo lectura por `/root/inventory_admin_gap_v2`, perfil `sdd_researcher` (Luna high solicitado): confirmó falta de identidad de Área, ubicación duplicada en Device, arrays fijos, detalles dependientes de `ds[0]`, conteos fijos y ausencia de persistencia del catálogo. La normalización y tolerancia a entidades vacías preceden las pantallas.
- Reviewer en contexto nuevo `/root/spec02_v2_plan_review`, perfil `sdd_reviewer` (Sol high solicitado), examinó revisión 2 de Spec 02, tareas, índice y referencia de integración. P1: faltaba CTA para alta de Device con cliente vacío. P2: tarea QA no exigía ejecución dinámica después de formularios. Sugirió precisar secuencias válidas de niveles.
- Correcciones del coordinador: cabecera de Contenido con +Activo/+Dispositivo/Asignar, flujo sin asignación, recuperación de padre faltante, QA dinámica en OPA-QA, niveles y alcance administrativo explícitos. `followup_task` solicitó revalidación y se recibió **aprobado para presentar el plan al usuario**. Aprobación solo documental, sin pruebas de HTML.
- No se asignó implementador ni se editó `designs/IoTArg.html`. Las tareas Base/A/B/C, retiro del timeline y QA esperan confirmación del usuario sobre el plan. La matriz de verificación de Spec 02 define las comprobaciones futuras.

## Spec 02 — OPA-BASE, revisión estática, 2026-10-21

Sol high actualizó el catálogo de demo a relaciones con ID estable, lectores comunes, persistencia de sesión versionada, lecturas con procedencia y vistas tolerantes a entidades sin datos/ubicación. Astra medium recomendó conservar un solo escritor para el HTML y cerrar primero Base; Luna high localizó los acoplamientos del prototipo. La secuencia y aceptación se registran en [orchestration.md](orchestration.md) y [tasks.md](tasks.md).

- Primera revisión independiente Sol high: hallazgos sobre ubicación opcional, muestra incompatible con clave/unidad editada, escape de entradas, enlaces a IDs borrados y actualización del texto de pines.
- Segunda revisión: hallazgos anteriores resueltos; encontró además el pin 0,0 para coordenadas nulas en SVG y navegación a áreas sin ubicación.
- Revisión estática final: guardia de coordenadas y navegación de áreas sin ubicación corregidos; no se identificaron bloqueos restantes para OPA-BASE.
- Alcance aprobado estáticamente: modelo/versionado, compatibilidad de relaciones, vacíos y recuperación de enlaces. Alta/edición/borrado y movimientos pertenecen a OPA-C; la validación dinámica integrada queda para OPA-QA.
- No se ejecutaron pruebas ni se inspeccionó el resultado en navegador en este corte.

## Spec 02 — OPA-A1, revisión estática, 2026-10-21

Sol high implementó Inventario con vistas tabulares de Clientes, Ubicaciones, Activos y Dispositivos, accesos descendientes, filtros locales, orden, alcances contextuales y restauración de hash/historial.

- Revisión estática independiente Sol high encontró P1: abrir un detalle de otro cliente mantenía scopes descendientes incompatibles; y P2: `customer=all` se interpretaba como cliente borrado.
- Sol agregó poda de scopes para los destinos de navegación y permitió `customer=all` en la lectura del hash. La revisión independiente confirmó ambas correcciones y no identificó hallazgos nuevos en esas rutas.
- Aprobado estáticamente para el corte OPA-A1. Administración/CRUD no forman parte de este corte. No se ejecutaron pruebas ni se inspeccionó el resultado en navegador; la QA dinámica queda para OPA-QA.

## Spec 02 — OPA-B, revisión y carga inicial, 2026-10-21

Sol high implementó Administración con Estructura y Contenido coordinados, expansión independiente de la selección, búsqueda, activos y dispositivos del subárbol, Sin asignar, estados vacíos y restauración de `node`/`content` desde el hash. Las acciones CRUD están visibles y deshabilitadas hasta OPA-C.

- Revisión estática independiente Sol high: sin hallazgos P1/P2 en jerarquía, selección, contenido, hash, vacíos, escape de texto ni CSS móvil.
- La consola del usuario identificó un error de sintaxis en la plantilla de `adminAssetRow`; se corrigió el literal. Los seis scripts inline pasaron `node --check` y el navegador abrió el mapa 3D y Administración sin errores de ejecución. Permanece un aviso de Three.js sobre su distribución clásica.
- A pedido del usuario, Vista global inicia con el sidebar completo y conserva el botón para mostrar solo íconos. En navegador se comprobó el ancho inicial de 215 px y el ancho de 68 px después del cambio.
- La QA integral de Spec 02 sigue pendiente en OPA-QA, junto con los formularios y relaciones editables de OPA-C.

## Spec 02 — OPA-A2, instantánea simulada, 2026-10-21

El usuario priorizó quitar reproducción y Escenarios, y mostrar una instantánea fija de la demo. Sol high retiró franja, controles, temporizador, listeners y navegación de Escenarios; normalizó hashes heredados de `scenario`/`time`; fijó las lecturas a las 10:28 y mantuvo la última muestra de `p1s2` a las 10:11.

- Revisión independiente Sol high: el código no mostró hallazgos P1/P2 de ejecución estática. Detectó que la aceptación anterior aún exigía minuto/escenario compartibles; se actualizó el contrato OPA-006 y su verificación para reflejar la decisión posterior del usuario.
- El implementador verificó sintaxis de cinco scripts inline y carga inicial de la maqueta en Chrome headless. La QA integrada de navegación, gráficos y tamaños queda pendiente.
