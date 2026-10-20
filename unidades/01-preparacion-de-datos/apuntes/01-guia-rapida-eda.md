# Guía rápida - EDA antes de modelar

## Las seis preguntas

1. **Forma:** ¿cuántas filas y columnas hay?, ¿qué tipo tiene cada variable?, ¿hay faltantes o duplicados?
2. **Centro y dispersión:** ¿qué dicen media, mediana, desviación, asimetría y curtosis?
3. **Distribución:** ¿qué muestran histogramas y boxplots que los números no muestran?
4. **Casos raros:** ¿son errores, observaciones reales, valores colectivos o topes censurados?
5. **Relaciones:** ¿Pearson y Spearman cuentan la misma historia?, ¿hay grupos o variables confusoras?
6. **Decisión:** ¿qué se conserva, transforma, marca o excluye, y cómo se comprobará el efecto?

## Fórmulas mínimas

- Varianza muestral: $s^2=\frac{1}{n-1}\sum_i(x_i-\bar{x})^2$.
- Puntaje z: $z_i=\frac{x_i-\bar{x}}{s}$.
- Rango intercuartílico: $IQR=Q_3-Q_1$.
- Cercas de Tukey: $[Q_1-1.5\,IQR,\;Q_3+1.5\,IQR]$.
- Pearson: $r=\frac{s_{xy}}{s_xs_y}$.
- Spearman: correlación de Pearson aplicada a los rangos.

## Errores que hay que evitar

- Confiar solo en `describe()` sin mirar distribuciones.
- Borrar automáticamente todo lo que el boxplot marque como atípico.
- Tratar un tope censurado como si fuera un valor real libre.
- Calcular transformaciones con todo el conjunto antes de separar entrenamiento y prueba.
- Interpretar correlación como causalidad.
- Declarar dos variables redundantes por Pearson sin revisar atípicos y Spearman.

## Criterio para una buena entrega

Cada decisión debe contestar tres cosas: qué evidencia la motiva, qué efecto puede tener en el
modelo y cómo se validará sin fuga de información.
