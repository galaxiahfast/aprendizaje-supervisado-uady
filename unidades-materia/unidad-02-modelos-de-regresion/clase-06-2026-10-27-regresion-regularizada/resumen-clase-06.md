# Clase 6 - regresión regularizada

Fecha: **27 de octubre de 2026**

La clase explicó cómo frenar un modelo con pesos grandes. Se compararon Ridge, Lasso y Elastic Net.
La segunda parte aplicó regresión lineal a datos simulados para revisar colinealidad, valores atípicos
y transformaciones.

## Temas vistos

- Función de costo con un término de regularización.
- Diferencia entre Ridge L2 y Lasso L1.
- Papel de `alpha` en el equilibrio entre ajuste y complejidad.
- Curvas de aprendizaje y alta dimensión.
- Elección de `alpha` mediante validación cruzada.
- Escalamiento antes de regularizar.
- Comportamiento ante variables colineales.
- Comparación de modelos lineales y polinomiales.
- Efecto de eliminar atípicos con la regla del IQR.
- Transformación logarítmica y comprobación de su utilidad.

Los [apuntes de regresión regularizada](apuntes-regresion-regularizada.md) reúnen las diferencias entre
los métodos y las conclusiones del ejemplo.

## Minutos de la clase

| Minuto | Contenido |
| --- | --- |
| [00:00:04](z-transcripcion-clase-06-2026-10-27-es.vtt#t=00:00:04) | Función de costo y término regularizador |
| [00:03:45](z-transcripcion-clase-06-2026-10-27-es.vtt#t=00:03:45) | Presentación de Ridge L2 y Lasso L1 |
| [00:12:54](z-transcripcion-clase-06-2026-10-27-es.vtt#t=00:12:54) | OLS frente a modelos regularizados |
| [00:18:24](z-transcripcion-clase-06-2026-10-27-es.vtt#t=00:18:24) | Regularización y estabilidad con pocos datos |
| [00:24:17](z-transcripcion-clase-06-2026-10-27-es.vtt#t=00:24:17) | Penalización Ridge |
| [00:28:03](z-transcripcion-clase-06-2026-10-27-es.vtt#t=00:28:03) | Penalización Lasso |
| [00:29:27](z-transcripcion-clase-06-2026-10-27-es.vtt#t=00:29:27) | Efecto del parámetro `alpha` |
| [00:33:53](z-transcripcion-clase-06-2026-10-27-es.vtt#t=00:33:53) | Implementación de Ridge y Lasso |
| [00:50:23](z-transcripcion-clase-06-2026-10-27-es.vtt#t=00:50:23) | Trayectoria de los coeficientes |
| [00:51:30](z-transcripcion-clase-06-2026-10-27-es.vtt#t=00:51:30) | Selección de la fuerza de regularización |
| [01:00:13](z-transcripcion-clase-06-2026-10-27-es.vtt#t=01:00:13) | Pregunta sobre entrenamiento y validación |
| [01:07:08](z-transcripcion-clase-06-2026-10-27-es.vtt#t=01:07:08) | Inicio del ejemplo con datos simulados |
| [01:17:08](z-transcripcion-clase-06-2026-10-27-es.vtt#t=01:17:08) | Revisión de colinealidad |
| [01:29:21](z-transcripcion-clase-06-2026-10-27-es.vtt#t=01:29:21) | Entrenamiento del modelo lineal |
| [01:33:04](z-transcripcion-clase-06-2026-10-27-es.vtt#t=01:33:04) | Comparación con modelos polinomiales |
| [01:44:16](z-transcripcion-clase-06-2026-10-27-es.vtt#t=01:44:16) | Qué se pierde al eliminar atípicos |
| [01:45:18](z-transcripcion-clase-06-2026-10-27-es.vtt#t=01:45:18) | Transformaciones logarítmicas |
| [01:48:43](z-transcripcion-clase-06-2026-10-27-es.vtt#t=01:48:43) | Notebook de práctica y tema de la siguiente clase |

## Avisos

- El profesor indicó que compartiría el notebook para revisarlo con calma.
- La siguiente clase será el jueves 29 de octubre.
- El tema anunciado para esa sesión es máquinas de soporte vectorial.
- No se anunció una entrega nueva durante esta clase.

## Archivos de esta clase

- [presentación oficial](presentacion-regresion-regularizada.pdf)
- [transcripción](z-transcripcion-clase-06-2026-10-27-es.vtt)
- [práctica de regresión regularizada](../../../tareas-practicas/practicas-clase/practica-05-regresion-regularizada/resumen-practica-05.md)

La grabación está guardada en esta carpeta con el prefijo `z-`. Git la ignora y no se sube al
repositorio.
