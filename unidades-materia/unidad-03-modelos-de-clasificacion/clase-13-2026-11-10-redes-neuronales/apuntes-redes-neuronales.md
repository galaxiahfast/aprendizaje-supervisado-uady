# Apuntes de redes neuronales

## Neurona artificial

Una neurona combina las entradas con pesos y un sesgo:

\[
z = \sum_i w_i x_i + b
\]

Después aplica una función de activación. Un perceptrón aislado produce una frontera lineal. Por
eso no puede separar las clases de XOR.

## Red multicapa

Una MLP conecta varias capas:

- la entrada recibe las variables
- las capas ocultas transforman la información
- la salida produce la predicción

En una capa completamente conectada, cada neurona recibe la salida de todas las neuronas de la capa
anterior. Para una capa \(l\):

\[
z^{(l)} = W^{(l)}a^{(l-1)} + b^{(l)}, \qquad
a^{(l)} = f\left(z^{(l)}\right)
\]

Sin una activación no lineal, varias capas se reducen a una sola transformación lineal. Agregar
capas en esas condiciones no resuelve XOR.

## Funciones de activación

### Sigmoide

Convierte la salida a un valor entre 0 y 1. Es apropiada para una salida binaria. En capas profundas
puede causar desvanecimiento del gradiente porque su derivada se acerca a cero.

### ReLU

\[
\operatorname{ReLU}(z) = \max(0,z)
\]

Es una opción habitual en capas ocultas. Mantiene un gradiente sencillo para valores positivos. Una
neurona puede quedar inactiva si permanece en la zona negativa.

### Softmax

Convierte las salidas de una clasificación multiclase en probabilidades que suman uno. Se usa en la
capa de salida cuando existen varias clases.

## Pase hacia adelante

El pase hacia adelante calcula la salida capa por capa usando los pesos actuales. Es el proceso que
se ejecuta al predecir con una red ya entrenada.

## Backpropagation

Backpropagation calcula el efecto de cada peso sobre la pérdida. Empieza en la salida y aplica la
regla de la cadena hacia las capas anteriores. Los resultados intermedios se reutilizan, lo que evita
recalcular la red para cada peso.

Los pesos se actualizan con descenso de gradiente:

\[
W \leftarrow W - \eta \frac{\partial L}{\partial W}
\]

Una tasa \(\eta\) muy pequeña produce aprendizaje lento. Una tasa demasiado grande puede provocar
oscilaciones o divergencia.

## Entrenamiento práctico

- Una época es una pasada completa por los datos de entrenamiento.
- Un lote contiene las observaciones usadas para una actualización.
- Los lotes pequeños producen gradientes más ruidosos, pero requieren menos cálculo por paso.
- `adam` suele funcionar bien como punto de partida.
- `early_stopping=True` detiene el entrenamiento cuando la validación deja de mejorar.
- Las variables deben escalarse porque la red combina valores mediante sumas ponderadas.

## Qué revisar después del ajuste

- pérdida de entrenamiento por época
- desempeño en validación
- diferencia entre entrenamiento y prueba
- matriz de confusión
- efecto de la arquitectura, regularización y tasa de aprendizaje

Una pérdida que sigue bajando mientras la validación se estanca es una señal de sobreajuste.
