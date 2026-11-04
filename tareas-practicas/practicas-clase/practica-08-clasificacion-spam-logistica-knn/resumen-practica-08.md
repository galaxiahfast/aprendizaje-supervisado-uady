# Práctica 8 - clasificación de correo spam

Actividad individual de la clase 9. Compara regresión logística con k vecinos más cercanos para
clasificar correos como spam o no spam.

## Archivo preparado

[práctica resuelta y ejecutada](practica-08-clasificacion-spam-logistica-knn.ipynb)

## Revisión del trabajo

- Exploración del balance de clases: completa.
- División estratificada de entrenamiento y prueba: completa.
- Búsqueda de `C` con validación cruzada: completa.
- Elección de `k` con validación cruzada: completa.
- Comparación con reporte de clasificación: completa.
- Matrices de confusión: completas.
- Respuestas y conclusión: completas.
- Ejecución de principio a fin: verificada sin errores.

## Resultados

| Modelo | Parámetro elegido | Exactitud de prueba | F1 para spam |
| --- | ---: | ---: | ---: |
| Regresión logística | `C = 1` | 0.831 | 0.75 |
| kNN | `k = 17` | 0.787 | 0.66 |

La regresión logística detectó 195 de los 272 correos spam. kNN detectó 153. kNN tuvo nueve falsos
positivos menos, pero dejó pasar 42 correos spam adicionales.

## Entrega

La diapositiva 41 de la presentación usa la palabra **entregable** para este cuaderno. En la clase no
se indicó fecha ni plataforma. Por ahora queda listo y separado del examen del módulo 2. No debe
subirse hasta que el profesor publique el medio de entrega o confirme que lo solicita.
