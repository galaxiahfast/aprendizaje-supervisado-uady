# Clase 13 - redes neuronales

**Fecha:** 10 de noviembre de 2026

**Duración:** 2 h

**Tema:** introducción a redes neuronales para clasificación

Esta fue la última clase del módulo. La sesión explicó desde el perceptrón hasta una red multicapa,
incluyendo las ideas necesarias para entender cómo se entrena un `MLPClassifier`.

## Temas vistos

- Breve historia de las redes neuronales.
- Perceptrón y límite ante el problema XOR.
- Capas de entrada, ocultas y de salida.
- Capas completamente conectadas.
- Pase hacia adelante y papel de la no linealidad.
- Teorema de aproximación universal.
- Funciones sigmoide, ReLU y softmax.
- Desvanecimiento del gradiente y neuronas ReLU inactivas.
- Descenso de gradiente, regla de la cadena y backpropagation.
- Épocas, tamaño de lote y tasa de aprendizaje.
- Uso de `MLPClassifier`, escalamiento y detención temprana.

## Minutos de la clase

| Minuto | Contenido |
| --- | --- |
| [00:03:17](z-transcripcion-clase-13-2026-11-10-es.vtt#t=00:03:17) | Confirmación de que era la última clase del módulo |
| [00:04:39](z-transcripcion-clase-13-2026-11-10-es.vtt#t=00:04:39) | Breve historia de las redes neuronales |
| [00:16:11](z-transcripcion-clase-13-2026-11-10-es.vtt#t=00:16:11) | Componentes de una neurona artificial |
| [00:31:29](z-transcripcion-clase-13-2026-11-10-es.vtt#t=00:31:29) | Arquitectura con varias capas |
| [00:37:10](z-transcripcion-clase-13-2026-11-10-es.vtt#t=00:37:10) | Capas completamente conectadas |
| [00:43:10](z-transcripcion-clase-13-2026-11-10-es.vtt#t=00:43:10) | Por qué las capas lineales no resuelven XOR |
| [00:45:08](z-transcripcion-clase-13-2026-11-10-es.vtt#t=00:45:08) | Pase hacia adelante |
| [00:49:25](z-transcripcion-clase-13-2026-11-10-es.vtt#t=00:49:25) | Teorema de aproximación universal |
| [01:03:58](z-transcripcion-clase-13-2026-11-10-es.vtt#t=01:03:58) | Sigmoide, softmax y funciones de activación |
| [01:05:35](z-transcripcion-clase-13-2026-11-10-es.vtt#t=01:05:35) | Desvanecimiento del gradiente |
| [01:06:20](z-transcripcion-clase-13-2026-11-10-es.vtt#t=01:06:20) | ReLU y sus ventajas |
| [01:18:54](z-transcripcion-clase-13-2026-11-10-es.vtt#t=01:18:54) | Regla de la cadena para calcular gradientes |
| [01:22:25](z-transcripcion-clase-13-2026-11-10-es.vtt#t=01:22:25) | Idea central de backpropagation |
| [01:31:40](z-transcripcion-clase-13-2026-11-10-es.vtt#t=01:31:40) | Significado de una época |
| [01:33:01](z-transcripcion-clase-13-2026-11-10-es.vtt#t=01:33:01) | Implementación con `MLPClassifier` |
| [01:37:26](z-transcripcion-clase-13-2026-11-10-es.vtt#t=01:37:26) | Uso de lotes para aproximar el gradiente |
| [01:41:50](z-transcripcion-clase-13-2026-11-10-es.vtt#t=01:41:50) | Efecto de la tasa de aprendizaje |
| [01:43:17](z-transcripcion-clase-13-2026-11-10-es.vtt#t=01:43:17) | Detención cuando la validación deja de mejorar |
| [01:45:30](z-transcripcion-clase-13-2026-11-10-es.vtt#t=01:45:30) | Importancia del escalamiento en una MLP |
| [01:49:35](z-transcripcion-clase-13-2026-11-10-es.vtt#t=01:49:35) | Presentación del examen del módulo 3 |
| [01:53:15](z-transcripcion-clase-13-2026-11-10-es.vtt#t=01:53:15) | Fecha anunciada para la tercera evaluación |
| [01:54:37](z-transcripcion-clase-13-2026-11-10-es.vtt#t=01:54:37) | Estado de las calificaciones |
| [01:58:05](z-transcripcion-clase-13-2026-11-10-es.vtt#t=01:58:05) | El formulario aún no estaba disponible durante la clase |

## Avisos del cierre

- El examen del módulo 3 se entrega el domingo 15 de noviembre de 2026 a las 23:00.
- Durante la clase el formulario todavía no estaba listo. Después fue publicado en el sitio oficial.
- No habrá clase el jueves 12 ni el viernes 13 de noviembre.
- El siguiente curso comenzará el martes 17 de noviembre porque el lunes es inhábil.
- El profesor esperaba terminar la revisión del examen 2 durante esa semana.
- La calificación final se estimó para el 21 o 22 de noviembre.

## Actividades relacionadas

- [práctica de redes neuronales](../../../tareas-practicas/practicas-clase/practica-14-redes-neuronales/resumen-practica-14.md)
- [examen del módulo 3](../../../tareas-practicas/tareas-entregables/tarea-03-examen-modulo-03/resumen-tarea-03.md)

## Material

- [apuntes de redes neuronales](apuntes-redes-neuronales.md)
- [presentación oficial](presentacion-redes-neuronales.pdf)
- [ejemplo de MLP desde cero](ejemplo-mlp-desde-cero.ipynb)
- [transcripción](z-transcripcion-clase-13-2026-11-10-es.vtt)

La grabación está guardada en esta carpeta con el prefijo `z-`. Git la ignora y no la sube al
repositorio.
