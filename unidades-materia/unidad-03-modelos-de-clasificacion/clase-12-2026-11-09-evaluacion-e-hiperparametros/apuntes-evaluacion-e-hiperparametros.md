# Apuntes de evaluación e hiperparámetros

## Clases desbalanceadas

La exactitud puede ocultar un modelo inútil. Si solo 2 % de las operaciones son fraude, predecir
siempre la clase legítima produce 98 % de exactitud sin detectar un solo fraude.

El coeficiente de correlación de Matthews usa las cuatro partes de la matriz de confusión:

\[
MCC = \frac{VP \cdot VN - FP \cdot FN}
{\sqrt{(VP+FP)(VP+FN)(VN+FP)(VN+FN)}}
\]

Un MCC de 1 indica predicción perfecta. Un valor de 0 se parece al azar. Un valor de -1 representa
una predicción completamente invertida.

Kappa de Cohen compara el acuerdo observado con el que podría aparecer por azar:

\[
\kappa = \frac{p_o-p_e}{1-p_e}
\]

En clasificación binaria, MCC y kappa suelen contar una historia parecida. Kappa también se usa para
medir acuerdo entre personas que etiquetan los mismos casos.

## Log-loss

Exactitud, MCC y kappa trabajan con la clase final. Log-loss también considera la probabilidad
predicha. Castiga especialmente una respuesta equivocada emitida con mucha confianza.

\[
log\text{-}loss = -\frac{1}{n}\sum_i
[y_i\log(\hat p_i)+(1-y_i)\log(1-\hat p_i)]
\]

Un valor menor es mejor. La métrica requiere `predict_proba`.

## Tratamiento del desbalance

- El submuestreo elimina casos de la clase mayoritaria. Es rápido, pero puede perder información.
- El sobremuestreo repite casos minoritarios. Conserva los datos originales, aunque puede sobreajustar.
- SMOTE crea observaciones entre vecinos de la clase minoritaria. Los valores atípicos pueden generar puntos poco útiles.
- `class_weight` aumenta el costo de equivocarse en la clase minoritaria sin alterar el conjunto.

El remuestreo debe ocurrir dentro de cada pliegue de validación. Un `Pipeline` de `imbalanced-learn`
evita que copias o puntos relacionados pasen al conjunto de validación.

## Búsqueda de hiperparámetros

`GridSearchCV` prueba todas las combinaciones de una malla. Funciona bien cuando hay pocos parámetros
y pocos valores.

`RandomizedSearchCV` toma un número fijo de combinaciones. Resulta más práctico con muchos parámetros
o rangos continuos porque `n_iter` controla directamente el costo.

`HalvingGridSearchCV` comienza con pocos datos, elimina candidatos débiles y dedica más recursos a
los que sobreviven.

Optuna usa los resultados anteriores para orientar la siguiente prueba hacia regiones prometedoras
del espacio de hiperparámetros.

La métrica de `scoring` debe representar el problema. Con clases desbalanceadas no conviene optimizar
exactitud por omisión.

## Calibración

Una probabilidad está calibrada si, entre los casos a los que el modelo asigna 0.8, cerca de 80 %
resulta positivo. La salida de `predict_proba` no garantiza esa relación en todos los modelos.

`CalibratedClassifierCV` ajusta una función sobre las salidas del modelo. Puede usar una sigmoide o
regresión isotónica. El conjunto de calibración debe quedar separado del entrenamiento y de la prueba.

La calibración busca mejorar log-loss y Brier score. Puede empeorar si hay pocos casos positivos en
el conjunto usado para calibrar.
