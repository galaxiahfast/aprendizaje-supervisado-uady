# Clase 2 — preprocesamiento de datos

Fecha: **20 de octubre de 2026**

Duración: **1 h 55 min**

Próxima sesión indicada: **jueves 22 de octubre de 2026**

## Avisos

- El material oficial incluye una actividad individual sobre preprocesamiento.
- La actividad pide un notebook ejecutado y una tabla comparativa.
- No se indicó una fecha posterior. La diapositiva señala trabajarla durante el tiempo restante de la sesión.

## Archivos de la clase

- [apuntes de preprocesamiento](apuntes-preprocesamiento-datos.md)
- [presentación de preprocesamiento](presentacion-preprocesamiento-datos.pdf)
- [transcripción en español](z-transcripcion-clase-02-2026-10-20-es.vtt)
- [transcripción original](z-transcripcion-clase-02-2026-10-20-original.vtt)
- [tarea resuelta](../../../tareas-practicas/tareas-entregables/tarea-01-pipeline-preprocesamiento/resumen-tarea-01.md)

El video `z-video-clase-02-2026-10-20.mp4` está en esta carpeta solo en el equipo. Git no lo sube.

## Minutos y temas

| Minutos | Tema | Contenido |
| --- | --- | --- |
| `00:00-08:40` | Panorama | Presenta faltantes, categorías, escalamiento, particiones y pipelines. |
| `08:40-20:50` | Datos faltantes | Revisa la columna `total_bedrooms` y diferencia MCAR, MAR y MNAR. |
| `21:20-37:20` | Eliminación e imputación | Compara borrar filas, media, mediana, moda y métodos basados en vecinos. |
| `37:20-52:30` | Imputación avanzada | Explica imputación iterativa, indicadores de ausencia y revisión del efecto. |
| `52:30-1:05:08` | Variables categóricas | Distingue categorías nominales y ordinales. Explica one-hot y categorías raras. |
| `1:05:08-1:22:28` | Escalamiento | Compara StandardScaler, MinMaxScaler y RobustScaler. Muestra el efecto en KNN. |
| `1:22:28-1:35:19` | Partición de datos | Explica entrenamiento, validación, prueba, estratificación y validación cruzada. |
| `1:35:19-1:47:03` | Fuga de datos | Señala por qué las transformaciones se ajustan solo con entrenamiento. |
| `1:47:03-1:54:08` | Pipeline completo | Integra imputación, escalado, one-hot y modelo con Pipeline y ColumnTransformer. |
| `1:54:08-1:55:17` | Cierre | Corrige que la siguiente clase será el jueves. |

## Resumen

El preprocesamiento convierte datos incompletos o incompatibles en una entrada adecuada para el
modelo. Cada transformación debe responder al tipo de variable y al algoritmo elegido. La decisión
también debe conservar la separación entre entrenamiento, validación y prueba.

Los faltantes pueden eliminarse o imputarse. Media y mediana son opciones simples. KNN e imputación
iterativa aprovechan relaciones entre variables. Ningún método resuelve por sí solo un mecanismo MNAR.
Cuando la ausencia puede aportar información se agrega un indicador.

Las categorías nominales no tienen orden. Asignarles enteros introduce distancias artificiales.
One-hot crea una columna por categoría. Las categorías ordinales sí requieren un orden explícito.

KNN y los métodos basados en gradiente son sensibles a la escala. Los árboles comparan umbrales y
cambian poco al escalar. StandardScaler usa media y desviación estándar. MinMaxScaler lleva los datos
a un intervalo. RobustScaler usa mediana e IQR para resistir mejor los valores extremos.

La fuga aparece cuando una transformación aprende información fuera del bloque de entrenamiento.
Pipeline y ColumnTransformer ajustan cada paso dentro de la partición correcta. Esto también permite
usar validación cruzada sin repetir el preprocesamiento a mano.

