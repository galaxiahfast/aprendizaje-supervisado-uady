# Práctica 9 - Naive Bayes para texto

Actividad individual de la clase 10. Compara MultinomialNB con BernoulliNB para clasificar textos de
cocina y cine.

## Archivo preparado

[práctica resuelta y ejecutada](practica-09-naive-bayes-texto.ipynb)

## Revisión del trabajo

- Exploración del conjunto y del vocabulario: completa.
- Entrenamiento de MultinomialNB: completo.
- Entrenamiento de BernoulliNB: completo.
- Palabras con mayor peso por clase: revisadas.
- Tres documentos de prueba escritos y clasificados: completos.
- Comparación del efecto de palabras repetidas: completa.
- Respuestas escritas con base en los resultados: completas.
- Ejecución de principio a fin: verificada sin errores.

## Resultados

| Modelo | Exactitud de prueba |
| --- | ---: |
| MultinomialNB | 1.000 |
| BernoulliNB | 1.000 |

Los dos modelos separaron correctamente las clases. La diferencia se observó al repetir una palabra.
MultinomialNB aumentó su confianza porque usa frecuencias. BernoulliNB mantuvo casi la misma
probabilidad porque solo registra la presencia de la palabra.

## Entrega

La diapositiva 34 de la presentación pide el cuaderno con las respuestas y los tres documentos de
prueba escritos por el estudiante. No se indicó fecha ni plataforma. El archivo queda listo, pero no
debe subirse hasta que el profesor publique el medio de entrega o confirme que lo solicita.
