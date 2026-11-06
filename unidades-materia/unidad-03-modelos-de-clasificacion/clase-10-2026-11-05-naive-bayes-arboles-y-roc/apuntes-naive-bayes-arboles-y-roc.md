# Apuntes de Naive Bayes, árboles y curva ROC

## Naive Bayes

El teorema de Bayes permite calcular la probabilidad de una clase después de observar sus variables:

\[
P(C\mid X)=\frac{P(X\mid C)P(C)}{P(X)}
\]

Para comparar clases no hace falta calcular el denominador porque es el mismo para todas. El modelo
elige la clase con mayor producto entre la probabilidad previa y la verosimilitud.

Naive Bayes supone que las variables son independientes cuando se conoce la clase. El supuesto casi
nunca se cumple por completo, pero simplifica el cálculo y suele funcionar bien en clasificación de
texto.

### Variantes

- `GaussianNB` modela variables continuas con una distribución normal por clase.
- `MultinomialNB` trabaja con conteos, como la frecuencia de palabras.
- `BernoulliNB` registra presencia o ausencia, por ejemplo si una palabra aparece en un documento.

Si una palabra nunca apareció en una clase, su probabilidad puede quedar en cero. El suavizado de
Laplace agrega una cantidad pequeña a los conteos para evitar que todo el producto se anule.

## Árboles de clasificación

Un árbol divide los datos mediante preguntas sobre una variable. Cada división busca formar nodos
con clases más puras.

La impureza Gini para varias clases se calcula como:

\[
Gini = 1 - \sum_k p_k^2
\]

La entropía se calcula como:

\[
H = -\sum_k p_k \log_2(p_k)
\]

El algoritmo compara variables y umbrales. Después pondera la impureza de los nodos hijos según el
número de observaciones que recibe cada uno. Se elige la división con mayor reducción de impureza.

Los árboles no necesitan escalado porque sus decisiones usan umbrales de una variable a la vez. Un
árbol profundo puede ajustarse al ruido. También puede cambiar mucho si se modifica una parte pequeña
de los datos. Esa varianza alta motiva el uso de bagging y Random Forest.

## Curva ROC

Un clasificador binario puede cambiar de comportamiento al modificar su umbral. Para cada umbral se
calculan dos tasas:

\[
TPR = \frac{VP}{VP + FN}
\]

\[
FPR = \frac{FP}{FP + VN}
\]

La curva ROC representa `TPR` frente a `FPR`. Un modelo útil se acerca a la esquina superior
izquierda. La diagonal corresponde a una clasificación equivalente al azar.

El AUC resume el área bajo la curva:

- Un valor de 0.5 indica una separación similar al azar.
- Un valor cercano a 1 indica mejor capacidad para ordenar positivos por encima de negativos.
- El AUC permite comparar modelos sin fijar primero un solo umbral.

El umbral final depende del costo de los errores. En un diagnóstico médico puede ser preferible
aceptar más falsos positivos para reducir los falsos negativos.
