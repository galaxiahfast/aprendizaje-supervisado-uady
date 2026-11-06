# Práctica 10 - árboles para diabetes

Actividad individual de la clase 10. Compara árboles de clasificación con GaussianNB para predecir
diabetes a partir de variables clínicas.

## Archivo preparado

[práctica resuelta y ejecutada](practica-10-arboles-diabetes.ipynb)

## Revisión del trabajo

- Exploración del balance y promedios por clase: completa.
- Árbol con impureza Gini y búsqueda de profundidad: completo.
- Árbol con entropía y búsqueda de profundidad: completo.
- Reporte de clasificación y matriz de confusión: completos.
- Curva ROC y AUC del árbol: completos.
- Comparación con GaussianNB: completa.
- Conclusión y recomendación: completas.
- Ejecución de principio a fin: verificada sin errores.

## Resultados

| Modelo | Exactitud de prueba | AUC |
| --- | ---: | ---: |
| Árbol con entropía, profundidad 4 | 0.767 | 0.798 |
| GaussianNB | 0.778 | 0.834 |

GaussianNB obtuvo la mejor exactitud y el mejor AUC. El árbol produjo 87 falsos negativos. La
recomendación del cuaderno se basa en los resultados observados, sin ocultar el supuesto de
independencia que utiliza GaussianNB.

## Entrega

La diapositiva 35 de la presentación pide el cuaderno con la curva ROC, el AUC de ambos modelos y una
conclusión breve. No se indicó fecha ni plataforma. El archivo queda listo, pero no debe subirse hasta
que el profesor publique el medio de entrega o confirme que lo solicita.
