# Datos, simulación y estado

Este documento distingue el contrato observado del comportamiento propuesto. No prescribe todavía un esquema de base de datos.

## Entidades actuales

| Entidad | Identidad y relación |
| --- | --- |
| Cliente | ID estable; posee ubicaciones |
| Ubicación | ID, referencia al cliente, país, coordenadas, área textual y soluciones |
| Área | Actualmente campo de ubicación; no tiene colección independiente |
| Activo | ID y referencia a ubicación; pertenencia al área implícita |
| Dispositivo | ID único, activo, ubicación, métrica, unidad, base y umbrales |
| Solución | ID y familia; selecciona ubicaciones y una representación de sus datos |
| Alarma | Derivada del estado de un dispositivo; no hay registro histórico independiente |

En una migración, preservar IDs o definir una conversión explícita para enlaces guardados. No introducir múltiples áreas reutilizando un campo textual como clave única.

## Alcance observado

`scopedLocations()` intersecta cliente, país y solución. `scopedDevices()` toma dispositivos de esas ubicaciones. En esta versión una solución filtra ubicaciones; no garantiza que cada dispositivo de la ubicación sea específico de la solución.

Los estados agregados de ubicación y país priorizan `red > yellow > offline > green`. `none` expresa ausencia de ubicaciones en el alcance, no un equipo sano. Alarmas incluye rojo, amarillo y sin señal.

## Simulación observada

- Tiempo de 0 a 60 minutos, mostrado como 10:00–11:00.
- Valores determinados por dispositivo, escenario y minuto mediante `value()`.
- Sobretemperatura: `p1s1` incrementa temperatura después del minuto 10; `n1s1` después del minuto 8.
- Sin señal: `p1s2` devuelve estado offline desde el minuto 12.
- Crítico: valor mayor o igual al umbral crítico; advertencia: mayor o igual al umbral de advertencia; normal en otro caso.
- Ventanas de gráfica: escenario completo o últimos 15 minutos.
- Reconocimientos: `Set` en memoria. Seleccionar un escenario con su botón o restablecer demo los borra; recargar también. Cambiar escenario mediante Atrás/Adelante no limpia el `Set`, por lo que puede reaparecer un reconocimiento anterior.

`value()` sigue calculando números cuando un dispositivo está sin señal. Por eso cálculo interno y lectura presentada no deben considerarse equivalentes. La definición exacta de última muestra disponible se resolverá con DATA-004 antes de modificar la gráfica.

## URL y persistencia observadas

| Campo URL | Valores / función |
| --- | --- |
| `view` | Vista global, secciones o detalle |
| `customer` | `all` o ID de cliente |
| `country` | Código de país de la cartografía |
| `id` | ID de entidad de detalle |
| `solution` | ID de solución |
| `scenario` | `normal`, `overheat`, `offline` |
| `time` | Número acotado a 0–60 |
| `layer` | `health`, `devices`, `coverage` |
| `range` | 60 o 15 |

Ejemplo existente:

```text
#view=device&customer=porta&country=AR&id=p1s1&layer=health&range=60
```

El tema se guarda en `iotarg-theme`. Una vista se guarda en `iotarg-dashboard`. El fragmento no transporta reconocimiento de alarmas, tema ni estado de reproducción. `alarmFilter` tampoco forma parte de los campos serializados por `writeHash()`. El portapapeles copia la URL cuando está disponible; no sube el HTML.

Pendiente para IMP-05: decidir y validar si el cambio de escenario por historial debe limpiar reconocimientos igual que el botón. La diferencia actual es comportamiento observado, no una regla de producto confirmada.

## Requisitos para evolución

| ID | Aceptación observable |
| --- | --- |
| DATA-001 | Con mismos IDs, escenario y minuto se obtienen los mismos valores y estados en todas las vistas; cambiar la ventana no cambia el valor actual. |
| DATA-002 | Cambiar cliente/país/solución recalcula ubicaciones, dispositivos, KPI, alarmas y vistas relacionadas bajo el mismo alcance. |
| DATA-003 | Una condición roja domina amarilla; amarilla domina sin señal; sin señal domina normal en agregados. Ausencia de cobertura se muestra como sin datos. |
| DATA-004 | Definir el último reporte previo a desconexión; desde el minuto 12 `p1s2` no presenta una lectura calculada posterior como nueva medición. Etiquetas visibles, gráfica y nombre accesible coinciden. |
| DATA-005 | Reconocimiento no modifica telemetría ni severidad. Recarga y cambio de escenario respetan el alcance de persistencia documentado. |
| DATA-006 | URL malformada, ID desconocido y combinación incompatible de entidad/cliente/país/solución se normalizan de forma determinista o muestran una recuperación explícita, sin error de render ni contexto contradictorio. |
| DATA-007 | Guardar/restaurar dashboard y cambiar tema toleran ausencia o contenido inválido de `localStorage`; la UI informa resultado sin bloquear navegación. |
| DATA-008 | Una fixture adicional representa cliente con varios países, varios clientes en un país y ubicación con varias áreas antes de declarar soporte de esos casos en la aplicación. |

DATA-004 admite como propuesta usar el minuto 11 como última muestra entera, dado el inicio offline en 12. La resolución debe quedar registrada antes de implementar; hoy la gráfica usa un límite de 12 y no se declara corregida.

## Evolución de dominio propuesta

Separar `Area`, `TelemetrySample` y `Alarm` cuando la aplicación requiera varias áreas, historial y reconocimiento persistido. Distinguir timestamp del evento, tiempo de recepción y estado de conectividad. Definir claves del proveedor y unidades normalizadas en el adaptador, sin propagar directamente su esquema por la UI.

Estas son decisiones de arquitectura pendientes de implementación y no implican una base de datos o un proveedor ya seleccionado.
