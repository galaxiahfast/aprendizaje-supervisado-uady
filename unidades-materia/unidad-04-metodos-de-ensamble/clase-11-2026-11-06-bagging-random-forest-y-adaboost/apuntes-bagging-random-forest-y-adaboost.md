# Apuntes de bagging, Random Forest y AdaBoost

## Bagging

Bagging entrena varios modelos en paralelo. Cada uno recibe una muestra bootstrap del conjunto de
entrenamiento. La muestra conserva el mismo tamaño, pero se obtiene con reemplazo. Algunas filas
pueden repetirse y otras quedan fuera.

Las observaciones que no entran en una muestra se llaman fuera de bolsa u OOB. En promedio queda
fuera cerca de 37 % de los datos. Esas observaciones permiten estimar el error sin separar otro
conjunto de validación.

Para clasificación se usa el voto mayoritario. En regresión se promedian las predicciones.

El modelo base suele ser un árbol porque es rápido y tiene varianza alta. Bagging también admite
otros estimadores. Su objetivo principal es reducir varianza, no corregir el sesgo del modelo base.

## Random Forest

Si una variable es muy dominante, muchos árboles de bagging pueden comenzar con el mismo corte y
quedar demasiado correlacionados. Random Forest agrega una restricción: en cada división solo permite
examinar un subconjunto aleatorio de variables.

La combinación queda así:

1. Se crea una muestra bootstrap para cada árbol.
2. En cada nodo se toma un subconjunto aleatorio de variables.
3. Se elige el mejor corte dentro de ese subconjunto.
4. Las predicciones de todos los árboles se combinan.

El bosque conserva la estimación OOB. También calcula `feature_importances_` con la reducción de
impureza acumulada en todos los árboles.

Random Forest suele ser más estable que un árbol solo. A cambio se pierde la facilidad de seguir una
secuencia corta de reglas.

## AdaBoost

AdaBoost entrena aprendices débiles de manera secuencial. El modelo habitual es un árbol de
profundidad uno, también llamado stump.

Al inicio cada observación recibe el mismo peso:

\[
w_i = \frac{1}{n}
\]

Después de entrenar un aprendiz se calcula su error ponderado. El peso de su voto es:

\[
\alpha_m = \frac{1}{2}\log\left(\frac{1-error_m}{error_m}\right)
\]

Un aprendiz con menor error recibe un voto mayor. Los pesos de las observaciones se actualizan para
dar más importancia a los casos mal clasificados:

\[
w_i \leftarrow w_i\exp(-\alpha_m y_i h_m(x_i))
\]

Los pesos se normalizan antes de la siguiente ronda. La predicción final usa el signo de la suma
ponderada de todos los aprendices.

AdaBoost puede concentrarse demasiado en valores atípicos o etiquetas incorrectas porque aumenta
repetidamente su peso. Conviene vigilar el error de validación mientras crece el número de aprendices.

## Diferencia principal

Bagging y Random Forest entrenan modelos independientes en paralelo para reducir varianza. AdaBoost
entrena modelos en serie. Cada aprendiz corrige errores del anterior para reducir sesgo.
