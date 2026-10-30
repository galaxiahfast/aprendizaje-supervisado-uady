"""Completa y ejecuta la actividad entregable de SVR."""

from __future__ import annotations

import argparse
from pathlib import Path

import nbformat
from nbclient import NotebookClient


RAIZ = Path(__file__).resolve().parents[2]
ORIGEN = RAIZ / "z-asistente" / "plantillas-originales" / "unidad-02-clase-07-actividad-svr.ipynb"
CARPETA = RAIZ / "tareas-practicas" / "tareas-entregables" / "tarea-02-svr-consumo-energetico"
SALIDA = CARPETA / "ortiz-julian-actividad-svr.ipynb"


CODIGO = {
    2: '''import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.metrics import mean_squared_error

warnings.filterwarnings("ignore")
plt.rcParams.update({"figure.dpi": 110, "axes.grid": True, "grid.alpha": 0.3})

datos = pd.read_csv("consumo-energetico.csv")
FEATS = ["temperatura_c", "superficie_m2", "ocupantes", "aislamiento", "fin_semana"]
X = datos[FEATS].values
y = datos["consumo_kwh"].values

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=42)
kf = KFold(5, shuffle=True, random_state=0)

def rmse(m, X, y):
    return np.sqrt(mean_squared_error(y, m.predict(X)))

print(f"n entrenamiento = {len(Xtr)}   n prueba = {len(Xte)}   variables = {FEATS}")
datos.describe().round(2).T''',
    6: '''lineal = make_pipeline(
    StandardScaler(), SVR(kernel="linear", C=10, epsilon=1.0)
).fit(Xtr, ytr)
print(f"SVR lineal   RMSE entrenamiento = {rmse(lineal, Xtr, ytr):.2f}    RMSE prueba = {rmse(lineal, Xte, yte):.2f}")
print(f"Vectores de soporte: {lineal[-1].support_.shape[0]} de {len(Xtr)}")''',
    9: '''rbf_defecto = make_pipeline(StandardScaler(), SVR(kernel="rbf")).fit(Xtr, ytr)
print(f"SVR RBF (por defecto)  RMSE entrenamiento = {rmse(rbf_defecto, Xtr, ytr):.2f}    RMSE prueba = {rmse(rbf_defecto, Xte, yte):.2f}")
print(f"Hiperparámetros usados: C={rbf_defecto[-1].C}, epsilon={rbf_defecto[-1].epsilon}, gamma={rbf_defecto[-1].gamma}")
print(f"Vectores de soporte: {rbf_defecto[-1].support_.shape[0]} de {len(Xtr)}")''',
    12: '''valores_C = [0.01, 0.1, 1, 10, 100, 1000]
filas_c = []
for C in valores_C:
    m = make_pipeline(
        StandardScaler(), SVR(kernel="rbf", C=C, epsilon=1.0)
    ).fit(Xtr, ytr)
    filas_c.append({"C": C, "rmse_train": rmse(m, Xtr, ytr), "rmse_test": rmse(m, Xte, yte),
                     "vectores_soporte": int(m[-1].support_.shape[0])})
tabla_c = pd.DataFrame(filas_c)
print(tabla_c.round(2).to_string(index=False))

fig, ax1 = plt.subplots(figsize=(6.3, 3.6))
ax1.plot(tabla_c["C"], tabla_c["rmse_test"], "o-", color="#065A82", label="RMSE prueba")
ax1.set_xscale("log"); ax1.set_xlabel("C"); ax1.set_ylabel("RMSE prueba", color="#065A82")
ax2 = ax1.twinx()
ax2.plot(tabla_c["C"], tabla_c["vectores_soporte"], "s--", color="#E07A1F", label="# vect. soporte")
ax2.set_ylabel("# vectores de soporte", color="#E07A1F")
ax1.set_title("Efecto de C sobre el error y el número de vectores de soporte");''',
    13: '''valores_eps = [0.1, 0.5, 1, 2, 4, 8]
filas_e = []
for eps in valores_eps:
    m = make_pipeline(
        StandardScaler(), SVR(kernel="rbf", C=50, epsilon=eps)
    ).fit(Xtr, ytr)
    filas_e.append({"epsilon": eps, "rmse_train": rmse(m, Xtr, ytr), "rmse_test": rmse(m, Xte, yte),
                     "vectores_soporte": int(m[-1].support_.shape[0])})
tabla_e = pd.DataFrame(filas_e)
print(tabla_e.round(2).to_string(index=False))''',
    16: '''modelos4 = {
    "lineal": SVR(kernel="linear", C=50, epsilon=1.0),
    "poly(3)": SVR(kernel="poly", degree=3, coef0=1, C=50, epsilon=1.0),
    "rbf": SVR(kernel="rbf", C=50, epsilon=1.0),
}
filas4 = []
for nombre, svr in modelos4.items():
    m = make_pipeline(StandardScaler(), svr).fit(Xtr, ytr)
    filas4.append({"kernel": nombre, "rmse_train": rmse(m, Xtr, ytr), "rmse_test": rmse(m, Xte, yte),
                    "vectores_soporte": int(m[-1].support_.shape[0])})
tabla4 = pd.DataFrame(filas4)
print(tabla4.round(2).to_string(index=False))

fig, ax = plt.subplots(figsize=(5.2, 3.6))
ax.bar(tabla4["kernel"], tabla4["rmse_test"], color=["#607D8B", "#1C7293", "#02C39A"])
ax.set_ylabel("RMSE de prueba"); ax.set_title("Comparación de kernels (mismo C, mismo ε)");''',
    19: '''pipe_rbf = make_pipeline(StandardScaler(), SVR(kernel="rbf"))
malla = {"svr__C": np.logspace(0, 3, 6), "svr__gamma": np.logspace(-2, 1, 6), "svr__epsilon": [0.5, 1.0, 2.0]}
bus = GridSearchCV(
    pipe_rbf, malla, cv=kf, scoring="neg_root_mean_squared_error", n_jobs=1
)
bus.fit(Xtr, ytr)
print("Mejores hiperparámetros:", bus.best_params_)
print(f"RMSE de validación = {-bus.best_score_:.2f}    RMSE de prueba = {rmse(bus, Xte, yte):.2f}")
print(f"Vectores de soporte: {bus.best_estimator_[-1].support_.shape[0]} de {len(Xtr)}")''',
    22: '''modelos6 = {
    "OLS": make_pipeline(StandardScaler(), LinearRegression()),
    "Ridge": make_pipeline(StandardScaler(), RidgeCV(alphas=np.logspace(-2, 4, 50), cv=kf)),
    "Lasso": make_pipeline(
        StandardScaler(), LassoCV(alphas=np.logspace(-3, 2, 60), cv=kf, max_iter=100000)
    ),
    "SVR lineal": make_pipeline(StandardScaler(), SVR(kernel="linear", C=50, epsilon=1.0)),
    "SVR RBF (GridSearchCV)": bus.best_estimator_,
}
filas6 = []
for nombre, m in modelos6.items():
    if nombre != "SVR RBF (GridSearchCV)":
        m.fit(Xtr, ytr)
    filas6.append({"modelo": nombre, "rmse_prueba": round(rmse(m, Xte, yte), 3)})
comparacion = pd.DataFrame(filas6).sort_values("rmse_prueba").reset_index(drop=True)
print(comparacion.to_string(index=False))

comentarios = {
    "SVR RBF (GridSearchCV)": "Captura la relación no lineal y obtiene el menor error.",
    "SVR lineal": "No representa la curva en U de la temperatura.",
    "OLS": "Sirve como referencia lineal, pero no capta la curvatura.",
    "Ridge": "Regulariza los coeficientes sin añadir relaciones no lineales.",
    "Lasso": "Selecciona variables, aunque conserva una forma lineal.",
}
entregable = comparacion.copy()
entregable["comentario"] = entregable["modelo"].map(comentarios)
entregable.to_csv("entregable-unidad-06.csv", index=False)
entregable''',
    25: '''mediana = datos[FEATS].median()
rejilla_temp = np.linspace(-5, 40, 25)
filas7 = []
for t in rejilla_temp:
    fila = mediana.copy()
    fila["temperatura_c"] = t
    xf = fila[FEATS].values.reshape(1, -1)
    filas7.append({"temperatura": t,
                    "OLS": modelos6["OLS"].predict(xf)[0],
                    "SVR_RBF": modelos6["SVR RBF (GridSearchCV)"].predict(xf)[0]})
dep = pd.DataFrame(filas7)

fig, ax = plt.subplots(figsize=(6.3, 3.8))
ax.plot(dep["temperatura"], dep["OLS"], color="#607D8B", lw=2, label="OLS")
ax.plot(dep["temperatura"], dep["SVR_RBF"], color="#02C39A", lw=2.3, label="SVR RBF (GridSearchCV)")
ax.set_xlabel("temperatura (°C), el resto de las variables fijas en su mediana")
ax.set_ylabel("consumo predicho (kWh/día)")
ax.set_title("Dependencia parcial de la temperatura")
ax.legend();''',
}


RESPUESTAS = {
    4: """**Respuesta:**

Una recta solo puede subir o bajar, mientras el consumo disminuye hasta una zona de confort y luego
vuelve a aumentar. En la gráfica, el consumo más bajo se concentra aproximadamente entre 18 °C y
24 °C.""",
    7: """**Respuesta:**

El RMSE de prueba es 11.54 kWh/día, casi igual a la desviación estándar de 11.19. Es alto para un
consumo medio de 29.23. El kernel lineal solo produce un hiperplano, por lo que no puede representar
el descenso y el aumento de la curva en U.""",
    10: """**Respuesta:**

El RBF por defecto reduce el RMSE de prueba de 11.54 a 6.50 kWh/día. El resultado confirma que la
relación necesita curvatura y no puede resumirse con una sola recta.""",
    14: """**Respuesta:**

Con `C=0.01` el modelo subajusta y el RMSE de prueba es 12.04. El error baja hasta 3.05 con `C=100`,
pero sube a 3.22 con `C=1000`. Los vectores de soporte bajan en general al aumentar `C`, aunque no de
forma estricta en esta muestra. Al ampliar `epsilon` bajan de 653 a 51 porque más observaciones quedan
dentro del tubo sin penalización.""",
    17: """**Respuesta:**

El kernel lineal obtiene el peor RMSE de prueba, 11.54, porque no sigue la curva en U. El polinomial
de grado 3 logra 2.37 y RBF 3.10. Ambos mejoran mucho al lineal, aunque el polinomial queda arriba y
usa un poco menos vectores de soporte: 478 frente a 484.""",
    20: """**Respuesta:**

La búsqueda eligió `C=1000`, `gamma=0.03981` y `epsilon=1`. El RMSE de prueba baja de 6.50 a 2.52
frente al RBF por defecto. Refinaría la rejilla alrededor de esos valores, con más puntos entre
`gamma=0.02` y `0.08`, además de valores de `C` cercanos a 1000, usando la misma validación cruzada.""",
    23: """**Respuesta:**

El orden es SVR RBF, Ridge, Lasso, OLS y SVR lineal. El SVR mejora en 8.62 kWh/día al mejor modelo
lineal, Ridge. Ridge y Lasso regularizan coeficientes, pero no crean la curvatura necesaria. Para
confiar más en la diferencia repetiría la comparación con validación cruzada anidada o con varias
particiones de prueba.""",
    26: """**Respuesta:**

OLS produce una línea y no muestra una temperatura de confort. El SVR RBF sí forma un mínimo cerca de
21 °C. Esta diferencia permite ubicar una zona razonable de operación antes de encender calefacción
o aire acondicionado, sin interpretar una tendencia lineal que no existe.""",
    27: """**Respuesta:**

Usaría SVR con kernel RBF porque puede representar relaciones curvas como la temperatura y el consumo.
Estandarizaría las variables dentro del pipeline para que ninguna escala domine las distancias.
Ajustaría `C`, `epsilon` y `gamma` juntos mediante validación cruzada.
En datos como estos esperaría un RMSE menor que el de un modelo lineal.
Reservaría el conjunto de prueba para una sola evaluación final.
También revisaría el costo de cómputo y la menor facilidad de interpretación de SVR.
Si el conjunto creciera mucho, compararía alternativas más rápidas antes de ampliar la búsqueda.""",
    30: """**Respuesta:**

Sin escalado, el RMSE de prueba aumenta de 3.10 a 9.19. `superficie_m2` domina las distancias porque
sus valores son mucho mayores que los de `aislamiento`, `fin_semana` y las demás variables.""",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--solo-respuestas", action="store_true")
    args = parser.parse_args()

    if args.solo_respuestas:
        cuaderno = nbformat.read(SALIDA, as_version=4)
        for indice, fuente in RESPUESTAS.items():
            cuaderno.cells[indice].source = fuente
        nbformat.write(cuaderno, SALIDA)
        print(SALIDA)
        return

    cuaderno = nbformat.read(ORIGEN, as_version=4)
    cuaderno.cells[0].source += "\n\n**Nombre:** Julian Emiliano Ortiz Rivero"

    for indice, fuente in CODIGO.items():
        cuaderno.cells[indice].source = fuente
    for indice, fuente in RESPUESTAS.items():
        cuaderno.cells[indice].source = fuente

    cliente = NotebookClient(
        cuaderno,
        timeout=900,
        kernel_name="python3",
        resources={"metadata": {"path": str(CARPETA)}},
    )
    cliente.execute()
    nbformat.write(cuaderno, SALIDA)
    print(SALIDA)


if __name__ == "__main__":
    main()
