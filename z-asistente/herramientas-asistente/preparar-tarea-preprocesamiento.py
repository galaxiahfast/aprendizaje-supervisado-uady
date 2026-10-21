"""Completa y ejecuta la tarea de preprocesamiento de la clase 2."""

from __future__ import annotations

from pathlib import Path

import nbformat
from nbclient import NotebookClient


RAIZ = Path(__file__).resolve().parents[2]
TAREA = (
    RAIZ
    / "tareas-practicas"
    / "tareas-entregables"
    / "tarea-01-pipeline-preprocesamiento"
)
PLANTILLA = (
    RAIZ
    / "z-asistente"
    / "plantillas-originales"
    / "unidad-01-clase-02-actividad-preprocesamiento.ipynb"
)
SALIDA = TAREA / "tarea-01-pipeline-preprocesamiento-resuelta.ipynb"


RESPUESTAS = {
    8: """

Solo `total_bedrooms` tiene valores faltantes: 207 filas, cerca del 1 % del conjunto. Las medias de
las filas con dato y sin dato son parecidas en las variables comparadas. Eso es compatible con MCAR,
pero no demuestra el mecanismo. Esta revisión no permite descartar una relación con una variable no
observada ni con el propio valor perdido. No aparecen ceros o mínimos imposibles en las columnas
numéricas, por lo que no se detectaron faltantes disfrazados con esos códigos.
""",
    12: """

Las proporciones de las cinco categorías de ingreso quedan prácticamente iguales en el conjunto
completo, entrenamiento y prueba. Se usa `median_income` porque es la variable con mayor relación con
el precio y sus grupos altos son menos frecuentes. Una división aleatoria simple puede dejar alguno
de esos grupos sobrerrepresentado o subrepresentado, lo que vuelve menos comparable la evaluación.
""",
    16: """

Media y mediana asignan un único valor a todos los casos ocultos. Sus RMSE fueron 397.445 y 407.344.
También redujeron la desviación estándar desde 412.666 hasta 371.883 y 374.154. KNN sin escalar dejó
que las variables de mayor magnitud dominaran la distancia y obtuvo un RMSE de 74.269. Al
estandarizar, las columnas participaron en una escala comparable y el RMSE bajó a 64.317. La
imputación iterativa obtuvo 67.284. KNN escalado dio el menor error de esta comparación.
""",
    17: """

El caso corresponde a MNAR porque la ausencia depende del ingreso que no se declara. KNN no corrige
por sí solo ese sesgo. Imputa a partir de quienes sí respondieron, un grupo que no representa a quienes
ocultaron el dato. Agregaría un indicador de ingreso faltante y documentaría un análisis de
sensibilidad. También revisaría el proceso de captura antes de interpretar el resultado del modelo.
""",
    22: """

El código entero impone un orden alfabético y distancias que no existen entre zonas costeras. La
regresión intenta ajustar una sola recta sobre esos códigos. One-hot asigna un coeficiente distinto a
cada categoría y representa mejor una variable nominal. Si una categoría aparece solo en prueba,
`OrdinalEncoder` usa -1 con la configuración elegida. `OneHotEncoder` produce una fila de ceros por
`handle_unknown="ignore"`. Para las tallas, la codificación automática fue L=0, M=1, S=2. Ese orden
es incorrecto. El orden explícito correcto es S=0, M=1, L=2.
""",
    26: """

Las columnas de prueba no quedan exactamente con media 0 y desviación 1 porque se transforman con la
media y la desviación aprendidas en entrenamiento. Eso evita usar información de prueba. KNN pasó de
un RMSE de 96.63 sin escalar a 62.59 con StandardScaler. MinMaxScaler obtuvo 63.44 y RobustScaler
64.02. El árbol se mantuvo cerca de 66.86 con las cuatro opciones porque compara umbrales dentro de
cada variable. `RobustScaler` resulta más apropiado cuando hay valores extremos o colas pesadas.
""",
    29: """

La selección con fuga examina todas las etiquetas antes de validar. Entre 2 000 atributos de ruido
encuentra asociaciones accidentales y después las evalúa sobre las mismas etiquetas. Así produjo una
exactitud media de 0.85. El pipeline repite la selección dentro de cada partición de entrenamiento y
la exactitud bajó a 0.52, cerca del azar. Escalar con todos los datos suele causar un sesgo menor
porque no usa directamente la etiqueta. La selección de atributos sí busca la relación con el
objetivo. En crédito habría fuga al usar días de atraso observados después del préstamo para predecir
la mora.
""",
    34: """

`prep__num__imputer__strategy` identifica el parámetro `strategy` del paso `imputer`, dentro de la
rama `num` del transformador `prep`. `GridSearchCV` recibe el pipeline completo. En cada partición
ajusta imputación, escalado y modelo solo con el bloque de entrenamiento. Si se ejecutara
`StandardScaler().fit_transform(X)` antes de dividir, la media y la desviación de validación o prueba
influirían en los datos de entrenamiento. La puntuación dejaría de representar datos realmente nuevos.
""",
    40: """

El escalado produjo el cambio principal porque KNN calcula distancias y las variables originales
tienen magnitudes muy distintas. El RMSE de validación bajó de 96.63 a 62.59. Agregar one-hot lo llevó
a 61.20. La mejor media fue 61.14 con KNNImputer. En prueba obtuvo RMSE 58.85 y R² 0.734. Borrar 207
filas o cambiar la imputación tuvo poco efecto. Sin el pipeline, imputar, escalar, codificar o
seleccionar atributos antes de cada división habría filtrado información. Elegir hiperparámetros con
la prueba también la convertiría en validación.

Mi secuencia para datos tabulares es: separar primero la prueba, revisar tipos y faltantes sobre el
entrenamiento, después encapsular las transformaciones y el modelo en un pipeline evaluado con
validación cruzada.
""",
}


def agregar_respuesta(celda: nbformat.NotebookNode, respuesta: str) -> None:
    fuente = celda.source.rstrip()
    if "**Respuesta:**" not in fuente:
        raise ValueError("La celda esperada no contiene el marcador de respuesta")
    celda.source = fuente + respuesta.rstrip() + "\n"


def reemplazar(celda: nbformat.NotebookNode, anterior: str, nuevo: str) -> None:
    if anterior not in celda.source:
        raise ValueError(f"No se encontró el fragmento esperado: {anterior}")
    celda.source = celda.source.replace(anterior, nuevo)


def main() -> None:
    notebook = nbformat.read(PLANTILLA, as_version=4)

    for indice, respuesta in RESPUESTAS.items():
        agregar_respuesta(notebook.cells[indice], respuesta)

    reemplazar(notebook.cells[5], "n_falt = ...", "n_falt = df.isna().sum()")
    reemplazar(notebook.cells[5], "pct_falt = ...", "pct_falt = 100 * df.isna().mean()")
    reemplazar(
        notebook.cells[10],
        'train_test_split(df, test_size=0.2, random_state=42)',
        'train_test_split(df, test_size=0.2, random_state=42, stratify=df["income_cat"])',
    )
    reemplazar(
        notebook.cells[14],
        'imputaciones["media"] = ...',
        'imputaciones["media"] = SimpleImputer(strategy="mean").fit_transform(X_mask)[oculto, j]',
    )
    reemplazar(
        notebook.cells[14],
        'imputaciones["mediana"] = ...',
        'imputaciones["mediana"] = SimpleImputer(strategy="median").fit_transform(X_mask)[oculto, j]',
    )
    reemplazar(
        notebook.cells[20],
        "ord_enc = ...",
        'ord_enc = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1).fit(cat_train)',
    )
    reemplazar(
        notebook.cells[20],
        "oh_enc = ...",
        'oh_enc = OneHotEncoder(handle_unknown="ignore").fit(cat_train)',
    )
    notebook.cells[21].source = notebook.cells[21].source.replace(
        "enc = OrdinalEncoder()",
        'enc = OrdinalEncoder(categories=[["S", "M", "L"]])',
    )
    reemplazar(notebook.cells[24], "sc = ...", "sc = StandardScaler().fit(Xtr)")
    reemplazar(
        notebook.cells[25],
        "pipe = ...",
        'pipe = Pipeline([("imputer", SimpleImputer(strategy="median")), '
        '("scaler", escalador), ("modelo", modelo)])',
    )
    reemplazar(
        notebook.cells[28],
        "pipe_ok = ...",
        "pipe_ok = make_pipeline(SelectKBest(f_classif, k=20), LogisticRegression(max_iter=500))",
    )
    reemplazar(
        notebook.cells[31],
        "num_pipe = ...",
        'num_pipe = Pipeline([("imputer", SimpleImputer(strategy="median")), '
        '("scaler", StandardScaler())])',
    )
    reemplazar(
        notebook.cells[31],
        "cat_pipe = ...",
        'cat_pipe = Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), '
        '("onehot", OneHotEncoder(handle_unknown="ignore"))])',
    )
    reemplazar(
        notebook.cells[31],
        "prep = ...",
        'prep = ColumnTransformer([("num", num_pipe, NUM), ("cat", cat_pipe, CAT)])',
    )
    reemplazar(
        notebook.cells[32],
        '"knn__n_neighbors": [5, 10, 20],',
        '"knn__n_neighbors": [5, 10, 20],\n'
        '    "prep__num__imputer__strategy": ["mean", "median"],',
    )
    reemplazar(
        notebook.cells[36],
        'crea_prep(SimpleImputer(strategy="median"), ...)',
        'crea_prep(SimpleImputer(strategy="median"), RobustScaler())',
    )
    reemplazar(
        notebook.cells[36],
        'crea_prep(..., StandardScaler())',
        'crea_prep(KNNImputer(n_neighbors=5), StandardScaler())',
    )
    reemplazar(
        notebook.cells[36],
        'SimpleImputer(strategy=..., add_indicator=...)',
        'SimpleImputer(strategy="median", add_indicator=True)',
    )
    notebook.cells[37].source = '''tabla_final = pd.DataFrame(resultados)
comentarios = [
    "Pierde 207 filas y conserva escalas incompatibles para KNN.",
    "Conserva las filas, pero las variables grandes dominan la distancia.",
    "El escalado produce la reducción principal del error.",
    "La categoría costera agrega una mejora pequeña y medible.",
    "Es resistente a extremos y ofrece un resultado cercano al estándar.",
    "La imputación compleja cambia poco porque solo falta cerca del 1 %.",
    "El indicador aporta poca señal cuando la ausencia parece casi aleatoria.",
]
tabla_final["comentario"] = comentarios
tabla_final'''
    notebook.cells[38].source = notebook.cells[38].source.replace(
        'entregable_unidad2.csv',
        'entregable-unidad-02.csv',
    )
    notebook.cells[39].source = notebook.cells[39].source.replace(
        'mejor = "..."',
        'mejor = tabla_final.loc[tabla_final["RMSE validación"].idxmin(), "estrategia"]',
    )

    TAREA.mkdir(parents=True, exist_ok=True)
    cliente = NotebookClient(
        notebook,
        timeout=1200,
        kernel_name="python3",
        resources={"metadata": {"path": str(TAREA)}},
    )
    cliente.execute()
    nbformat.write(notebook, SALIDA)
    print(SALIDA)
    print(TAREA / "entregable-unidad-02.csv")


if __name__ == "__main__":
    main()
