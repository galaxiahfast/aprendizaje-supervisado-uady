# Actividad 1 - EDA de California Housing

## Objetivo

Explorar el conjunto California Housing, identificar valores extremos y topes, comparar Pearson
con Spearman y justificar un tratamiento por cada variable predictora antes de modelar.

## Archivos para entregar

- [`actividad_eda_california_housing_resuelta.ipynb`](actividad_eda_california_housing_resuelta.ipynb): notebook contestado y ejecutado de principio a fin.
- [`entregable_unidad1.csv`](entregable_unidad1.csv): tabla solicitada con porcentaje de atípicos, decisión y justificación por variable.

La [plantilla original](plantilla/actividad_eda_california_housing.ipynb) se conserva como referencia y no es la versión que debe subirse.

## Cobertura de los criterios

- [x] Carga, forma, tipos, faltantes y duplicados.
- [x] Media, mediana, desviación, asimetría y curtosis.
- [x] Histogramas y explicación del recorte exclusivamente visual.
- [x] Atípicos con $1.5\,IQR$ y $3\,IQR$.
- [x] Revisión contextual de filas extremas.
- [x] Diferencia entre atípicos y topes censurados.
- [x] Comparación de `clip`, logaritmo y datos originales.
- [x] Análisis bivariado, mapa y cuartiles de ingreso.
- [x] Pearson, Spearman, heatmaps y VIF.
- [x] Tabla de decisiones y reflexión final.
- [x] Reto opcional IQR frente a puntaje z.

## Hallazgos principales

- El conjunto tiene 20 640 distritos, nueve variables, cero faltantes y cero duplicados.
- `AveOccup` alcanza 1 243.33 porque algunos distritos contienen muy pocos hogares; su máximo está a unas 119 desviaciones estándar de la media.
- `MedHouseVal` contiene 992 casos en el tope 5.0 y `HouseAge`, 1 273 en el tope 52.
- `MedInc` es la variable más asociada con el objetivo (Pearson 0.688).
- La relación `AveRooms`-`AveBedrms` cae de 0.848 con Pearson a 0.082 con Spearman: unos pocos extremos inflan la correlación lineal.
- Al retirar `AveBedrms`, el VIF de `AveRooms` baja de 8.34 a 1.26.

## Reproducir la entrega

Con Python 3.10 o posterior:

```bash
python -m pip install numpy pandas matplotlib scikit-learn jupyter nbclient nbformat
python herramientas/preparar_entrega_unidad1.py
```

La primera ejecución puede descargar aproximadamente 1 MB del conjunto California Housing.

## Verificación realizada

Se ejecutaron las 29 celdas de código en orden. La revisión automática terminó con **29/29 celdas ejecutadas y 0 errores**; el CSV fue generado desde la tabla visible en el notebook.
