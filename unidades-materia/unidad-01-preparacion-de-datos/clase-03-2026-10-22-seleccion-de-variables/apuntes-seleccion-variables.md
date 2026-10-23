# Apuntes de ingeniería y selección de variables

## Crear variables

Una variable nueva representa una hipótesis sobre el problema. Debe tener sentido en el dominio y
mejorar la validación cruzada para conservarse.

- Razón: compara cantidades en una escala común, como dormitorios por habitación.
- Diferencia: representa un cambio entre dos momentos.
- Agregado: resume varias observaciones de una persona o periodo.
- Logaritmo: comprime colas largas en variables positivas.
- Polinomio: permite que un modelo lineal represente curvas.
- Interacción: expresa que el efecto de una variable depende de otra.

Los polinomios aumentan rápido el número de columnas. Con 30 variables, grado 2 genera 495 columnas.
Grado 3 genera 5 455. Conviene usar grados bajos y regularización.

## Familias de selección

| Familia | Cómo decide | Costo | Riesgo principal |
| --- | --- | ---: | --- |
| Filtro | puntaje estadístico por variable | bajo | no considera bien las variables juntas |
| Envoltura | prueba subconjuntos con un modelo | alto | puede sobreajustar la selección |
| Integrado | selecciona durante el entrenamiento | medio | depende de la escala y del hiperparámetro |

## Métodos de filtro

- VarianceThreshold retira columnas constantes o casi constantes.
- La varianza depende de las unidades. Un umbral fijo puede borrar información útil.
- La correlación detecta relaciones lineales o monótonas.
- La información mutua también detecta relaciones no lineales.
- Un filtro por objetivo puede elegir varias versiones de la misma información.
- La poda por redundancia conserva una variable de cada grupo muy correlacionado.

La presentación usa un umbral de correlación absoluta mayor a 0.9 para localizar redundancia. En los
datos de cáncer de mama, radio, perímetro y área forman un grupo muy parecido.

## RFE y RFECV

RFE entrena un modelo, ordena las variables por importancia, retira la menos útil y vuelve a entrenar.
El reentrenamiento importa porque los coeficientes cambian cuando existen variables correlacionadas.

RFECV repite el proceso con validación cruzada para estimar cuántas variables conservar. El máximo de
la curva no siempre es la única opción. Un subconjunto menor puede ser preferible si queda muy cerca.

## Lasso

La penalización L1 lleva algunos coeficientes exactamente a cero. Esas variables salen del modelo.
En clasificación se usa regresión logística con `penalty="l1"`. Un valor menor de C significa mayor
penalización.

Las variables deben estandarizarse antes. Cuando varias columnas son muy correlacionadas, Lasso puede
elegir una distinta en cada muestra. La estabilidad se revisa repitiendo la selección con remuestreos.

## Reglas anotadas

1. Separar la prueba antes de crear o seleccionar variables.
2. Colocar escalamiento y selección dentro del pipeline.
3. Elegir k o C mediante validación cruzada.
4. Comparar contra el modelo con todas las variables.
5. Revisar estabilidad y sentido del dominio.
6. Tocar la prueba una sola vez al final.

