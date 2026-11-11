from pathlib import Path
import os

from nbclient import NotebookClient
from nbformat import read, write


RAIZ = Path(__file__).resolve().parents[2]
ORIGEN = (
    RAIZ
    / "z-asistente/procesamiento-temporal/curso-oficial/unidad11/actividad_redes_neuronales.ipynb"
)
DESTINO = (
    RAIZ
    / "tareas-practicas/practicas-clase/practica-14-redes-neuronales/practica-14-redes-neuronales.ipynb"
)


CODIGO = {
    2: {
        'datos = np.load("fashion_mnist_subset.npz")': (
            'datos = np.load("datos-fashion-mnist-subset.npz")'
        ),
    },
    6: {
        'X_train_s = ...     # ✏️ escalar pixeles a [0,1] (dividir entre 255.0)': (
            'X_train_s = X_train_flat / 255.0'
        ),
        'X_test_s = ...     # ✏️ igual que X_train_s, pero sobre X_test_flat': (
            'X_test_s = X_test_flat / 255.0'
        ),
    },
    9: {
        'mlp_base = ...     # ✏️ MLPClassifier(hidden_layer_sizes=(128, 64), activation="relu",\n'
        '                  #     solver="adam", max_iter=60, random_state=0).fit(X_train_s, y_train)': (
            'mlp_base = MLPClassifier(hidden_layer_sizes=(128, 64), activation="relu",\n'
            '                         solver="adam", max_iter=60, random_state=0).fit(X_train_s, y_train)'
        ),
    },
    12: {
        'modelo = ...     # ✏️ MLPClassifier(hidden_layer_sizes=(128, 64), activation="relu",\n'
        '                     #     solver=solver, max_iter=60, random_state=0).fit(X_train_s, y_train)': (
            'modelo = MLPClassifier(hidden_layer_sizes=(128, 64), activation="relu",\n'
            '                            solver=solver, max_iter=60, random_state=0).fit(X_train_s, y_train)'
        ),
    },
    15: {
        'modelo = ...     # ✏️ MLPClassifier(hidden_layer_sizes=(128, 64), activation="relu", solver="sgd",\n'
        '                     #     batch_size=cfg["batch_size"], learning_rate_init=cfg["learning_rate_init"],\n'
        '                     #     max_iter=60, random_state=0).fit(X_train_s, y_train)': (
            'modelo = MLPClassifier(hidden_layer_sizes=(128, 64), activation="relu", solver="sgd",\n'
            '                            batch_size=cfg["batch_size"], learning_rate_init=cfg["learning_rate_init"],\n'
            '                            max_iter=60, random_state=0).fit(X_train_s, y_train)'
        ),
    },
    18: {
        'mlp_final = ...     # ✏️ MLPClassifier(hidden_layer_sizes=(128, 64), activation="relu", solver="adam",\n'
        '                  #     alpha=1e-4, early_stopping=True, validation_fraction=0.15,\n'
        '                  #     n_iter_no_change=10, max_iter=200, random_state=0).fit(X_train_s, y_train)': (
            'mlp_final = MLPClassifier(hidden_layer_sizes=(128, 64), activation="relu", solver="adam",\n'
            '                          alpha=1e-4, early_stopping=True, validation_fraction=0.15,\n'
            '                          n_iter_no_change=10, max_iter=200, random_state=0).fit(X_train_s, y_train)'
        ),
    },
}


RESPUESTAS = {
    4: (
        "**Respuesta:** El conjunto está balanceado porque contiene 400 imágenes de cada clase. "
        "A simple vista, camiseta, pulóver y camisa forman el grupo más parecido por su silueta."
    ),
    7: (
        "**Respuesta:** Un árbol compara una variable con un umbral. Cambiar sus unidades también "
        "cambia el umbral, pero no el orden de los casos ni el corte. Una MLP combina todas las "
        "variables mediante sumas ponderadas y descenso de gradiente. Si unas entradas son mucho "
        "mayores que otras, producen pasos desiguales y vuelven el entrenamiento más lento o inestable."
    ),
    10: (
        "**Respuesta:** La exactitud de prueba fue 0.8170, mientras entrenamiento alcanzó 0.9683. "
        "La diferencia de 0.1513 es clara y sugiere que el modelo se ajustó demasiado a las imágenes "
        "de entrenamiento."
    ),
    13: (
        "**Respuesta:** `adam` obtuvo la mejor exactitud, 0.8170. En esta ejecución, `lbfgs` fue el "
        "más rápido con 3.9 segundos, seguido por `sgd` con 4.6. El resultado es razonable: `lbfgs` "
        "puede ser competitivo en conjuntos pequeños, mientras `adam` suele funcionar mejor como "
        "punto de partida en conjuntos medianos. El tiempo puede cambiar según el equipo."
    ),
    16: (
        "**Respuesta:** El lote de 16 con tasa 0.01 muestra más ruido que el lote de 2,000 porque "
        "estima el gradiente con menos ejemplos. La tasa 1.5 oscila y termina con exactitud 0.10, "
        "tal como se esperaba para un paso demasiado grande. El mejor punto de partida es lote 16 "
        "con tasa 0.01, que alcanzó 0.8020 y mantuvo una pérdida descendente."
    ),
    21: (
        "**Respuesta:** El entrenamiento se detuvo en la época 23, mucho antes del máximo de 200. "
        "Esto indica que la validación dejó de mejorar durante el margen configurado y la detención "
        "temprana evitó seguir ajustando. La confusión más frecuente fue pulóver clasificado como "
        "abrigo, con 22 casos. Coincide con la expectativa inicial de que camiseta, pulóver y camisa "
        "serían difíciles de separar, aunque el abrigo también resultó muy parecido."
    ),
}


def actualiza_respuestas(notebook):
    for indice, respuesta in RESPUESTAS.items():
        notebook.cells[indice].source = (
            notebook.cells[indice].source.split("**Respuesta:**")[0] + respuesta
        )


def main():
    os.environ.update(
        OPENBLAS_NUM_THREADS="1",
        OMP_NUM_THREADS="1",
        MKL_NUM_THREADS="1",
        NUMEXPR_NUM_THREADS="1",
    )
    notebook = read(ORIGEN, as_version=4)
    notebook.cells[0].source = notebook.cells[0].source.replace(
        "**Aprendizaje Supervisado · Sesión 11 · Redes neuronales para clasificación**",
        "**Aprendizaje Supervisado · Sesión 11 · Redes neuronales para clasificación**\n\n"
        "**Estudiante:** Julian Emiliano Ortiz Rivero",
    )
    for indice, reemplazos in CODIGO.items():
        for anterior, nuevo in reemplazos.items():
            notebook.cells[indice].source = notebook.cells[indice].source.replace(anterior, nuevo)
    actualiza_respuestas(notebook)
    write(notebook, DESTINO)

    cliente = NotebookClient(
        notebook,
        timeout=3600,
        kernel_name="python3",
        resources={"metadata": {"path": str(DESTINO.parent)}},
    )
    cliente.execute()
    for celda in notebook.cells:
        celda.metadata.pop("execution", None)
    write(notebook, DESTINO)


if __name__ == "__main__":
    main()
