# Clase 11 - bagging, Random Forest y AdaBoost

**Fecha:** 6 de noviembre de 2026

**Duración:** 1 h 58 min

**Tema:** métodos de ensamble para reducir varianza y corregir errores

## Temas vistos

- Diferencia entre ensambles paralelos y secuenciales.
- Remuestreo bootstrap con reemplazo.
- Observaciones fuera de bolsa y error OOB.
- Bagging para clasificación y regresión.
- Random Forest como bagging con selección aleatoria de variables.
- Importancia de variables en un bosque.
- AdaBoost con árboles de profundidad uno.
- Peso de cada aprendiz y actualización de observaciones mal clasificadas.

## Minutos de la clase

| Minuto | Contenido |
| --- | --- |
| [00:01:08](z-transcripcion-clase-11-2026-11-06-es.vtt#t=00:01:08) | Presentación de bagging y boosting |
| [00:03:50](z-transcripcion-clase-11-2026-11-06-es.vtt#t=00:03:50) | Diferencia entre ensamble paralelo y secuencial |
| [00:06:25](z-transcripcion-clase-11-2026-11-06-es.vtt#t=00:06:25) | Inicio del remuestreo bootstrap |
| [00:09:24](z-transcripcion-clase-11-2026-11-06-es.vtt#t=00:09:24) | Observaciones fuera de bolsa |
| [00:11:30](z-transcripcion-clase-11-2026-11-06-es.vtt#t=00:11:30) | Tamaño aproximado del conjunto OOB |
| [00:14:12](z-transcripcion-clase-11-2026-11-06-es.vtt#t=00:14:12) | Bagging con distintos modelos base |
| [00:18:00](z-transcripcion-clase-11-2026-11-06-es.vtt#t=00:18:00) | Implementación con `BaggingClassifier` |
| [00:26:00](z-transcripcion-clase-11-2026-11-06-es.vtt#t=00:26:00) | Problema de una variable dominante |
| [00:34:19](z-transcripcion-clase-11-2026-11-06-es.vtt#t=00:34:19) | Random Forest y selección aleatoria de variables |
| [00:38:16](z-transcripcion-clase-11-2026-11-06-es.vtt#t=00:38:16) | Importancia de variables |
| [00:44:44](z-transcripcion-clase-11-2026-11-06-es.vtt#t=00:44:44) | Implementación de bagging paso a paso |
| [01:03:11](z-transcripcion-clase-11-2026-11-06-es.vtt#t=01:03:11) | Inicio de boosting y AdaBoost |
| [01:04:49](z-transcripcion-clase-11-2026-11-06-es.vtt#t=01:04:49) | Aprendices débiles y árboles de profundidad uno |
| [01:06:29](z-transcripcion-clase-11-2026-11-06-es.vtt#t=01:06:29) | Peso del voto de cada aprendiz |
| [01:16:06](z-transcripcion-clase-11-2026-11-06-es.vtt#t=01:16:06) | Aumento de peso en observaciones mal clasificadas |
| [01:30:26](z-transcripcion-clase-11-2026-11-06-es.vtt#t=01:30:26) | Evolución del error y riesgo de memorizar |
| [01:50:15](z-transcripcion-clase-11-2026-11-06-es.vtt#t=01:50:15) | Preguntas sobre la búsqueda de hiperparámetros del examen 2 |
| [01:52:26](z-transcripcion-clase-11-2026-11-06-es.vtt#t=01:52:26) | Validación cruzada anidada opcional |
| [01:55:01](z-transcripcion-clase-11-2026-11-06-es.vtt#t=01:55:01) | Cambio en la revisión del conjunto privado de prueba |

## Avisos

- Gradient Boosting y XGBoost quedaron pendientes para otra sesión.
- En el examen 2 se podía usar el método de búsqueda de hiperparámetros que cada estudiante eligiera.
- La validación cruzada anidada no era obligatoria.
- El profesor decidió omitir la ejecución sobre un conjunto privado de prueba.
- Para calificar revisaría el notebook y sus resultados guardados, sin volver a entrenar todos los modelos.
- La siguiente clase quedó anunciada para el lunes 9 de noviembre.

## Actividades relacionadas

Las presentaciones oficiales incluyen dos cuadernos individuales:

- [Práctica 12 - bagging y Random Forest](../../../tareas-practicas/practicas-clase/practica-12-bagging-random-forest/resumen-practica-12.md)
- [Práctica 13 - boosting](../../../tareas-practicas/practicas-clase/practica-13-boosting-clasificacion/resumen-practica-13.md)

Las diapositivas llaman entregables a ambos cuadernos. No indican fecha ni plataforma.

## Material

- [apuntes de la clase](apuntes-bagging-random-forest-y-adaboost.md)
- [presentación de bagging y Random Forest](presentacion-bagging-y-random-forest.pdf)
- [presentación de boosting](presentacion-boosting.pdf)
- [transcripción](z-transcripcion-clase-11-2026-11-06-es.vtt)
