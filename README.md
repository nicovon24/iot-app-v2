# IoTArg — operaciones conectadas

> **Estado: prototipo HTML interactivo en evolución.** [designs/IoTArg.html](designs/IoTArg.html) incluye navegación, telemetría simulada y visualizaciones. Next.js, Server Actions, base de datos e integración ThingsBoard corresponden a la siguiente etapa.

IoTArg permite explorar un mapa mundial y pasar al contexto de un cliente, una ubicación y un sensor. La primera pantalla se centra en cuatro ubicaciones de **Sudamérica: Argentina, Chile, Perú y Uruguay**. El proyecto funciona con datos propios de demostración; un futuro conector de ThingsBoard se incorporará detrás de un modelo normalizado.

## Documentación y especificaciones

El objetivo confirmado es una **demo de portfolio con un recorrido operativo convincente**. [PRODUCT.md](PRODUCT.md) conserva el contexto de producto y [DESIGN.md](DESIGN.md) documenta el sistema visual existente.

Las [especificaciones en docs/specs](docs/specs/README.md) distinguen lo observado en la maqueta, la validación pendiente y la evolución propuesta. El [plan de tareas](docs/specs/tasks.md) es el registro de avance; la [orquestación](docs/specs/orchestration.md) contrasta el harness de referencia con la ejecución real de esta entrega.

El HTML editable está en [designs/IoTArg.html](designs/IoTArg.html). La [Spec 01 de diseño espacial, mapa y recorrido](docs/specs/subspecs/01-initial-design.md) se implementa por etapas e incluye el foco sudamericano y su entrada animada. [cartography.md](docs/specs/cartography.md) registra fuentes, cobertura y licencias de la geometría.

## Abrir la demo

1. Abrir [designs/IoTArg.html](designs/IoTArg.html) en un navegador moderno.
2. Elegir **Porta** en el selector superior o **Argentina** en el mapa.
3. Abrir **Córdoba → Inaudi → Máquina 01 → Sensor 1**.
4. Mover el reloj o cambiar el escenario para comparar lecturas y alarmas.
5. Probar el tema claro/oscuro y las otras secciones del sidebar.

Abrí el HTML **dentro de la carpeta `designs/`**, junto con `map-data/`: la capa administrativa mundial se carga desde ese archivo local. No necesita instalar paquetes, una cuenta, API key ni conexión a ThingsBoard. El render 3D requiere WebGL; si no está disponible se activa un mapa SVG 2D. El listado de ubicaciones también permite navegar.

**Persistencia:** tema y una vista de dashboard se guardan en el navegador cuando este permite almacenamiento local. El reconocimiento de alarmas vive en memoria hasta recargar la página; también se borra al seleccionar un escenario con su botón o restablecer la demo. Atrás/Adelante puede cambiar de escenario sin limpiar esos reconocimientos. `Compartir vista` copia la URL con filtros y escenario; al abrir desde un archivo local, la otra persona necesita la carpeta `designs/` completa y debe aplicar el fragmento `#...` a su propia ruta.

## Qué funciona en este HTML


| Función       | Implementación actual                                                                                                                      |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Vista global  | Mapa protagonista desde el primer viewport; globo Ver mundo y restablecer a Sudamérica abajo a la derecha, con Centrar en mis datos y Quitar filtros en la barra geográfica. Hay 242 territorios seleccionables y detalle administrativo disponible en 240 países. Solo Argentina, Chile, Perú y Uruguay tienen ubicaciones IoT simuladas. |
| Cámara inicial | Primer fotograma sudamericano centrado y derecho, seguido por un acercamiento suave de 5–8 %; los cuatro marcadores aparecen y Córdoba pulsa una vez. La superficie muestra preparación hasta ese fotograma; movimiento reducido y enlaces directos abren en su estado final. |
| Mapa 3D       | Países y divisiones extruidos con Three.js y cámara siempre cenital; capas Estado/Dispositivos/Cobertura con leyenda, alturas semánticas y tooltip de sensores por alcance. Alternativa SVG automática sin WebGL. |
| Alcance       | Cliente + país + solución; chips para quitar filtros, KPI y entidades recalculados.                                                        |
| Navegación    | Sidebar, breadcrumbs, búsqueda por entidades, URL con estado y Atrás del navegador.                                                        |
| Jerarquía     | Cliente → ubicación → área → activo → dispositivo. Una sola área por ubicación en este dataset inicial.                                    |
| Instalaciones | Ilustración isométrica seleccionable para abrir activos. No es un plano real ni una capa de edificios urbanos.                             |
| Telemetría    | Series deterministas, unidades, umbral, lectura actual, mínimo/máximo del escenario y línea de eventos.                                    |
| Alarmas       | Severidad, reconocimiento local, filtro de reconocidas y enlace a investigación del dispositivo.                                           |
| Soluciones    | Siete páginas con ubicaciones y una serie representativa dentro del alcance.                                                               |
| Dashboards    | Gráficas del alcance; guardar/restaurar una vista local. Sin editor de widgets.                                                            |
| Escenarios    | Normal, sobretemperatura y sensor sin señal; reloj compartido de 60 minutos.                                                               |
| Diseño        | Temas claro/oscuro, estados vacíos, foco visible y estilos adaptables a pantallas pequeñas.                                                |


Las páginas de soluciones son una primera aproximación de navegación. Tracking todavía no reproduce rutas ni geocercas; Air Quality usa CO₂; Airport y Data Center comparten plantillas de análisis. No hay inferencia con IA, RAG, manuales, machine learning ni acciones sobre equipos reales.

## Datos de demostración

El ejemplo principal solicitado se conserva tal cual:


| Nivel    | Ejemplo                                                |
| -------- | ------------------------------------------------------ |
| Customer | **Porta**                                              |
| Location | **Córdoba**, Argentina                                 |
| Area     | **Inaudi**                                             |
| Assets   | **Máquina 01**, **Máquina 02**                         |
| Devices  | **Sensor 1**, **Sensor 2** por máquina, con IDs únicos |


Porta tiene únicamente Córdoba en esta versión. No se atribuyen a la empresa operaciones reales adicionales. Todos los dispositivos, lecturas, coordenadas de demo y alarmas son ilustrativos.

Para explorar los cuatro países del foco inicial se agregan organizaciones ficticias:


| Cliente   | Ubicación         | País           | Área               | Activos                   |
| --------- | ----------------- | -------------- | ------------------ | ------------------------- |
| Porta     | Córdoba           | Argentina      | Inaudi             | Máquina 01, Máquina 02    |
| Aero Demo | **Lima** | Perú | Terminal A         | HVAC 01, Zona de embarque |
| Nexo Data | Santiago          | Chile          | Sala de servidores | Rack R01, UPS 01          |
| Ruta Sur  | Montevideo         | Uruguay         | Base operativa     | Vehículo 01, Vehículo 02  |


Total inicial: **4 clientes, 4 ubicaciones, 8 activos y 16 dispositivos**. Lima es un caso aeroportuario ficticio, sin integración con un aeropuerto real.

## Cliente y país: dos entradas al mismo contexto

La propiedad sigue **Customer → Location → Area → Asset → Device**. `countryCode` pertenece a `Location`; el país filtra y enfoca el mapa. Un cliente podrá tener ubicaciones en distintos países sin duplicarse.


| Entrada      | Recorrido                                                                                 |
| ------------ | ----------------------------------------------------------------------------------------- |
| Por cliente  | Todos → Porta → países con sus datos → Argentina → Córdoba                                |
| Por país     | Mundo o Sudamérica → Argentina → elegir Porta → Córdoba                                     |
| Por solución | Soluciones → Environment / Temperature → ubicación disponible → activo → sensor           |
| Búsqueda     | Buscar cliente, ubicación, activo o dispositivo → abrir resultado y restaurar su contexto |


Seleccionar un cliente conserva el país activo. Si esa combinación no tiene datos, se muestra un estado vacío y controles para quitar el filtro. Quitar el país recupera todas las ubicaciones del cliente. Las soluciones conservan cliente y país. El selector **País** de la Vista global contiene solo Vista general, Argentina, Chile, Perú y Uruguay, derivado de las ubicaciones con sensores. El mapa mundial permite seleccionar otros países; su nombre y ausencia de datos aparecen en el contexto del visor, mientras el selector permanece en Vista general.

En el mapa, **Quitar filtros** junto a País/Provincia limpia ambos niveles geográficos y conserva cliente, solución, capa y escenario. **Centrar en mis datos** encuadra las ubicaciones del cliente y solución activos; el cálculo usa sus coordenadas y admite sedes de otros continentes. El ícono de globo abajo a la derecha abre el mundo y el control de restablecer vuelve a Sudamérica. Al pasar, enfocar o tocar un territorio o marcador aparece un resumen con nombre, cobertura y sensores; Salud separa normales, en atención, críticos y sin señal. En pantallas táctiles, el primer toque muestra el resumen y el segundo abre el destino.

**Expansión multinacional:** cuando un cliente tenga 3–4 países, el selector superior mostrará todas sus ubicaciones; hacer clic en un país reducirá ese conjunto. El HTML demuestra el modelo con un país por cliente. Validar múltiples países por cliente y varios clientes en el mismo país será un caso adicional del MVP.

El enlace conserva vista, cliente, país, entidad, solución, escenario, minuto, capa y ventana de gráficas. Ejemplo de fragmento:

```
#view=device&customer=porta&country=AR&id=p1s1&scenario=overheat&time=28&layer=health&range=60
```

## Vistas y navegación

Se usan las **10 secciones enumeradas** en el alcance; áreas y páginas de solución son vistas internas.


| Sección      | Qué permite hacer                                                 |
| ------------ | ----------------------------------------------------------------- |
| Vista global | Ver sedes en Sudamérica o el mundo, centrar los datos del alcance, quitar país/provincia y abrir una ubicación desde mapa o lista. |
| Clientes     | Explorar las cuentas y sus ubicaciones dentro del alcance.        |
| Ubicaciones  | Abrir instalación, área y representación espacial.                |
| Activos      | Consultar equipos, estado y dispositivos asociados.               |
| Dispositivos | Ver lectura, conectividad, serie y contexto del sensor.           |
| Alarmas      | Priorizar, reconocer e investigar condiciones activas.            |
| Soluciones   | Entrar por necesidad operativa.                                   |
| Dashboards   | Comparar series y guardar una vista en el navegador.              |
| Escenarios   | Cambiar el caso y reproducir eventos.                             |
| Metodología  | Entender datos simulados, cálculos y límites.                     |


Breadcrumb de referencia: **Vista global / Porta / Córdoba / Inaudi / Máquina 01 / Sensor 1**. Argentina aparece como chip geográfico. Si se llegó desde Temperature, un enlace permite regresar a esa solución. El botón Atrás recupera el estado anterior de navegación.

En la Vista global de escritorio, el mapa ocupa la mayor parte del área de trabajo; el sidebar se reduce a un riel con nombres accesibles y la condición, filtros y cobertura se muestran sobre el visor. La lista de ubicaciones se puede plegar. En móvil, el mapa aparece primero, la leyenda y la lista quedan debajo y el menú lateral pasa a un panel desplegable.

## Soluciones


| Familia      | Página                 | Dataset inicial              | Evolución prevista                                         |
| ------------ | ---------------------- | ---------------------------- | ---------------------------------------------------------- |
| Environment  | Air Quality            | CO₂ en Lima                | PM2.5/PM10, distribuciones y tiempos fuera de umbral.      |
| Environment  | Temperature            | Córdoba, Lima y Santiago   | Comparación entre áreas y sensores.                        |
| Tracking     | People                 | Ocupación agregada en Lima | Flujos ficticios entre zonas; sin personas identificables. |
| Tracking     | Assets                 | Vehículos en Montevideo       | Posiciones, recorridos y geocercas simuladas.              |
| Management   | Airport Management     | Lima, Perú                | Terminales, HVAC, energía, ocupación y detalle espacial.   |
| Management   | Data Center Management | Santiago                     | Racks, UPS, humedad, refrigeración y consumo.              |
| Intelligence | Predictive Maintenance | Máquinas en Inaudi           | Correlación de vibración/temperatura y eventos anteriores. |


Una solución configura una vista sobre las entidades existentes: no crea otra jerarquía ni duplica telemetría. Las personas no se modelan como activos; la demo de People muestra ocupación agregada.

## Simulación y reglas de estado

La simulación usa funciones deterministas de escenario, dispositivo y minuto. El mismo enlace reproduce los mismos valores. El tiempo de demostración va de **10:00 a 11:00**; el selector superior cambia las gráficas entre escenario completo y últimos 15 minutos. Los KPI de estado corresponden al instante seleccionado; los mínimos/máximos del sensor indican explícitamente que cubren el escenario.


| Escenario        | Comportamiento                                                                                                                                                   |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Normal           | Todos los sensores reportan dentro de sus umbrales.                                                                                                              |
| Sobretemperatura | La temperatura de Máquina 01 aumenta después del minuto 10. A las 10:28 alcanza aproximadamente 80,9 °C y estado crítico; Rack R01 presenta advertencia térmica. |
| Sensor sin señal | Sensor 2 de Máquina 01 queda sin señal desde el minuto 12. La gráfica se recorta en ese minuto; la representación consistente de la última lectura válida y su etiqueta accesible está pendiente de corrección. |


Los umbrales son ilustrativos. Reconocer una alarma confirma que alguien la revisó, pero no resuelve la condición ni modifica el sensor.

- **Verde:** no hay condiciones activas en el alcance.
- **Amarillo:** hay al menos una advertencia y ninguna crítica.
- **Rojo:** existe una condición crítica.
- **Violeta / Sin señal:** pérdida de conectividad; se informa también en texto.
- **Gris / Sin datos:** no hay cobertura para ese país y alcance.

La agregación usa la mayor severidad entre los dispositivos de las ubicaciones visibles. Los conteos de clientes y ubicaciones son únicos. Las observaciones de telemetría y las posibles explicaciones se presentan separadas. La explicación es texto ilustrativo, no un diagnóstico confirmado.

## Dirección visual y referencias

- **Nombre:** IoTArg.
- **Referencia de producto:** ThingsBoard; IoTArg utiliza un modelo y una experiencia propios.
- `provincial-dashboard-v2 (1).html`**:** referencia solo para la forma, perspectiva y estilo del mapa. El dashboard provincial pertenece a otro proyecto.
- **[Municipios Argentinos](https://municipiosargentinos.net/):** referencia para profundidad de territorios, mapa como entrada y jerarquía visual.
- **Identidad:** grafito en modo oscuro, superficies claras en modo claro, acento lavanda y colores de estado reservados para información operativa.
- **3D progresivo:** países a escala continental; edificios y capas urbanas cuando haya datos apropiados; modelos de instalación cuando ayuden a localizar equipos.
- **“City Layers”:** intención de agregar capas urbanas, no dependencia de una biblioteca confirmada.
- **Alternativas:** lista de ubicaciones y mapa 2D para mantener el recorrido sin WebGL.

## Arquitectura de la siguiente etapa

El HTML es la referencia de interacción y diseño. La aplicación de portfolio se implementará con **Next.js App Router + TypeScript**.
