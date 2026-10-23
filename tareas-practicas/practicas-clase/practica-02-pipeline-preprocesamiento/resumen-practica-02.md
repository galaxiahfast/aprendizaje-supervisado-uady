# Práctica 2 — pipeline de preprocesamiento

Clase relacionada: **clase 2 del 20 de octubre de 2026**

Estado: **resuelta y ejecutada. No se entrega**

El 22 de octubre el profesor aclaró que los tres notebooks de la primera semana son para practicar.
El entregable será otro notebook integrador.

## Archivos de la práctica

- [notebook resuelto](practica-02-pipeline-preprocesamiento-resuelta.ipynb)
- [tabla comparativa](resultados-preprocesamiento-datos.csv)

Estos archivos sirven para estudiar y preparar el laboratorio integrador.

## Criterios cubiertos

- [x] Carga California Housing y cuantifica los faltantes.
- [x] Divide entrenamiento y prueba con estratificación por ingreso.
- [x] Compara media, mediana, KNN e imputación iterativa sobre valores ocultos.
- [x] Contrasta codificación entera y one-hot.
- [x] Compara StandardScaler, MinMaxScaler y RobustScaler con KNN.
- [x] Provoca una fuga de datos, mide su efecto y la corrige con Pipeline.
- [x] Construye un ColumnTransformer para columnas numéricas y categóricas.
- [x] Evalúa las estrategias con validación cruzada.
- [x] Incluye una tabla con estrategia, RMSE de validación y comentario.
- [x] Ejecuta todas las celdas sin errores.

## Resultados principales

| Resultado | Valor |
| --- | ---: |
| KNN sin escalar | RMSE 96.63 |
| KNN con StandardScaler | RMSE 62.59 |
| Pipeline con mediana y one-hot | RMSE de validación 61.20 |
| Mejor estrategia con KNNImputer | RMSE de validación 61.14 |
| Mejor estrategia en prueba | RMSE 58.85, R² 0.734 |
| Selección de variables con fuga | exactitud 0.85 |
| Selección dentro del pipeline | exactitud 0.52 |

El cambio principal provino del escalamiento. La imputación con KNN produjo la mejor media de
validación, aunque la diferencia frente a la mediana fue pequeña.

