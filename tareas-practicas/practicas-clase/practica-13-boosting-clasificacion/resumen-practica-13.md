# Práctica 13 - boosting para clasificación

Actividad individual relacionada con la clase 11. Compara AdaBoost y Gradient Boosting contra un
Random Forest de referencia.

## Archivos preparados

- [práctica resuelta y ejecutada](practica-13-boosting-clasificacion.ipynb)
- [tabla final de resultados](resultados-boosting-clasificacion.csv)

## Revisión del trabajo

- Curvas de error de AdaBoost: completas.
- Comparación contra Random Forest: completa.
- Ajuste de Gradient Boosting con GridSearchCV: completo.
- Tabla final de exactitud y tiempo: completa.
- Interpretación y elección de modelo: completas.
- Riesgo con valores atípicos y etiquetas ruidosas: explicado.
- XGBoost: parte opcional no ejecutada porque la biblioteca no está instalada.
- Nombre del estudiante: incluido.
- Ejecución de principio a fin: verificada sin errores.

## Resultados

| Modelo | Exactitud de prueba |
| --- | ---: |
| Random Forest | 0.910 |
| Gradient Boosting | 0.900 |
| AdaBoost | 0.870 |

Gradient Boosting eligió `learning_rate=0.1` con 200 árboles. AdaBoost alcanzó su mejor error de
prueba, 0.120, con 250 aprendices. El cuaderno recomienda Random Forest para este conjunto.

## Entrega

La diapositiva 20 pide el cuaderno con la curva de AdaBoost, la búsqueda de hiperparámetros, la tabla
comparativa y la interpretación del modelo. XGBoost aparece como ampliación opcional. No se indicó
fecha ni plataforma. El archivo queda listo, pero no debe subirse hasta que el profesor confirme el
medio de entrega.
