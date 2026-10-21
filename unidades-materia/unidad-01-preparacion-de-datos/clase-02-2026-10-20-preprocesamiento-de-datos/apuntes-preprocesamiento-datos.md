# Apuntes de preprocesamiento de datos

## Datos faltantes

- MCAR: la ausencia no depende de variables observadas ni del valor faltante.
- MAR: la ausencia se explica con otras variables observadas.
- MNAR: la ausencia depende del propio valor faltante o de información no observada.
- Borrar filas reduce la muestra. Conviene medir cuántas observaciones se pierden.
- Media y mediana reducen la variabilidad porque repiten un valor central.
- KNN necesita variables comparables para calcular distancias útiles.
- Un indicador de faltante conserva la señal de que el dato fue imputado.

## Variables categóricas

- Nominal: sus categorías no tienen orden, como `ocean_proximity`.
- Ordinal: sus categorías siguen una secuencia, como pequeña, mediana y grande.
- La codificación entera de una variable nominal crea un orden inexistente.
- One-hot evita ese orden mediante una columna binaria por categoría.
- `handle_unknown="ignore"` permite transformar categorías no vistas durante el ajuste.
- Muchas categorías aumentan la cantidad de columnas. Las categorías raras pueden agruparse.

## Escalamiento

| Método | Cálculo | Uso anotado |
| --- | --- | --- |
| StandardScaler | resta la media y divide entre la desviación estándar | opción común sin extremos fuertes |
| MinMaxScaler | lleva cada variable a un intervalo | útil cuando se necesita un rango definido |
| RobustScaler | resta la mediana y divide entre el IQR | mejor resistencia ante valores extremos |

KNN cambia mucho al escalar porque trabaja con distancias. Los árboles casi no cambian porque separan
con umbrales dentro de cada variable.

## Separación de los datos

1. Apartar el conjunto de prueba.
2. Ajustar transformaciones solo con entrenamiento.
3. Elegir modelo e hiperparámetros con validación o validación cruzada.
4. Aplicar al conjunto de prueba las transformaciones aprendidas.
5. Evaluar la prueba una sola vez al final.

La estratificación conserva proporciones importantes en cada partición. Resulta útil cuando existen
clases o grupos poco frecuentes.

## Fuga de datos

Hay fuga cuando el entrenamiento recibe información que no estaría disponible al predecir datos
nuevos. Ejemplos de la clase:

- calcular media o desviación con todo el conjunto antes de dividir
- seleccionar variables usando todas las etiquetas
- elegir hiperparámetros con el resultado de prueba
- incluir una variable generada después del evento que se quiere predecir

## Pipeline

`ColumnTransformer` aplica pasos distintos a columnas numéricas y categóricas. `Pipeline` une ese
preprocesamiento con el modelo. Al ejecutar `fit`, cada transformación aprende solo del conjunto que
recibe. Al ejecutar `predict`, reutiliza los mismos parámetros.

