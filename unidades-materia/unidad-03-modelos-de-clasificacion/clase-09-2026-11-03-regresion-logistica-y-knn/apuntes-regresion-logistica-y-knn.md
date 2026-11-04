# Apuntes de regresión logística y kNN

## Clasificación

En regresión se estima una cantidad. En clasificación se elige una categoría. Un filtro de correo,
por ejemplo, puede decidir entre `spam` y `no spam`.

## Regresión logística

Primero se calcula una combinación lineal de las variables:

\[
z = w^T x + b
\]

La función sigmoide convierte ese valor en una probabilidad entre 0 y 1:

\[
p = \frac{1}{1 + e^{-z}}
\]

Con un umbral de 0.5, el modelo asigna la clase 1 cuando la probabilidad es igual o mayor que 0.5.
El umbral puede cambiar cuando un tipo de error cuesta más que otro.

La pérdida usada es log-loss. Penaliza con fuerza una predicción incorrecta hecha con mucha
seguridad. No se usa MSE porque la combinación de MSE con la sigmoide dificulta la optimización.

En `LogisticRegression`, `C` controla la regularización de forma inversa:

- `C` grande significa menos regularización.
- `C` pequeño significa más regularización.

Una frontera logística es lineal en las variables que recibe. Si se agregan variables polinomiales,
puede representar fronteras curvas en el espacio original.

## Más de dos clases

Uno contra el resto entrena un clasificador por clase. Cada modelo separa una clase de todas las
demás.

Uno contra uno entrena un modelo por cada pareja de clases. Para `K` clases necesita
`K(K - 1) / 2` modelos.

Softmax calcula una probabilidad para cada clase. Todas las probabilidades suman 1.

## k vecinos más cercanos

kNN no aprende una ecuación. Guarda los ejemplos de entrenamiento. Para un dato nuevo busca los
`k` puntos más cercanos y usa la clase mayoritaria.

- Un `k` pequeño puede memorizar ruido y tener varianza alta.
- Un `k` grande suaviza la frontera, aunque puede producir sesgo alto.
- El valor de `k` se elige con validación cruzada.

La distancia puede ser euclidiana, Manhattan o coseno. No hay una métrica que siempre sea la mejor.
Se comparan con validación.

El escalado es obligatorio cuando las variables manejan unidades diferentes. Sin escalado, una
variable con números grandes domina la distancia aunque no sea la más informativa.

Con muchas variables, las distancias comienzan a parecerse. Este problema se conoce como maldición
de la dimensionalidad. Conviene seleccionar variables o reducir la dimensión antes de usar kNN.

## Matriz de confusión

| | Predicción positiva | Predicción negativa |
| --- | ---: | ---: |
| Real positiva | Verdadero positivo | Falso negativo |
| Real negativa | Falso positivo | Verdadero negativo |

La exactitud indica la proporción total de aciertos. Puede engañar cuando una clase aparece muy poco.

La precisión responde qué proporción de los casos marcados como positivos era realmente positiva:

\[
precision = \frac{VP}{VP + FP}
\]

El recall responde qué proporción de los positivos reales detectó el modelo:

\[
recall = \frac{VP}{VP + FN}
\]

F1 resume precisión y recall mediante su media armónica:

\[
F1 = 2\frac{precision \cdot recall}{precision + recall}
\]

La métrica se elige según el costo del error. En un filtro de spam importa evitar que un correo
legítimo termine oculto. En una prueba médica suele importar más detectar los casos positivos.
