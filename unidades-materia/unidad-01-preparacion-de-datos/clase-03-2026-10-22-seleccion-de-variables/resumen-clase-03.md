# Clase 3 — ingeniería y selección de variables

Fecha: **22 de octubre de 2026**

Duración: **1 h 55 min**

Próxima sesión indicada: **viernes 23 de octubre de 2026**

## Avisos

- Los notebooks de las clases 1, 2 y 3 son prácticas. No se entregan.
- En la clase del 23 de octubre se compartirá un notebook integrador que sí cuenta para evaluación.
- El plazo acordado para ese notebook fue el viernes 30 de octubre de 2026.
- El medio de entrega se confirmará el 23 de octubre. Se mencionaron GitHub y Google Forms.

## Archivos de la clase

- [apuntes de selección de variables](apuntes-seleccion-variables.md)
- [presentación de selección de variables](presentacion-seleccion-variables.pdf)
- [transcripción en español](z-transcripcion-clase-03-2026-10-22-es.vtt)
- [transcripción original](z-transcripcion-clase-03-2026-10-22-original.vtt)
- [práctica resuelta](../../../tareas-practicas/practicas-clase/practica-03-seleccion-de-variables/resumen-practica-03.md)
- [entrega anunciada](../../../tareas-practicas/tareas-entregables/tarea-01-examen-modulo-01/resumen-tarea-01.md)

El video `z-video-clase-03-2026-10-22.mp4` está en esta carpeta solo en el equipo. Git no lo sube.

## Minutos y temas

| Minutos | Tema | Contenido |
| --- | --- | --- |
| `00:00-16:06` | Panorama | Explica por qué sobran variables y presenta filtro, envoltura e integrado. |
| `16:06-32:24` | Variables del dominio | Revisa razones, fechas, agregados, logaritmos y transformaciones. |
| `32:24-48:13` | Polinomios e interacciones | Muestra crecimiento de columnas, flexibilidad y sobreajuste. |
| `49:37-57:04` | Familias de selección | Compara costo, uso del modelo y limitaciones de cada familia. |
| `57:04-1:02:51` | Umbral de varianza | Explica su dependencia de las unidades y el efecto de estandarizar. |
| `1:02:51-1:10:34` | Correlación y redundancia | Ordena por relación con la salida y retira variables repetidas. |
| `1:10:34-1:21:20` | Información mutua | Contrasta relaciones lineales, no lineales y ruido. |
| `1:21:20-1:33:00` | RFE y RFECV | Elimina variables por rondas y decide cuántas conservar. |
| `1:33:00-1:44:32` | Lasso | Explica penalización L1, coeficientes en cero y efecto de C. |
| `1:44:32-1:50:24` | Comparación | Contrasta filtros, RFE y Lasso con el mismo protocolo. |
| `1:50:24-1:55:51` | Entregas | Aclara cuáles notebooks son práctica, anuncia el entregable y fija el plazo. |

## Resumen

La ingeniería de variables crea representaciones que el modelo no obtiene por sí solo. Las razones
eliminan el efecto del tamaño. Los logaritmos reducen asimetría. Los polinomios representan curvas.
Las interacciones expresan efectos conjuntos. Cada propuesta se conserva solo si mejora la validación.

La selección reduce ruido, costo y dificultad de interpretación. Los filtros usan puntajes
estadísticos. RFE prueba el aporte de las variables con un modelo. Lasso selecciona durante el ajuste
mediante coeficientes que llegan a cero.

La correlación puede repetir radio, perímetro y área porque describen casi lo mismo. La información
mutua detecta relaciones no lineales. RFE y Lasso consideran el modelo, aunque su lista puede cambiar
cuando existen variables correlacionadas.

La selección aprende de las etiquetas. Debe estar dentro del pipeline y de la validación cruzada.
Seleccionar antes de validar produce fuga de datos y resultados demasiado optimistas.

