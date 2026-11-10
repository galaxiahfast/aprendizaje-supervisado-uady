# Clase 12 - evaluación e hiperparámetros

**Fecha:** 9 de noviembre de 2026

**Duración:** 1 h 51 min

**Tema:** evaluación con clases desbalanceadas, búsqueda de hiperparámetros y calibración

## Temas vistos

- Problemas de la exactitud cuando la clase de interés aparece pocas veces.
- Coeficiente de correlación de Matthews y kappa de Cohen.
- Diferencia entre métricas duras y log-loss.
- Submuestreo, sobremuestreo, SMOTE y pesos de clase.
- GridSearchCV, RandomizedSearchCV, HalvingGridSearchCV y Optuna.
- Calibración de probabilidades con `CalibratedClassifierCV`.
- Uso de un conjunto separado para calibrar un modelo ya entrenado.

## Minutos de la clase

| Minuto | Contenido |
| --- | --- |
| [00:00:22](z-transcripcion-clase-12-2026-11-09-es.vtt#t=00:00:22) | Las calificaciones del examen 1 todavía no eran definitivas |
| [00:02:07](z-transcripcion-clase-12-2026-11-09-es.vtt#t=00:02:07) | Aclaración sobre el orden real de las unidades |
| [00:08:00](z-transcripcion-clase-12-2026-11-09-es.vtt#t=00:08:00) | Inicio del problema de clases desbalanceadas |
| [00:16:00](z-transcripcion-clase-12-2026-11-09-es.vtt#t=00:16:00) | Coeficiente de correlación de Matthews |
| [00:20:00](z-transcripcion-clase-12-2026-11-09-es.vtt#t=00:20:00) | Kappa de Cohen |
| [00:34:00](z-transcripcion-clase-12-2026-11-09-es.vtt#t=00:34:00) | Métricas duras frente a métricas suaves |
| [00:37:00](z-transcripcion-clase-12-2026-11-09-es.vtt#t=00:37:00) | Interpretación de log-loss |
| [00:44:53](z-transcripcion-clase-12-2026-11-09-es.vtt#t=00:44:53) | Estrategias para datos desbalanceados |
| [00:45:35](z-transcripcion-clase-12-2026-11-09-es.vtt#t=00:45:35) | Submuestreo y pérdida de información |
| [00:48:00](z-transcripcion-clase-12-2026-11-09-es.vtt#t=00:48:00) | Sobremuestreo de la clase minoritaria |
| [00:52:28](z-transcripcion-clase-12-2026-11-09-es.vtt#t=00:52:28) | Generación de observaciones con SMOTE |
| [00:58:49](z-transcripcion-clase-12-2026-11-09-es.vtt#t=00:58:49) | Pesos de clase |
| [01:07:15](z-transcripcion-clase-12-2026-11-09-es.vtt#t=01:07:15) | Costo de una búsqueda exhaustiva |
| [01:08:31](z-transcripcion-clase-12-2026-11-09-es.vtt#t=01:08:31) | RandomizedSearchCV |
| [01:10:48](z-transcripcion-clase-12-2026-11-09-es.vtt#t=01:10:48) | HalvingGridSearchCV |
| [01:14:34](z-transcripcion-clase-12-2026-11-09-es.vtt#t=01:14:34) | Optuna y búsqueda adaptativa |
| [01:18:33](z-transcripcion-clase-12-2026-11-09-es.vtt#t=01:18:33) | Inicio de calibración de probabilidades |
| [01:36:43](z-transcripcion-clase-12-2026-11-09-es.vtt#t=01:36:43) | Uso de `CalibratedClassifierCV` |
| [01:39:59](z-transcripcion-clase-12-2026-11-09-es.vtt#t=01:39:59) | Aclaración sobre la revisión del examen 2 |
| [01:42:50](z-transcripcion-clase-12-2026-11-09-es.vtt#t=01:42:50) | Redes neuronales anunciadas para el 10 de noviembre |
| [01:44:50](z-transcripcion-clase-12-2026-11-09-es.vtt#t=01:44:50) | Posible evaluación final mediante formulario |

## Avisos

- Las calificaciones publicadas del examen 1 seguían en revisión. El profesor indicó que algunos puntajes podían subir.
- El examen 2 se revisará con los datos disponibles de entrenamiento y validación porque el conjunto privado no fue compartido.
- Para el 10 de noviembre anunció una explicación breve de redes neuronales.
- Comentó que no habría clase el jueves 12 ni el viernes 13 de noviembre.
- Consideraba una evaluación corta mediante formulario para el jueves o viernes, pero no confirmó fecha, enlace ni instrucciones.
- El curso de aprendizaje no supervisado comenzaría el lunes 16 de noviembre con otro profesor.

## Actividad de la clase

La presentación pide un flujo completo de detección de fraude. El cuaderno resuelto está en la
[práctica 11](../../../tareas-practicas/practicas-clase/practica-11-evaluacion-fraude/resumen-practica-11.md).
La diapositiva lo llama entregable, pero no señala fecha ni lugar de envío.

## Material

- [apuntes de la clase](apuntes-evaluacion-e-hiperparametros.md)
- [presentación](presentacion-evaluacion-e-hiperparametros.pdf)
- [transcripción](z-transcripcion-clase-12-2026-11-09-es.vtt)
