"""Completa y ejecuta la tarea de selección de variables de la clase 3."""

from __future__ import annotations

from pathlib import Path

import nbformat
from nbclient import NotebookClient


RAIZ = Path(__file__).resolve().parents[2]
TAREA = (
    RAIZ
    / "tareas-practicas"
    / "practicas-clase"
    / "practica-03-seleccion-de-variables"
)
PLANTILLA = (
    RAIZ
    / "z-asistente"
    / "plantillas-originales"
    / "unidad-01-clase-03-actividad-seleccion-variables.ipynb"
)
SALIDA = TAREA / "practica-03-seleccion-de-variables-resuelta.ipynb"


RESPUESTAS = {
    6: """

La regresión logística penaliza coeficientes. Estandarizar evita que la unidad de medida determine
cuánto se penaliza cada variable. El escalador va dentro del pipeline para aprender media y
desviación únicamente con cada bloque de entrenamiento. La exactitud no distingue los tipos de
error. En este diagnóstico es más grave clasificar un caso maligno como benigno porque puede retrasar
la atención. Por eso también se mide la sensibilidad a malignos y se revisa la matriz de confusión.
""",
    8: """

KNN sufrió más porque calcula distancias. Su exactitud bajó de 0.968 a 0.906 al agregar 200 columnas
de ruido. La regresión logística pasó de 0.978 a 0.934. Cada columna inútil vuelve menos claros los
vecinos reales y agrega parámetros sin señal. Seleccionar variables ayuda a quitar ruido, reducir
costo y conservar un modelo más claro.
""",
    12: """

Las cuatro variables creadas resumen forma y cambio entre mediciones medias y peores. La razón de
radio tuvo la mayor correlación con el diagnóstico, 0.644. La exactitud quedó en 0.978, igual que la
línea base, mientras la sensibilidad subió de 0.961 a 0.965. Una variable nueva puede repetir
información que ya contienen radio, perímetro o área. En ese caso el modelo gana poco aunque la
variable tenga sentido desde el dominio.
""",
    15: """

El grado 2 genera 495 columnas a partir de 30 variables, más que las 455 filas de entrenamiento. La
exactitud bajó a 0.961 con C igual a 1.0. Una regularización mayor no ayudó en este caso. Con C igual a
0.01 bajó a 0.955 y la sensibilidad quedó en 0.894. Usaría grado bajo, interacciones justificadas,
regularización y selección dentro del pipeline. El grado se elegiría con validación cruzada.
""",
    18: """

La varianza depende de las unidades. Una medida informativa expresada con números pequeños puede
quedar debajo del umbral. Al estandarizar, todas las variables tienen varianza cercana a uno y el
filtro deja de distinguirlas. Este método sirve para retirar columnas constantes o casi constantes
cuando sus escalas son comparables.
""",
    22: """

Las cinco correlaciones más altas incluyen varias mediciones del tamaño del núcleo. Radio, perímetro
y área repiten casi la misma información. Se encontraron 21 pares con correlación mayor a 0.9. La
poda dejó 21 variables y obtuvo exactitud 0.974 frente a 0.978 de la línea base. La pérdida fue de
0.004 a cambio de retirar nueve mediciones redundantes.
""",
    25: """

Los órdenes fueron muy parecidos. Su correlación de rangos fue 0.96 y coincidieron en nueve de las
diez variables principales. Esto ocurre porque las relaciones son principalmente monótonas. La
información mutua tendría ventaja en una relación en U, por ejemplo cuando el riesgo es alto tanto
para valores muy bajos como para valores muy altos. Pearson puede quedar cerca de cero porque ambos
lados se cancelan.
""",
    28: """

Los filtros igualaron o superaron la línea base cerca de k igual a 20. ANOVA F obtuvo 0.982 con 20
variables frente a 0.978 de la línea base. El número se elige con la misma validación cruzada usada
para comparar modelos. SelectKBest debe estar dentro del pipeline porque usa las etiquetas para
ordenar variables. Si se ajusta antes de validar, cada bloque de validación influye en la selección y
la estimación queda inflada.
""",
    32: """

RFE conservó mediciones de tamaño, concavidad y textura. Entre las últimas estuvieron `worst area`,
`worst concave points`, `worst radius`, `radius error` y `worst texture`. RFECV recomendó 22 variables
con exactitud 0.976. Elegiría 10 porque obtuvo 0.971 con menos de la mitad de las mediciones. RFE
reentrena en cada ronda porque al retirar una variable cambian los coeficientes de las que estaban
correlacionadas con ella.
""",
    36: """

Al disminuir C aumenta la penalización. Los coeficientes se encogen y más variables quedan en cero.
El mejor C fue 0.151 con nueve variables activas y exactitud 0.976. Con cuatro variables la exactitud
bajó a 0.938. Sin estandarizar, las unidades decidirían qué coeficientes reciben mayor castigo. Lasso
con C igual a 0.3 compartió siete variables con RFE de k igual a 10. La coincidencia muestra un núcleo
estable y las diferencias reflejan redundancia.
""",
    40: """

Con ocho variables, Lasso obtuvo exactitud 0.973 y sensibilidad 0.953. RFE quedó en 0.962 y 0.943. Los
filtros obtuvieron 0.949 y repitieron mediciones de tamaño. Cerca de 20 variables todos se acercaron a
la línea base. La sensibilidad sí cambia la elección. Lasso con diez variables mantuvo exactitud
0.973 y subió la sensibilidad a 0.959, casi igual al 0.961 de la línea base.
""",
    46: """

Elegí Lasso con diez variables porque conserva una exactitud de validación de 0.973 y sensibilidad de
0.959 con un tercio de las mediciones. En prueba igualó a la línea base con exactitud 0.982 y
sensibilidad 0.976. Ambos perdieron uno de los 42 casos malignos. Con 114 pacientes, diferencias de
uno o dos aciertos son demasiado pequeñas para declarar un ganador. Un paciente cambia la
sensibilidad cerca de 2.4 puntos porcentuales. Harían falta más casos y un intervalo de confianza
antes de afirmar una mejora clínica.
""",
    49: """

Los filtros fueron más estables. Sus cinco variables principales tuvieron frecuencias medias de 0.95
y 0.94. RFE obtuvo 0.78 con 12 variables distintas. Lasso obtuvo 0.68 con 13. Estos métodos reparten
la elección entre mediciones correlacionadas que pueden sustituirse. Para explicarlo a un médico
mostraría las variables elegidas con mayor frecuencia, sus grupos de medición y la variación entre
remuestreos. No presentaría una lista inestable como una verdad biológica.
""",
    52: """

La selección externa revisa todas las etiquetas y encuentra asociaciones accidentales entre mil
columnas de ruido. Así obtuvo una exactitud de 0.833. Con el selector dentro del pipeline bajó a 0.450,
cerca del azar. Esta última es la cifra creíble. Creación de variables basada en estadísticas, poda
por correlación, estandarización o ajuste de C tendrían el mismo problema si aprendieran de todos los
datos antes de dividir.
""",
    53: """

Propongo una regresión logística con diez variables elegidas mediante Lasso. En validación obtuvo
exactitud 0.973 y sensibilidad a malignos 0.959. Usa `mean texture`, `mean concave points`,
`radius error`, `fractal dimension error`, `worst radius`, `worst texture`, `worst area`,
`worst smoothness`, `worst concave points` y `worst symmetry`. El escalamiento y la selección
permanecen dentro del pipeline para impedir fuga. La estabilidad se revisa con remuestreos y se
comunica como frecuencia, no como certeza. Un especialista debe validar el sentido clínico de estas
mediciones. También se necesita validación externa antes de usar el modelo.
""",
}


def agregar_respuesta(celda: nbformat.NotebookNode, respuesta: str) -> None:
    fuente = celda.source.rstrip()
    if "**Respuesta:**" not in fuente:
        raise ValueError("La celda esperada no contiene el marcador de respuesta")
    if "\n---" in fuente:
        pregunta, resto = fuente.split("\n---", 1)
        celda.source = pregunta + respuesta.rstrip() + "\n\n---" + resto + "\n"
    else:
        celda.source = fuente + respuesta.rstrip() + "\n"


def reemplazar(celda: nbformat.NotebookNode, anterior: str, nuevo: str) -> None:
    if anterior not in celda.source:
        raise ValueError(f"No se encontró el fragmento esperado: {anterior}")
    celda.source = celda.source.replace(anterior, nuevo)


def main() -> None:
    notebook = nbformat.read(PLANTILLA, as_version=4)
    for indice, respuesta in RESPUESTAS.items():
        agregar_respuesta(notebook.cells[indice], respuesta)

    reemplazar(
        notebook.cells[5],
        "train_test_split(X, y, test_size=0.2, random_state=42)",
        "train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)",
    )
    reemplazar(
        notebook.cells[5],
        "base = ...",
        "base = make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000))",
    )
    reemplazar(notebook.cells[5], "cv=cv, n_jobs=-1,", "cv=cv, n_jobs=1,")
    reemplazar(
        notebook.cells[10],
        'd["razon radio peor/medio"] = ...',
        'd["razon radio peor/medio"] = d["worst radius"] / d["mean radius"]',
    )
    reemplazar(
        notebook.cells[10],
        'd["razon textura peor/medio"] = ...',
        'd["razon textura peor/medio"] = d["worst texture"] / d["mean texture"]',
    )
    reemplazar(
        notebook.cells[14],
        "poly = ...",
        "poly = PolynomialFeatures(degree=2, include_bias=False).fit(X_train)",
    )
    reemplazar(
        notebook.cells[17],
        "vt = ...",
        "vt = VarianceThreshold(threshold=0.01).fit(X_train)",
    )
    reemplazar(
        notebook.cells[21],
        "if ...:",
        "if not elegidas or (Xd[elegidas].corrwith(Xd[c]).abs() <= umbral).all():",
    )
    reemplazar(
        notebook.cells[27],
        "pipe = ...",
        "pipe = make_pipeline(StandardScaler(), SelectKBest(score, k=k), LogisticRegression(max_iter=3000))",
    )
    reemplazar(
        notebook.cells[30],
        "rfe = ...",
        "rfe = RFE(LogisticRegression(max_iter=3000), n_features_to_select=10, step=1).fit(Xs_train, y_train)",
    )
    reemplazar(
        notebook.cells[31],
        "rfecv = ...",
        'rfecv = RFECV(LogisticRegression(max_iter=3000), step=1, cv=StratifiedKFold(5, shuffle=True, random_state=0), scoring="accuracy").fit(Xs_train, y_train)',
    )
    reemplazar(
        notebook.cells[34],
        "m = ...",
        'm = LogisticRegression(penalty="l1", solver="liblinear", random_state=0, C=C_, max_iter=5000).fit(Xs_train, y_train)',
    )
    reemplazar(
        notebook.cells[35],
        "sfm = ...",
        'sfm = SelectFromModel(LogisticRegression(penalty="l1", solver="liblinear", random_state=0, C=0.3, max_iter=5000)).fit(Xs_train, y_train)',
    )
    reemplazar(
        notebook.cells[38],
        "return ...     # ✏️ RFE(lr(), n_features_to_select=k, step=1)",
        "return RFE(lr(), n_features_to_select=k, step=1)",
    )
    reemplazar(
        notebook.cells[38],
        'return ...     # ✏️ SelectFromModel(LogisticRegression(penalty="l1", solver="liblinear", random_state=0, C=0.3, max_iter=5000), max_features=k, threshold=-np.inf)',
        'return SelectFromModel(LogisticRegression(penalty="l1", solver="liblinear", random_state=0, C=0.3, max_iter=5000), max_features=k, threshold=-np.inf)',
    )
    notebook.cells[42].source = notebook.cells[42].source.replace(
        '"Línea base (30 variables)": "✏️ escribe tu comentario",',
        '"Línea base (30 variables)": "Referencia con toda la información y mayor costo de medición.",',
    ).replace(
        '"Filtro: información mutua": "✏️ escribe tu comentario",',
        '"Filtro: información mutua": "Filtro rápido que capta relaciones no lineales, pero revisa cada variable sola.",',
    ).replace(
        '"Filtro: ANOVA F": "✏️ escribe tu comentario",',
        '"Filtro: ANOVA F": "Filtro rápido para relaciones lineales, sensible a información redundante.",',
    ).replace(
        '"Envoltura: RFE": "✏️ escribe tu comentario",',
        '"Envoltura: RFE": "Busca un subconjunto complementario mediante reentrenamientos sucesivos.",',
    ).replace(
        '"Integrado: Lasso": "✏️ escribe tu comentario",',
        '"Integrado: Lasso": "Selecciona durante el ajuste y puede alternar entre variables correlacionadas.",',
    )
    notebook.cells[43].source = notebook.cells[43].source.replace(
        "entregable_unidad3.csv", "resultados-seleccion-variables.csv"
    )
    reemplazar(
        notebook.cells[45],
        "metodo_elegido, k_elegido = ..., ...",
        'metodo_elegido, k_elegido = "Integrado: Lasso", 10',
    )
    reemplazar(
        notebook.cells[51],
        "pipe_bien = ...",
        'pipe_bien = make_pipeline(SelectKBest(f_classif, k=10), LogisticRegression())',
    )

    TAREA.mkdir(parents=True, exist_ok=True)
    cliente = NotebookClient(
        notebook,
        timeout=1800,
        kernel_name="python3",
        resources={"metadata": {"path": str(TAREA)}},
    )
    cliente.execute()
    nbformat.write(notebook, SALIDA)
    print(SALIDA)
    print(TAREA / "resultados-seleccion-variables.csv")


if __name__ == "__main__":
    main()
