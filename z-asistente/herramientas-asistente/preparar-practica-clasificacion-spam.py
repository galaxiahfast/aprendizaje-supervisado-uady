from pathlib import Path
import argparse
import os

from nbclient import NotebookClient
from nbformat import read, write


RAIZ = Path(__file__).resolve().parents[2]
ORIGEN = RAIZ / "z-asistente/plantillas-originales/unidad-03-clase-09-actividad-spam-logistica-knn.ipynb"
DESTINO = RAIZ / "tareas-practicas/practicas-clase/practica-08-clasificacion-spam-logistica-knn/practica-08-clasificacion-spam-logistica-knn.ipynb"


RESPUESTAS = {
    4: """**Respuesta:** Hay 1 911 correos no spam y 1 089 spam. El spam representa 36.3 % del total. Hay más correos legítimos, pero la diferencia no es grave porque ambas clases tienen suficientes observaciones. Un conjunto con solo 2 % de positivos sí exigiría mayor cuidado, pues la exactitud podría ocultar un mal resultado en la clase minoritaria.""",
    8: """**Respuesta:** La búsqueda eligió `C=1` y la exactitud de prueba fue 0.831. Las variables con mayor peso son `num_palabras_dinero` con signo positivo, `remitente_conocido` con signo negativo y `num_signos_exclamacion` con signo positivo. `num_adjuntos` tiene un coeficiente de -0.06, cercano a cero, lo que coincide con su poca influencia real.""",
    11: """**Respuesta:** El mejor valor fue `k=17`, con exactitud de validación de 0.780. Es menor que el 0.831 obtenido por la regresión logística en prueba. Sin escalado, `num_palabras` dominaría la distancia por manejar valores mucho mayores que `prop_mayusculas`. El resultado reflejaría las unidades de medida en lugar de la cercanía real.""",
    14: """**Respuesta:** La regresión logística produce más falsos positivos, 50 frente a 41. kNN comete más falsos negativos, 119 frente a 77. Para la clase spam, la regresión logística tiene el mejor F1, con 0.75 frente a 0.66. Detecta una proporción mayor del spam sin perder demasiado en precisión.""",
    16: """**Respuesta:**  
Recomiendo la regresión logística para el filtro de spam.  
En la clase spam alcanza precisión de 0.80 y recall de 0.72.  
kNN obtiene precisión de 0.79 y recall de 0.56.  
Un falso positivo suele ser más costoso porque puede ocultar un correo legítimo.  
kNN comete menos falsos positivos, pero deja escapar mucho más spam.  
La regresión logística ofrece un equilibrio más útil para este conjunto.""",
}


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
        write(nb, DESTINO)
        return

    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    nb = read(ORIGEN, as_version=4)
    nb.cells[6].source = nb.cells[6].source.replace(
        'busq_lr = ...     # ✏️ GridSearchCV(pipe_lr, malla_C, cv=kf, scoring="accuracy").fit(Xtr, ytr)',
        'busq_lr = GridSearchCV(pipe_lr, malla_C, cv=kf, scoring="accuracy").fit(Xtr, ytr)',
    )
    nb.cells[10].source = nb.cells[10].source.replace(
        'exact_cv.append(...     # ✏️ cross_val_score(pipe_knn, Xtr, ytr, cv=kf, scoring="accuracy").mean())',
        'exact_cv.append(cross_val_score(pipe_knn, Xtr, ytr, cv=kf, scoring="accuracy").mean())',
    )
    actualiza_respuestas(nb)
    write(nb, DESTINO)
    os.environ.update(OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", MKL_NUM_THREADS="1")
    cliente = NotebookClient(
        nb,
        timeout=1200,
        kernel_name="python3",
        resources={"metadata": {"path": str(DESTINO.parent)}},
    )
    cliente.execute()
    write(nb, DESTINO)


if __name__ == "__main__":
    main()
