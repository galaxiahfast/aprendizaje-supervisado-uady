# Práctica 11 - evaluación de fraude

Actividad individual de la clase 12. Construye un flujo de evaluación para un conjunto con cerca de
2 % de operaciones fraudulentas.

## Archivos preparados

- [práctica resuelta y ejecutada](practica-11-evaluacion-fraude.ipynb)
- [tabla final de resultados](resultados-evaluacion-fraude.csv)

## Revisión del trabajo

- Exactitud, MCC y kappa del modelo base: completos.
- Comparación de log-loss contra un modelo todo negativo: completa.
- `class_weight`, RandomOverSampler y SMOTE dentro de validación cruzada: completos.
- GridSearchCV y RandomizedSearchCV con el mismo presupuesto: completos.
- Curvas de calibración antes y después: completas.
- Comparación final y recomendación de modelo: completas.
- Nombre del estudiante: incluido.
- Ejecución de principio a fin: verificada sin errores.

## Resultados

| Modelo | Exactitud | MCC | Kappa | Log-loss |
| --- | ---: | ---: | ---: | ---: |
| Bosque base | 0.982 | 0.459 | 0.348 | 0.081 |
| Pesos balanceados con GridSearchCV | 0.986 | 0.608 | 0.584 | 0.086 |
| Modelo calibrado | 0.982 | 0.498 | 0.468 | 0.107 |

GridSearchCV obtuvo MCC de validación de 0.509. RandomizedSearchCV obtuvo 0.507 con el mismo número de
combinaciones. El cuaderno recomienda el modelo ajustado sin calibrar para la decisión con umbral 0.5.
También explica cuándo conviene bajar el umbral para detectar más fraudes.

## Entrega

La diapositiva 42 pide el cuaderno con la tabla comparativa, las curvas de calibración y la
justificación del modelo con su umbral. No se indicó fecha ni plataforma. El archivo queda listo,
pero no debe subirse hasta que el profesor publique el medio de entrega o confirme que lo solicita.
