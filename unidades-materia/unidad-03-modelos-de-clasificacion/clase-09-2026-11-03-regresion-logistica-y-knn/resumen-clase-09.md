# Clase 9 - regresión logística y kNN

**Fecha:** 3 de noviembre de 2026  
**Duración:** 1 h 55 min  
**Tema:** primeros modelos y métricas de clasificación

La presentación identifica el contenido como sesión 8. En el orden real del curso corresponde a la
clase 9 porque el 23 de octubre hubo una sesión adicional de repaso.

## Temas vistos

- Diferencia entre predecir una cantidad y predecir una clase.
- Regresión logística con función sigmoide, umbral y pérdida logarítmica.
- Regularización y fronteras no lineales con variables polinomiales.
- Clasificación multiclase con uno contra el resto, uno contra uno y softmax.
- k vecinos más cercanos, elección de `k` y métricas de distancia.
- Importancia del escalado en kNN.
- Exactitud, precisión, recall, F1 y matriz de confusión.
- Problemas de la exactitud cuando las clases están desbalanceadas.

## Minutos de la clase

| Minuto | Contenido |
| --- | --- |
| [00:00:36](z-transcripcion-clase-09-2026-11-03-es.vtt#t=00:00:36) | Organización de los temas que quedan en el curso |
| [00:01:40](z-transcripcion-clase-09-2026-11-03-es.vtt#t=00:01:40) | Inicio de regresión logística y kNN |
| [00:04:49](z-transcripcion-clase-09-2026-11-03-es.vtt#t=00:04:49) | Ejemplo de clasificación de correo spam |
| [00:32:01](z-transcripcion-clase-09-2026-11-03-es.vtt#t=00:32:01) | Pérdida logarítmica en lugar de MSE |
| [00:57:00](z-transcripcion-clase-09-2026-11-03-es.vtt#t=00:57:00) | Clasificación con más de dos clases |
| [01:14:06](z-transcripcion-clase-09-2026-11-03-es.vtt#t=01:14:06) | Inicio de k vecinos más cercanos |
| [01:25:27](z-transcripcion-clase-09-2026-11-03-es.vtt#t=01:25:27) | Elección de vecinos y efecto de `k` |
| [01:34:32](z-transcripcion-clase-09-2026-11-03-es.vtt#t=01:34:32) | Métricas para clasificación |
| [01:37:41](z-transcripcion-clase-09-2026-11-03-es.vtt#t=01:37:41) | Precisión |
| [01:42:29](z-transcripcion-clase-09-2026-11-03-es.vtt#t=01:42:29) | Cuándo priorizar precisión o recall |
| [01:45:56](z-transcripcion-clase-09-2026-11-03-es.vtt#t=01:45:56) | Medida F1 |
| [01:48:48](z-transcripcion-clase-09-2026-11-03-es.vtt#t=01:48:48) | Matriz de confusión |
| [01:50:41](z-transcripcion-clase-09-2026-11-03-es.vtt#t=01:50:41) | Cómo evaluará el profesor el examen del módulo 2 |
| [01:54:08](z-transcripcion-clase-09-2026-11-03-es.vtt#t=01:54:08) | Fecha límite de la segunda entrega |

## Avisos

- La segunda entrega es el examen del módulo 2.
- Se entrega el domingo 8 de noviembre a las 23:00.
- El profesor conservará el conjunto de prueba. Pondrá el archivo junto al notebook para ejecutarlo.
- La siguiente clase quedó anunciada para el jueves 5 de noviembre.
- El profesor planea compactar SVM, Naive Bayes y árboles de clasificación.
- Para el viernes mencionó bagging y boosting en lugar de redes neuronales.

## Actividad de la clase

La presentación pide comparar regresión logística con kNN para clasificar correo spam. El cuaderno
resuelto está en la [práctica 8](../../../tareas-practicas/practicas-clase/practica-08-clasificacion-spam-logistica-knn/resumen-practica-08.md).
La diapositiva lo llama entregable, pero no señala fecha ni lugar de envío.

## Material

- [apuntes de la clase](apuntes-regresion-logistica-y-knn.md)
- [presentación](presentacion-regresion-logistica-y-knn.pdf)
- [transcripción](z-transcripcion-clase-09-2026-11-03-es.vtt)
