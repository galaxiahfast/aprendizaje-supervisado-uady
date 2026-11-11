# Tarea 3 - examen del módulo 3

**Tema:** evaluación de modelos con datos desbalanceados  
**Fecha límite:** domingo 15 de noviembre de 2026 a las 23:00  
**Entrega:** [formulario oficial](https://forms.gle/2qxkfK9Qv6ApbiiU7)  
**Estado:** listo para subir

## Archivo que se entrega

[Ortiz_Julian_Examen_Modulo3.ipynb](Ortiz_Julian_Examen_Modulo3.ipynb)

Solo se sube ese notebook. El PDF de criterios se conserva como referencia y no forma parte de la
entrega.

## Revisión de los criterios

| Criterio | Valor | Estado |
| --- | ---: | --- |
| Preparación, partición estratificada y modelo base | 20 | Completo |
| Sobremuestreo con validación y prueba | 15 | Completo |
| Submuestreo con validación y prueba | 15 | Completo |
| SMOTE con validación y prueba | 15 | Completo |
| Pesos balanceados con validación y prueba | 10 | Completo |
| Tabla comparativa y recomendación fundamentada | 10 | Completo |
| Calibración, curva de confiabilidad y Brier score | 15 | Completo |
| **Total cubierto** | **100** | **Completo** |

## Comprobaciones

- El dataset usa exactamente el bloque y las semillas indicadas.
- La prueba se separa antes de comparar estrategias.
- El remuestreo ocurre dentro de cada pliegue de validación.
- Se reportan media y desviación del MCC en cinco pliegues.
- Se reportan exactitud, MCC y kappa sobre prueba.
- La estrategia se elige con validación, no reutilizando prueba.
- La calibración se ajusta solo con entrenamiento.
- Las versiones de las librerías aparecen al inicio.
- El notebook fue ejecutado completo sin errores.

## Antes de enviarlo

- [ ] Abrir el notebook y revisar que se vean las gráficas.
- [ ] Subir solamente `Ortiz_Julian_Examen_Modulo3.ipynb`.
- [ ] Confirmar que el formulario muestre el envío registrado.
- [ ] Guardar una captura de la confirmación en esta carpeta.

Los [criterios oficiales](criterios-evaluacion-modulo-03.pdf) están guardados junto al notebook.
