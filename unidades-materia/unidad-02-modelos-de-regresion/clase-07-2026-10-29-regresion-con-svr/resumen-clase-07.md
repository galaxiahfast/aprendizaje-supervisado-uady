# Clase 7 - regresión con máquinas de soporte vectorial

Fecha: **29 de octubre de 2026**

La clase comenzó con un repaso del ejemplo de regresión regularizada. Después se explicó cómo adaptar
las máquinas de soporte vectorial a un problema de regresión. La idea central es permitir una banda
de error alrededor de la predicción y concentrar el ajuste en los puntos que quedan fuera.

La presentación identifica el tema como sesión 6. En el orden cronológico de la materia es la clase
7 porque la sesión de repaso del 23 de octubre se guardó como clase 4.

## Temas vistos

- Margen duro y margen blando.
- Papel de `C` en la tolerancia a errores.
- Tubo de tolerancia `epsilon`.
- Vectores de soporte en regresión.
- Kernel lineal, polinomial y RBF.
- Efecto de `gamma` sobre la forma de la curva.
- Escalamiento antes de usar SVR.
- Búsqueda conjunta de hiperparámetros.
- Comparación con regresión lineal y polinomial.

Los [apuntes de SVR](apuntes-regresion-con-svr.md) reúnen las ideas principales y las reglas para
elegir los hiperparámetros.

## Minutos de la clase

| Minuto | Contenido |
| --- | --- |
| [00:03:59](z-transcripcion-clase-07-2026-10-29-es.vtt#t=00:03:59) | Repaso del ejemplo de regresión regularizada |
| [00:17:59](z-transcripcion-clase-07-2026-10-29-es.vtt#t=00:17:59) | Aviso sobre el notebook de la clase anterior |
| [00:20:00](z-transcripcion-clase-07-2026-10-29-es.vtt#t=00:20:00) | Inicio de máquinas de soporte vectorial |
| [00:22:47](z-transcripcion-clase-07-2026-10-29-es.vtt#t=00:22:47) | Margen blando y parámetro `C` |
| [00:34:02](z-transcripcion-clase-07-2026-10-29-es.vtt#t=00:34:02) | Vectores de soporte |
| [00:35:20](z-transcripcion-clase-07-2026-10-29-es.vtt#t=00:35:20) | Diferencia entre margen duro y margen blando |
| [00:44:58](z-transcripcion-clase-07-2026-10-29-es.vtt#t=00:44:58) | Paso de clasificación a regresión |
| [00:46:31](z-transcripcion-clase-07-2026-10-29-es.vtt#t=00:46:31) | Tubo de tolerancia en SVR |
| [00:56:27](z-transcripcion-clase-07-2026-10-29-es.vtt#t=00:56:27) | Solución basada en pocos vectores de soporte |
| [00:59:56](z-transcripcion-clase-07-2026-10-29-es.vtt#t=00:59:56) | Efecto del parámetro `C` |
| [01:07:06](z-transcripcion-clase-07-2026-10-29-es.vtt#t=01:07:06) | Efecto de `epsilon` |
| [01:17:42](z-transcripcion-clase-07-2026-10-29-es.vtt#t=01:17:42) | Truco del kernel |
| [01:19:45](z-transcripcion-clase-07-2026-10-29-es.vtt#t=01:19:45) | Kernel lineal, polinomial y gaussiano |
| [01:33:37](z-transcripcion-clase-07-2026-10-29-es.vtt#t=01:33:37) | Cambios en la curva según los parámetros |
| [01:36:44](z-transcripcion-clase-07-2026-10-29-es.vtt#t=01:36:44) | Selección mediante búsqueda en malla |
| [01:39:13](z-transcripcion-clase-07-2026-10-29-es.vtt#t=01:39:13) | Tema anunciado para la siguiente clase |
| [01:42:00](z-transcripcion-clase-07-2026-10-29-es.vtt#t=01:42:00) | Notebook de la actividad de SVR |

## Práctica de clase

La versión actual del cuaderno oficial aclara que ya está completa y no se entrega. Está guardada
como [práctica 6](../../../tareas-practicas/practicas-clase/practica-06-svr-consumo-energetico/resumen-practica-06.md).

## Archivos de esta clase

- [presentación oficial](presentacion-regresion-con-svr.pdf)
- [transcripción](z-transcripcion-clase-07-2026-10-29-es.vtt)
- [práctica 6 de SVR](../../../tareas-practicas/practicas-clase/practica-06-svr-consumo-energetico/resumen-practica-06.md)

La grabación está guardada en esta carpeta con el prefijo `z-`. Git la ignora.
