# Clase 1 — introducción y análisis exploratorio de datos

> Fecha: **19 de octubre de 2026** · Duración: **2 h 09 min** · Siguiente sesión indicada:
> **20 de octubre de 2026 a las 18:00**

## Lo urgente

- La práctica de California Housing es para estudiar y **no se entrega**.
- No hay fechas de entrega publicadas.
- La evaluación es: laboratorios 30 %, proyecto de regresión 35 % y proyecto de clasificación 35 %.

## Archivos de esta clase

- [guía rápida de EDA](guia-rapida-eda.md)
- [práctica resuelta y ejecutada](practica-eda-california-housing-resuelta.ipynb)
- [tabla de decisiones de la práctica](practica-eda-decisiones.csv)
- [presentación de la unidad](presentacion-unidad-01-eda.pdf)
- [transcripción en español](z-transcripcion-clase-01-2026-10-19-es.vtt)
- [transcripción original](z-transcripcion-clase-01-2026-10-19-original.vtt)

El video `z-video-clase-01-2026-10-19.mp4` está en esta misma carpeta, pero solo en el equipo: Git
lo excluye automáticamente.

## Minutos importantes

Los tramos indispensables suman aproximadamente **57 minutos**; a velocidad `1.5x` toman cerca de
**38 minutos**.

| Minutos | Tema | Motivo |
| --- | --- | --- |
| `03:31-04:34` | Evaluación | Distingue prácticas de actividades calificables y explica porcentajes. |
| `11:29-20:30` | Aprendizaje supervisado | Datos etiquetados, entradas, salida, pérdida y regularización. |
| `27:07-31:10` | Generalización | Subajuste, sobreajuste y memorización. |
| `48:49-51:04` | Cuarteto de Anscombe | Explica por qué los resúmenes numéricos no bastan. |
| `57:13-1:00:11` | Centro | Media, mediana, moda y valores extremos. |
| `1:03:00-1:08:49` | Posición y forma | Cuantiles, cuartiles, IQR y asimetría. |
| `1:14:42-1:22:06` | Preparación | Transformaciones, histogramas, boxplots y atípicos. |
| `1:27:43-1:42:33` | Correlación | Pearson, Spearman y efecto de los valores extremos. |
| `1:44:48-1:49:20` | Interpretación | Correlación, causalidad y variables confusoras. |
| `1:51:00-1:55:17` | Receta de EDA | Flujo completo y explicación de la práctica. |
| `2:08:34-2:09:23` | Entregas | Confirma que esta práctica no se entrega. |

Si solo hay 20 minutos, conviene revisar Anscombe, medidas de centro, tratamiento de atípicos,
Pearson frente a Spearman y la aclaración final sobre entregas.

## Resumen

El aprendizaje supervisado utiliza variables de entrada y una salida conocida. Una salida continua
define un problema de regresión; una categoría define clasificación. Entrenar consiste en ajustar
una función que reduzca el error sin memorizar los datos, pues el objetivo es funcionar bien con
observaciones nuevas.

El análisis exploratorio ocurre antes del modelo: inspecciona, limpia, transforma y documenta los
datos. El cuarteto de Anscombe demuestra que conjuntos con estadísticas casi idénticas pueden tener
formas muy diferentes, por lo que siempre hay que combinar números y gráficas.

### Conceptos clave

- La media es sensible a valores extremos; mediana y moda son más robustas ante sesgo.
- El IQR describe el 50 % central y ayuda a detectar observaciones inusuales.
- Un dato marcado por IQR no es automáticamente incorrecto: puede ser raro, censurado o legítimo.
- Pearson mide asociación lineal y es sensible a extremos; Spearman trabaja con rangos.
- Correlación no implica causalidad y una tercera variable puede explicar la asociación.
- Predictores muy correlacionados pueden volver inestables algunos modelos.

Antes de eliminar un atípico hay que justificar si es error, observación real o valor censurado y
comparar el desempeño del modelo antes y después. La decisión debe realizarse sin fuga de
información y quedar documentada.

## Práctica asociada

La práctica revisa forma, tipos, estadísticos, histogramas, boxplots, atípicos, topes,
transformaciones, correlaciones y VIF. Quedó resuelta y ejecutada sin errores para estudiar, pero no
debe copiarse a una entrega mientras el profesor no cambie la indicación.
