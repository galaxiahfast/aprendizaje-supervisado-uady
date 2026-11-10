# Práctica 12 - bagging y Random Forest

Actividad individual relacionada con la clase 11. Compara un árbol, bagging y Random Forest sobre el
mismo conjunto sintético.

## Archivos preparados

- [práctica resuelta y ejecutada](practica-12-bagging-random-forest.ipynb)
- [tabla final de resultados](resultados-bagging-random-forest.csv)

## Revisión del trabajo

- Comparación entre árbol solo y bagging: completa.
- Efecto de `max_features` sobre la raíz: completo.
- Curva de error OOB: completa.
- Importancia de variables: completa.
- Comparación entre error OOB y error de prueba: completa.
- Tabla final de exactitud y tiempo: completa.
- Interpretación y elección de modelo: completas.
- Nombre del estudiante: incluido.
- Ejecución de principio a fin: verificada sin errores.

## Resultados

| Modelo | Exactitud de prueba |
| --- | ---: |
| Random Forest | 0.910 |
| Bagging | 0.905 |
| Árbol solo | 0.845 |

El error OOB se estabilizó cerca de 0.10 a partir de 40 árboles. Con 300 árboles, el error OOB y el
error de prueba fueron 0.090. Las variables con menor importancia fueron x7, x5 y x0.

## Entrega

La diapositiva 16 pide el cuaderno con la curva OOB, las importancias, la tabla comparativa y la
interpretación del modelo. No se indicó fecha ni plataforma. El archivo queda listo, pero no debe
subirse hasta que el profesor publique el medio de entrega o confirme que lo solicita.
