"""Prepara y ejecuta la práctica de EDA de la Unidad 1.

La plantilla oficial se conserva sin cambios. Este script genera una copia resuelta,
la ejecuta de principio a fin y deja también el CSV solicitado por la práctica.
"""

from __future__ import annotations

from pathlib import Path

import nbformat
from nbclient import NotebookClient


RAIZ = Path(__file__).resolve().parents[2]
CLASE = (
    RAIZ
    / "unidades"
    / "unidad-01-preparacion-de-datos"
    / "clase-01-2026-10-19-introduccion-y-eda"
)
PLANTILLA = (
    RAIZ
    / "z-asistente"
    / "plantillas-originales"
    / "unidad-01-clase-01-actividad-eda-california-housing.ipynb"
)
SALIDA = CLASE / "practica-eda-california-housing-resuelta.ipynb"


RESPUESTAS = {
    5: """

Hay **20 640 filas y 9 columnas**, sin valores faltantes ni filas duplicadas. `Population` y
`HouseAge` son variables numéricas discretas aunque pandas las almacene como `float`; `Latitude`
y `Longitude` son coordenadas continuas; `MedInc`, `AveRooms`, `AveBedrms`, `AveOccup` y
`MedHouseVal` se tratan como continuas. `MedHouseVal` es la variable objetivo.

Cada registro resume un distrito. Por eso, un promedio extremo no describe una casa individual:
puede aparecer cuando el denominador (número de hogares) es muy pequeño o cuando el distrito
representa una residencia colectiva. Antes de marcarlo como error hay que revisar la fila completa.
""",
    10: """

En `MedInc`, `media - mediana` es positivo (aprox. 0.34) y la asimetría también es positiva
(1.65). Es coherente: la cola de ingresos altos desplaza la media hacia la derecha.

Las tres variables más asimétricas son `AveOccup` (97.64), `AveBedrms` (31.32) y `AveRooms`
(20.70). `AveOccup` tiene además una curtosis en exceso cercana a 10 651, señal de una cola
dominada por muy pocos valores extremos. Su máximo está a unas **119 desviaciones estándar** de
la media; este resultado también muestra que media y desviación estándar dejan de ser resúmenes
robustos en esta variable.
""",
    14: """

`MedInc` tiene cola derecha; `HouseAge` es casi uniforme y acumula observaciones en 52;
`Population` presenta una cola derecha larga; `MedHouseVal` es asimétrica a la derecha y tiene un
pico en 5.0. Las barras adicionales del extremo derecho aparecen en `HouseAge` y `MedHouseVal` y
corresponden a topes del conjunto de datos.

Al usar el cuantil 1.0 en `AveOccup`, el eje debe llegar hasta 1 243 y casi todas las observaciones
quedan comprimidas en las primeras barras. El recorte al 99.5 % solo era visual y permitía ver la
forma del grueso de los datos sin modificar la tabla.
""",
    17: """

Con la semilla indicada, la regla marca cerca de **0.72 %** en la normal y **7.82 %** en la
lognormal. En una distribución con cola larga, un porcentaje alto de puntos fuera de las cercas no
implica que todos sean errores: la propia forma de la variable puede producirlos. La regla sirve
para localizar casos que requieren revisión, no para borrarlos automáticamente.
""",
    20: """

Con $k=1.5$, `AveBedrms` tiene el porcentaje mayor (6.90 %), seguido de `Population` (5.80 %).
Sin embargo, el valor más alejado de su cerca aparece en `AveOccup`: su máximo es 1 243.33 y la
cerca superior es 4.56. No coinciden porque el porcentaje cuenta cuántos casos quedan fuera,
mientras la distancia mide qué tan extremo es un caso. Una cola moderadamente larga puede aportar
muchos atípicos sin contener un valor tan desproporcionado.

Con $k=3$, `MedInc` baja a 0.68 %, `AveRooms` a 0.87 %, `AveBedrms` a 3.51 %, `Population` a
2.04 % y `AveOccup` a 0.64 %. `HouseAge`, `Latitude`, `Longitude` y `MedHouseVal` quedan en 0 %.
Las coordenadas y la edad ocupan rangos acotados; en `MedHouseVal`, la cerca de 7.00 queda por
encima del tope publicado de 5.0. Aun con $k=3$, los máximos de `AveOccup`, `AveRooms` y
`AveBedrms` siguen siendo extremos claros.
""",
    24: """

Los máximos de `AveOccup` no parecen simples errores tipográficos: por ejemplo, 7 460 personas y
seis hogares producen 1 243 ocupantes por hogar y son compatibles con una residencia colectiva,
una cárcel o un cuartel. Son datos posibles, pero raros y fuera del significado residencial usual.
Los máximos de `AveRooms` aparecen en distritos de 11 a 48 hogares y muy poca población; pueden
corresponder a hoteles, instituciones o propiedades grandes agregadas. Los valores 5.0 de precio y
52 de edad son otro caso: son topes o censura, no errores ni observaciones libres.

Para un modelo de vivienda residencial, marcaría los distritos con menos de diez hogares y los
separaría del entrenamiento principal, conservándolos para un análisis de sensibilidad. La regla
afecta **51 de 20 640 filas (0.25 %)**. No los eliminaría sin registrar los índices y sin comparar el
desempeño con y sin ellos.
""",
    29: """

Un atípico se define por su posición respecto del resto de la distribución; un tope aparece porque
el proceso de publicación sustituye todos los valores mayores por un límite. Hay **992 distritos**
en el tope de `MedHouseVal` y **1 273** en el de `HouseAge`.

La correlación `MedInc`–`MedHouseVal` pasa de 0.688 a 0.647 al quitar el tope, pero eso no vuelve
incorrecto al cálculo original. Borrar esas filas elimina de forma selectiva zonas caras y de
ingresos altos, subrepresenta ese segmento y cambia la población estudiada. Conservaría las filas,
agregaría un indicador `precio_en_tope` y reportaría métricas separadas para casos censurados y no
censurados. Si el objetivo fuera estimar precios por encima de 5.0, buscaría una fuente sin censura.
""",
    33: r"""

En `AveOccup`, Pearson cambia de -0.024 a -0.271 con recorte a $3\,IQR$ (-0.281 con
$1.5\,IQR$), mientras Spearman permanece alrededor de -0.257. Los extremos estaban aplastando la
relación lineal. Spearman casi no cambia porque usa rangos: el recorte conserva prácticamente el
orden, aunque reduzca la magnitud de los máximos.

El logaritmo de `Population` lleva la asimetría de 4.94 a -1.04: comprimió tanto la cola derecha
que dejó una cola izquierda. No es automáticamente un problema; la transformación debe elegirse
por su utilidad para el modelo y la interpretación, no por forzar asimetría cero.

El umbral $1.5\,IQR$ es más agresivo. Por ejemplo, recorta 711 valores de `AveOccup`, 511 de
`AveRooms` y 1 196 de `Population`, frente a 132, 180 y 421 con $3\,IQR$. Aunque `clip` no elimina
filas, sí reemplaza más valores y borra diferencias en la cola; por eso usaría $3\,IQR$ y validaría
la decisión con el desempeño fuera de muestra.
""",
    39: """

La línea horizontal superior es el tope de `MedHouseVal` en 5.0: valores reales mayores quedaron
registrados con la misma cifra. El hexbin permite ver dónde se concentra la muestra cuando 20 640
puntos se enciman; el color muestra densidad y evita confundir una mancha saturada con una región
uniforme.

La mediana de `MedHouseVal` sube de **1.039** en Q1 a **1.563**, **1.933** y **2.952** en Q4; el
aumento es monótono. En el mapa, los valores altos se concentran sobre todo cerca de la costa y de
los principales centros urbanos. La ubicación puede elevar a la vez ingreso y precio, de modo que
la correlación con `MedInc` no basta para afirmar causalidad.
""",
    44: """

`MedInc` es la variable con mayor correlación con el objetivo (Pearson 0.688). Entre predictores, el
par más correlacionado es `Latitude`–`Longitude` (-0.925), coherente con la geometría de la costa;
el segundo es `AveRooms`–`AveBedrms` (0.848), pues ambas son razones calculadas con el mismo número
de hogares.

La mayor diferencia Pearson–Spearman con el objetivo aparece en `AveOccup`: -0.024 frente a
-0.257. En `AveRooms`–`AveBedrms`, Pearson baja de 0.848 a solo 0.082 al usar rangos. Unos pocos
distritos con denominadores muy pequeños inflan la relación lineal. Antes de declarar variables
redundantes, revisaría dispersión, extremos y una medida robusta; no usaría un único coeficiente.
""",
    47: """

Los VIF altos son `Latitude` (9.30), `Longitude` (8.96), `AveRooms` (8.34) y `AveBedrms` (6.99),
como sugería el heatmap de Pearson. La dependencia geográfica se mantiene también con Spearman y
es estructural; en cambio, la pareja habitaciones–dormitorios cae a 0.082 con Spearman, por lo que
gran parte de su aparente colinealidad proviene de distritos extremos.

Al quitar `AveBedrms`, el VIF de `AveRooms` baja de 8.34 a **1.26**. Conservaría `AveRooms` porque
expresa el tamaño total de la vivienda y tiene una asociación más clara con `MedHouseVal`. Aun así,
la elección final debe hacerse dentro de validación cruzada, no solo con VIF.
""",
    52: """

El hallazgo que más cambiaría el entrenamiento es la censura de `MedHouseVal`: conservaría un
indicador del tope y separaría la evaluación de la zona censurada. La decisión más discutible es
recortar `AveOccup`; pediría el número real de hogares y el tipo de establecimiento antes de fijar
la regla. Las dos trampas más claras fueron tratar topes como atípicos y aceptar correlaciones de
Pearson infladas o aplastadas por unas cuantas filas extremas.

**Reto opcional.** El IQR marca 711 casos en `AveOccup` y 681 en `MedInc`; $|z|>3$ marca solo 8 y
345, respectivamente. El puntaje z es más sensible a la contaminación porque sus propios
parámetros, media y desviación estándar, se desplazan e inflan con los extremos. Los cuartiles del
IQR son mucho más robustos.
""",
}


def agregar_respuesta(celda: nbformat.NotebookNode, respuesta: str) -> None:
    fuente = celda.source.rstrip()
    if "**Respuesta:**" not in fuente:
        raise ValueError("La celda esperada no contiene el marcador de respuesta")
    celda.source = fuente + respuesta.rstrip() + "\n"


def main() -> None:
    notebook = nbformat.read(PLANTILLA, as_version=4)
    for indice, respuesta in RESPUESTAS.items():
        agregar_respuesta(notebook.cells[indice], respuesta)

    notebook.cells[18].source = notebook.cells[18].source.replace(
        "K = 1.5                        # ✏️ cambia a 3.0 y vuelve a ejecutar esta celda y la siguiente\n"
        "tabla = tabla_atipicos(df, K)\n"
        "tabla.round(2)",
        "tabla_k15 = tabla_atipicos(df, 1.5)\n"
        "tabla_k30 = tabla_atipicos(df, 3.0)\n"
        "K = 1.5\n"
        "tabla = tabla_k15\n"
        "print('Cercas con k = 1.5')\n"
        "display(tabla_k15.round(2))\n"
        "print('Cercas con k = 3.0')\n"
        "display(tabla_k30.round(2))",
    )

    notebook.cells[31].source = '''def logaritmo(s):
    # conteos (pueden valer 0): log(1 + x); promedios estrictamente positivos: log(x)
    return np.log1p(s) if s.name == "Population" else np.log(s)

def efecto(c, k=3.0):
    x = df[c]
    lo, hi = cercas_iqr(x, k)
    variantes = {
        "original": x,
        f"clip (k={k})": x.clip(lo, hi),
        "log": logaritmo(x),
    }
    filas = []
    for nombre, v in variantes.items():
        filas.append(dict(version=nombre, asimetria=v.skew(), curtosis_exc=v.kurt(),
                          r_con_objetivo=v.corr(df["MedHouseVal"]),
                          spearman=v.corr(df["MedHouseVal"], method="spearman")))
    return pd.DataFrame(filas).set_index("version"), variantes

for k_comparacion in [3.0, 1.5]:
    print(f"===== k = {k_comparacion} =====")
    for c in ["AveOccup", "AveRooms", "Population"]:
        t, _ = efecto(c, k=k_comparacion)
        print(f"── {c}")
        print(t.round(3).to_string(), "\\n")'''

    notebook.cells[50].source = '''entrega = tabla_atipicos(df.drop(columns="MedHouseVal"), 1.5)[["pct_atipicos"]].round(1).copy()
criterios = {
    "MedInc": ("ninguno", "Cola derecha real; conservar para no comprimir la señal socioeconómica. Probar log solo dentro de validación."),
    "HouseAge": ("indicador de tope", "No tiene atípicos por IQR, pero 1 273 filas están censuradas en 52; conservar y marcar el tope."),
    "AveRooms": ("clip en 3·IQR", "Los máximos provienen de distritos con pocos hogares e inflan Pearson; el recorte conserva las filas."),
    "AveBedrms": ("clip en 3·IQR", "Comparte denominador con AveRooms y unos pocos extremos crean colinealidad aparente."),
    "Population": ("log1p", "Es un conteo positivo con cola larga; log1p reduce la escala sin perder distritos."),
    "AveOccup": ("marcar hogares < 10 y clip en 3·IQR", "Los máximos representan distritos colectivos y aplastan Pearson; separar 51 filas y limitar el resto."),
    "Latitude": ("ninguno", "Rango geográfico acotado y 0 % de atípicos; mantiene la estructura espacial."),
    "Longitude": ("ninguno", "Rango geográfico acotado y 0 % de atípicos; se conserva aunque colinee con Latitude."),
}
for variable, (decision, justificacion) in criterios.items():
    entrega.loc[variable, "decision"] = decision
    entrega.loc[variable, "justificacion"] = justificacion
pd.set_option("display.max_colwidth", 100)
entrega'''

    notebook.cells[51].source = notebook.cells[51].source.replace(
        'entregable_unidad1.csv',
        'practica-eda-decisiones.csv',
    )

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    cliente = NotebookClient(
        notebook,
        timeout=300,
        kernel_name="python3",
        resources={"metadata": {"path": str(SALIDA.parent)}},
    )
    cliente.execute()
    nbformat.write(notebook, SALIDA)
    print(SALIDA)
    print(CLASE / "practica-eda-decisiones.csv")


if __name__ == "__main__":
    main()
