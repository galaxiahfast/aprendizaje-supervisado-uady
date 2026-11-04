# Tarea 2 - examen del módulo 2

Evaluación individual sobre métodos de regresión aplicados a la estabilidad de redes eléctricas.

## Archivo que se sube

- [`Ortiz_Julian_Examen_Modulo2.ipynb`](Ortiz_Julian_Examen_Modulo2.ipynb)

El formulario acepta un solo notebook de hasta 10 MB. No se suben el PDF, los datos de entrenamiento
ni archivos de predicciones por separado.

## Lugar de entrega

[Formulario oficial del examen del módulo 2](https://forms.gle/4TRwhUbqJoGmpm89A)

## Estado

- EDA y preprocesamiento: completos.
- Cinco modelos: completos.
- Validación cruzada de cinco pliegues: completa.
- Tabla comparativa y conclusiones: completas.
- Archivo de prueba: lo colocará el profesor al calificar.
- Bloque final: probado con un archivo sin `stab`. Genera las cinco predicciones.
- Fecha límite: **domingo 8 de noviembre de 2026 a las 23:00**.
- Envío: pendiente.

El cuaderno tiene 12 celdas de código ejecutadas y no presenta errores. Está preparado para leer
`electrical_grid_stability_test.csv` cuando el profesor lo coloque junto al notebook. No es necesario
tener ese archivo antes de entregar.

## Resultado actual

La regresión polinomial de grado 3 obtuvo el menor RMSE de validación: **0.008720 ± 0.000168**. SVR
con RBF quedó muy cerca con **0.008847 ± 0.000165**. Esta comparación usa únicamente las 8 000 filas
de entrenamiento.
