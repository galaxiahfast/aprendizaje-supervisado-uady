# Clase 10 - Naive Bayes, árboles y curva ROC

**Fecha:** 5 de noviembre de 2026  
**Duración:** 1 h 59 min  
**Tema:** modelos probabilísticos, árboles de clasificación y evaluación con ROC-AUC

## Temas vistos

- Teorema de Bayes y supuesto de independencia condicional.
- Diferencias entre GaussianNB, MultinomialNB y BernoulliNB.
- Clasificación de texto con conteos o presencia de palabras.
- Árboles de clasificación con impureza Gini y entropía.
- Elección de variables y umbrales para dividir un nodo.
- Inestabilidad de los árboles y relación con los métodos de ensamble.
- Tasa de verdaderos positivos, tasa de falsos positivos y curva ROC.
- Comparación de modelos mediante el área bajo la curva.

## Minutos de la clase

| Minuto | Contenido |
| --- | --- |
| [00:03:01](z-transcripcion-clase-10-2026-11-05-es.vtt#t=00:03:01) | Inicio de Naive Bayes |
| [00:12:04](z-transcripcion-clase-10-2026-11-05-es.vtt#t=00:12:04) | Supuesto de independencia condicional |
| [00:15:48](z-transcripcion-clase-10-2026-11-05-es.vtt#t=00:15:48) | Variante multinomial |
| [00:19:53](z-transcripcion-clase-10-2026-11-05-es.vtt#t=00:19:53) | Variante Bernoulli |
| [00:21:41](z-transcripcion-clase-10-2026-11-05-es.vtt#t=00:21:41) | Variante gaussiana |
| [00:36:00](z-transcripcion-clase-10-2026-11-05-es.vtt#t=00:36:00) | Ejemplo de clasificación de texto |
| [00:44:57](z-transcripcion-clase-10-2026-11-05-es.vtt#t=00:44:57) | Inicio de árboles de clasificación |
| [00:46:39](z-transcripcion-clase-10-2026-11-05-es.vtt#t=00:46:39) | Impureza Gini y entropía |
| [00:54:40](z-transcripcion-clase-10-2026-11-05-es.vtt#t=00:54:40) | Selección del umbral de una división |
| [01:19:00](z-transcripcion-clase-10-2026-11-05-es.vtt#t=01:19:00) | Varianza alta y adelanto de Random Forest |
| [01:21:27](z-transcripcion-clase-10-2026-11-05-es.vtt#t=01:21:27) | Los árboles no requieren escalado |
| [01:39:44](z-transcripcion-clase-10-2026-11-05-es.vtt#t=01:39:44) | Inicio de la evaluación con ROC |
| [01:43:45](z-transcripcion-clase-10-2026-11-05-es.vtt#t=01:43:45) | Construcción de la curva ROC |
| [01:55:36](z-transcripcion-clase-10-2026-11-05-es.vtt#t=01:55:36) | Interpretación del AUC |
| [01:57:21](z-transcripcion-clase-10-2026-11-05-es.vtt#t=01:57:21) | Aclaración sobre el archivo privado del examen 2 |
| [01:58:19](z-transcripcion-clase-10-2026-11-05-es.vtt#t=01:58:19) | El conjunto de prueba no se usa para ajustar el modelo |

## Avisos

- SVM no alcanzó a verse. El profesor comentó que podría retomarlo brevemente en la siguiente clase.
- Para la clase del 6 de noviembre anunció bagging y boosting.
- El conjunto privado del examen 2 lo colocará el profesor junto al notebook al momento de evaluar.
- El ajuste debe realizarse con entrenamiento y validación. El archivo privado queda solo para la prueba final.
- En esta clase no se anunció una nueva fecha ni un formulario de entrega.

## Actividades de la clase

La presentación incluye dos actividades individuales:

- [Práctica 9 - Naive Bayes para texto](../../../tareas-practicas/practicas-clase/practica-09-naive-bayes-texto/resumen-practica-09.md)
- [Práctica 10 - árboles para diabetes](../../../tareas-practicas/practicas-clase/practica-10-arboles-diabetes/resumen-practica-10.md)

Las diapositivas llaman entregables a los dos cuadernos. No indican fecha ni plataforma, por lo que
quedan preparados en espera de la instrucción del profesor.

## Material

- [apuntes de la clase](apuntes-naive-bayes-arboles-y-roc.md)
- [presentación](presentacion-naive-bayes-arboles-y-roc.pdf)
- [transcripción](z-transcripcion-clase-10-2026-11-05-es.vtt)
