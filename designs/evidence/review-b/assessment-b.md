# Assessment B: detector y evidencia de browser

Revisión independiente de Assessment A. Target: `IoTArg.html`; servidor del coordinador: `http://127.0.0.1:8766/IoTArg.html`.

## Detector

Ejecutado una vez con `C:\Users\Nicolas\.codex\skills\impeccable\scripts\impeccable.cmd detect --json IoTArg.html`; exit code 0. Salida completa: [detector.json](detector.json).

- 24 matches: 19 `warning`, 5 `advisory`.
- Reglas: `undersized-ui-text` 12; `gpt-thin-border-wide-shadow` 5; `tiny-text` 3; `layout-transition` 1; `wide-tracking` 1; `overused-font` 1; `kicker-above-heading` 1.
- El detector informa `line: 0` en los 24 casos; no aporta una línea fuente utilizable. El target está muy minificado y contiene un bundle Three.js inline. Ubicaciones de contexto inspeccionables: mapa/capas en `IoTArg.html:23`, render de ubicación `:75`, activo `:77`, explicación de límites `:85`.
- Los cinco avisos de borde/sombra son advisory y repetidos; no se trataron como cinco defectos confirmados. `overused-font` y kicker son heurísticas de estilo, no fallos funcionales por sí solos.

## Browser

Sesión aislada `iotarg-review-b`, Chromium headless, URL local del coordinador. Capturas:

- [overview.png](overview.png), [overview-cleared.png](overview-cleared.png): encabezado, 4 KPIs, mapa y ubicaciones.
- [location.png](location.png): Porta → Córdoba → área Inaudi; la vista del sitio se presenta como ilustración isométrica.
- [device.png](device.png): Máquina 01, gráfico simulado de Temperatura y umbral 75 °C; lista Sensor 1 y Sensor 2.
- [mobile390-clean.png](mobile390-clean.png): vista global a 390×844, sin overlay.
- [map-2d.png](map-2d.png), [map-3d.png](map-3d.png), [layer-devices.png](layer-devices.png), [layer-coverage.png](layer-coverage.png): toggles y capas.
- [offline390.png](offline390.png): resultado de recargar con el modo offline del browser activo.
- [overlay.png](overlay.png), [overlay-console.log](overlay-console.log): detector dinámico cargado en la vista; el console reporta 72 anti-patterns para el DOM inspeccionado.

Observaciones concretas:

- Los botones de capa cambian la selección y la leyenda (`Dispositivos en el país` / `Con información`). En este conjunto de cuatro países, las capturas de dispositivos y cobertura se ven muy parecidas porque todos tienen datos.
- El botón alterna su etiqueta visible entre `3D` y `2D`; el nombre accesible del canvas sigue diciendo `Mapa 3D de América` tras alternarlo. En las capturas headless no se distingue con claridad un cambio geométrico entre los modos.
- El click del pin `Córdoba` fue rechazado porque otro `button.map-pin` cubría su punto de click. La fila de Córdoba en la lista sí permitió llegar al detalle.
- Al activar offline y recargar el URL servido por localhost, Chromium mostró `ERR_INTERNET_DISCONNECTED`. Esto acredita que ese reload no tiene fallback desde la sesión; no prueba qué ocurriría abriendo el HTML local ni con una caché previa.
- La consola del prototipo mostró la advertencia de Three.js sobre `build/three.js`/`build/three.min.js` deprecados; el mapa sí renderizó en esta sesión.

## Overlay y cleanup

La preflight mutable del DOM tuvo éxito. Se inició `impeccable live-server --background` en puerto 8400 para `/detect.js`; el script se inyectó en la pestaña local y el console devolvió 72 findings. Registro de inicio y parada: [live-server-start.log](live-server-start.log), [live-server-stop.log](live-server-stop.log). Se paró solo el servidor temporal de puerto 8400 con `impeccable live-server stop --keep-inject`; se cerró `iotarg-review-b`. No se detuvo el servidor del coordinador en puerto 8766.

## Límites

La vista usa Chromium headless; estas capturas no certifican rendimiento en GPU/dispositivo físico. La advertencia Three.js es una deprecación, no un fallo observado. El conteo overlay (72) y el scan de archivo (24) cubren superficies distintas y no deben sumarse. Las ubicaciones `line: 0` del JSON requieren localizar snippets por búsqueda en el HTML.
