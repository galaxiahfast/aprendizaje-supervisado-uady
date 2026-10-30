# Apuntes de regresión con máquinas de soporte vectorial

## Del margen al tubo de tolerancia

En clasificación, una máquina de soporte vectorial busca una frontera que separe las clases con el
margen más amplio posible. Los puntos cercanos a la frontera son los vectores de soporte. El margen
duro no admite violaciones. El margen blando acepta algunas mediante una penalización.

En regresión, la frontera se convierte en una función de predicción. A su alrededor se construye un
tubo de ancho `2 * epsilon`. Los errores que quedan dentro del tubo no reciben penalización. Los
puntos que quedan fuera son los que influyen directamente en el ajuste.

## Parámetros principales

### C

`C` controla cuánto cuesta salirse del tubo.

- Un valor pequeño tolera más errores y puede producir subajuste.
- Un valor grande intenta seguir más de cerca los datos y puede producir sobreajuste.

### Epsilon

`epsilon` define el error que se considera aceptable.

- Un valor pequeño crea un tubo angosto y suele dejar más vectores de soporte.
- Un valor grande crea un tubo ancho y reduce la cantidad de puntos que reciben penalización.

### Gamma

`gamma` controla el alcance de cada punto cuando se usa el kernel RBF.

- Un valor pequeño produce una influencia amplia y una curva más suave.
- Un valor grande vuelve la influencia local y puede memorizar el ruido.

Los tres parámetros interactúan. Se eligen juntos mediante validación cruzada.

## Truco del kernel

Un SVR lineal solo puede formar una recta o un hiperplano. El kernel permite representar relaciones
curvas sin construir manualmente todas las variables nuevas.

- Lineal: adecuado cuando la relación ya es aproximadamente lineal.
- Polinomial: útil para curvaturas que pueden describirse con un grado conocido.
- RBF: flexible para relaciones no lineales de forma desconocida.

## Reglas para aplicar SVR

- Separar entrenamiento y prueba antes de ajustar cualquier transformación.
- Colocar `StandardScaler` dentro del pipeline.
- Elegir `C`, `epsilon` y `gamma` con validación cruzada.
- Comparar el resultado contra un modelo base sencillo.
- Evaluar el conjunto de prueba una sola vez al final.
- Revisar el número de vectores de soporte y la diferencia entre entrenamiento y prueba.

SVR puede funcionar bien con conjuntos pequeños o medianos. Su costo aumenta cuando hay demasiadas
observaciones. También es menos fácil de interpretar que una regresión lineal.
