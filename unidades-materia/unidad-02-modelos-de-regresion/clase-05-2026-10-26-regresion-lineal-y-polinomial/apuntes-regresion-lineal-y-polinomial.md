# Apuntes de regresión lineal y polinomial

## Regresión lineal

La regresión predice un número. En el modelo lineal cada variable aporta un coeficiente:

\[
\hat y=b+w_1x_1+\cdots+w_px_p
\]

El residuo es la diferencia entre el valor real y la predicción. Mínimos cuadrados ordinarios elige
los parámetros que reducen la suma de residuos al cuadrado. Ese criterio evita que los errores
positivos y negativos se cancelen, aunque también hace que los valores extremos pesen mucho.

Un coeficiente indica cuánto cambia la predicción cuando su variable aumenta una unidad y las demás
se mantienen fijas. Para comparar la magnitud de varios coeficientes, las entradas deben estar en
una escala común.

## Descenso de gradiente

La regla de actualización es:

\[
\theta \leftarrow \theta-\eta\nabla J(\theta)
\]

Una tasa muy pequeña tarda en llegar al mínimo. Una tasa demasiado grande salta de un lado a otro y
puede hacer crecer el error. El escalamiento evita que una variable domine el gradiente solo por sus
unidades.

- Por lotes usa todos los datos en cada paso.
- SGD usa una observación por paso.
- Minilotes usa grupos pequeños y suele ser el punto medio práctico.

## Regresión polinomial

`PolynomialFeatures` agrega potencias e interacciones. El modelo sigue siendo lineal en sus
coeficientes, pero puede representar curvas. Aumentar el grado reduce el error de entrenamiento.
Después de cierto punto puede aumentar el error de validación por sobreajuste.

El grado se elige con validación cruzada dentro de un pipeline. El conjunto de prueba queda reservado
para una sola evaluación final.

## Métricas

- MAE: error absoluto promedio. Es fácil de traducir a las unidades del problema.
- MSE: promedio de los errores al cuadrado. Penaliza más los errores grandes.
- RMSE: raíz del MSE. Queda en las mismas unidades del objetivo.
- \(R^2\): proporción de variación explicada respecto a predecir el promedio.

Las métricas no sustituyen el análisis de residuos. Un patrón en los residuos indica que el modelo
no captó alguna estructura. Una diferencia grande entre validación y prueba puede señalar fuga,
cambio de distribución o una decisión tomada con la prueba.
