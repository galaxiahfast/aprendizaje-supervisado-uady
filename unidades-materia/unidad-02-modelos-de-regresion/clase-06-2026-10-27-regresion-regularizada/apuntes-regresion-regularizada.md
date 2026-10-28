# Apuntes de regresión regularizada

## Idea principal

La regularización agrega un costo por usar coeficientes grandes:

\[
\text{error de ajuste}+\alpha\,\text{penalización de los pesos}
\]

Con `alpha=0` se recupera OLS. Al aumentar `alpha`, el modelo acepta un poco más de sesgo para reducir
la varianza. Un valor excesivo lleva los coeficientes cerca de cero y produce subajuste. `alpha` se
elige con validación cruzada.

## Ridge, Lasso y Elastic Net

Ridge usa la suma de los coeficientes al cuadrado. Reduce todos los pesos de forma gradual, pero no
los lleva exactamente a cero. Es útil con variables correlacionadas porque reparte el peso entre
ellas y estabiliza la solución.

Lasso usa la suma del valor absoluto de los coeficientes. Puede llevar algunos a cero, por lo que
también funciona como selector de variables. Si varias columnas contienen casi la misma información,
puede elegir una y apagar las demás.

Elastic Net mezcla ambas penalizaciones. `l1_ratio` controla cuánto se parece a Lasso o a Ridge.
Puede conservar grupos de variables correlacionadas sin perder por completo la selección dispersa.

## Reglas de uso

- Escalar las variables dentro del pipeline.
- Elegir `alpha` con validación cruzada.
- Ajustar el escalador y el modelo solo con entrenamiento.
- Medir validación y prueba con la métrica normal, sin sumar la penalización.
- Comparar error de entrenamiento y validación para detectar sobreajuste o subajuste.
- Revisar cuántas variables quedan activas y si la solución es estable.

La regularización ayuda más cuando el número de variables es grande respecto al número de casos.
Con muchos datos, OLS y los modelos regularizados pueden producir resultados parecidos.

## Conclusiones del ejemplo

La colinealidad puede volver inestables los coeficientes sin arruinar de inmediato la predicción.
Escalar las variables tuvo más efecto que eliminar una sola columna correlacionada en el ejemplo de
la clase.

Quitar atípicos redujo el RMSE, pero también eliminó observaciones válidas y parte del ruido. Un error
menor después del recorte no demuestra por sí solo que la decisión sea correcta.

La transformación logarítmica volvió simétricas varias variables, aunque redujo su relación con el
objetivo y empeoró el RMSE. La transformación debe conservar información útil. No se aplica solo para
forzar una distribución simétrica.
