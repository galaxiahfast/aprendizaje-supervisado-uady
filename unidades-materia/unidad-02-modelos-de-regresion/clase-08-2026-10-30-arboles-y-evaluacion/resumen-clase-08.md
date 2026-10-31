# Clase 8 - árboles y evaluación de modelos

Fecha: **30 de octubre de 2026**

La primera parte retomó el cuaderno de SVR. Después se estudiaron los árboles de decisión para
regresión. Se explicó cómo CART elige cortes, cómo una hoja produce una predicción y por qué un árbol
sin límites puede memorizar los datos.

## Temas vistos

- nodos, raíz, ramas y hojas
- predicción por promedio dentro de una hoja
- cortes de CART mediante MSE ponderado
- profundidad y número mínimo de observaciones por hoja
- sobreajuste y poda
- validación cruzada para elegir complejidad
- inestabilidad de los árboles
- introducción a la comparación entre modelos

Los [apuntes de árboles y evaluación](apuntes-arboles-y-evaluacion.md) reúnen las definiciones y las
decisiones prácticas.

## Minutos de la clase

| Minuto | Contenido |
| --- | --- |
| [00:01:21](z-transcripcion-clase-08-2026-10-30-es.vtt#t=00:01:21) | Presentación del tema de árboles |
| [00:01:40](z-transcripcion-clase-08-2026-10-30-es.vtt#t=00:01:40) | Pregunta sobre el cierre del examen |
| [00:21:55](z-transcripcion-clase-08-2026-10-30-es.vtt#t=00:21:55) | Inicio formal de árboles para regresión |
| [00:29:39](z-transcripcion-clase-08-2026-10-30-es.vtt#t=00:29:39) | Idea del algoritmo CART |
| [00:35:50](z-transcripcion-clase-08-2026-10-30-es.vtt#t=00:35:50) | Estructura de un árbol |
| [00:37:21](z-transcripcion-clase-08-2026-10-30-es.vtt#t=00:37:21) | Nodos finales y hojas |
| [00:38:32](z-transcripcion-clase-08-2026-10-30-es.vtt#t=00:38:32) | Por qué un árbol no necesita escalado |
| [00:40:02](z-transcripcion-clase-08-2026-10-30-es.vtt#t=00:40:02) | Árbol aplicado a regresión |
| [00:43:55](z-transcripcion-clase-08-2026-10-30-es.vtt#t=00:43:55) | Efecto de aumentar la profundidad |
| [00:52:50](z-transcripcion-clase-08-2026-10-30-es.vtt#t=00:52:50) | Construcción mediante CART |
| [00:55:04](z-transcripcion-clase-08-2026-10-30-es.vtt#t=00:55:04) | Sobreajuste en hojas pequeñas |
| [01:42:38](z-transcripcion-clase-08-2026-10-30-es.vtt#t=01:42:38) | Examen abierto hasta las 12 de la noche |
| [01:44:21](z-transcripcion-clase-08-2026-10-30-es.vtt#t=01:44:21) | Actividad para la siguiente semana |

## Actividad entregable

El cuaderno de árboles y evaluación sí se entrega. Pide comparar siete modelos, usar validación
cruzada anidada y preparar un informe breve. La [tarea 2 está lista](../../../tareas-practicas/tareas-entregables/tarea-02-arboles-evaluacion-modelos/resumen-tarea-02.md).

El profesor dijo que se entrega la siguiente semana. No indicó día, hora ni plataforma.

## Siguiente clase

No habrá clase el lunes. La siguiente sesión será el **martes 3 de noviembre de 2026**. Quedó
pendiente continuar la evaluación de modelos antes de pasar a clasificación.

## Archivos de esta clase

- [presentación oficial](presentacion-arboles-y-evaluacion.pdf)
- [transcripción](z-transcripcion-clase-08-2026-10-30-es.vtt)
- [tarea 2](../../../tareas-practicas/tareas-entregables/tarea-02-arboles-evaluacion-modelos/resumen-tarea-02.md)

La grabación está en esta carpeta con el prefijo `z-`. Git la ignora.
