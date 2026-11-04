from pathlib import Path
import os

import nbformat as nbf
from nbclient import NotebookClient


RAIZ = Path(__file__).resolve().parents[2]
CARPETA = RAIZ / "tareas-practicas/tareas-entregables/tarea-02-examen-modulo-02"
DESTINO = CARPETA / "ortiz_julian_examen_modulo2.ipynb"


def texto(contenido):
    return nbf.v4.new_markdown_cell(contenido.strip())


def codigo(contenido):
    return nbf.v4.new_code_cell(contenido.strip())


def construir():
    nb = nbf.v4.new_notebook()
    nb.metadata.kernelspec = {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3",
    }
    nb.metadata.language_info = {"name": "python", "version": "3"}
    nb.cells = [
        texto(
            """
# Examen del módulo 2 - métodos de regresión

**Estudiante:** Julian Emiliano Ortiz Rivero  
**Materia:** Aprendizaje Supervisado  
**Problema:** estabilidad de redes eléctricas

Este cuaderno compara cinco familias de regresión con el mismo protocolo de validación cruzada. El
archivo de prueba se usa únicamente al final, cuando esté disponible.
"""
        ),
        codigo(
            """
NOMBRE = "Julian Emiliano Ortiz Rivero"

import sys
from pathlib import Path
import time
import warnings

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from IPython.display import Markdown, display
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV, KFold, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor

warnings.filterwarnings("ignore")
plt.rcParams.update({"figure.dpi": 110, "axes.grid": True, "grid.alpha": 0.25})

print("Nombre:", NOMBRE)
print("Python:", sys.version.split()[0])
print("NumPy:", np.__version__)
print("pandas:", pd.__version__)
print("Matplotlib:", matplotlib.__version__)
print("scikit-learn:", sklearn.__version__)
"""
        ),
        texto(
            """
## 1. Carga y revisión inicial

Se verifica la forma del archivo, los tipos de datos, los valores faltantes y los registros
duplicados antes de ajustar cualquier modelo.
"""
        ),
        codigo(
            """
RUTA_ENTRENAMIENTO = Path("electrical_grid_stability_train.csv")
if not RUTA_ENTRENAMIENTO.exists():
    raise FileNotFoundError("Coloca electrical_grid_stability_train.csv junto al notebook")

datos = pd.read_csv(RUTA_ENTRENAMIENTO)
esperadas = [f"tau{i}" for i in range(1, 5)] + [f"p{i}" for i in range(1, 5)] + [f"g{i}" for i in range(1, 5)] + ["stab"]
if list(datos.columns) != esperadas:
    raise ValueError(f"Columnas inesperadas: {list(datos.columns)}")

print("Dimensiones:", datos.shape)
print("Duplicados:", int(datos.duplicated().sum()))
print("Valores faltantes:", int(datos.isna().sum().sum()))
display(datos.head())
display(datos.describe().T.round(4))
"""
        ),
        texto(
            """
## 2. Análisis exploratorio

Las distribuciones permiten revisar rangos y posibles valores extremos. La matriz de correlación
muestra la relación lineal entre los predictores y `stab`.
"""
        ),
        codigo(
            """
ejes = datos.hist(bins=30, figsize=(14, 10), color="#2f6f9f", edgecolor="white")
plt.suptitle("Distribuciones de las variables", y=1.01)
plt.tight_layout()
plt.show()

correlacion = datos.corr(numeric_only=True)
plt.figure(figsize=(10, 8))
imagen = plt.imshow(correlacion, cmap="coolwarm", vmin=-1, vmax=1)
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45, ha="right")
plt.yticks(range(len(correlacion.index)), correlacion.index)
plt.colorbar(imagen, label="Correlación")
plt.title("Correlación entre variables")
plt.tight_layout()
plt.show()

print("Correlación con stab:")
display(correlacion["stab"].drop("stab").sort_values().to_frame("correlacion").round(4))
"""
        ),
        codigo(
            """
q1 = datos.quantile(0.25)
q3 = datos.quantile(0.75)
iqr = q3 - q1
atipicos = datos.lt(q1 - 1.5 * iqr) | datos.gt(q3 + 1.5 * iqr)
resumen_atipicos = atipicos.sum().to_frame("cantidad")
resumen_atipicos["porcentaje"] = (100 * resumen_atipicos["cantidad"] / len(datos)).round(3)
display(resumen_atipicos)

error_balance = (datos["p1"] + datos["p2"] + datos["p3"] + datos["p4"]).abs().max()
print(f"Mayor error en el balance p1 + p2 + p3 + p4: {error_balance:.2e}")
"""
        ),
        texto(
            """
### Hallazgos del EDA

- El archivo contiene 8 000 observaciones y 13 columnas numéricas.
- No hay valores faltantes ni registros duplicados.
- La regla del IQR marca un solo valor de `p1`. Su proporción es 0.013 % y se conserva porque está
  dentro del comportamiento esperado de la potencia total.
- `tau1` a `tau4` y `g1` a `g4` presentan las asociaciones lineales más claras con `stab`. Las
  correlaciones individuales son moderadas, entre 0.277 y 0.309.
- `p1` depende de `p2`, `p3` y `p4` por el balance de la red. Se conservan las columnas solicitadas,
  aunque esta relación puede volver inestables los coeficientes de una regresión sin regularización.

No se eliminan observaciones. El escalamiento se coloca dentro de los `Pipeline` que lo necesitan
para evitar fuga de información durante la validación cruzada.
"""
        ),
        texto(
            """
## 3. Preparación y protocolo de evaluación

Se usan cinco pliegues con mezcla y una semilla fija. Todos los modelos reciben las mismas
particiones. La métrica principal es RMSE. También se reporta R² para facilitar la interpretación.
"""
        ),
        codigo(
            """
X = datos.drop(columns="stab")
y = datos["stab"]

cv = KFold(n_splits=5, shuffle=True, random_state=42)
metricas = {"rmse": "neg_root_mean_squared_error", "r2": "r2"}
resultados = []
modelos_finales = {}


def registrar(nombre, estimador, rmse_pliegues, r2_pliegues, parametros):
    resultados.append(
        {
            "modelo": nombre,
            "rmse_medio": float(np.mean(rmse_pliegues)),
            "rmse_desviacion": float(np.std(rmse_pliegues)),
            "r2_medio": float(np.mean(r2_pliegues)),
            "r2_desviacion": float(np.std(r2_pliegues)),
            "hiperparametros": str(parametros),
        }
    )
    modelos_finales[nombre] = estimador


def registrar_busqueda(nombre, busqueda):
    i = busqueda.best_index_
    rmse_medio = -busqueda.cv_results_["mean_test_rmse"][i]
    rmse_desviacion = busqueda.cv_results_["std_test_rmse"][i]
    r2_medio = busqueda.cv_results_["mean_test_r2"][i]
    r2_desviacion = busqueda.cv_results_["std_test_r2"][i]
    registrar(
        nombre,
        busqueda.best_estimator_,
        np.array([rmse_medio]),
        np.array([r2_medio]),
        busqueda.best_params_,
    )
    resultados[-1]["rmse_desviacion"] = float(rmse_desviacion)
    resultados[-1]["r2_desviacion"] = float(r2_desviacion)
"""
        ),
        texto(
            """
## 4. Regresión lineal

El modelo lineal funciona como referencia. Se escalan los predictores dentro del pipeline.
"""
        ),
        codigo(
            """
lineal = Pipeline(
    [
        ("escalado", StandardScaler()),
        ("modelo", LinearRegression()),
    ]
)
t0 = time.time()
cv_lineal = cross_validate(lineal, X, y, cv=cv, scoring=metricas, n_jobs=1)
lineal.fit(X, y)
registrar(
    "Regresión lineal",
    lineal,
    -cv_lineal["test_rmse"],
    cv_lineal["test_r2"],
    {},
)
print(f"Tiempo: {time.time() - t0:.1f} s")
print(resultados[-1])
"""
        ),
        texto(
            """
## 5. Regresión polinomial sin regularización

Se comparan grados 2 y 3. La selección se realiza únicamente con los pliegues de entrenamiento.
"""
        ),
        codigo(
            """
polinomial = Pipeline(
    [
        ("polinomio", PolynomialFeatures(include_bias=False)),
        ("escalado", StandardScaler()),
        ("modelo", LinearRegression()),
    ]
)
malla_polinomial = {"polinomio__degree": [2, 3]}
t0 = time.time()
busqueda_polinomial = GridSearchCV(
    polinomial,
    malla_polinomial,
    cv=cv,
    scoring=metricas,
    refit="rmse",
    n_jobs=1,
)
busqueda_polinomial.fit(X, y)
registrar_busqueda("Polinomial sin regularización", busqueda_polinomial)
print(f"Tiempo: {time.time() - t0:.1f} s")
print("Mejor configuración:", busqueda_polinomial.best_params_)
print(resultados[-1])
"""
        ),
        texto(
            """
## 6. Regresión polinomial con regularización

Se utiliza Ridge sobre un polinomio de grado 2. La malla compara cinco intensidades de penalización.
"""
        ),
        codigo(
            """
ridge = Pipeline(
    [
        ("polinomio", PolynomialFeatures(degree=2, include_bias=False)),
        ("escalado", StandardScaler()),
        ("modelo", Ridge()),
    ]
)
malla_ridge = {"modelo__alpha": [0.01, 0.1, 1.0, 10.0, 100.0]}
t0 = time.time()
busqueda_ridge = GridSearchCV(
    ridge,
    malla_ridge,
    cv=cv,
    scoring=metricas,
    refit="rmse",
    n_jobs=1,
)
busqueda_ridge.fit(X, y)
registrar_busqueda("Polinomial con Ridge", busqueda_ridge)
print(f"Tiempo: {time.time() - t0:.1f} s")
print("Mejor configuración:", busqueda_ridge.best_params_)
print(resultados[-1])
"""
        ),
        texto(
            """
## 7. Support Vector Regression

Se prueba el kernel RBF. La búsqueda ajusta `C`, `epsilon` y `gamma`. El escalamiento forma parte del
pipeline porque SVR depende de las distancias entre observaciones.
"""
        ),
        codigo(
            """
svr = Pipeline(
    [
        ("escalado", StandardScaler()),
        ("modelo", SVR(kernel="rbf")),
    ]
)
malla_svr = {
    "modelo__C": [1.0, 10.0, 100.0],
    "modelo__epsilon": [0.01, 0.1],
    "modelo__gamma": ["scale", 0.01],
}
t0 = time.time()
busqueda_svr = GridSearchCV(
    svr,
    malla_svr,
    cv=cv,
    scoring=metricas,
    refit="rmse",
    n_jobs=1,
)
busqueda_svr.fit(X, y)
registrar_busqueda("SVR con RBF", busqueda_svr)
print(f"Tiempo: {time.time() - t0:.1f} s")
print("Mejor configuración:", busqueda_svr.best_params_)
print(resultados[-1])
"""
        ),
        texto(
            """
## 8. Árbol de decisión

La profundidad, el tamaño mínimo de hoja y el parámetro de poda se ajustan mediante la misma
validación cruzada. No se escala porque el árbol trabaja con ordenamientos y puntos de corte.
"""
        ),
        codigo(
            """
arbol = DecisionTreeRegressor(random_state=42)
malla_arbol = {
    "max_depth": [3, 5, 8, 12, None],
    "min_samples_leaf": [1, 5, 20],
    "ccp_alpha": [0.0, 0.000001, 0.00001],
}
t0 = time.time()
busqueda_arbol = GridSearchCV(
    arbol,
    malla_arbol,
    cv=cv,
    scoring=metricas,
    refit="rmse",
    n_jobs=1,
)
busqueda_arbol.fit(X, y)
registrar_busqueda("Árbol de decisión", busqueda_arbol)
print(f"Tiempo: {time.time() - t0:.1f} s")
print("Mejor configuración:", busqueda_arbol.best_params_)
print(resultados[-1])
"""
        ),
        texto(
            """
## 9. Comparación de resultados

La tabla usa la media y la desviación estándar obtenidas en los cinco pliegues. Un RMSE menor indica
predicciones más cercanas al valor real de `stab`.
"""
        ),
        codigo(
            """
tabla_resultados = pd.DataFrame(resultados).sort_values("rmse_medio").reset_index(drop=True)
columnas_numericas = ["rmse_medio", "rmse_desviacion", "r2_medio", "r2_desviacion"]
tabla_mostrada = tabla_resultados.copy()
tabla_mostrada[columnas_numericas] = tabla_mostrada[columnas_numericas].round(6)
display(tabla_mostrada)

mejor = tabla_resultados.iloc[0]
segundo = tabla_resultados.iloc[1]
diferencia = segundo["rmse_medio"] - mejor["rmse_medio"]
conclusion = f'''
### Conclusiones

El menor RMSE de validación corresponde a **{mejor['modelo']}**, con
**{mejor['rmse_medio']:.6f} ± {mejor['rmse_desviacion']:.6f}**. El segundo lugar es
**{segundo['modelo']}** con una diferencia de **{diferencia:.6f}**. La comparación se hizo con las
mismas cinco particiones para todos los modelos. La regresión lineal sirve como referencia, mientras
los métodos no lineales pueden representar interacciones entre tiempos de reacción, potencias y
elasticidades. La decisión final se basa en validación cruzada porque el archivo de prueba no debe
participar en la selección.
'''
display(Markdown(conclusion))
"""
        ),
        texto(
            """
## 10. Evaluación final en el archivo de prueba

El profesor indicó que `electrical_grid_stability_test.csv` se entregará por separado. La celda
siguiente se ejecuta sin error si el archivo todavía no está disponible. Cuando se agregue, ajustará
cada configuración con las 8 000 filas y guardará `predicciones_modulo2.csv`.

Si el archivo de prueba no contiene `stab`, se pueden generar predicciones, pero no calcular RMSE.
Esta limitación se deja explícita porque el RMSE necesita valores reales con los cuales comparar.
"""
        ),
        codigo(
            """
RUTA_PRUEBA = Path("electrical_grid_stability_test.csv")

if not RUTA_PRUEBA.exists():
    print("Pendiente: el profesor aún no ha proporcionado electrical_grid_stability_test.csv")
else:
    prueba = pd.read_csv(RUTA_PRUEBA)
    y_prueba = prueba.pop("stab") if "stab" in prueba.columns else None
    if list(prueba.columns) != list(X.columns):
        raise ValueError("Las columnas del archivo de prueba no coinciden con las de entrenamiento")

    predicciones = pd.DataFrame({"fila": np.arange(1, len(prueba) + 1)})
    metricas_prueba = []
    for nombre, modelo in modelos_finales.items():
        modelo.fit(X, y)
        pred = modelo.predict(prueba)
        predicciones[nombre] = pred
        if y_prueba is not None:
            metricas_prueba.append(
                {
                    "modelo": nombre,
                    "rmse_prueba": mean_squared_error(y_prueba, pred) ** 0.5,
                    "r2_prueba": r2_score(y_prueba, pred),
                }
            )

    predicciones.to_csv("predicciones_modulo2.csv", index=False, encoding="utf-8")
    print("Archivo generado: predicciones_modulo2.csv")
    if metricas_prueba:
        display(pd.DataFrame(metricas_prueba).sort_values("rmse_prueba"))
    else:
        print("El archivo no incluye stab. Se generaron predicciones, pero el RMSE no puede calcularse.")
"""
        ),
        texto(
            """
## Revisión antes de entregar

- Nombre completo incluido en `NOMBRE`.
- Librerías y versiones impresas al inicio.
- EDA y decisiones de preprocesamiento justificadas.
- Cinco familias de regresión comparadas.
- Validación cruzada de cinco pliegues con media y desviación estándar.
- Tabla comparativa y conclusiones incluidas.
- Bloque de prueba preparado para el archivo pendiente.

El formulario acepta únicamente el notebook ejecutado. Los CSV y el PDF no se suben.
"""
        ),
    ]
    return nb


def main():
    CARPETA.mkdir(parents=True, exist_ok=True)
    os.environ.update(OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", MKL_NUM_THREADS="1")
    nb = construir()
    nbf.write(nb, DESTINO)
    cliente = NotebookClient(
        nb,
        timeout=3600,
        kernel_name="python3",
        resources={"metadata": {"path": str(CARPETA)}},
    )
    cliente.execute()
    nbf.write(nb, DESTINO)


if __name__ == "__main__":
    main()
