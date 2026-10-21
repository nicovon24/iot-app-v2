# IoTArg

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Objetivo confirmado: demo de portfolio con un recorrido operativo convincente.

El visitante evalúa el criterio de producto, diseño e implementación. El rol representado en la demo es una persona que supervisa instalaciones y necesita localizar e investigar una condición operativa. Ese rol es una hipótesis de diseño, no evidencia de entrevistas con usuarios reales.

## Product Purpose

Permitir explorar un mapa mundial, con inicio en Sudamérica, y pasar de las ubicaciones de demostración en Argentina, Chile, Perú y Uruguay al contexto de un cliente, una ubicación, un área, un activo y un sensor; entender una lectura y su alarma con datos reproducibles. La cobertura cartográfica mundial no equivale a cobertura IoT mundial.

El recorrido prioritario es detectar una condición, localizar la instalación, abrir el equipo, investigar el sensor y reconocer la alarma. El ejemplo principal es **Porta → Córdoba → Inaudi → Máquina 01 → Sensor 1**.

Éxito esperado para la primera etapa: un visitante completa ese recorrido, comprende que usa una simulación y puede reproducirlo con el mismo escenario y minuto. Su validación en navegador está pendiente.

## Positioning

Una experiencia de operaciones conectadas que une contexto geográfico, jerarquía de equipos y telemetría simulada. ThingsBoard es una referencia de producto y una integración futura; no hay conector operativo actualmente.

## Operating Context

- Etapa actual: prototipo HTML autocontenido, abierto en un navegador.
- Entrada por mapa, cliente, solución o búsqueda.
- El país filtra ubicaciones; no es propietario de los clientes.
- La solución organiza una vista de las entidades existentes.
- Primera etapa de trabajo: mejorar y validar la maqueta. La aplicación Next.js + TypeScript corresponde a una etapa posterior.

## Capabilities and Constraints

- Jerarquía: cliente → ubicación → área → activo → dispositivo.
- Dataset inicial: 4 clientes, 4 ubicaciones, 8 activos y 16 dispositivos; una sola área por ubicación.
- Encuadre inicial sudamericano; el mapa mundial continúa explorable y los países sin instalaciones se presentan sin datos IoT.
- Escenarios de operación normal, sobretemperatura y sensor sin señal.
- Datos deterministas y tiempo de demostración; no telemetría real.
- Mapa Three.js con alternativa SVG y navegación por listados.
- Persistencia limitada al navegador; no cuentas, backend ni almacenamiento compartido.
- Reconocer una alarma indica revisión local; no resuelve la condición ni controla el equipo.
- No hay inferencia predictiva, RAG, manuales conectados ni control sobre equipos reales.
- Pendientes de producto: alcance preciso del MVP posterior, roles reales, fuente de identidad, base de datos, despliegue y contrato del futuro conector.

## Brand Commitments

Nombre: IoTArg. Interfaz principalmente en español. Conservar el contexto operativo y señalar el carácter simulado de los datos. Los detalles de identidad visual se documentan en [DESIGN.md](DESIGN.md).

## Evidence on Hand

- [IoTArg.html](designs/IoTArg.html): implementación existente.
- [README.md](README.md): descripción inicial.
- [Inventario de la maqueta](docs/specs/baseline.md): evidencia estática, límites y validación pendiente.
- Porta es el ejemplo solicitado. No se atribuyen operaciones adicionales reales a esa empresa.
- Aero Demo, Nexo Data y Ruta Sur son organizaciones ficticias del dataset.
- No existen pruebas documentadas de uso por clientes, testimonios ni resultados comerciales.

## Product Principles

1. Mantener el contexto desde la vista global hasta el sensor.
2. Explicar el estado con texto y datos además del color.
3. Hacer reproducible la demostración.
4. Distinguir observaciones, explicaciones ilustrativas y condiciones reales.
5. Priorizar un recorrido completo antes de ampliar familias de soluciones.

## Accessibility & Inclusion

La primera etapa debe permitir completar el recorrido prioritario con teclado y en pantallas pequeñas, conservar una alternativa al mapa 3D y respetar movimiento reducido. Son objetivos de aceptación; no se declara conformidad auditada.

## Especificación y seguimiento

[docs/specs/README.md](docs/specs/README.md) reúne contratos, requisitos y tareas. El estado de ejecución vive únicamente en [tasks.md](docs/specs/tasks.md).
