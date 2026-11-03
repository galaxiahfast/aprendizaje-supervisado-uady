# Tarea 3 - examen del módulo 2

Evaluación individual sobre métodos de regresión aplicados a la estabilidad de redes eléctricas.

## Archivo que se sube

- [`ortiz_julian_examen_modulo2.ipynb`](ortiz_julian_examen_modulo2.ipynb)

El formulario acepta un solo notebook de hasta 10 MB. No se suben el PDF, los datos de entrenamiento
ni archivos de predicciones por separado.

## Lugar de entrega

[Formulario oficial del examen del módulo 2](https://forms.gle/4TRwhUbqJoGmpm89A)

## Estado

- EDA y preprocesamiento: completos.
- Cinco modelos: completos.
- Validación cruzada de cinco pliegues: completa.
- Tabla comparativa y conclusiones: completas.
- Archivo de prueba: pendiente de publicación por el profesor.
- Fecha límite: no publicada.
- Envío: pendiente.

El cuaderno tiene 12 celdas de código ejecutadas y no presenta errores. Cuando se reciba
`electrical_grid_stability_test.csv`, debe colocarse junto al notebook y ejecutarse otra vez. El
bloque final generará `predicciones_modulo2.csv`. Solo podrá calcular RMSE de prueba si el archivo
incluye la columna `stab`.

## Resultado actual

La regresión polinomial de grado 3 obtuvo el menor RMSE de validación: **0.008720 ± 0.000168**. SVR
con RBF quedó muy cerca con **0.008847 ± 0.000165**. Esta comparación usa únicamente las 8 000 filas
de entrenamiento.
