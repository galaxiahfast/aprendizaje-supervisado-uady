# Guía rápida de EDA

## Seis preguntas

1. **Forma:** ¿cuántas filas y columnas existen? ¿Qué tipo tiene cada variable?
2. **Calidad:** ¿hay datos faltantes o duplicados?
3. **Distribución:** ¿qué muestran los histogramas y boxplots?
4. **Casos raros:** ¿son errores, observaciones reales o valores censurados?
5. **Relaciones:** ¿Pearson y Spearman cuentan la misma historia?
6. **Decisión:** ¿qué se conserva, transforma, marca o excluye? ¿Cómo se comprobará el efecto?

## Fórmulas básicas

- Varianza muestral: $s^2=\frac{1}{n-1}\sum_i(x_i-\bar{x})^2$.
- Puntaje z: $z_i=\frac{x_i-\bar{x}}{s}$.
- Rango intercuartílico: $IQR=Q_3-Q_1$.
- Cercas de Tukey: $[Q_1-1.5\,IQR,\ Q_3+1.5\,IQR]$.
- Pearson: $r=\frac{s_{xy}}{s_xs_y}$.
- Spearman: correlación de Pearson aplicada a los rangos.

## Errores comunes

- Confiar solo en `describe()`.
- Borrar todos los puntos marcados por un boxplot.
- Tratar un tope censurado como un valor libre.
- Transformar todo el conjunto antes de separar entrenamiento y prueba.
- Interpretar correlación como causalidad.
- Declarar variables redundantes sin revisar los datos extremos.

Una buena decisión explica la evidencia, el posible efecto sobre el modelo y la forma de validarla.
