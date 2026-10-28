"""Completa y ejecuta el examen del módulo 1."""

from __future__ import annotations

from pathlib import Path

import nbformat
from nbclient import NotebookClient


RAIZ = Path(__file__).resolve().parents[2]
PLANTILLA = (
    RAIZ
    / "z-asistente"
    / "plantillas-originales"
    / "examen-modulo-01-preparacion-datos.ipynb"
)
CARPETA = (
    RAIZ
    / "tareas-practicas"
    / "tareas-entregables"
    / "tarea-01-examen-modulo-01"
)
SALIDA = CARPETA / "ortiz_julian_examen_modulo1.ipynb"


RESPUESTAS = {
    9: """

El precio tiene asimetría positiva (3.38) y curtosis alta (22.95), así que presenta una cola
derecha marcada y varios valores extremos. La media es 5 271 y la mediana 4 504. Usaría la mediana
para representar un precio típico porque cambia menos ante las viviendas más caras.
""",
    14: """

El logaritmo reduce la asimetría de 3.38 a 0.22 y los atípicos de 57 a 14, pero no los elimina por
completo. No borraría automáticamente las viviendas más caras porque pueden ser ventas reales.
Usaría el logaritmo y revisaría esos registros para separar precios válidos de errores de captura.
""",
    17: """

Spearman vale 0.637 en ambos casos porque el logaritmo conserva el orden de los precios. Pearson
sube de 0.546 a 0.616 porque usa las distancias entre valores y el logaritmo comprime la cola
derecha. Así los precios extremos tienen menos influencia en el coeficiente.
""",
    22: """

`superficie_m2` y `recamaras` son las explicativas más relacionadas, con una correlación de 0.829.
Incluir ambas puede volver inestables sus coeficientes y dificultar su interpretación. Compararía
el desempeño al retirar una o usaría regularización.
""",
    27: """

Los faltantes de `antiguedad_anios` son compatibles con MAR: llegan a 21.6 % en Sur y 19.1 % en
Oriente, mientras las demás zonas quedan entre 0 % y 4.4 %. Los de `superficie_m2` se parecen más
a MCAR porque van de 4.0 % a 6.7 % sin un patrón claro. Borrar filas incompletas reduciría la
muestra y dejaría menos viviendas de Sur y Oriente.
""",
    30: """

Conviene estratificar porque Costa representa una parte pequeña del conjunto. Así se mantienen
proporciones similares de cada zona en entrenamiento y prueba.
""",
    32: """

La media de imputación y los parámetros del escalador se calculan con observaciones que luego
forman parte de cada bloque de validación. Esa información adelanta la distribución de los datos
que deberían permanecer sin ver y vuelve optimista la evaluación. La corrección es colocar
imputación, escalamiento y modelo dentro de un `Pipeline` evaluado completo en cada partición.
""",
    35: """

Elegí imputación por mediana porque las variables numéricas tienen asimetría y valores extremos.
Usé `RobustScaler` porque se apoya en la mediana y el IQR. El pipeline obtuvo RMSE 0.254 en
validación y 0.251 en prueba.
""",
    38: """

`StandardScaler` es más sensible: el dato de 5 000 m² comprime el IQR a 0.354. Con `RobustScaler`
el IQR se mantiene en 1, aunque el extremo alcanza 84.28. Escalar importa sobre todo en modelos
basados en distancias, gradientes o penalizaciones.
""",
    41: """

El codificador predeterminado falla porque `Costa` no apareció durante el ajuste. Con enteros se
impondría un orden y distancias inexistentes entre zonas, lo que distorsionaría un modelo lineal.
""",
    46: """

En la escala original se eliminan `lin_c` y `casi_const`. `lin_c` sí contiene señal, pero su unidad
hace que tenga poca varianza. Tras estandarizar no se elimina ninguna. El umbral depende de la
escala y no mide la relación con el objetivo.
""",
    49: """

ANOVA selecciona `ruido_08`, mientras información mutua recupera `cuad`. La variable `cuad` separa
las clases de forma no lineal y su correlación de Pearson con `y_b` es -0.024. El estadístico F no
detecta bien ese patrón, pero información mutua sí encuentra la dependencia.
""",
    52: """

El par redundante es `lin_a` con `lin_a_copia`, cuya correlación es 0.994. El filtro puntúa cada
variable por separado y puede elegir ambas aunque repitan información. Conservaría una del par o
usaría un método multivariado.
""",
    55: """

RFE conserva seis variables, pero no recupera `cuad` porque la regresión logística busca una
frontera lineal. RFECV recomienda cuatro variables. Frente a un filtro, RFE cuesta más porque
ajusta el modelo repetidas veces mientras elimina columnas.
""",
    58: """

Con `C` de 0.005, 0.01, 0.05, 0.1 y 1 se seleccionan 0, 2, 4, 4 y 23 variables. Un `C` mayor reduce
la penalización y deja más coeficientes activos. Este método considera el efecto conjunto dentro
del modelo, a diferencia de un filtro que evalúa cada variable por separado.
""",
    61: """

La selección externa usa las etiquetas de todo el conjunto antes de validar y alcanza 0.85 al
escoger asociaciones accidentales del ruido. En el pipeline, cada pliegue selecciona usando solo
su entrenamiento y la exactitud baja a 0.57, cerca del azar. La selección siempre debe repetirse
dentro de cada partición.
""",
    64: """

Agregar `cuad_2` sube la exactitud de 0.903 a 0.968, pero generar 285 columnas eleva el costo y facilita el sobreajuste.
""",
}


CODIGO = {
    1: '''import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, KFold, StratifiedKFold
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import (StandardScaler, MinMaxScaler, RobustScaler, OneHotEncoder,
                                   OrdinalEncoder, PolynomialFeatures)
from sklearn.linear_model import Ridge, LogisticRegression
from sklearn.feature_selection import (VarianceThreshold, SelectKBest, f_classif, mutual_info_classif,
                                       RFE, RFECV, SelectFromModel)
from sklearn.metrics import mean_squared_error

warnings.filterwarnings("ignore")
plt.rcParams.update({"figure.dpi": 100, "axes.grid": True, "grid.alpha": .3})

NOMBRE = "Julian Emiliano Ortiz Rivero"''',
    6: '''asim = viv[NUM].skew()
curt = viv[NUM].kurt()
mas_asimetrica = asim.idxmax()

print(pd.DataFrame({"asimetría": asim, "curtosis": curt}).round(2))
print("Más asimétrica:", mas_asimetrica)''',
    11: '''def atipicos_iqr(s, k=1.5):
    s = s.dropna()
    q1, q3 = s.quantile([0.25, 0.75])
    iqr = q3 - q1
    return (s < q1 - k * iqr) | (s > q3 + k * iqr)


n_atip = {variable: int(atipicos_iqr(viv[variable]).sum()) for variable in NUM}
print(n_atip)''',
    13: '''log_precio = np.log(viv.precio_miles)
asim_log = log_precio.skew()
n_atip_log = int(atipicos_iqr(log_precio).sum())
print(f"asimetría: {asim_log:.2f}   atípicos: {n_atip_log}")''',
    16: '''d = pd.DataFrame({"precio": viv.precio_miles, "log_precio": log_precio, "superficie": viv.superficie_m2})

r = {
    "pearson_crudo": d["precio"].corr(d["superficie"]),
    "pearson_log": d["log_precio"].corr(d["superficie"]),
    "spearman_crudo": d["precio"].corr(d["superficie"], method="spearman"),
    "spearman_log": d["log_precio"].corr(d["superficie"], method="spearman"),
}
print({k: round(v, 3) for k, v in r.items()})''',
    19: 'resp_VF = {"a": False, "b": True, "c": False, "d": True}',
    21: '''cols = ["superficie_m2", "recamaras", "antiguedad_anios", "dist_centro_km"]
datos_corr = viv[cols].copy()
datos_corr["log_precio"] = log_precio
C = datos_corr.corr()

fig, ax = plt.subplots(figsize=(5, 4))
imagen = ax.imshow(C, cmap="coolwarm", vmin=-1, vmax=1)
fig.colorbar(imagen, ax=ax)
ax.set_xticks(range(len(C.columns)), C.columns, rotation=45, ha="right")
ax.set_yticks(range(len(C.index)), C.index)
for i in range(len(C.index)):
    for j in range(len(C.columns)):
        ax.text(j, i, f"{C.iloc[i, j]:.2f}", ha="center", va="center", fontsize=8)
plt.tight_layout()

cor_exp = C.loc[cols, cols].abs()
triangulo = cor_exp.where(np.triu(np.ones(cor_exp.shape), k=1).astype(bool))
par = triangulo.stack().idxmax()
print(par)''',
    25: '''faltantes = pd.DataFrame({"n": viv.isna().sum(), "%": 100 * viv.isna().mean()})
falt_por_zona = viv.groupby("zona")[["antiguedad_anios", "superficie_m2"]].agg(lambda s: s.isna().mean())

print(faltantes[faltantes["n"] > 0])
print((100 * falt_por_zona).round(1))''',
    29: '''X = viv.drop(columns="precio_miles")
y = log_precio
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0, stratify=X["zona"]
)

prop = pd.DataFrame({
    "train": X_train["zona"].value_counts(normalize=True),
    "test": X_test["zona"].value_counts(normalize=True),
}).fillna(0)
print((100 * prop).round(1))''',
    34: '''NUM_X = ["superficie_m2", "recamaras", "antiguedad_anios", "dist_centro_km"]
NOM = ["zona"]
ORD = ["acabados"]

num_pipe = Pipeline([
    ("imputacion", SimpleImputer(strategy="median")),
    ("escalado", RobustScaler()),
])
nom_pipe = Pipeline([
    ("imputacion", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore")),
])
ord_pipe = OrdinalEncoder(
    categories=[["Básico", "Medio", "Alto", "Premium"]],
    handle_unknown="use_encoded_value",
    unknown_value=-1,
)

pre = ColumnTransformer([
    ("numericas", num_pipe, NUM_X),
    ("nominal", nom_pipe, NOM),
    ("ordinal", ord_pipe, ORD),
])
modelo = Pipeline([("preprocesamiento", pre), ("ridge", Ridge(alpha=1.0))])

cv = KFold(5, shuffle=True, random_state=0)
rmse_cv = -cross_val_score(
    modelo, X_train, y_train, cv=cv, scoring="neg_root_mean_squared_error"
).mean()
modelo.fit(X_train, y_train)
rmse_test = mean_squared_error(y_test, modelo.predict(X_test)) ** 0.5

print(f"RMSE CV = {rmse_cv:.3f}    RMSE prueba = {rmse_test:.3f}")''',
    37: '''s = X_train["superficie_m2"].fillna(X_train["superficie_m2"].median())
s = pd.concat([s, pd.Series([5000.0])], ignore_index=True).to_frame()

z_std = StandardScaler().fit_transform(s).ravel()
z_rob = RobustScaler().fit_transform(s).ravel()

def resumen(z):
    q1, q3 = np.percentile(z, [25, 75])
    return {"IQR": round(q3 - q1, 3), "|max|": round(np.abs(z).max(), 2)}

print("Standard:", resumen(z_std))
print("Robust:  ", resumen(z_rob))''',
    40: '''sin_costa = X_train.loc[X_train["zona"] != "Costa", ["zona"]]
nueva = pd.DataFrame({"zona": ["Costa"]})

msg_error = None
try:
    OneHotEncoder().fit(sin_costa).transform(nueva)
except ValueError as e:
    msg_error = str(e)[:90]

codificador = OneHotEncoder(handle_unknown="ignore")
fila_ignore = codificador.fit(sin_costa).transform(nueva).toarray()

print("Error:", msg_error)
print("Fila con ignore:", fila_ignore)''',
    45: '''selector_crudo = VarianceThreshold(threshold=0.01).fit(X_b)
quitadas_crudo = X_b.columns[~selector_crudo.get_support()].tolist()

X_b_std = StandardScaler().fit_transform(X_b)
selector_std = VarianceThreshold(threshold=0.01).fit(X_b_std)
n_quitadas_std = int((~selector_std.get_support()).sum())

print("Original:", quitadas_crudo)
print("Estandarizada:", n_quitadas_std)''',
    48: '''selector_F = SelectKBest(f_classif, k=5).fit(X_b, y_b)
sel_F = X_b.columns[selector_F.get_support()].tolist()

selector_MI = SelectKBest(
    lambda X, y: mutual_info_classif(X, y, random_state=0), k=5
).fit(X_b, y_b)
sel_MI = X_b.columns[selector_MI.get_support()].tolist()

print("F :", sel_F)
print("MI:", sel_MI)''',
    51: '''R = X_b[sel_MI].corr()
triangulo = R.abs().where(np.triu(np.ones(R.shape), k=1).astype(bool))
par_redundante = triangulo.stack().idxmax()
print(par_redundante, round(abs(R.loc[par_redundante[0], par_redundante[1]]), 3))''',
    54: '''pipe_rfe = Pipeline([
    ("escalador", StandardScaler()),
    ("rfe", RFE(LogisticRegression(max_iter=1000), n_features_to_select=6)),
])
pipe_rfe.fit(X_b, y_b)
sel_rfe = X_b.columns[pipe_rfe.named_steps["rfe"].get_support()].tolist()

pipe_cv = Pipeline([
    ("escalador", StandardScaler()),
    ("rfecv", RFECV(LogisticRegression(max_iter=1000), cv=cv_b, scoring="accuracy")),
])
pipe_cv.fit(X_b, y_b)
k_opt = int(pipe_cv.named_steps["rfecv"].n_features_)

print(sel_rfe)
print("k óptimo:", k_opt)''',
    57: '''n_sel = {}
for C in [0.005, 0.01, 0.05, 0.1, 1]:
    seleccion = SelectFromModel(
        LogisticRegression(penalty="l1", solver="liblinear", C=C, max_iter=1000)
    )
    pipe_l1 = Pipeline([("escalador", StandardScaler()), ("seleccion", seleccion)])
    pipe_l1.fit(X_b, y_b)
    n_sel[C] = int(pipe_l1.named_steps["seleccion"].get_support().sum())
print(n_sel)''',
    60: '''rng = np.random.default_rng(0)
Xn = rng.normal(size=(100, 1000))
yn = rng.integers(0, 2, 100)
cv_n = StratifiedKFold(5, shuffle=True, random_state=0)

selector_ruido = SelectKBest(f_classif, k=20).fit(Xn, yn)
Xn_elegido = selector_ruido.transform(Xn)
acc_mal = cross_val_score(
    LogisticRegression(max_iter=1000), Xn_elegido, yn, cv=cv_n, scoring="accuracy"
).mean()

pipe_ruido = make_pipeline(
    SelectKBest(f_classif, k=20), LogisticRegression(max_iter=1000)
)
acc_bien = cross_val_score(pipe_ruido, Xn, yn, cv=cv_n, scoring="accuracy").mean()
print(f"Mal: {acc_mal:.2f}    Bien: {acc_bien:.2f}")''',
    63: '''lr = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))

acc_base = cross_val_score(lr, X_b, y_b, cv=cv_b, scoring="accuracy").mean()
X_b_nueva = X_b.assign(cuad_2=X_b["cuad"] ** 2)
acc_nueva = cross_val_score(lr, X_b_nueva, y_b, cv=cv_b, scoring="accuracy").mean()
print(f"Base: {acc_base:.3f}    Con cuad_2: {acc_nueva:.3f}")

from math import comb
n_poly = comb(10 + 3, 3) - 1
n_poly_sk = PolynomialFeatures(degree=3, include_bias=False).fit(
    np.zeros((1, 10))
).n_output_features_
print(n_poly, n_poly_sk)''',
}


def agregar_respuesta(celda: nbformat.NotebookNode, respuesta: str) -> None:
    fuente = celda.source.rstrip()
    if "**Respuesta:**" not in fuente:
        raise ValueError("La celda esperada no contiene el marcador de respuesta")
    celda.source = fuente + respuesta.rstrip() + "\n"


def main() -> None:
    notebook = nbformat.read(PLANTILLA, as_version=4)

    for indice, fuente in CODIGO.items():
        notebook.cells[indice].source = fuente
    for indice, respuesta in RESPUESTAS.items():
        agregar_respuesta(notebook.cells[indice], respuesta)

    CARPETA.mkdir(parents=True, exist_ok=True)
    cliente = NotebookClient(
        notebook,
        timeout=1200,
        kernel_name="python3",
        resources={"metadata": {"path": str(CARPETA)}},
    )
    cliente.execute()
    nbformat.write(notebook, SALIDA)
    print(SALIDA)


if __name__ == "__main__":
    main()
