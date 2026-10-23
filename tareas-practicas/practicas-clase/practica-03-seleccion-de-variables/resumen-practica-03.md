# Práctica 3 — selección de variables

Clase relacionada: **clase 3 del 22 de octubre de 2026**

Estado: **resuelta y ejecutada. No se entrega**

El profesor aclaró al final de la clase que este notebook es para practicar. El entregable será otro
notebook que integra los tres temas de la primera semana.

## Archivos de la práctica

- [notebook resuelto](practica-03-seleccion-de-variables-resuelta.ipynb)
- [tabla comparativa](resultados-seleccion-variables.csv)

Estos archivos sirven para estudiar y preparar el laboratorio integrador.

## Criterios cubiertos

- [x] Explora el conjunto de cáncer de mama y establece una línea base.
- [x] Crea variables del dominio y comprueba su efecto.
- [x] Aplica varianza, correlación, redundancia e información mutua.
- [x] Ejecuta RFE y RFECV.
- [x] Ejecuta selección integrada con Lasso.
- [x] Compara los cuatro métodos con el mismo protocolo de validación cruzada.
- [x] Mide estabilidad mediante 30 remuestreos.
- [x] Provoca una fuga de datos y la corrige con Pipeline.
- [x] Incluye método, k, exactitud, sensibilidad, variables y comentario.
- [x] Ejecuta todas las celdas sin errores.

## Resultados principales

| Resultado | Exactitud | Sensibilidad a malignos |
| --- | ---: | ---: |
| Línea base con 30 variables | 0.978 | 0.961 |
| Información mutua con 8 variables | 0.949 | 0.924 |
| ANOVA F con 8 variables | 0.949 | 0.920 |
| RFE con 8 variables | 0.962 | 0.943 |
| Lasso con 8 variables | 0.973 | 0.953 |
| Lasso con 10 variables | 0.973 | 0.959 |

Se eligió Lasso con diez variables. En prueba obtuvo exactitud 0.982 y sensibilidad 0.976. Igualó la
línea base usando un tercio de las mediciones. Ambos modelos perdieron uno de los 42 casos malignos.

La prueba de fuga produjo exactitud 0.833 con datos de ruido. Al colocar el selector dentro del
pipeline bajó a 0.450, cerca del azar esperado.

