# Apuntes de árboles y evaluación

## Árbol de regresión

Un árbol divide los datos con preguntas del tipo `variable <= valor`. Cada respuesta conduce a otro
nodo. La última región es una hoja. En regresión, la hoja predice el promedio de los valores que
llegaron a ella.

## Cómo elige CART

CART prueba variables y puntos de corte. Para cada opción calcula el MSE de los dos grupos y lo
pondera por su tamaño. Conserva el corte con el menor error. El proceso se repite en los nodos
nuevos.

## Complejidad

Un árbol profundo puede formar hojas con muy pocos casos. El error de entrenamiento baja, pero el
modelo se vuelve sensible a cambios en la muestra. Se puede controlar con:

- `max_depth`: limita la profundidad
- `min_samples_leaf`: exige más observaciones en cada hoja
- `ccp_alpha`: poda ramas con poca aportación

Los valores se eligen con validación cruzada. No se decide la complejidad usando el conjunto de
prueba.

## Escalado e interpretación

Los árboles trabajan con ordenamientos y umbrales. Escalar una variable no cambia el orden de sus
valores, por eso las particiones permanecen iguales. Esto es distinto de SVR, que usa distancias.

La estructura se puede leer como reglas. Esa claridad no garantiza estabilidad. Dos muestras
parecidas pueden producir árboles distintos.

## Evaluación correcta

La validación cruzada simple sirve para ajustar parámetros. Cuando se quiere comparar modelos y
reportar su rendimiento, la validación cruzada anidada separa la búsqueda interna de la evaluación
externa. El conjunto de prueba se reserva para una medición final.
