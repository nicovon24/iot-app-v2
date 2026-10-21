# Estado observado de la maqueta

Fecha: 2026-10-20. Fuente: `IoTArg.html` en la raíz. Inspección estática; no se ejecutaron pruebas de navegador en esta entrega.

SHA-256 de referencia: `D55DCCA186D0B159A8A074B6E56ECB591203932C4E031D51D58C010AFCC47C8E`.

## Inventario

| Área | Observado en código | Referencia |
| --- | --- | --- |
| Empaquetado | HTML con estilos, JavaScript, Three.js y cartografía integrados | Bloques `style` y `script` |
| Navegación | 9 entradas dinámicas y acceso estático a Metodología; 10 secciones | `navs`, línea 48; `nav-bottom`, línea 20 |
| Detalles | Ubicación, área, activo, dispositivo y solución | `renderLocation`, `renderAsset`, `renderDevice`, `renderSolution`, líneas 75–82 |
| Datos | 4 clientes, 4 ubicaciones, 8 activos, 16 dispositivos | `customers`, `locations`, `assets`, `devices`, líneas 42–46 |
| Alcance | Intersección cliente + país + solución sobre ubicaciones | `scopedLocations`, `scopedDevices`, líneas 54–55 |
| Mapa | Países extruidos, zoom, selección, capas y etiquetas de ubicaciones | `initMap`, `pickMap`, `renderMapLabels`, líneas 107–116 |
| Alternativa al 3D | Mapa SVG y navegación por listados | `renderFallback`, línea 119; `locationTable` |
| Instalación | Ilustración isométrica con activos seleccionables | `factory`, `renderLocation` |
| Telemetría | Valores deterministas, gráficas, umbrales, ventana temporal y eventos | `value`, `status`, `chart`, líneas 56–57 y 76 |
| Alarmas | Condiciones de severidad o desconexión, filtros y reconocimiento local | `alarmDevices`, `renderAlarms`, manejador `ack` |
| Soluciones | Siete vistas agrupadas en cuatro familias | `solutions`, `renderSolutions`, `renderSolution` |
| Dashboard | Series del alcance y una vista guardada/restaurada | `renderDashboards`, `save-dashboard`, `load-dashboard` |
| Simulación | Normal, sobretemperatura y sin señal; reloj 0–60 | `renderScenarios`, `play`, manejadores de escenario |
| Navegación reproducible | Fragmento URL, búsqueda y `popstate` | `writeHash`, `readHash`, `searchModal`, `searchResults` |
| Preferencias | Tema y vista de dashboard en almacenamiento local | `setTheme`, `save-dashboard` |
| Accesibilidad parcial | Foco visible, nombres accesibles, SVG con teclado, movimiento reducido | CSS; `searchModal`; `renderFallback`; `animateMap` |

Las líneas corresponden al HTML original. La biblioteca embebida ocupa líneas muy extensas; usar nombres de función al reubicar o formatear el archivo.

## Dataset y cobertura

| Cliente | País / ubicación | Área | Activos |
| --- | --- | --- | --- |
| Porta | Argentina / Córdoba | Inaudi | Máquina 01 y Máquina 02 |
| Aero Demo | Estados Unidos / Austin | Terminal A | HVAC 01 y Zona de embarque |
| Nexo Data | Chile / Santiago | Sala de servidores | Rack R01 y UPS 01 |
| Ruta Sur | México / Monterrey | Base operativa | Vehículo 01 y Vehículo 02 |

Cada activo tiene dos sensores con IDs únicos. El nombre de un sensor no es su identidad global. El área está representada dentro de la ubicación, sin colección independiente.

## Límites existentes

- No hay backend, autenticación, base de datos, conector ThingsBoard ni acciones sobre equipos reales.
- Una ubicación por cliente y un área por ubicación no prueban el caso multinacional o multiarea.
- Air Quality representa CO₂; Tracking Assets no reproduce rutas/geocercas; People usa ocupación agregada.
- Airport y Data Center reutilizan plantillas. Predictive Maintenance no realiza inferencia predictiva.
- El dashboard no tiene editor de widgets.
- El archivo puede abrirse localmente; compartir su URL no distribuye el archivo a otra persona.
- Reconocimientos de alarmas viven en memoria y se pierden con una recarga.

## Observaciones para la siguiente etapa

| ID | Evidencia estática | Tratamiento |
| --- | --- | --- |
| OBS-01 | Canvas usa punteros para países; SVG ofrece teclado | Validar recorrido equivalente sin depender de WebGL ni del puntero |
| OBS-02 | Búsqueda enfoca el input al abrir, pero no se observa trampa de foco ni devolución explícita al disparador | Implementar y probar ciclo de foco |
| OBS-03 | Texto secundario 10–12 px y controles de icono pequeños | Revisar legibilidad y áreas táctiles en navegador |
| OBS-04 | README describe violeta para sin señal; `color()` usa `#697a88` en mapa | Unificar semántica documentada y distinguir representación de badge/mapa |
| OBS-05 | `readHash()` valida valores individuales; no demuestra coherencia entre entidad y contexto combinados | Probar enlaces con cliente, país e ID incompatibles |
| OBS-06 | Serie offline recorta el final al minuto 12, mientras el sensor ya está offline desde ese minuto; el nombre accesible del gráfico usa `value(d)` actual | Definir último reporte y evitar anunciar valores actuales ficticios sin señal |
| OBS-07 | Referencia visual `provincial-dashboard-v2 (1).html` no está en el proyecto | No usarla como evidencia accesible hasta obtener el archivo |
| OBS-08 | El botón de escenario limpia reconocimientos, pero `popstate` restaura escenario sin limpiar el `Set` | Resolver la política de reconocimiento al navegar por historial en IMP-05 |

La hipótesis inicial del investigador sobre falta de acceso a Metodología fue descartada al integrar: hay un botón estático en `nav-bottom` (línea 20).

## Validación pendiente

Abrir la maqueta y recorrer entradas, detalles, búsqueda, Atrás/Adelante, filtros, simulación, persistencia, temas, teclado y fallback. Los criterios están en [ux.md](ux.md) y [data.md](data.md); la planificación está en [tasks.md](tasks.md).
