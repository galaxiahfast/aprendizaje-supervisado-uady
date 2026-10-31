from pathlib import Path
import argparse
import json
import os

from nbclient import NotebookClient
from nbformat import read, write


RAIZ = Path(__file__).resolve().parents[2]
ORIGEN = RAIZ / "z-asistente/plantillas-originales/unidad-02-clase-08-actividad-arboles-evaluacion.ipynb"
DESTINO = RAIZ / "tareas-practicas/tareas-entregables/tarea-02-arboles-evaluacion-modelos/ortiz-julian-actividad-arboles-evaluacion.ipynb"


CODIGO = {
    4: "arbol_libre = DecisionTreeRegressor(random_state=0).fit(Xtr, ytr)",
    11: "busq_arbol = GridSearchCV(DecisionTreeRegressor(random_state=0), malla_arbol, cv=kf, scoring=SCORE, n_jobs=1).fit(Xtr, ytr)",
    14: "cvs.append(-cross_val_score(arbol_p, Xtr, ytr, cv=KFold(5, shuffle=True, random_state=s), scoring=SCORE, n_jobs=1).mean())",
    18: "skf = StratifiedKFold(5, shuffle=True, random_state=s)",
    21: "anidada = -cross_val_score(busq, Xtr, ytr, cv=externo, scoring=SCORE, n_jobs=1)",
    26: "busqueda = GridSearchCV(modelo, malla, cv=int3, scoring=SCORE, n_jobs=1)",
    29: "\"rmse_prueba\": round(rmse(g.best_estimator_, Xte, yte), 3)})",
    32: "if brecha > tol:",
    34: ("sesgo2 = np.mean((preds.mean(axis=0) - f_real) ** 2)", "varianza = np.mean(preds.var(axis=0))"),
    37: "ns, tr, va = learning_curve(est, Xtr, ytr, train_sizes=np.linspace(0.15, 1, 7), cv=kf, scoring=SCORE, n_jobs=1)",
    44: "a_con = make_pipeline(StandardScaler(), DecisionTreeRegressor(max_depth=5, min_samples_leaf=5, random_state=0)).fit(Xtr, ytr)",
}


RESPUESTAS = {
    5: "**Respuesta:** La raíz usa `superficie` con un corte de 121.4. Cada hoja predice el promedio de los precios que llegan a ella. El árbol libre tiene 400 hojas, profundidad 16 y RMSE de entrenamiento igual a 0. Su RMSE de validación es 0.492. La brecha muestra varianza alta porque memorizó el entrenamiento.",
    8: "**Respuesta:** Gana `superficie`. Reduce el MSE de 1.2650 a 0.5977, una baja de 0.6673. Coincide con el corte de `scikit-learn` en 121.37. Las variables de ruido quedan al final porque no guardan una relación estable con el precio. `superficie` y `habitaciones` tienen MSE parecidos por su correlación. Gana una sola porque CART conserva el corte con la reducción mayor.",
    12: "**Respuesta:** El menor RMSE aparece con profundidad 8 y cinco observaciones por hoja: 0.451. Al aumentar la profundidad, el error de entrenamiento sigue bajando aunque la validación ya no mejora. El resultado queda 0.201 arriba del piso de 0.25. Hay varias combinaciones entre 0.451 y 0.468, así que la zona buena es amplia y no hace falta afinar con una malla demasiado estrecha.",
    19: "**Respuesta:** Con una división el RMSE va de 0.349 a 0.581 y su desviación es 0.045. Con cinco pliegues va de 0.429 a 0.475 y la desviación baja a 0.012. Una sola partición depende demasiado de qué datos caigan en validación. Con k=2 el RMSE es 0.494 porque cada ajuste usa solo la mitad de los datos. Recomiendo k=5 por estabilidad y costo. La estratificación baja la dispersión de los promedios de 0.1102 a 0.0262. También reparte los 20 casos raros en cuatro por pliegue.",
    24: "**Respuesta:** Con 400 observaciones la CV simple da 0.460 y la anidada 0.452 ± 0.062. La diferencia es pequeña. Con 60 datos la anidada queda 0.066 arriba en promedio porque la CV simple reutiliza los resultados que sirvieron para elegir. Para reportar el error esperado usaría la validación anidada. Para escoger los hiperparámetros finales haría una búsqueda sobre todo el entrenamiento.",
    27: "**Respuesta:** El orden es Árbol, SVR, Polinomial, Elastic Net, Lasso, Lineal y Ridge. Árbol obtiene 0.446 ± 0.062. SVR obtiene 0.450 ± 0.020. La diferencia de 0.004 es menor que la dispersión, por lo que no se puede afirmar que el árbol sea superior. Lineal y Ridge quedan claramente atrás porque no alcanzan el mismo equilibrio para esta relación no lineal.",
    30: "**Respuesta:** En prueba gana Árbol con 0.429, seguido de Polinomial con 0.439. El orden cambia un poco frente a la CV anidada, donde SVR era segundo. El mejor queda 0.179 arriba del piso de 0.25. El 0.429 de prueba está cerca del 0.446 anidado, por lo que la estimación fue honesta. El 0.244 de entrenamiento del árbol es optimista y muestra la brecha de generalización.",
    35: "**Respuesta:** El diagnóstico por brecha marca varianza alta solo para Árbol. Los demás aparecen con sesgo alto. En la simulación, Lineal tiene el mayor sesgo² con 0.1784. Árbol tiene la mayor varianza con 0.0944. Coincide con los extremos esperados: la recta es rígida y el árbol cambia mucho con la muestra. Ridge, Lasso y Elastic Net reducen la variación del polinomio mediante penalizaciones, a cambio de algo de sesgo.",
    38: "**Respuesta:** En el modelo lineal las curvas quedan juntas pero en un error alto, señal de sesgo; más datos ayudarían poco. En el árbol libre aparece una brecha grande, señal de varianza; más datos sí pueden reducirla. En SVR las curvas se acercan a un error bajo, por lo que más datos podrían aportar una mejora menor y más estable.",
    42: "**Respuesta:**  \nRecomiendo el árbol con `max_depth=8` y `min_samples_leaf=5`.  \nLo evalué con validación cruzada anidada para separar el ajuste de la medición.  \nSu RMSE esperado es 0.446 ± 0.062, frente al piso de ruido de 0.25.  \nEn prueba obtuvo 0.429, equivalente a unos 42 900 pesos.  \nSu sesgo es bajo, aunque la varianza es mayor que la de SVR.  \nLa diferencia de 0.004 frente a SVR no supera la dispersión, así que ambos son defendibles.  \nLos datos son simulados. En uso real revisaría extrapolación, cambios de distribución y reentrenamiento.",
    45: "**Respuesta:** El árbol ordena los valores y decide cortes del tipo variable menor o igual que un umbral. Un escalado monótono conserva ese orden, por eso produce las mismas particiones. SVR usa distancias y productos entre observaciones. Cambiar la escala modifica esas distancias, el efecto de `gamma` y la forma de la función ajustada.",
}

OBJETIVOS = {
    4: "arbol_libre",
    11: "busq_arbol",
    14: "cvs.append",
    18: "skf",
    21: "anidada",
    26: "busqueda",
    29: '"rmse_prueba"',
    32: "if ...",
    34: ("sesgo2", "varianza"),
    37: "ns, tr, va",
    44: "a_con",
}


def reemplaza_linea(texto, inicio, nueva):
    lineas = []
    for linea in texto.splitlines():
        if linea.strip().startswith(inicio):
            sangria = linea[: len(linea) - len(linea.lstrip())]
            lineas.append(sangria + nueva)
        else:
            lineas.append(linea)
    return "\n".join(lineas)


def actualiza_respuestas(nb):
    for indice, respuesta in RESPUESTAS.items():
        nb.cells[indice].source = nb.cells[indice].source.split("**Respuesta:**")[0] + respuesta


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--solo-respuestas", action="store_true")
    args = parser.parse_args()
    if args.solo_respuestas:
        nb = read(DESTINO, as_version=4)
        actualiza_respuestas(nb)
        for celda in nb.cells:
            if celda.cell_type == "code":
                celda.source = celda.source.replace("n_jobs=-1", "n_jobs=1")
        write(nb, DESTINO)
        return
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    nb = read(ORIGEN, as_version=4)
    nb.cells[0].source += "\n\n**Estudiante:** Julian Emiliano Ortiz Rivero"
    nb.cells[7].source = nb.cells[7].source.replace(
        "return ...     # ✏️ np.mean((y - y.mean()) ** 2)",
        "return np.mean((y - y.mean()) ** 2)",
    ).replace(
        "return ...     # ✏️ (n_i * mse_nodo(y_izq) + n_d * mse_nodo(y_der)) / (n_i + n_d)",
        "return (n_i * mse_nodo(y_izq) + n_d * mse_nodo(y_der)) / (n_i + n_d)",
    )
    for celda in nb.cells:
        if celda.cell_type == "code":
            celda.source = celda.source.replace("n_jobs=-1", "n_jobs=1")
    for indice, valor in CODIGO.items():
        fuente = nb.cells[indice].source
        valores = valor if isinstance(valor, tuple) else (valor,)
        objetivos = OBJETIVOS[indice] if isinstance(OBJETIVOS[indice], tuple) else (OBJETIVOS[indice],)
        for nuevo, objetivo in zip(valores, objetivos):
            fuente = reemplaza_linea(fuente, objetivo, nuevo)
        nb.cells[indice].source = fuente
    nb.cells[40].source = '''comentarios = {
    "Lineal": "Presenta sesgo alto porque no capta la relación no lineal.",
    "Polinomial": "Capta la curvatura, aunque su flexibilidad aumenta la variación.",
    "Ridge": "Regulariza el polinomio y estabiliza sus coeficientes.",
    "Lasso": "Reduce coeficientes y conserva un ajuste compacto.",
    "Elastic Net": "Combina las dos penalizaciones y mantiene estabilidad.",
    "SVR": "Logra un ajuste no lineal estable después del escalado.",
    "Árbol": "Es interpretable, pero resulta sensible a las muestras de entrenamiento.",
}
salida = informe.reset_index()[["modelo", "hiperparametros", "rmse_cv_anidada", "rmse_cv_anidada_sd", "rmse_entrenamiento", "rmse_prueba", "diagnostico"]].copy()
salida["comentario"] = salida["modelo"].map(comentarios)
salida.to_csv("entregable_unidad7.csv", index=False, encoding="utf-8")
print(salida.to_string(index=False))'''
    actualiza_respuestas(nb)
    write(nb, DESTINO)
    os.environ.update(OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", MKL_NUM_THREADS="1")
    cliente = NotebookClient(nb, timeout=1800, kernel_name="python3", resources={"metadata": {"path": str(DESTINO.parent)}})
    cliente.execute()
    write(nb, DESTINO)


if __name__ == "__main__":
    main()
