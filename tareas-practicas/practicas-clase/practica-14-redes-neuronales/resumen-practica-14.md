# Práctica 14 - redes neuronales

Estado: **resuelta y verificada**

## Archivos preparados

- [notebook resuelto y ejecutado](practica-14-redes-neuronales.ipynb)
- `datos-fashion-mnist-subset.npz`, requerido por el notebook

La actividad usa 4,000 imágenes de entrenamiento y 1,000 de prueba de Fashion-MNIST. Compara
optimizadores, tamaños de lote y tasas de aprendizaje. El modelo final usa detención temprana y se
revisa con una matriz de confusión.

## Revisión

- Nombre del estudiante: incluido.
- Escalamiento de píxeles: completo.
- Comparación de `lbfgs`, `sgd` y `adam`: completa.
- Experimentos de lote y tasa de aprendizaje: completos.
- Curvas de pérdida y validación: generadas.
- Matriz de confusión: generada e interpretada.
- Respuestas: completas con las cifras obtenidas.
- Ejecución de principio a fin: verificada sin errores.

## Resultados principales

- La primera MLP obtuvo 0.817 de exactitud en prueba.
- `adam` fue el optimizador con mejor exactitud en la comparación.
- Una tasa de aprendizaje de 1.5 produjo un resultado cercano al azar.
- El modelo con detención temprana terminó en la época 23.
- La confusión más frecuente fue pulóver clasificado como abrigo.

## Entrega

La presentación llama entregable al cuaderno con curvas, comparación y respuestas. No se publicó
fecha ni formulario para esta práctica. Queda lista, pero no debe confundirse con el examen del
módulo 3, que sí tiene formulario y fecha límite.
