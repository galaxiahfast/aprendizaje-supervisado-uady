# Clase 4 — repaso y preparación de la evaluación

Fecha: **23 de octubre de 2026**

Esta sesión reunió lo principal de las tres clases anteriores. El profesor explicó cómo será la
primera evaluación, repasó el flujo de preparación de datos y abrió el cuaderno de EDA para comentar
las preguntas.

## Temas vistos

- Separar prueba antes de aprender estadísticas o tomar decisiones sobre los datos.
- Repetir el preprocesamiento dentro de cada pliegue de validación cruzada.
- Revisar faltantes, atípicos, topes y distribuciones antes de transformar variables.
- Elegir entre Pearson y Spearman según la forma de la relación y la presencia de extremos.
- Imputar, codificar y escalar dentro de un `Pipeline`.
- Crear variables con sentido para el problema.
- Detectar redundancia con correlaciones, VIF y métodos de selección.
- Interpretar los resultados del cuaderno de California Housing.

Los [apuntes del repaso](apuntes-repaso-y-evaluacion.md) reúnen las ideas que conviene conservar.

## Minutos de la clase

| Minuto | Contenido |
| --- | --- |
| [00:03:15](z-transcripcion-clase-04-2026-10-23-es.vtt#t=00:03:15) | Forma de entrega, datos del formulario y uso del notebook |
| [00:11:14](z-transcripcion-clase-04-2026-10-23-es.vtt#t=00:11:14) | Inicio del repaso de las unidades 1 a 3 |
| [00:12:57](z-transcripcion-clase-04-2026-10-23-es.vtt#t=00:12:57) | Fuga de datos y decisiones aprendidas solo con entrenamiento |
| [00:21:31](z-transcripcion-clase-04-2026-10-23-es.vtt#t=00:21:31) | Regla del IQR y tratamiento de valores atípicos |
| [00:23:47](z-transcripcion-clase-04-2026-10-23-es.vtt#t=00:23:47) | Pearson, Spearman y matrices de correlación |
| [00:28:16](z-transcripcion-clase-04-2026-10-23-es.vtt#t=00:28:16) | Tipos de faltantes e imputación |
| [00:31:27](z-transcripcion-clase-04-2026-10-23-es.vtt#t=00:31:27) | Codificación y escalamiento |
| [00:33:32](z-transcripcion-clase-04-2026-10-23-es.vtt#t=00:33:32) | División estratificada y conservación de proporciones |
| [00:35:17](z-transcripcion-clase-04-2026-10-23-es.vtt#t=00:35:17) | Pipeline de preprocesamiento |
| [00:38:01](z-transcripcion-clase-04-2026-10-23-es.vtt#t=00:38:01) | Ingeniería y selección de variables |
| [00:40:28](z-transcripcion-clase-04-2026-10-23-es.vtt#t=00:40:28) | Selección dentro de validación cruzada |
| [00:42:32](z-transcripcion-clase-04-2026-10-23-es.vtt#t=00:42:32) | Las tres prácticas no se entregan |
| [00:44:23](z-transcripcion-clase-04-2026-10-23-es.vtt#t=00:44:23) | Revisión del notebook de EDA |
| [01:20:02](z-transcripcion-clase-04-2026-10-23-es.vtt#t=01:20:02) | Correlación y multicolinealidad en California Housing |
| [01:31:40](z-transcripcion-clase-04-2026-10-23-es.vtt#t=01:31:40) | Pregunta sobre selección de variables sin fuga |
| [01:39:53](z-transcripcion-clase-04-2026-10-23-es.vtt#t=01:39:53) | Pregunta sobre atípicos al dividir los datos |
| [01:45:18](z-transcripcion-clase-04-2026-10-23-es.vtt#t=01:45:18) | Confirmación de la fecha límite |

## Evaluación confirmada

- Se entrega el notebook de la evaluación, no los tres cuadernos de práctica.
- La entrega será mediante un formulario.
- El formulario pide nombre completo, correo electrónico y matrícula.
- El notebook debe guardar el nombre del estudiante en la variable `NOMBRE`.
- Las respuestas deben ir donde el notebook indique `Respuesta:`.
- El archivo debe ejecutarse completo y conservar los nombres solicitados.
- Se sube un solo `.ipynb` de máximo 10 MB con el nombre `apellido_nombre_examen_modulo1.ipynb`.
- Es posible reenviar antes del cierre. Se revisa el último archivo recibido.
- Fecha límite confirmada: **sábado 31 de octubre de 2026**.

El notebook de la evaluación todavía no está en los materiales disponibles. Su estado está en la
[tarea 1](../../../tareas-practicas/tareas-entregables/tarea-01-examen-modulo-01/resumen-tarea-01.md).

## Archivos de esta clase

- [presentación de repaso](presentacion-repaso-unidades-01-a-03.pdf)
- [transcripción limpia](z-transcripcion-clase-04-2026-10-23-es.vtt)
- [transcripción original](z-transcripcion-clase-04-2026-10-23-original.vtt)

La grabación está guardada aquí con el prefijo `z-`. Git la ignora y no se sube al repositorio.
