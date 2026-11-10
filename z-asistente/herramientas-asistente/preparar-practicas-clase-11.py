from pathlib import Path
import os

from nbclient import NotebookClient
from nbformat import read, write


RAIZ = Path(__file__).resolve().parents[2]

PRACTICAS = {
    "bagging": {
        "origen": RAIZ / "z-asistente/plantillas-originales/unidad-04-clase-11-actividad-bagging-random-forest.ipynb",
        "destino": RAIZ / "tareas-practicas/practicas-clase/practica-12-bagging-random-forest/practica-12-bagging-random-forest.ipynb",
        "codigo": {
            4: {
                "bagging = ...     # ✏️ BaggingClassifier(estimator=DecisionTreeClassifier(), n_estimators=200, n_jobs=1, random_state=0).fit(Xtr, ytr)": (
                    "bagging = BaggingClassifier(estimator=DecisionTreeClassifier(), n_estimators=200, n_jobs=1, random_state=0).fit(Xtr, ytr)"
                ),
            },
            7: {
                'conteo_rf = ...     # ✏️ raices(lambda s: DecisionTreeClassifier(max_depth=1, max_features="sqrt", random_state=s))': (
                    'conteo_rf = raices(lambda s: DecisionTreeClassifier(max_depth=1, max_features="sqrt", random_state=s))'
                ),
            },
            10: {
                'bosque_final = ...     # ✏️ RandomForestClassifier(n_estimators=300, max_features="sqrt", oob_score=True, random_state=0, n_jobs=1).fit(Xtr, ytr)': (
                    'bosque_final = RandomForestClassifier(n_estimators=300, max_features="sqrt", oob_score=True, random_state=0, n_jobs=1).fit(Xtr, ytr)'
                ),
                "print(imp)": (
                    'print(imp)\nerror_oob_final = 1 - bosque_final.oob_score_\n'
                    'error_prueba_final = 1 - bosque_final.score(Xte, yte)\n'
                    'print(f"Error OOB final: {error_oob_final:.3f}")\n'
                    'print(f"Error de prueba final: {error_prueba_final:.3f}")'
                ),
                'plt.grid(alpha=0.3); plt.show()': (
                    'plt.grid(alpha=0.3); plt.show()\n'
                    'print(pd.DataFrame({"n_estimators": n_list, "error_oob": np.round(oob_err, 3)}))'
                ),
            },
            13: {
                'tabla_final.to_csv("entregable_unidad13.csv", index=False)': (
                    'tabla_final.to_csv("resultados-bagging-random-forest.csv", index=False)'
                ),
            },
        },
        "respuestas": {
            5: (
                "**Respuesta:** Bagging obtuvo 0.882 de exactitud media en validación cruzada, frente a 0.880 "
                "del árbol solo. La mejora es pequeña, pero el ensamble resulta más estable. Un árbol sin podar "
                "tiene varianza alta porque un cambio pequeño en los datos puede modificar sus primeros cortes y "
                "la estructura completa. Con solo cinco árboles el promedio sería menos estable y la exactitud "
                "podría variar más entre particiones."
            ),
            8: (
                "**Respuesta:** La variable dominante siguió siendo x9. Sin restricción apareció en las 30 raíces, "
                "mientras que con max_features='sqrt' apareció en 9 de 30. La selección aleatoria no eliminó su "
                "importancia, pero permitió que otras variables iniciaran más árboles. Esto reduce la correlación "
                "entre los árboles y aumenta la diversidad del bosque."
            ),
            11: (
                "**Respuesta:** El error OOB baja con rapidez hasta 40 árboles, donde llega a 0.098. Después se "
                "mantiene cerca de 0.10 y termina en 0.090 con 300 árboles. Las variables con menor importancia son "
                "x7, x5 y x0, por lo que parecen aportar principalmente ruido. El error de prueba final también fue "
                "0.090, igual al error OOB del bosque de 300 árboles."
            ),
            14: (
                "**Respuesta:** Elegiría Random Forest porque obtuvo la mayor exactitud de prueba, con 0.910.\n\n"
                "Bagging quedó muy cerca con 0.905, pero su ventaja de tiempo fue pequeña en este conjunto.\n\n"
                "El árbol solo fue mucho más rápido, aunque su exactitud bajó a 0.845.\n\n"
                "Random Forest ofrece el mejor balance entre exactitud y estabilidad para este problema.\n\n"
                "A cambio se pierde la interpretación directa de las reglas que sí permite un solo árbol."
            ),
        },
    },
    "boosting": {
        "origen": RAIZ / "z-asistente/plantillas-originales/unidad-04-clase-11-actividad-boosting.ipynb",
        "destino": RAIZ / "tareas-practicas/practicas-clase/practica-13-boosting-clasificacion/practica-13-boosting-clasificacion.ipynb",
        "codigo": {
            4: {
                "ada = ...     # ✏️ AdaBoostClassifier(estimator=DecisionTreeClassifier(max_depth=1), n_estimators=ne, random_state=0).fit(Xtr, ytr)": (
                    "ada = AdaBoostClassifier(estimator=DecisionTreeClassifier(max_depth=1), n_estimators=ne, random_state=0).fit(Xtr, ytr)"
                ),
                'print(f"Error de prueba con 1 aprendiz: {ada_te[0]:.3f}  |  con 250: {ada_te[-1]:.3f}")': (
                    'print(f"Error de prueba con 1 aprendiz: {ada_te[0]:.3f}  |  con 250: {ada_te[-1]:.3f}")\n'
                    'print(f"Menor error de entrenamiento: {min(ada_tr):.3f}")\n'
                    'mejor_indice = int(np.argmin(ada_te))\n'
                    'print(f"Mejor error de prueba: {ada_te[mejor_indice]:.3f} con {n_est_list[mejor_indice]} aprendices")'
                ),
            },
            7: {
                "busqueda = ...     # ✏️ GridSearchCV(GradientBoostingClassifier(max_depth=3, random_state=0), malla, cv=kf, n_jobs=1).fit(Xtr, ytr)": (
                    "busqueda = GridSearchCV(GradientBoostingClassifier(max_depth=3, random_state=0), malla, cv=kf, n_jobs=1).fit(Xtr, ytr)"
                ),
            },
            10: {
                'tabla_final.to_csv("entregable_unidad14.csv", index=False)': (
                    'tabla_final.to_csv("resultados-boosting-clasificacion.csv", index=False)'
                ),
            },
        },
        "respuestas": {
            5: (
                "**Respuesta:** El error de entrenamiento no llegó a cero. Su menor valor fue 0.040, por lo que "
                "AdaBoost todavía dejó algunos casos sin ajustar aun con muchas rondas. El mejor error de prueba "
                "fue 0.120 con 250 aprendices. Random Forest obtuvo un error menor de 0.090. Aunque en esta corrida "
                "no apareció sobreajuste marcado, aumentar rondas puede concentrar el modelo en observaciones "
                "difíciles o ruidosas."
            ),
            8: (
                "**Respuesta:** La combinación ganadora fue learning_rate=0.1 con 200 árboles y alcanzó 0.903 de "
                "exactitud media en validación cruzada. El resultado tiene sentido porque una tasa de aprendizaje "
                "moderada necesita varios árboles para corregir el error de forma gradual. Una tasa mayor suele "
                "requerir menos árboles, pero puede producir pasos demasiado agresivos."
            ),
            11: (
                "**Respuesta:** Elegiría Random Forest porque logró la mayor exactitud de prueba, con 0.910.\n\n"
                "Gradient Boosting quedó cerca con 0.900, mientras que AdaBoost obtuvo 0.870.\n\n"
                "Con etiquetas ruidosas evitaría AdaBoost porque aumenta el peso de los casos que sigue clasificando mal.\n\n"
                "Ese comportamiento puede hacer que dedique demasiadas rondas a valores atípicos o etiquetas incorrectas.\n\n"
                "Si solo importara la exactitud, probaría XGBoost con validación cruzada y ajuste de regularización.\n\n"
                "Random Forest es el más fácil de paralelizar porque sus árboles se entrenan de forma independiente.\n\n"
                "Esa independencia reduce el tiempo cuando se dispone de varios núcleos."
            ),
        },
    },
}


def agrega_estudiante(nb):
    nombre = "**Estudiante:** Julian Emiliano Ortiz Rivero"
    if nombre not in nb.cells[0].source:
        lineas = nb.cells[0].source.splitlines()
        lineas.insert(2, nombre)
        nb.cells[0].source = "\n".join(lineas)


def actualiza_respuestas(nb, respuestas):
    for indice, respuesta in respuestas.items():
        nb.cells[indice].source = nb.cells[indice].source.split("**Respuesta:**")[0] + respuesta


def prepara(nombre, solo_respuestas):
    datos = PRACTICAS[nombre]
    destino = datos["destino"]
    if solo_respuestas:
        nb = read(destino, as_version=4)
        agrega_estudiante(nb)
        actualiza_respuestas(nb, datos["respuestas"])
        write(nb, destino)
        return

    destino.parent.mkdir(parents=True, exist_ok=True)
    nb = read(datos["origen"], as_version=4)
    agrega_estudiante(nb)
    for celda in nb.cells:
        if celda.cell_type == "code":
            celda.source = celda.source.replace("n_jobs=-1", "n_jobs=1")
    for indice, reemplazos in datos["codigo"].items():
        for anterior, nuevo in reemplazos.items():
            nb.cells[indice].source = nb.cells[indice].source.replace(anterior, nuevo)
    actualiza_respuestas(nb, datos["respuestas"])
    write(nb, destino)

    cliente = NotebookClient(
        nb,
        timeout=1800,
        kernel_name="python3",
        resources={"metadata": {"path": str(destino.parent)}},
    )
    cliente.execute()
    for celda in nb.cells:
        celda.metadata.pop("execution", None)
    write(nb, destino)


if __name__ == "__main__":
    os.environ.update(
        OPENBLAS_NUM_THREADS="1",
        OMP_NUM_THREADS="1",
        MKL_NUM_THREADS="1",
        NUMEXPR_NUM_THREADS="1",
    )
    solo_respuestas = "--solo-respuestas" in os.sys.argv
    for practica in PRACTICAS:
        prepara(practica, solo_respuestas)
