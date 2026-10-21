# Spec 01 — Diseño espacial, mapa y recorrido operativo

Fecha: 2026-10-20. **Estado: implementación por cortes.** La revisión inicial se hizo sobre `IoTArg.html` en raíz; el archivo editable está ahora en `designs/IoTArg.html`. El avance observable se registra en [tasks.md](../tasks.md); esta especificación no implica que todo el rediseño esté implementado.

Objetivo confirmado: demo de portfolio con un recorrido operativo convincente. Encargo actual: revisar con Impeccable y UI/UX Pro Max, proponer mapa/3D, componentes y estilo, y preparar implementación posterior con Sol high.

## 1. Decisión propuesta

Convertir IoTArg en una **consola industrial compacta con navegación espacial continua**:

- Mapa protagonista, condición activa visible y panel operativo con la siguiente acción.
- Recorrido Sudamérica → Córdoba → Inaudi → Máquina 01 → Sensor 1 → alarma.
- Grafito, superficies sobrias y lavanda para interacción; colores semánticos para estado.
- Three.js existente para mapa y maqueta industrial esquemática; controles y datos esenciales en HTML.
- Vista móvil con estado primero, mapa de altura acotada y lista inmediatamente después.

El usuario confirmó ambas preferencias durante esta revisión: **mapa estilizado + instalación industrial esquemática**, y **mapa protagonista con una condición destacada para investigar**. La composición y aceptación detalladas siguen siendo la propuesta de implementación.

Esta spec reúne el rediseño espacial y el foco sudamericano de la demo, que forman un único alcance de producto. `ux.md`, `data.md` y los demás documentos transversales conservan sus IDs y responsabilidades. No renumerar requisitos existentes ni duplicar su aceptación.

## 2. Evidencia y diagnóstico

Inspección visual independiente A, detector y navegador B, más revisión del coordinador. Capturas: escritorio 1440×900 y móvil 390×844, con muestras de ambos temas. No se completó aún la matriz V-01 a V-07.

| Prioridad | Hallazgo observado | Cambio necesario |
| --- | --- | --- |
| P1 | Córdoba y Santiago se superponen. B no pudo pulsar Córdoba porque otro pin cubría el punto. En móvil el encuadre recorta la cartografía. | Encuadre según viewport, separación de etiquetas, selección inequívoca y lista sincronizada. |
| P1 | Cabecera y cuatro KPI desplazan el mapa; el sensor carece de acción directa hacia su alarma. Ubicación y área repiten composición. | Resumen compacto, condición destacada, jerarquía por nivel y alarma contextual. |
| P1 | La ilustración asigna el estado de ubicación a cada máquina. Un sensor crítico muestra solo el umbral de advertencia. | Agregación propia por activo; mostrar advertencia y crítico; coherencia entre mapa, lista y serie. |
| P1 | En móvil se ocultan búsqueda y rango temporal; el SVG reduce demasiado sus etiquetas. | Controles accesibles, gráfica adaptable, menos marcas y texto legible. |
| P2 | Navegación plana, información repetida y controles de simulación lejanos. Capas visualmente parecidas y controles cartográficos dispersos. | Agrupación, composición contextual, significado explícito de cada capa y controles accesibles. |

La evaluación heurística A obtuvo **23/40**: es una valoración de diseño, no un porcentaje de cumplimiento ni una certificación. [Crítica completa](../../../designs/evidence/critique-2026-10-20.md). [Assessment B y límites](../../../designs/evidence/review-b/assessment-b.md).

El detector estático devolvió 24 coincidencias: 19 warnings y 5 advisories, todas con `line: 0`. El overlay devolvió 72 coincidencias sobre el DOM. Son superficies diferentes: no sumar conteos ni convertir cada aviso en defecto confirmado. La legibilidad sí tiene corroboración visual.

### Referencia visual aportada después

El usuario aportó dos capturas de [Municipios Argentinos](https://municipiosargentinos.net/): [Argentina](../../../designs/evidence/reference/municipios-argentina.png) y [Buenos Aires](../../../designs/evidence/reference/municipios-buenos-aires.png). Son evidencia de dirección visual, no datos, marca ni assets para incorporar a IoTArg. El sitio no cargó desde el entorno de revisión; las observaciones siguientes se limitan a esas capturas.

| Rasgo visible en la referencia | Estado de IoTArg | Traducción para IoTArg |
| --- | --- | --- |
| El territorio domina la pantalla, con paneles superpuestos y controles periféricos. | Mapa en tarjeta bajo cabecera y cuatro KPI; sidebar de 215 px. | En Vista global, visor de al menos 65 % del alto visible en escritorio y superficie principal amplia; cabecera/resumen compactos, condición y acción en panel acotado. |
| Polígonos administrativos extruidos con cara superior luminosa, laterales oscuros y límites legibles. | Países extruidos entre 0,8 y 2,2 unidades, cámara cenital; profundidad visual tenue. | Cámara cenital fija, volumen y sombras locales visibles; material superior/lateral separados y contorno de selección. |
| Argentina muestra provincias; Buenos Aires muestra muchos municipios al acercarse. | El HTML contiene solo geometría de países y cuatro ubicaciones. | Primer nivel adicional: provincias argentinas con una sola Córdoba con datos IoT; otros territorios se muestran como «sin datos». Geometría municipal solo si luego existe alcance y datos que lo justifiquen. |
| El color y la altura se explican con leyenda y distribución. | Las capas cambian color/leyenda, pero altura depende de tener ubicación. | Cada capa declara su propio color, altura y unidad: estado, cantidad de dispositivos o cobertura. No asignar valores a territorios sin cobertura. |
| Etiquetas pequeñas sobre puntos, jerarquía por zoom y controles de encuadre a la derecha. | Pines rectangulares superpuestos; Córdoba queda bloqueada por Santiago. | Puntos con etiqueta desplazable, colisión resuelta, selección equivalente por lista y controles agrupados. |

La referencia usa tonos cálidos y verdes saturados. IoTArg conserva su identidad grafito/lavanda; se puede elevar la intensidad de la paleta **dentro del mapa** para estados semánticos. No copiar el titular, la marca, la métrica del índice municipal ni la composición de landing: la pantalla de IoTArg inicia una investigación operativa.

## 3. Nueva composición

### Escritorio

```text
Navegación | Vista global · Demo    Alcance / búsqueda / tema
           | Condición activa: Córdoba · Investigar
           | Resumen compacto del alcance
           | ┌────────────────────────┬──────────────────────┐
           | │ Visor espacial         │ Panel operativo      │
           | │ breadcrumb + controles │ entidades y estados  │
           | │ mapa / sitio / máquina │ detalle y acción     │
           | └────────────────────────┴──────────────────────┘
           | Escenario e instante simulados visibles en contexto
```

Panel lateral orientativo de 320 px, adaptable al espacio disponible. El visor ocupa el resto. El resumen cambia según nivel; no repetir cuatro tarjetas por defecto. En detalle de sensor, lectura, unidad, instante y condición tienen prioridad; mínimo/máximo quedan como información secundaria.

Navegación propuesta:

- **Operaciones:** Vista global, Inventario (Clientes, Ubicaciones, Activos y Dispositivos), Alarmas. [Spec 02](02-operational-tables-admin.md) define las pestañas de Inventario y Administración con Estructura/Contenido.
- **Análisis:** Soluciones, Dashboards.
- **Demo:** Escenarios, Metodología.

### Móvil

Título/alcance → condición y acción → resumen → visor de aproximadamente 280–320 px → lista operativa. La selección abre detalle accesible; no depender de hover ni de precisión sobre el mapa. El panel del sensor y su gráfica utilizan el ancho disponible. Búsqueda y rango siguen disponibles.

La condición y el acceso a investigar deben entrar en la primera pantalla a 390×844. El instante simulado sigue identificable; la franja inferior de reproducción se retira según [Spec 02](02-operational-tables-admin.md).

## 4. Dirección visual y componentes

Conservar la identidad documentada en [DESIGN.md](../../../DESIGN.md), ajustando contraste tras medirlo. Propuesta de escala: cuerpo 14 px, etiquetas esenciales y ejes de al menos 12 px visibles, cifras tabulares, títulos de contexto más compactos. Controles principales con área de 44×44 px. Bordes y sombras discretos; profundidad concentrada en el visor.

| Componente | Responsabilidad propuesta |
| --- | --- |
| Cabecera de alcance | Cliente, país y solución visibles y removibles; búsqueda disponible en todos los tamaños. |
| Franja de atención | Severidad, entidad y acceso a investigar. En estado normal, confirmación breve sin fabricar urgencia. |
| Visor espacial | Nivel, cámara cenital, selección, leyenda y retorno al encuadre inicial. |
| Lista operativa | Las mismas entidades del visor, ordenadas por severidad; nombre, pertenencia, estado y acción. |
| Panel de investigación | Información contextual y siguiente paso; evita repetir ubicación/área como pantallas idénticas. |
| Estado de activo | Agrega exclusivamente los sensores del activo, respetando DATA-003. |
| Resumen del sensor | Lectura válida, unidad, instante, estado y último reporte cuando corresponde. |
| Alarma contextual | Abre la condición del sensor y permite reconocerla; feedback accesible y reconocimiento local explícito. |
| Gráfica adaptable | Umbrales de advertencia y crítico, ventana visible, discontinuidad sin señal y datos accesibles. |
| Contexto de escenario | Escenario e instante simulados coherentes en todas las vistas, sin barra inferior de reproducción. |

Microinteracciones breves, sugeridas entre 180–300 ms; fundido/encuadre algo mayor solo cuando facilite entender un cambio de nivel. Sin giro automático ni pulsaciones constantes. `prefers-reduced-motion` lleva al estado final.

UI/UX Pro Max aportó agrupación, lectura de datos, contraste, selección 3D y adaptación. Su primera búsqueda propuso una landing con glassmorphism: se descartó por no corresponder al producto. La búsqueda específica de dashboard de datos sí se utilizó. Impeccable aportó crítica independiente, prioridades y comprobación visual; las sugerencias automáticas se contrastaron con el recorrido real.

## 5. Mapa y 3D

### Recorrido

| Nivel | Representación | Acción y continuidad |
| --- | --- | --- |
| Mundo / Sudamérica | Países del mundo; arranque encuadrado en las cuatro ubicaciones sudamericanas de la demo, según la sección «Foco sudamericano» de esta spec. | «Mundo» encuadra el planeta; seleccionar un país muestra su nivel administrativo cuando exista. |
| Córdoba | Aproximación al punto y transición al esquema del sitio. | Porta y Argentina visibles; área Inaudi seleccionable. |
| Inaudi | Suelo, límites y dos máquinas volumétricas simples. | Seleccionar activo lo encuadra y conserva breadcrumb. |
| Máquina 01 | Equipo esquemático con puntos de sensores y etiquetas HTML. | Selección sincronizada con lista; estado por activo. |
| Sensor 1 | Equipo y punto seleccionado como contexto espacial. | Lectura, gráfica y alarma; volver conserva alcance y selección. |

El país sigue siendo filtro; no se introduce como padre del cliente. El dataset carece de planos y posiciones físicas de sensores: la escena local se identifica como **esquema de demostración**. No se infieren edificios reales.

### Implementación recomendada

El HTML ya incluye **Three.js r160** y cámara ortográfica; el mapa renderizó durante la revisión. Conviene reutilizarlo en la primera etapa:

1. Un contenedor persistente con escenas/grupos de mapa, sitio y activo. Evitar recrear todo el renderer al navegar.
2. Separar datos de escena de objetos gráficos; IDs compartidos con listas, URL y detalle.
3. Calcular encuadre según límites y viewport. Resolver colisiones de etiquetas proyectadas con desplazamientos y líneas de unión.
4. Selección mediante raycasting y equivalentes HTML; el teclado no depende del canvas.
5. Animar solo durante cambios o interacción que lo necesiten; pausar cuando la pestaña no es visible. Liberar recursos descartados.
6. Mantener recorrido completo por SVG/listado sin WebGL. El fallo gráfico no impide investigar y reconocer una condición.

### Detalle territorial inspirado por las capturas

En escritorio, Vista global muestra una superficie cartográfica amplia con panel operativo compacto. Reducir la navegación global a una barra compacta cuando convenga a ese encuadre; conservar acceso a todas las secciones, incluida Administración cuando se implemente Spec 02. La condición activa y «Investigar» permanecen visibles sin ocultar marcadores. En móvil se mantiene la secuencia estado → mapa acotado → lista definida arriba.

La escena se organiza por nivel de detalle: `mundo` (países), `alcance sudamericano` (cuatro ubicaciones), `país` (divisiones administrativas disponibles) y `sitio` (maqueta industrial). Una capa de contexto territorial oscura permanece detrás del territorio enfocado. El encuadre pasa suavemente entre niveles y ofrece Volver/Encuadrar/Mundo. Evitar cambiar bruscamente de cámara o reconstruir el renderer. La sección «Foco sudamericano» concreta el encuadre inicial y la animación cenital.

Para la vista de Argentina, incorporar polígonos administrativos de Georef con identificadores estables, geometría simplificada y fuente/atribución verificadas antes de empaquetar el HTML. Asociar la ubicación Córdoba a su provincia mediante ID explícito y una proyección compartida con el mapa actual; no deducir pertenencia por etiqueta visible. Manejar multipolígonos y huecos. Las provincias sin ubicaciones en el alcance quedan en color «sin datos», sin alarmas ni recuentos inventados. Para los demás países, usar divisiones admin 1 de Natural Earth 1:10m donde existan; si no existen, conservar la vista nacional y explicarlo. [Fuente, cobertura y licencia](../cartography.md).

La **cara superior** usa color semántico y el lateral una variante más oscura; selección con borde claro y elevación breve. Candidatos para el mapa oscuro: crítico coral, advertencia ámbar, normal verde y sin señal violeta, medidos antes de fijarlos como tokens. Sin datos: grafito tenue. Color y altura siempre van acompañados de texto/leyenda. En la capa Estado, color = peor estado; altura = porcentaje de dispositivos con estado rojo/amarillo/sin señal sobre dispositivos del territorio, más una base decorativa igual para todos. En Dispositivos, altura = cantidad de dispositivos y color neutro de la capa; cantidades iguales producen alturas iguales. En Cobertura, altura fija y color distingue con datos/sin datos. Cada leyenda declara unidad, escala, alcance y minuto. Un territorio sin dispositivos no recibe valor operativo ni altura de dato. Al cambiar escenario/minuto o filtros, mapa, KPI y lista usan el mismo agregado. Ninguna barra o relieve implica altura física.

Las etiquetas se muestran por prioridad y zoom. Córdoba/Santiago mantienen dos puntos y nombres distinguibles; las demás etiquetas aparecen al acercarse o seleccionar. El usuario puede activar los mismos destinos con controles HTML. Separar controles de navegación geográfica (país/provincia/volver) de capas de datos (Estado/Dispositivos/Cobertura). La barra de distribución, si se usa, cuenta **sensores o ubicaciones realmente cubiertos**, y declara alcance, unidad y minuto; nunca copia el índice municipal.

El foco en `Córdoba · provincia` es navegación cartográfica; `Córdoba · ubicación` abre la instalación y sus datos. Seleccionar una provincia no agrega silenciosamente un filtro de entidades. Cliente, país y solución conservan su comportamiento visible. El foco administrativo se identifica por ID estable y se persiste de forma explícita en el fragmento URL si la vista se comparte o recorre con Atrás/Adelante. Seleccionar una provincia sin instalaciones muestra «Sin datos IoT en este alcance» y permite volver al país.

Las capas deben comunicar magnitudes distintas:

- **Estado:** severidad agregada con texto y leyenda.
- **Dispositivos:** conteo numérico por país/ubicación; escala y unidad explícitas.
- **Cobertura:** ubicaciones con información dentro del alcance; sin datos distinto de normal.

Si dos capas muestran lo mismo en el dataset actual, no exagerar diferencias mediante extrusión arbitraria. La altura decorativa no se presenta como medición.

La vista cartográfica mantiene relieve **3D** con cámara cenital fija; no ofrece selector 2D/3D ni inclina el mapa. Si WebGL no está disponible, el fallback SVG/listado conserva la navegación en una representación plana.

| Tecnología | Encaje |
| --- | --- |
| Three.js actual | Recomendado para HTML autocontenido, cartografía estilizada y esquema industrial propio. |
| MapLibre + Three.js | Alternativa si se eligen calles/cartografía urbana. Requiere definir fuentes cartográficas, licencias, atribución, disponibilidad y comportamiento sin red. |
| deck.gl | Útil al incorporar muchos puntos/rutas y capas de datos. No justifica complejidad adicional para 16 sensores. |
| React Three Fiber | Evaluar en la etapa Next.js si facilita mantener escenas; no hace falta introducir React en este HTML. |

Fundamento técnico: Three.js documenta [render bajo demanda](https://threejs.org/manual/pages/rendering-on-demand.html) y [OrbitControls](https://threejs.org/docs/pages/OrbitControls.html); MapLibre muestra [integración de objetos y modelos con Three.js](https://maplibre.org/maplibre-gl-js/docs/examples/add-3d-tiles-3d-objects-and-models-using-threejs/); deck.gl describe [capas, interacción y grandes datasets](https://deck.gl/docs). La selección para IoTArg es una recomendación basada en su alcance, no una exigencia de esas bibliotecas.

No actualizar Three.js ni añadir proveedores solo por estética. Si se cambia la versión, tratarlo como migración explícita con verificación del visor y fallback.

## 6. Aceptación adicional

Estos criterios amplían, sin reemplazar, [UX](../ux.md) y [DATA](../data.md).

| ID | Resultado observable | Relación |
| --- | --- | --- |
| VIS-001 | En 1440×900 y 390×844, ambos temas, condición activa y acceso a investigar visibles en primera pantalla; sin scroll horizontal de página. | UX-001, UX-009 |
| VIS-002 | El mapa completo del alcance entra inicialmente en el visor; Córdoba y Santiago se seleccionan por separado y abren lo mismo que sus filas. | UX-002, UX-009 |
| VIS-003 | Sudamérica → Córdoba → Inaudi → Máquina 01 → Sensor 1 tiene niveles distinguibles; volver conserva alcance y selección; Atrás/Adelante restaura contexto. | UX-002, UX-004, DATA-006 |
| VIS-004 | Sobretemperatura, minuto 28: Máquina 01 crítica y Máquina 02 con su propio estado, coherentes en visor, listas y sensores. | DATA-001, DATA-003 |
| VIS-005 | Sensor 1 muestra lectura, unidad, instante, aviso 75 °C, crítico 80 °C, rango y acceso a su alarma. Reconocer no altera severidad. | UX-005, UX-006 |
| VIS-006 | En móvil se puede buscar, cambiar ventana 60/15 minutos y leer ejes; menos marcas antes que texto reducido; alternativa accesible a la gráfica. | UX-007, UX-009, UX-011 |
| VIS-007 | Para `p1s2`, minuto 11 es última muestra entera válida; desde 12 no se presenta cálculo posterior como medición. Lectura, gráfica y nombre accesible coinciden. | DATA-004, V-03 |
| VIS-008 | La vista WebGL muestra relieve 3D con cámara cenital fija y sin control 2D/3D; el fallback SVG/listado funciona sin WebGL y conserva la navegación. Cada capa declara magnitud, alcance y leyenda. | UX-010, UX-011, DATA-002 |
| VIS-009 | Recorrido por teclado y sin WebGL completo; búsqueda contiene/restaura foco. Movimiento reducido elimina transición prescindible; escenario y minuto compartible conservan datos coherentes sin barra de reproducción. | UX-007, UX-008, UX-010, UX-012, OPA-006 |
| VIS-010 | Con escena estática y sin interacción no hay bucle de render continuo innecesario. Evidencia en navegador registra dispositivo/entorno y límites; no inferir rendimiento físico de headless. | UX-012 |
| VIS-011 | A 1440×900, Vista global reserva al visor al menos 65 % del alto visible; la condición y acción siguen visibles sin tapar Córdoba/Santiago. A 390×844 conserva estado → mapa → lista sin scroll horizontal. | UX-001, UX-009 |
| VIS-012 | Seleccionar Argentina muestra provincias con límites y selección distinguibles sobre relieve 3D y cámara cenital fija. Córdoba identifica su ubicación; provincias sin ubicaciones en el alcance indican «sin datos». Volver recupera Sudamérica y filtros. La fuente geográfica y su atribución están documentadas. | UX-002, UX-010, DATA-002 |
| VIS-013 | En Estado, color representa peor severidad y altura el porcentaje de dispositivos con condición; en Dispositivos, altura representa cantidad; en Cobertura, altura fija y color distingue con/sin datos. Cada leyenda declara unidades, escala, alcance y minuto. Escenario/tiempo/filtros actualizan mapa, KPI y lista coherentemente. Sin dispositivos no hay valor operativo ni altura de dato. | DATA-001, DATA-002, DATA-003 |
| VIS-014 | En zoom continental y provincial las etiquetas prioritarias no se solapan; marcador y fila seleccionan la misma entidad. Controles Volver/Encuadrar, selección y leyenda quedan operables por teclado y tacto. | UX-002, UX-007, UX-009, UX-011 |
| VIS-015 | «Córdoba · provincia» y «Córdoba · ubicación» se distinguen en controles, breadcrumb y nombres accesibles. Foco provincial no altera silenciosamente filtros; Atrás/Adelante y Compartir restauran foco geográfico por ID, entidad y alcance sin contradicciones. | UX-003, UX-004, DATA-006 |
| VIS-016 | «Mundo» encuadra la base global y permite seleccionar países fuera de Sudamérica. Al entrar en un país con admin 1 disponible se muestran sus divisiones con IDs únicos y opción de volver; donde no exista, el visor indica que no hay desglose. La geometría global se carga sin frenar la pantalla inicial y funciona en `file://`. Países y divisiones sin instalaciones muestran «Sin datos IoT», sin color de normalidad ni severidad inventada. | UX-002, UX-010, DATA-002 |

VIS-007 fija la regla propuesta para resolver DATA-004 antes de implementar. Para DATA-005 se propone limpiar reconocimiento al cambiar escenario por cualquier entrada, incluido historial; la implementación debe registrar y probar esta regla de producto. No confundirla con el comportamiento actual.

## 7. Secuencia de implementación y modelos

Estado y dependencias ejecutables: [tasks.md](../tasks.md), único registro de avance. El HTML tendrá un solo escritor.

| Paso | Encargo | Modelo solicitado |
| --- | --- | --- |
| Preparación | Versionado local y traslado exacto a `designs/IoTArg.html`; actualizar rutas y comprobar hash. | Coordinación Astra xhigh; ejecución acotada Sol high |
| Datos | Estado por activo, último reporte, reconocimiento e historial/URL coherentes. | Sol high |
| Composición | Cabecera compacta, condición destacada, lista/panel, navegación, sensor y gráfica adaptable. | Mismo Sol high |
| Geodatos | Obtener/verificar/simplificar límites provinciales, IDs estables y atribución; asociar ubicación Córdoba. | Mismo Sol high |
| Espacial | Visor persistente, niveles, materiales, alturas semánticas, etiquetas, capas, cámara, selección y fallback. | Mismo Sol high |
| Accesibilidad | Teclado, foco, controles móviles, contraste y movimiento reducido. | Mismo Sol high |
| Revisión | Contexto nuevo; contraste contra UX, DATA, VIS y V-01 a V-07; evidencia real. | Sol high |
| Correcciones | El mismo implementador corrige los hallazgos del HTML; el reviewer revalida lo afectado en una ronda posterior. | Sol high, con responsabilidades separadas |
| Cierre | Coordinar correcciones, integrar resultados y actualizar documentos; el HTML conserva su escritor exclusivo. | Astra xhigh |

Luna high queda para preguntas de investigación delimitadas si aparecen; no hace falta abrir otra investigación general. Los pasos sobre el mismo HTML son secuenciales. La coordinación integra evidencia y mantiene aceptación; la revisión independiente no modifica el archivo.

Ante hallazgos en IMP-07, el coordinador devuelve un encargo acotado al mismo implementador Sol high. Este corrige y entrega evidencia; el reviewer vuelve a leer y verificar las partes afectadas. Solo entonces avanza IMP-08. La coordinación corrige documentación compartida y el implementador corrige el HTML.

La planificación de esta propuesta fue delegada expresamente a `gpt-6-astra` con esfuerzo `xhigh`. El recibo del runtime informa el agente, no telemetría independiente del modelo efectivo. [Registro de orquestación](../orchestration.md).

## 8. Pendientes de especificaciones previas

- **Organización:** Git local está inicializado y el HTML se trasladó a `designs/`; falta el resto de este rediseño y su verificación completa.
- **UX-001–014:** revisión visual parcial disponible; faltan implementación y comprobación completa de alarmas, navegación, teclado, fallback, temas, siete soluciones y estados vacíos.
- **DATA-001–007:** corregir inconsistencias y probar casos límite de URL, alcance, almacenamiento, reconocimiento y desconexión.
- **DATA-008:** fixture multinacional/multiarea para la aplicación futura; este rediseño no declara soporte nuevo de dominio.
- **APP-001–007:** Next.js/TypeScript, dominio desacoplado, proveedor simulado, rutas, contrato ThingsBoard, permisos/persistencia y despliegue siguen en etapa posterior.
- **OPS-00/01:** adaptar rutas de aceptación del harness externo e instalarlo/verificarlo sigue pendiente. La delegación de esta conversación no equivale a su instalación.

## 9. Entrega que deberá producir Sol high

Una sola maqueta editable en `designs/IoTArg.html`, README actualizado, DESIGN con decisiones implementadas, capturas escritorio/móvil en ambos temas, resultados concretos de V-01 a V-07 y VIS-001 a VIS-016, y lista de limitaciones pendientes. Publicación o migración de framework se especificará en su etapa.

Esta etapa comienza por la cartografía y el visor. Los demás criterios de UX, datos y recorrido se mantienen pendientes hasta su implementación y comprobación.


## 10. Foco sudamericano de la demo

### Decisión de producto

La primera pantalla encuadra Sudamérica y las cuatro instalaciones simuladas: **Córdoba (Argentina), Santiago (Chile), Lima (Perú) y Montevideo (Uruguay)**. Estados Unidos y México siguen disponibles como territorios del mapa mundial, pero no tienen instalaciones ni telemetría de esta demo. El botón Mundo y el alejamiento con rueda permiten explorar otros países sin atribuirles cobertura IoT.

Esta decisión fija el **encuadre inicial y las ubicaciones** de esta spec. La cartografía mundial, la jerarquía de entidades y los criterios de severidad descritos arriba permanecen vigentes. Los nombres de clientes son ficticios; Porta conserva el recorrido prioritario de Córdoba.

### Datos y navegación

| Cliente | Ubicación | País | Área y activos |
| --- | --- | --- | --- |
| Porta | Córdoba | Argentina | Inaudi; Máquina 01 y Máquina 02 |
| Aero Demo | Lima | Perú | Terminal A; HVAC-01 y Zona de embarque |
| Nexo Data | Santiago | Chile | Sala de servidores; Rack R-01 y UPS-01 |
| Ruta Sur | Montevideo | Uruguay | Base operativa; Vehículo 01 y Vehículo 02 |

El conjunto sigue teniendo 4 clientes, 4 ubicaciones, 8 activos y 16 dispositivos. La sustitución de ubicaciones no modifica los escenarios ni las lecturas deterministas. Los IDs internos de las dos ubicaciones reemplazadas se conservan para mantener enlaces de entidades existentes; los rótulos y países visibles deben corresponder al nuevo destino. Los enlaces anteriores cuyo país ya no coincide con una entidad deben normalizar el alcance al país actual de esa entidad. Una selección aislada de Estados Unidos o México sigue siendo válida y muestra «Sin datos IoT».

Las coordenadas de los marcadores son ilustrativas. Lima usa la división administrativa `PER-587` del asset Natural Earth local; Montevideo usa `UY-MO`. La simplificación de los polígonos exige comprobar que cada marcador quede dentro de su división en la fuente incluida.

El selector **País** de la Vista global se deriva de las ubicaciones con sensores y contiene siempre «Vista general», Argentina, Chile, Perú y Uruguay. Los demás territorios se eligen directamente en el mapa mundial y pueden mostrar «Sin datos IoT»; su nombre aparece en el alcance del mapa y el texto geográfico, sin incorporarse como opción temporal al selector.

Los controles geográficos ofrecen **Ver mundo** como botón con ícono de globo en la esquina inferior derecha del mapa. El botón de restablecer existente en ese grupo vuelve a Sudamérica; no hay un segundo botón textual «Ver Sudamérica». **Centrar en mis datos** y **Quitar filtros** permanecen junto a País/Provincia. Quitar filtros limpia país y provincia sin cambiar cliente, solución, capa ni escenario. Centrar en mis datos también sale del foco país/provincia y encuadra todas las ubicaciones del cliente y la solución activos; el encuadre se calcula a partir de coordenadas y no presupone que estarán en Sudamérica. Si el alcance no contiene ubicaciones, se informa y se conserva la cámara.

El tooltip identifica el territorio o la ubicación y resume solo los datos del alcance actual. En Salud muestra sensores normales, en atención, críticos y sin señal; en Dispositivos destaca la cantidad total; en Cobertura indica ubicaciones y sensores con datos. País y provincia sin telemetría dicen «Sin datos IoT». Los marcadores de ubicación deben ofrecer el mismo resumen por foco o interacción táctil, con una ruta clara a su detalle. Los recuentos no incluyen sensores de otros países, clientes o soluciones.

### Cámara y movimiento

Al abrir la vista global sin foco geográfico en la URL, el **primer fotograma visible** muestra Sudamérica ya centrada y cenital. Desde ese mismo centro y canvas, el mapa se acerca un 5–8 % durante aproximadamente 900 ms; la cámara permanece derecha, sin rotación ni desplazamiento. Los cuatro marcadores aparecen con un fundido breve y Córdoba recibe un solo pulso discreto que señala la condición activa. Un estado de preparación ocupa la misma superficie hasta que el primer fotograma correcto está dibujado. Si el usuario interactúa durante la entrada, la animación se detiene en un estado coherente. La geometría conserva el relieve 3D permanentemente, con cámara cenital y sin botón 2D/3D. Con `prefers-reduced-motion: reduce` se presenta directamente el estado final, sin zoom, fundido ni pulso. Los enlaces directos a país o provincia abren en su propio encuadre sin ejecutar la entrada sudamericana. El fallback SVG permanece plano, se revela ya centrado y no anima la cámara; cambiar el tamaño no reinicia la entrada.

La referencia de [Municipios Argentinos](https://municipiosargentinos.net/) y las capturas aportadas por el usuario orientan el efecto visual; esta especificación expresa la intención del usuario, sin afirmar una reproducción exacta de su implementación.

### Composición de la vista global

El mapa es la superficie principal de la primera pantalla, cercano a la altura útil del navegador y ocupando todo el ancho disponible del área de trabajo. La navegación lateral se reduce a un riel compacto en escritorio durante la vista global; las demás vistas conservan su estructura. El título, los filtros geográficos, las capas y la condición que se debe investigar se disponen como controles flotantes legibles sobre el visor, sin crear una fila de tarjetas que lo empuje debajo del primer pliegue. La condición activa conserva su enlace **Investigar**.

La cobertura y la lista de cuatro ubicaciones se integran en un panel compacto superpuesto o desplegable. Los marcadores y el listado siguen siendo rutas equivalentes a cada sitio. El encuadre deja aire para esos controles y mantiene visibles las cuatro ubicaciones en escritorio. La leyenda conserva unidad, estado y atribución cartográfica; en móvil pasa debajo del mapa si el espacio sobre el territorio no alcanza. Ningún overlay debe bloquear el clic o foco de un marcador.

La referencia visual guía escala del mapa y jerarquía, no la tipografía, colores, índice municipal o contenidos de otro producto. IoTArg conserva información de salud operativa y datos simulados.

### Criterios de aceptación

| ID | Verificación |
| --- | --- |
| SA-01 | Vista inicial, botón de restablecer y «Volver» encuadran Sudamérica; Córdoba, Santiago, Lima y Montevideo aparecen como ubicaciones de la demo y se pueden abrir por marcador o lista. |
| SA-02 | Estados Unidos y México no tienen instalaciones ni sensores; seleccionar esos países muestra «Sin datos IoT», sin severidad inventada. |
| SA-03 | Perú y Uruguay muestran su división administrativa y los dispositivos correspondientes a Lima y Montevideo. |
| SA-04 | Alejar con la rueda y usar Mundo permite ver y seleccionar países de fuera de Sudamérica; volver recupera el encuadre sudamericano. |
| SA-05 | Entrada cenital con zoom de 5–8 % durante unos 900 ms, sin giro ni traslado del centro; los cuatro marcadores aparecen suavemente y Córdoba pulsa una vez. El estado final permanece derecho. |
| SA-06 | La URL, búsqueda, páginas de solución, filtros, leyendas y accesibilidad nombran correctamente los nuevos destinos. Los enlaces de entidad heredados se normalizan cuando arrastran un país anterior. |
| SA-07 | Se comprueba escritorio y móvil, relieve 3D cenital, cambio de tamaño y fallback SVG sin WebGL, sin errores de aplicación. |
| SA-08 | A 1440×900 el mapa y la condición a investigar aparecen sin desplazar el visor fuera del primer viewport; el visor ocupa todo el ancho disponible del área de trabajo y la mayor parte de su altura útil. |
| SA-09 | En escritorio y móvil, filtros, lista de ubicaciones, marcadores, leyenda y acción Investigar son utilizables sin superposiciones que bloqueen los objetivos; el flujo principal sigue accesible por teclado. |
| SA-10 | En carga limpia, el primer fotograma visible del mapa es Sudamérica centrada y cenital; la preparación permanece en la misma superficie hasta ese render. Movimiento reducido muestra de inmediato mapa y marcadores finales; deep links, fallback SVG y resize no provocan un salto de encuadre ni reinician la entrada. |
| SA-11 | El selector País muestra siempre solo Vista general + AR/CL/PE/UY, derivado de ubicaciones con sensores. Otros países se seleccionan en el mapa y muestran su nombre y estado sin datos en el alcance, sin añadir opciones al selector. |
| SA-12 | Quitar filtros, junto a los selectores, limpia país y provincia, actualiza URL y mapa y conserva cliente, solución, capa y escenario. |
| SA-13 | El globo Ver mundo y el control Restablecer a Sudamérica son acciones independientes en el mapa. Centrar en mis datos encuadra todas las ubicaciones del alcance activo, incluidas futuras sedes fuera de Sudamérica, sin pérdida por cruce de longitud; sin ubicaciones comunica el vacío y conserva el encuadre. |
| SA-14 | País, provincia y ubicación muestran un tooltip legible y contextual para Salud, Dispositivos y Cobertura, con nombre, ubicaciones y sensores, y desglose de normal/atención/crítico/sin señal cuando corresponde; no inventa datos en territorios vacíos. |
| SA-15 | Los nuevos controles y el resumen de ubicación funcionan con ratón, teclado y tacto en escritorio/móvil; no bloquean marcadores ni generan desplazamiento horizontal. El fallback SVG conserva la navegación y el encuadre. |
| SA-16 | La cámara WebGL permanece cenital en Mundo, Sudamérica, país, provincia, fit, URL directa y tras la entrada; el relieve 3D de países/provincias conserva la semántica por capa. El botón 2D/3D desaparece y el fallback SVG sigue accesible si WebGL no está disponible. |
| SA-17 | La barra de filtros no contiene botones Ver mundo ni Ver Sudamérica. Un único botón de globo, con nombre accesible Ver mundo, aparece en el grupo inferior derecho del mapa; el control de restablecer vuelve a Sudamérica. Ambos son utilizables en escritorio y móvil sin tapar marcadores ni leyenda. |
| VIS-017 | Desde cualquier vista de escritorio, un único botón del sidebar alterna entre Solo íconos y Completo. El primero muestra una navegación compacta; el segundo, íconos y nombres. El mapa inicia con íconos; las demás vistas inician completas si el ancho supera 980 px y compactas entre 761 y 980 px. El cambio explícito se conserva al navegar. El botón anuncia la acción y el modo actual de forma accesible. En móvil, la cabecera abre el sidebar y su botón lo cierra. |

### Pendiente posterior

Los modelos detallados de aeropuertos, rutas reales de flota, geocercas y telemetría en vivo siguen fuera de este corte. El mapa muestra sitios esquemáticos con datos de demostración.
