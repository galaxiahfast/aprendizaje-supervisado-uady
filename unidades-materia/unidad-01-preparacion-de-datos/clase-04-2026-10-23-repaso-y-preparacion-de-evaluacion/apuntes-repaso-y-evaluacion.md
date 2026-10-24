# Apuntes del repaso y la evaluación

## El orden de trabajo

1. Reservar el conjunto de prueba.
2. Explorar el conjunto de entrenamiento.
3. Definir las transformaciones con los datos de entrenamiento.
4. Colocar imputación, codificación, escalamiento y selección dentro del pipeline.
5. Validar el pipeline completo.
6. Usar prueba una sola vez para medir el resultado final.

Durante validación cruzada, cada transformación que aprende parámetros debe volver a ajustarse con
el bloque de entrenamiento de ese pliegue. Calcular medias, cercas, correlaciones o variables
seleccionadas con todos los datos produce fuga.

## EDA

Primero se revisan tamaño, tipos, faltantes, duplicados y rangos. Después se estudia la forma de cada
variable con estadísticas y gráficas. Media y desviación estándar reaccionan mucho a los extremos.
Mediana e IQR son resúmenes más resistentes.

Un valor fuera de las cercas de Tukey no es un error por definición. Puede ser un dato válido, una
observación de otra población o un problema de captura. La decisión depende del contexto.

Los topes tampoco son atípicos comunes. En California Housing, `MedHouseVal` y `HouseAge` acumulan
casos en un límite de publicación. Borrar esas filas cambia la población estudiada.

## Relaciones entre variables

Pearson resume una relación lineal y puede cambiar mucho por unos cuantos extremos. Spearman trabaja
con rangos. Es útil cuando la relación es monótona, no lineal o cuando los extremos dominan a
Pearson.

Una correlación alta entre predictores puede volver inestables los coeficientes de un modelo lineal.
El heatmap sirve para localizar pares. El VIF permite revisar el efecto conjunto. Antes de quitar una
variable conviene estudiar qué representa y comprobar el resultado con validación.

## Preprocesamiento

- MCAR: la ausencia no depende de datos observados ni del valor faltante.
- MAR: la ausencia puede explicarse con variables observadas.
- MNAR: la ausencia depende del propio valor no observado o de información no disponible.

La imputación no recupera el valor verdadero. Mantiene filas y crea una estimación que debe quedar
documentada. Un indicador de ausencia puede conservar señal cuando faltar también significa algo.

Las categorías nominales suelen ir con one-hot. Las ordinales necesitan un orden explícito. Para una
categoría nueva, el codificador debe tener una regla definida.

El escalamiento importa en métodos que usan distancias o penalizaciones. `StandardScaler` usa media
y desviación estándar. `MinMaxScaler` depende de mínimos y máximos. `RobustScaler` usa mediana e IQR,
por lo que resiste mejor los extremos.

## Ingeniería y selección

Una variable nueva debe tener sentido para el problema. Puede ser una razón, una interacción, una
transformación logarítmica o un indicador. Su utilidad se comprueba dentro del proceso de validación.

Los métodos filtro son rápidos y no dependen de un modelo concreto. Los métodos envolventes prueban
subconjuntos y cuestan más. Los métodos embebidos seleccionan durante el ajuste. Ninguno sustituye la
revisión del significado de las variables.

## Lo que puede aparecer en la evaluación

La evaluación combina EDA, preprocesamiento y selección. El profesor indicó que no habrá temas
nuevos. Las preguntas piden interpretar resultados, justificar decisiones y completar código breve.

Antes de subir el notebook:

- escribir cada respuesta bajo `Respuesta:`
- no cambiar nombres solicitados
- reiniciar el entorno y ejecutar todo
- comprobar que no existan celdas con error
- ejecutar la autoverificación si aparece
- subir solo lo solicitado en el formulario
