from pathlib import Path
import os

from nbclient import NotebookClient
from nbformat import read, write


RAIZ = Path(__file__).resolve().parents[2]
ORIGEN = (
    RAIZ
    / "z-asistente/plantillas-originales/unidad-03-clase-12-actividad-evaluacion-hiperparametros.ipynb"
)
DESTINO = (
    RAIZ
    / "tareas-practicas/practicas-clase/practica-11-evaluacion-fraude/practica-11-evaluacion-fraude.ipynb"
)

CODIGO = {
    4: {
        "mcc_base = ...          # ✏️ matthews_corrcoef(yte, pred_base)": (
            "mcc_base = matthews_corrcoef(yte, pred_base)"
        ),
        "kappa_base = ...        # ✏️ cohen_kappa_score(yte, pred_base)": (
            "kappa_base = cohen_kappa_score(yte, pred_base)"
        ),
    },
    7: {
        'proba_negativo = ...     # ✏️ modelo_negativo.predict_proba(Xte)[:, 1]': (
            'proba_negativo = modelo_negativo.predict_proba(Xte)[:, 1]'
        ),
    },
    10: {
        "mcc_ros = ...     # ✏️ mcc_cv(pipe_ros)": "mcc_ros = mcc_cv(pipe_ros)",
        "mcc_smote = ...   # ✏️ mcc_cv(pipe_smote)": "mcc_smote = mcc_cv(pipe_smote)",
    },
    13: {
        "grid = ...     # ✏️ GridSearchCV(base_estimador, malla, cv=kf, scoring=mcc_scorer, n_jobs=1).fit(Xtr, ytr)": (
            "grid = GridSearchCV(base_estimador, malla, cv=kf, scoring=mcc_scorer, n_jobs=1).fit(Xtr, ytr)"
        ),
    },
    16: {
        'cal = ...     # ✏️ CalibratedClassifierCV(FrozenEstimator(base_sin_calibrar), method="isotonic").fit(Xcal, ycal)': (
            'cal = CalibratedClassifierCV(FrozenEstimator(base_sin_calibrar), method="isotonic").fit(Xcal, ycal)'
        ),
    },
    19: {
        'tabla_final.to_csv("entregable_unidad12.csv", index=False)': (
            'tabla_final.to_csv("resultados-evaluacion-fraude.csv", index=False)'
        ),
    },
}

RESPUESTAS = {
    5: (
        "**Respuesta:** La exactitud de 0.982 parece excelente, pero el MCC de 0.459 y el kappa de "
        "0.348 muestran que el desempeño sobre la clase minoritaria es mucho más limitado. MCC y kappa "
        "quedan relativamente cerca porque ambos consideran el acuerdo más allá de los aciertos esperados "
        "por azar. Un modelo que siempre predijera no fraude tendría cerca de 97.7 % de exactitud, ya que "
        "solo 2.3 % de las transacciones de entrenamiento pertenece a la clase fraude."
    ),
    8: (
        "**Respuesta:** El modelo todo negativo conserva una exactitud alta porque acierta la clase de la "
        "mayoría. Su log-loss sube a 0.807 porque asigna probabilidad cero a los fraudes reales y recibe una "
        "penalización fuerte por estar completamente seguro de una predicción incorrecta. La exactitud solo "
        "observa la clase final, mientras que log-loss también toma en cuenta la confianza."
    ),
    11: (
        "**Respuesta:** El remuestreo debe quedar dentro del Pipeline para que se aplique únicamente a la "
        "parte de entrenamiento de cada pliegue. Si se realiza antes, una copia o un punto sintético relacionado "
        "puede aparecer en entrenamiento y validación, lo que infla el MCC. Ganó class_weight=balanced con "
        "0.470, seguido de SMOTE con 0.455 y RandomOverSampler con 0.430. Las diferencias son moderadas. El "
        "desbalance es fuerte por frecuencia, pero crear más muestras no aportó una mejora clara frente a "
        "ponderar la clase minoritaria."
    ),
    14: (
        "**Respuesta:** GridSearchCV obtuvo el mejor MCC con 0.509, frente a 0.507 de RandomizedSearchCV. "
        "La diferencia de 0.002 es mínima porque solo se ajustaron tres hiperparámetros sobre una malla pequeña "
        "de ocho combinaciones. RandomizedSearchCV tendría una ventaja más clara con muchos hiperparámetros, "
        "rangos continuos amplios o un presupuesto que no permita recorrer toda la malla."
    ),
    17: (
        "**Respuesta:** La calibración mejoró el log-loss de 0.116 a 0.107 y el Brier score de 0.019 a 0.014 "
        "cuando se comparó sobre el mismo modelo entrenado con Xtr2. El conjunto Xcal contiene cerca de 26 "
        "fraudes, por lo que la estimación isotónica puede ser inestable aunque esta vez haya mejorado. Para "
        "darle una mejor oportunidad usaría más datos de calibración, probaría el método sigmoid o emplearía "
        "calibración con validación cruzada."
    ),
    20: (
        "**Respuesta:** Recomendaría el modelo ajustado sin calibrar para la decisión final con umbral 0.5.\n\n"
        "Obtuvo MCC de 0.608 y kappa de 0.584, los mejores valores de la tabla.\n\n"
        "La versión calibrada quedó en MCC de 0.498 y kappa de 0.468 porque usó menos datos para entrenar.\n\n"
        "El modelo ajustado sí mejoró claramente al modelo base, cuyo MCC fue 0.459.\n\n"
        "Para una alerta de fraude bajaría el umbral si el costo de omitir un fraude supera al de revisar una alerta falsa.\n\n"
        "El umbral exacto lo elegiría con validación y con el costo real de cada tipo de error.\n\n"
        "El mayor impacto provino del tratamiento del desbalance junto con la búsqueda de hiperparámetros."
    ),
}


def actualiza_respuestas(nb):
    for indice, respuesta in RESPUESTAS.items():
        nb.cells[indice].source = nb.cells[indice].source.split("**Respuesta:**")[0] + respuesta


def agrega_estudiante(nb):
    nombre = "**Estudiante:** Julian Emiliano Ortiz Rivero"
    if nombre not in nb.cells[0].source:
        lineas = nb.cells[0].source.splitlines()
        lineas.insert(2, nombre)
        nb.cells[0].source = "\n".join(lineas)


def prepara(solo_respuestas):
    if solo_respuestas:
        nb = read(DESTINO, as_version=4)
        agrega_estudiante(nb)
        actualiza_respuestas(nb)
        write(nb, DESTINO)
        return

    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    nb = read(ORIGEN, as_version=4)
    agrega_estudiante(nb)
    for celda in nb.cells:
        if celda.cell_type == "code":
            celda.source = celda.source.replace("n_jobs=-1", "n_jobs=1")
    for indice, reemplazos in CODIGO.items():
        for anterior, nuevo in reemplazos.items():
            nb.cells[indice].source = nb.cells[indice].source.replace(anterior, nuevo)
    actualiza_respuestas(nb)
    write(nb, DESTINO)

    cliente = NotebookClient(
        nb,
        timeout=1800,
        kernel_name="python3",
        resources={"metadata": {"path": str(DESTINO.parent)}},
    )
    cliente.execute()
    for celda in nb.cells:
        celda.metadata.pop("execution", None)
    write(nb, DESTINO)


if __name__ == "__main__":
    os.environ.update(
        OPENBLAS_NUM_THREADS="1",
        OMP_NUM_THREADS="1",
        MKL_NUM_THREADS="1",
        NUMEXPR_NUM_THREADS="1",
    )
    prepara(solo_respuestas="--solo-respuestas" in os.sys.argv)
