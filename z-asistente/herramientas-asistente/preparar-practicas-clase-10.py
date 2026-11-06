from pathlib import Path
import argparse
import os

from nbclient import NotebookClient
from nbformat import read, write


RAIZ = Path(__file__).resolve().parents[2]

PRACTICAS = {
    "texto": {
        "origen": RAIZ / "z-asistente/plantillas-originales/unidad-03-clase-10-actividad-naive-bayes-texto.ipynb",
        "destino": RAIZ / "tareas-practicas/practicas-clase/practica-09-naive-bayes-texto/practica-09-naive-bayes-texto.ipynb",
        "codigo": {
            6: (
                'mnb = ...     # ✏️ MultinomialNB().fit(Xtr, ytr)',
                'mnb = MultinomialNB().fit(Xtr, ytr)',
            ),
            9: (
                'bnb = ...     # ✏️ BernoulliNB().fit(Xtr_bin, ytr)',
                'bnb = BernoulliNB().fit(Xtr_bin, ytr)',
            ),
            15: (
                '    ...     # ✏️ "la pelicula de cocina mostraba un director preparando una receta en camara",     # tu tercer documento, mezclando vocabulario de ambos temas',
                '    "el director preparo una receta en la cocina durante una escena de la pelicula",',
            ),
        },
        "respuestas": {
            4: (
                "**Respuesta:** Hay 300 documentos de cocina y 300 de cine. El vocabulario tiene 36 palabras distintas. "
                "Las dos clases comparten 12 palabras generales, mientras que el resto del vocabulario se relaciona con cada tema."
            ),
            7: (
                "**Respuesta:** La exactitud fue de 1.00. El resultado es razonable porque las palabras propias de cocina y cine "
                "separan claramente las clases, aunque existan algunas palabras comunes."
            ),
            10: (
                "**Respuesta:** Bernoulli también obtuvo una exactitud de 1.00. En estos documentos cortos hay pocas repeticiones, "
                "por lo que contar las palabras o registrar solamente su presencia produce casi la misma información."
            ),
            13: (
                "**Respuesta:** En cine destacan escena, efectos, camara, personaje y director. En cocina aparecen cocina, sazon, "
                "especia, plato y fuego. Las palabras comunes tienen un peso parecido en ambas clases, por eso ayudan poco a distinguirlas."
            ),
            16: (
                "**Respuesta:** Los dos modelos clasificaron correctamente el texto de cine y el de cocina. El documento mezclado quedó "
                "como cine porque contiene director, escena y pelicula, frente a receta y cocina."
            ),
            19: (
                "**Respuesta:** La diferencia aparece cuando una palabra se repite. Multinomial considera la frecuencia, así que la "
                "probabilidad de cine pasó de 0.9898 a 1.0000 al repetir director. Bernoulli solo registra si la palabra está presente "
                "y mantuvo una probabilidad cercana a 0.9897."
            ),
        },
    },
    "diabetes": {
        "origen": RAIZ / "z-asistente/plantillas-originales/unidad-03-clase-10-actividad-arboles-diabetes.ipynb",
        "destino": RAIZ / "tareas-practicas/practicas-clase/practica-10-arboles-diabetes/practica-10-arboles-diabetes.ipynb",
        "codigo": {
            6: (
                'arbol_gini = ...     # ✏️ GridSearchCV(DecisionTreeClassifier(criterion="gini", random_state=0), malla_prof, cv=kf, scoring="accuracy").fit(Xtr, ytr)',
                'arbol_gini = GridSearchCV(DecisionTreeClassifier(criterion="gini", random_state=0), malla_prof, cv=kf, scoring="accuracy").fit(Xtr, ytr)',
            ),
            9: (
                'arbol_entropia = ...     # ✏️ GridSearchCV(DecisionTreeClassifier(criterion="entropy", random_state=0), malla_prof, cv=kf, scoring="accuracy").fit(Xtr, ytr)',
                'arbol_entropia = GridSearchCV(DecisionTreeClassifier(criterion="entropy", random_state=0), malla_prof, cv=kf, scoring="accuracy").fit(Xtr, ytr)',
            ),
            13: (
                'fpr, tpr, umbrales = ...     # ✏️ roc_curve(yte, proba_arbol)',
                'fpr, tpr, umbrales = roc_curve(yte, proba_arbol)',
            ),
            16: (
                'gnb = ...     # ✏️ GaussianNB().fit(Xtr, ytr)',
                'gnb = GaussianNB().fit(Xtr, ytr)',
            ),
        },
        "respuestas": {
            4: (
                "**Respuesta:** El 31.0 % de las personas tiene diabetes y el 69.0 % no la tiene. Existe un desbalance moderado, "
                "pero ambas clases conservan suficientes observaciones. La mayor diferencia entre promedios está en la glucosa, "
                "con 138.2 mg/dL en personas con diabetes frente a 108.8 mg/dL en personas sin diabetes."
            ),
            7: (
                "**Respuesta:** La mejor profundidad fue 4. La primera división usa glucosa_mgdl con un umbral de 127.5. "
                "Esto coincide con la exploración anterior, donde la glucosa mostró la mayor diferencia entre las dos clases."
            ),
            10: (
                "**Respuesta:** Ambos criterios eligieron profundidad 4 y obtuvieron 0.767 de exactitud en prueba. Entropía alcanzó "
                "0.782 en validación cruzada, frente a 0.778 de Gini. La diferencia es pequeña porque ambos criterios buscan divisiones "
                "que separen grupos con clases más puras."
            ),
            14: (
                "**Respuesta:** El árbol produjo 87 falsos negativos. Su AUC fue 0.798, un resultado claramente mejor que el azar, "
                "aunque todavía existe margen para separar mejor a las personas con diabetes."
            ),
            17: (
                "**Respuesta:** GaussianNB obtuvo un AUC de 0.834 y una exactitud de 0.778. El árbol logró 0.798 y 0.767, "
                "respectivamente. En este conjunto las variables continuas se ajustan razonablemente al modelo gaussiano, mientras "
                "que el árbol de profundidad limitada crea cortes más rígidos. Recomendaría GaussianNB porque logró el mejor AUC "
                "y la mayor exactitud, teniendo presente que supone independencia entre las variables."
            ),
        },
    },
}


def actualiza_respuestas(nb, respuestas):
    for indice, respuesta in respuestas.items():
        nb.cells[indice].source = nb.cells[indice].source.split("**Respuesta:**")[0] + respuesta


def agrega_estudiante(nb):
    nombre = "**Estudiante:** Julian Emiliano Ortiz Rivero"
    if nombre not in nb.cells[0].source:
        lineas = nb.cells[0].source.splitlines()
        lineas.insert(2, nombre)
        nb.cells[0].source = "\n".join(lineas)


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
    for indice, (anterior, nuevo) in datos["codigo"].items():
        nb.cells[indice].source = nb.cells[indice].source.replace(anterior, nuevo)
    actualiza_respuestas(nb, datos["respuestas"])
    write(nb, destino)
    cliente = NotebookClient(
        nb,
        timeout=1200,
        kernel_name="python3",
        resources={"metadata": {"path": str(destino.parent)}},
    )
    cliente.execute()
    for celda in nb.cells:
        celda.metadata.pop("execution", None)
    write(nb, destino)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--solo-respuestas", action="store_true")
    args = parser.parse_args()
    os.environ.update(OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", MKL_NUM_THREADS="1")
    for nombre in PRACTICAS:
        prepara(nombre, args.solo_respuestas)


if __name__ == "__main__":
    main()
