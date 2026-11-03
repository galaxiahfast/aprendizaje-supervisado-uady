# Criterios del examen del módulo 2

## Rúbrica oficial

| Rubro | Puntos | Estado |
| --- | ---: | --- |
| EDA y preprocesamiento justificados | 20 | Completo |
| Implementación de los cinco modelos | 30 | Completo |
| Validación cruzada de cinco pliegues | 20 | Completo |
| Evaluación en el conjunto de prueba | 20 | Pendiente del archivo de prueba |
| Tabla comparativa y conclusiones | 10 | Completo |

## Revisión del formato

- [x] Nombre completo en la variable `NOMBRE`.
- [x] Nombre del archivo en el formato solicitado.
- [x] Librerías y versiones al inicio.
- [x] Notebook ejecutado de principio a fin.
- [x] Ninguna celda con error.
- [x] Comentarios agregados en español.
- [x] Respuestas y conclusiones con cifras.
- [x] Tamaño menor de 10 MB.
- [ ] Evaluación con el archivo de prueba entregado por el profesor.
- [ ] Confirmación del envío en el formulario.

## Aclaración necesaria

Las instrucciones describen el archivo de prueba sin la columna `stab`, pero también piden calcular
RMSE sobre ese archivo. Sin los valores reales de `stab` se pueden generar predicciones, pero no
calcular RMSE. El cuaderno admite ambos casos y no inventa esa métrica.
