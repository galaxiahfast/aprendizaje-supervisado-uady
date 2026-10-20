# Clase 1 - Introducción al curso y análisis exploratorio de datos

> Fecha: **19 de octubre de 2026**  
> Duración: **2 h 09 min**  
> Siguiente sesión confirmada en la grabación: **20 de octubre de 2026 a las 18:00**

## Todo lo de esta clase

- [Resumen y minutos clave](README.md) — este documento.
- [Guía rápida de EDA](GUIA_RAPIDA_EDA.md).
- [Práctica resuelta y ejecutada](PRACTICA_EDA_CALIFORNIA_HOUSING_RESUELTA.ipynb).
- [Tabla de decisiones de la práctica](PRACTICA_EDA_DECISIONES.csv).
- [Presentación oficial de la unidad](PRESENTACION_UNIDAD_01_EDA.pdf).

## Lo urgente

- La notebook de California Housing es una **práctica no entregable**. Conviene resolverla y llevar
  dudas a la siguiente clase, pero no subirla como evidencia.
- Aún **no hay fechas de entrega publicadas**.
- La evaluación es: laboratorios 30 %, miniproyecto de regresión 35 % y miniproyecto de
  clasificación 35 %.
- El profesor espera pedir al menos una actividad por semana y avisará cuáles se entregan.

## Ruta corta de la grabación

Los siguientes tramos suman aproximadamente **57 minutos**; a `1.5x` toman cerca de **38 minutos**.

| Minutos | Tema | Por qué verlo |
| --- | --- | --- |
| `03:31-04:34` | Evaluación | Aclara que no todas las notebooks se entregan y presenta los porcentajes. |
| `11:29-20:30` | Qué es aprendizaje supervisado | Datos etiquetados, $X$, $y$, modelo, pérdida y regularización. |
| `27:07-31:10` | Generalización | Diferencia entre subajuste, sobreajuste y memorizar los datos. |
| `48:49-51:04` | Cuarteto de Anscombe | Demuestra por qué hay que combinar resúmenes con gráficas. |
| `57:13-1:00:11` | Centro | Media, mediana, moda y sensibilidad de la media a extremos. |
| `1:03:00-1:08:49` | Posición y forma | Cuantiles, cuartiles, IQR y signo de la asimetría. |
| `1:14:42-1:22:06` | Preparación práctica | Logaritmos, ancho de histogramas, boxplots y decisiones sobre atípicos. |
| `1:27:43-1:42:33` | Correlación | Pearson, Spearman, relaciones lineales y efecto de los valores extremos. |
| `1:44:48-1:49:20` | Interpretación | Causalidad, variables confusoras, matrices y mapas de calor. |
| `1:51:00-1:55:17` | Receta de EDA | Resume el flujo completo y presenta la notebook de práctica. |
| `2:08:34-2:09:23` | Entregas | Confirma que aún no hay fechas y que esta notebook no se entrega. |

Si solo hay 20 minutos, mira a `1.5x` los tramos de Anscombe, centro, atípicos,
Pearson/Spearman y la aclaración final de entregas.

## Resumen de la clase

### Organización de la materia

El curso tiene 14 sesiones de dos horas. El horario habitual indicado es lunes, martes, jueves y
viernes de 18:00 a 20:00. Los cuatro bloques son preparación de datos, regresión, clasificación y
métodos de ensamble. Se trabajará principalmente con Python, pandas, NumPy, Matplotlib y
scikit-learn; el curso no depende de PyTorch o TensorFlow.

No todas las notebooks cuentan para calificación. El profesor publicará material de práctica con
frecuencia y señalará cuáles deben devolverse. Planea un miniproyecto de regresión alrededor del
cierre de la segunda semana y otro de clasificación al final del curso, con días adicionales para
terminarlo; todavía no fijó fechas exactas.

### Fundamentos de aprendizaje supervisado

- En aprendizaje supervisado cada ejemplo tiene variables de entrada $X$ y una salida conocida $y$.
- Si la salida es continua, el problema es de **regresión**; si es una categoría, es de
  **clasificación**.
- Entrenar consiste en construir una función aproximada que minimice una pérdida sobre una muestra.
- El objetivo real no es memorizar el entrenamiento, sino generalizar a datos nuevos.
- Un modelo demasiado simple subajusta; uno demasiado complejo puede sobreajustar y obtener error
  casi cero en entrenamiento, pero fallar fuera de muestra.
- La regularización incorpora restricciones o conocimiento para reducir soluciones sensibles al
  ruido.

### Por qué el EDA va antes del modelo

El flujo planteado fue: datos crudos -> inspección -> limpieza y transformación -> construcción de
atributos -> modelo -> evaluación. Saltarse la exploración puede ocultar errores, censura,
distribuciones inadecuadas o variables redundantes.

El cuarteto de Anscombe muestra la idea central: cuatro conjuntos pueden compartir media, varianza,
correlación y recta de ajuste, pero tener formas completamente distintas. Los números resumen; las
gráficas revelan la estructura que el resumen perdió.

### Conceptos que hay que dominar

- **Media, mediana y moda:** la media es sensible a valores extremos; mediana y moda son más
  robustas en distribuciones sesgadas.
- **Varianza y desviación estándar:** cuantifican dispersión alrededor de la media. El puntaje z
  expresa una observación en unidades de desviación estándar.
- **Cuantiles e IQR:** $Q_1$, mediana y $Q_3$ dividen los datos ordenados. El IQR describe el 50 %
  central y las cercas de $1.5\,IQR$ detectan observaciones inusuales.
- **Asimetría:** el signo indica hacia dónde se alarga la cola. Una transformación logarítmica puede
  reducir una cola derecha, pero debe evaluarse por variable.
- **Curtosis:** la presentación oficial la interpreta como peso de las colas y presencia de extremos,
  no simplemente como qué tan puntiaguda se ve una curva.
- **Pearson:** mide asociación lineal y es sensible a valores extremos.
- **Spearman:** calcula Pearson sobre rangos; es útil con atípicos o relaciones monótonas no lineales.
- **Correlación no implica causalidad:** una tercera variable puede producir una asociación alta.
- **Multicolinealidad:** predictores muy correlacionados pueden volver inestables algunos modelos;
  hay que revisar si la relación es estructural o está creada por pocas filas extremas.

### Regla práctica para los valores atípicos

La regla del IQR identifica lo inusual, no lo incorrecto. Antes de borrar una fila hay que decidir si
es un error de captura, un dato real pero raro o un valor censurado. También importa el modelo:
regresiones lineales y logísticas suelen ser sensibles, mientras que los árboles son más robustos.
La decisión debe documentarse y compararse con resultados antes y después del tratamiento.

## Actividad asociada

La [práctica resuelta de EDA de California Housing](PRACTICA_EDA_CALIFORNIA_HOUSING_RESUELTA.ipynb)
pide revisar forma, tipos, estadísticos, histogramas, boxplots, atípicos, topes, transformaciones,
correlaciones y VIF, y terminar con una [tabla de decisiones](PRACTICA_EDA_DECISIONES.csv). Está
ejecutada para estudio, pero el profesor aclaró que **no debe entregarse**.

## Archivos de la sesión

- [Transcripción original de la plataforma](_FUENTES_CLASE/CLASE_01_2026-10-19_ORIGINAL.vtt)
- [Retranscripción local en español](_FUENTES_CLASE/CLASE_01_2026-10-19_RETRANSCRIPCION_ES.vtt)
- [Presentación oficial](PRESENTACION_UNIDAD_01_EDA.pdf)

La grabación está en `_FUENTES_CLASE/_VIDEO_LOCAL/CLASE_01_2026-10-19.mp4`; se conserva únicamente
en el equipo y está excluida de GitHub.
