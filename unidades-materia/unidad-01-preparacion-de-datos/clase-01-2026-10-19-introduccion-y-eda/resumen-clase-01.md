# Clase 1 — introducción al curso y EDA

Fecha: **19 de octubre de 2026**

Duración: **2 h 09 min**

Próxima sesión indicada: **20 de octubre de 2026 a las 18:00**

## Avisos

- La práctica de California Housing no se entrega.
- No hay fechas de entrega publicadas.
- La evaluación se reparte en laboratorios 30 %, proyecto de regresión 35 % y proyecto de clasificación 35 %.

## Archivos de la clase

- [apuntes de EDA](apuntes-eda.md)
- [presentación de la unidad](presentacion-unidad-01-eda.pdf)
- [transcripción en español](z-transcripcion-clase-01-2026-10-19-es.vtt)
- [transcripción original](z-transcripcion-clase-01-2026-10-19-original.vtt)
- [práctica resuelta](../../../tareas-practicas/practicas-clase/practica-01-eda-california-housing/resumen-practica-01.md)

El video `z-video-clase-01-2026-10-19.mp4` está en esta carpeta solo en el equipo. Git no lo sube.

## Minutos y temas

Los tramos registrados suman cerca de **57 minutos**. A velocidad `1.5x` duran unos **38 minutos**.

| Minutos | Tema | Contenido |
| --- | --- | --- |
| `03:31-04:34` | Evaluación | Diferencia las prácticas de los trabajos calificables. |
| `11:29-20:30` | Aprendizaje supervisado | Explica entradas, salida, pérdida y regularización. |
| `27:07-31:10` | Generalización | Compara subajuste, sobreajuste y memorización. |
| `48:49-51:04` | Cuarteto de Anscombe | Muestra por qué los números no bastan. |
| `57:13-1:00:11` | Medidas de centro | Media, mediana, moda y valores extremos. |
| `1:03:00-1:08:49` | Posición y forma | Cuantiles, IQR y asimetría. |
| `1:14:42-1:22:06` | Preparación | Transformaciones, histogramas, boxplots y atípicos. |
| `1:27:43-1:42:33` | Correlación | Pearson, Spearman y efecto de los extremos. |
| `1:44:48-1:49:20` | Interpretación | Causalidad y variables confusoras. |
| `1:51:00-1:55:17` | Flujo de EDA | Presenta el proceso completo y la práctica. |
| `2:08:34-2:09:23` | Entregas | Confirma que la práctica actual no se entrega. |

## Resumen

El aprendizaje supervisado usa variables de entrada y una salida conocida. Una salida continua
corresponde a regresión. Una categoría corresponde a clasificación. El objetivo es aprender un
patrón que funcione con datos nuevos, no memorizar el entrenamiento.

El análisis exploratorio permite conocer los datos antes de modelar. Ayuda a detectar errores,
sesgos, topes y relaciones engañosas. El cuarteto de Anscombe prueba que varias tablas pueden tener
estadísticas parecidas aunque sus gráficas sean muy distintas.

### Ideas clave

- La media cambia mucho ante valores extremos. La mediana suele resistir mejor.
- El IQR ayuda a localizar observaciones inusuales.
- Un valor inusual no siempre es un error.
- Pearson mide relaciones lineales. Spearman trabaja con rangos.
- Una correlación alta no demuestra causalidad.
- La multicolinealidad puede volver inestable un modelo.

Sobre los datos raros, el criterio anotado fue revisar su origen antes de eliminarlos. El efecto se
compara con el dato y sin él. La decisión queda documentada.
