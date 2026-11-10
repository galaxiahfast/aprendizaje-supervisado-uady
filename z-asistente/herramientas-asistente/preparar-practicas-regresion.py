from pathlib import Path
import argparse
import os

from nbclient import NotebookClient
from nbformat import read, write


RAIZ = Path(__file__).resolve().parents[2]

PRACTICAS = {
    "lineal": {
        "origen": RAIZ / "z-asistente/plantillas-originales/unidad-02-clase-05-actividad-regresion-lineal-polinomial.ipynb",
        "destino": RAIZ / "tareas-practicas/practicas-clase/practica-04-regresion-lineal-polinomial/practica-04-regresion-lineal-polinomial.ipynb",
        "codigo": {
            4: {
                'limpio = ...     # ✏️ conserva solo las filas que NO son extremas: datos[~extremo]': 'limpio = datos[~extremo]',
                'Xtr, Xte, ytr, yte = ...     # ✏️ train_test_split(X, y, test_size=0.2, random_state=42)': (
                    'Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)'
                ),
            },
            6: {
                'base = ...     # ✏️ DummyRegressor(strategy="mean")': 'base = DummyRegressor(strategy="mean")',
            },
            9: {
                'simple = ...     # ✏️ LinearRegression().fit(Xtr[["MedInc"]], ytr)': (
                    'simple = LinearRegression().fit(Xtr[["MedInc"]], ytr)'
                ),
            },
            12: {
                'multiple = ...     # ✏️ LinearRegression().fit(Xtr, ytr)': 'multiple = LinearRegression().fit(Xtr, ytr)',
            },
            15: {
                'theta_ols = ...     # ✏️ np.linalg.solve(Z.T @ Z, Z.T @ yv)': (
                    'theta_ols = np.linalg.solve(Z.T @ Z, Z.T @ yv)'
                ),
            },
            17: {
                'gradiente = ...     # ✏️ (2 / len(y)) * Z.T @ residuo': (
                    'gradiente = (2 / len(y)) * Z.T @ residuo'
                ),
                'ax.set_yscale("log"); ax.set_xlabel("iteración"); ax.set_ylabel("MSE de entrenamiento (cortado en 1000)"); ax.legend(); plt.tight_layout(); plt.show()': (
                    'ax.set_yscale("log"); ax.set_xlabel("iteración"); ax.set_ylabel("MSE de entrenamiento (cortado en 1000)"); ax.legend(); plt.tight_layout(); plt.show()\n\n'
                    'theta_lento, historia_lenta = descenso_lotes(Z, yv, eta=0.01, n_iter=5000)\n'
                    'print(f"Con eta=0.01 y 5000 iteraciones: MSE = {historia_lenta[-1]:.4f}, "\n'
                    '      f"máx |theta - OLS| = {np.abs(theta_lento - theta_ols).max():.6f}")'
                ),
            },
            23: {
                'sgd_con = ...     # ✏️ make_pipeline(StandardScaler(), SGDRegressor(**config))': (
                    'sgd_con = make_pipeline(StandardScaler(), SGDRegressor(**config))'
                ),
            },
            26: {
                'modelo = ...     # ✏️ make_pipeline(StandardScaler(), PolynomialFeatures(grado, include_bias=False), LinearRegression())': (
                    'modelo = make_pipeline(StandardScaler(), PolynomialFeatures(grado, include_bias=False), LinearRegression())'
                ),
            },
            29: {
                'GRADO = ...     # ✏️ escribe el grado que elegiste (un entero entre 1 y 5)': 'GRADO = 4',
            },
            38: {
                '"Siempre el promedio": "✏️ escribe tu comentario"': (
                    '"Siempre el promedio": "Referencia mínima que no usa las variables"'
                ),
                '"Recta con MedInc": "✏️ escribe tu comentario"': (
                    '"Recta con MedInc": "Mejora la referencia usando el ingreso, pero conserva una relación lineal"'
                ),
                '"Lineal con 7 variables": "✏️ escribe tu comentario"': (
                    '"Lineal con 7 variables": "Aprovecha todas las variables con una complejidad baja"'
                ),
                'f"Polinomial grado {GRADO}": "✏️ escribe tu comentario"': (
                    'f"Polinomial grado {GRADO}": "Modelo elegido mediante validación cruzada"'
                ),
            },
            42: {
                'r_sucio = ...     # ✏️ -cross_validate(poli3, Xtr_c, ytr_c, cv=kf, scoring="neg_root_mean_squared_error")["test_score"]': (
                    'r_sucio = -cross_validate(poli3, Xtr_c, ytr_c, cv=kf, scoring="neg_root_mean_squared_error")["test_score"]'
                ),
            },
        },
        "respuestas": {
            7: (
                "**Respuesta:** El MAE de la línea base es de 90,600 USD y el RMSE es de 114,800 USD. "
                "El $R^2$ queda cerca de cero porque predecir siempre el promedio no explica la variación entre distritos. "
                "El RMSE es mayor porque eleva los errores al cuadrado, por lo que los errores grandes pesan más."
            ),
            10: (
                "**Respuesta:** La pendiente indica un aumento aproximado de 42,000 USD en el valor de la vivienda por cada unidad adicional de `MedInc`. "
                "Para `MedInc = 5`, la recta predice 253,800 USD. El RMSE de validación baja de 114,800 a 82,800 USD, una mejora de 32,000 USD. "
                "Aun así, una recta no representa la curvatura de la nube ni el tope que aparece en los valores más altos."
            ),
            13: (
                "**Respuesta:** Las tres variables con mayor peso estandarizado son `Latitude` (-0.9446), `Longitude` (-0.8569) y `MedInc` (0.7358). "
                "Al mantener las demás variables fijas, avanzar hacia latitudes mayores o longitudes menos negativas reduce la predicción en este ajuste. "
                "El coeficiente original de `Population` parece casi cero por la escala de esa variable, no porque sea irrelevante. Estandarizado vale 0.0464. "
                "`AveRooms` puede tener correlación positiva con el precio, pero coeficiente negativo al controlar las otras variables por la relación que mantiene con ellas. "
                "El RMSE baja de 0.828 a 0.668, una mejora de 0.160, equivalente a unos 16,000 USD."
            ),
            18: (
                "**Respuesta:** Con $\\eta=0.01$ el descenso es estable, aunque avanza muy lento. Con $\\eta=0.3$ converge bien y con $\\eta=0.5$ diverge. "
                "La tasa de 0.3 llega prácticamente a OLS porque la diferencia máxima entre coeficientes es de $7.6\\times10^{-5}$. "
                "Para la tasa de 0.01 probé 5,000 iteraciones. La salida de la celda muestra que ya queda muy cerca de la solución OLS."
            ),
            21: (
                "**Respuesta:** El cambio ocurre entre 0.48, que todavía converge, y 0.50, que ya diverge. Coincide con el límite teórico aproximado de 0.484. "
                "El descenso de gradiente sigue siendo útil cuando el conjunto es demasiado grande para resolver la ecuación normal de forma cómoda. "
                "También permite actualizar el modelo por lotes o en línea y sirve para problemas que no tienen una solución cerrada."
            ),
            24: (
                "**Respuesta:** Con escalado, `SGDRegressor` obtiene un RMSE de validación de 0.6686, casi igual al 0.6681 de `LinearRegression`, con coeficientes muy parecidos. "
                "Sin escalar, el RMSE se dispara a aproximadamente $1.13\\times10^{15}$. `Population` abarca cerca de 9,931 unidades, mientras `MedInc` abarca unas 14.5, así que una sola tasa de aprendizaje produce pasos desproporcionados. "
                "El escalador va dentro del pipeline para calcular sus parámetros solo con cada partición de entrenamiento y evitar que la validación filtre información al modelo."
            ),
            27: (
                "**Respuesta:** El error de entrenamiento disminuye en cada grado. El de validación baja hasta el grado 4, de 0.668 a 0.557, pero sube a 0.604 en el grado 5. "
                "El sobreajuste empieza en el grado 5 porque su error de entrenamiento mejora hasta 0.492, mientras la validación empeora y la brecha crece a 0.112. "
                "Ese grado también es el menos estable, con una desviación cercana a 0.045 entre particiones, señal de mayor varianza."
            ),
            30: (
                "**Respuesta:** Elegí el grado 4 porque reduce el RMSE de validación de 0.579 a 0.557 frente al grado 3. "
                "Pasar al grado 5 aumenta la complejidad de 329 a 791 columnas, pero empeora el RMSE a 0.604 y vuelve el resultado menos estable."
            ),
            33: (
                "**Respuesta:** Los RMSE de prueba siguen el mismo orden que los de validación. Una diferencia grande indicaría una partición de prueba poco representativa o una selección ajustada de más a la validación. "
                "El polinomio de grado 4 tiene RMSE de entrenamiento de 0.531, validación de 0.557 y prueba de 0.588. Hay una brecha moderada, pero no el deterioro claro que aparece en el grado 5. "
                "En prueba, su MAE es de 39,670 USD y su RMSE de 58,830 USD. La línea base queda en 93,170 y 117,640 USD, respectivamente."
            ),
            36: (
                "**Respuesta:** El residuo promedio es 0.018, por lo que está cerca de cero, aunque la gráfica conserva estructura en los valores altos. "
                "La banda diagonal roja corresponde a viviendas registradas en el tope del conjunto. Como el valor real quedó truncado en ese límite, el modelo no puede observar cuánto valían en realidad y tiende a subestimarlas. "
                "El RMSE baja de 0.588 a 0.545 al retirar esos distritos. Una parte importante del error está concentrada en el tope, cuyo residuo promedio es 0.700."
            ),
            37: (
                "**Respuesta:** Reportaría el MAE porque se interpreta directamente como el error típico en dólares y no queda tan dominado por unos cuantos casos extremos. "
                "Preferiría el RMSE si equivocarse mucho en una propiedad costara bastante más que acumular varios errores pequeños."
            ),
            40: (
                "**Respuesta:**\n"
                "- Recomiendo el polinomio de grado 4 después de retirar los extremos definidos en la práctica.\n"
                "- Separé la prueba antes de elegir el modelo y dejé el escalado dentro del pipeline.\n"
                "- El grado se eligió con validación cruzada, donde obtuvo un RMSE de 0.557.\n"
                "- En prueba alcanzó un MAE de 39,670 USD y un RMSE de 58,830 USD.\n"
                "- La referencia del promedio obtuvo 93,170 USD de MAE y 117,640 USD de RMSE.\n"
                "- La diferencia entre entrenamiento, validación y prueba es moderada, sin la señal clara de sobreajuste del grado 5.\n"
                "- El tope del precio sigue causando errores sistemáticos. Probaría un modelo no lineal más flexible que trate mejor ese límite."
            ),
            43: (
                "**Respuesta:** El resultado depende de si los valores extremos caen en el entrenamiento o en la validación de cada partición. "
                "Al elevar una observación extrema a potencias, su magnitud crece con rapidez. Por ejemplo, el máximo de `AveOccup` pasa de 1,243 a más de 1,922 millones al cubo. "
                "Eso vuelve inestable el ajuste polinomial y explica RMSE que van de 0.64 a 123.90 sin limpieza. Una recta no crea esos términos elevados, por lo que el mismo extremo influye mucho menos."
            ),
        },
    },
    "regularizada": {
        "origen": RAIZ / "z-asistente/plantillas-originales/unidad-02-clase-06-actividad-regresion-regularizada.ipynb",
        "destino": RAIZ / "tareas-practicas/practicas-clase/practica-05-regresion-regularizada/practica-05-regresion-regularizada.ipynb",
        "codigo": {
            4: {
                'ols = ...     # ✏️ make_pipeline(StandardScaler(), LinearRegression()).fit(Xtr, ytr)': (
                    'ols = make_pipeline(StandardScaler(), LinearRegression()).fit(Xtr, ytr)'
                ),
            },
            7: {
                'm = ...     # ✏️ make_pipeline(StandardScaler(), LinearRegression()).fit(X1, y1)': (
                    'm = make_pipeline(StandardScaler(), LinearRegression()).fit(X1, y1)'
                ),
            },
            13: {
                'm = ...     # ✏️ Ridge(alpha=a).fit(Xs, ytr)': 'm = Ridge(alpha=a).fit(Xs, ytr)',
            },
            15: {
                'm = ...     # ✏️ make_pipeline(StandardScaler(), Ridge(alpha=a))': (
                    'm = make_pipeline(StandardScaler(), Ridge(alpha=a))'
                ),
            },
            16: {
                'ridge = ...     # ✏️ make_pipeline(StandardScaler(), RidgeCV(alphas=np.logspace(-2, 4, 50), cv=kf)).fit(Xtr, ytr)': (
                    'ridge = make_pipeline(StandardScaler(), RidgeCV(alphas=np.logspace(-2, 4, 50), cv=kf)).fit(Xtr, ytr)'
                ),
            },
            19: {
                'W_ridge.append(...)     # ✏️ Ridge(alpha=1).fit(Xd, yd).coef_': (
                    'W_ridge.append(Ridge(alpha=1).fit(Xd, yd).coef_)'
                ),
            },
            22: {
                'alphas_l, coefs_l, _ = ...     # ✏️ lasso_path(Xs, ytr - ytr.mean(), alphas=np.logspace(1.2, -3, 100))': (
                    'alphas_l, coefs_l, _ = lasso_path(Xs, ytr - ytr.mean(), alphas=np.logspace(1.2, -3, 100))'
                ),
            },
            23: {
                'lasso = ...     # ✏️ make_pipeline(StandardScaler(), LassoCV(alphas=ALPHAS, cv=kf, max_iter=100000)).fit(Xtr, ytr)': (
                    'lasso = make_pipeline(StandardScaler(), LassoCV(alphas=ALPHAS, cv=kf, max_iter=100000)).fit(Xtr, ytr)'
                ),
            },
            28: {
                'bus = ...     # ✏️ GridSearchCV(pipe_en, malla, cv=kf, scoring="neg_root_mean_squared_error")': (
                    'bus = GridSearchCV(pipe_en, malla, cv=kf, scoring="neg_root_mean_squared_error", n_jobs=1)'
                ),
            },
            33: {
                '"Lasso": ...,          # ✏️ make_pipeline(StandardScaler(), LassoCV(alphas=ALPHAS, cv=kf, max_iter=100000))': (
                    '"Lasso": make_pipeline(StandardScaler(), LassoCV(alphas=ALPHAS, cv=kf, max_iter=100000)),'
                ),
                '"Elastic Net": ...,    # ✏️ make_pipeline(StandardScaler(), ElasticNetCV(l1_ratio=[.1, .3, .5, .7, .9, .95], alphas=ALPHAS, cv=kf, max_iter=100000))': (
                    '"Elastic Net": make_pipeline(StandardScaler(), ElasticNetCV(l1_ratio=[.1, .3, .5, .7, .9, .95], alphas=ALPHAS, cv=kf, max_iter=100000)),'
                ),
            },
            35: {
                '"OLS": "✏️ escribe tu comentario"': '"OLS": "Memoriza el entrenamiento y generaliza mal cuando p supera a n"',
                '"Ridge": "✏️ escribe tu comentario"': '"Ridge": "Estabiliza todos los coeficientes sin eliminar variables"',
                '"Lasso": "✏️ escribe tu comentario"': '"Lasso": "Selecciona un subconjunto corto cuando la señal es dispersa"',
                '"Elastic Net": "✏️ escribe tu comentario"': (
                    '"Elastic Net": "Combina selección y estabilidad ante variables correlacionadas"'
                ),
            },
            37: {
                'disperso = ...     # ✏️ compara(BETA)': 'disperso = compara(BETA)',
                'denso = ...        # ✏️ compara(BETA_DENSO)': 'denso = compara(BETA_DENSO)',
            },
        },
        "respuestas": {
            5: (
                "**Respuesta:** Hay 150 pesos, además del intercepto, para solo 100 observaciones de entrenamiento. "
                "El RMSE de entrenamiento es 0.00, mientras el de prueba llega a 6.01, bastante por encima del ruido de 3. "
                "El modelo está memorizando la muestra. Es un caso de sobreajuste."
            ),
            8: (
                "**Respuesta:** Mientras $n$ no supera a $p$, OLS puede llevar el error de entrenamiento a cero. El error de prueba es inestable y alcanza 44.78 justo en $n=p=150$, donde la matriz queda cerca de ser singular. "
                "Cuando hay más observaciones que variables, el RMSE de entrenamiento sube hacia el ruido y el de prueba disminuye. Con $n=900$, el RMSE de prueba es 3.32, apenas 0.32 por encima del piso de 3."
            ),
            11: (
                "**Respuesta:** La ventaja de regularizar es mayor cuando hay pocas observaciones frente al número de variables. Con $n=100$, Lasso queda más cerca del piso con RMSE 3.69, frente a 5.43 de Ridge y 6.26 de OLS. "
                "Le favorece que la verdad del ejercicio es dispersa: solo 10 de las 150 variables tienen un efecto real."
            ),
            17: (
                "**Respuesta:** Al crecer $\\alpha$, Ridge encoge los coeficientes de forma continua, aunque no los hace exactamente cero. "
                "La validación tiene forma de U, con su mínimo cerca de $\\alpha=31.6$, mientras el error de entrenamiento aumenta con la penalización. "
                "`RidgeCV` elige $\\alpha=26.8$ y baja el RMSE de prueba de 6.01 a 5.36, una mejora de 0.65. Conserva las 150 variables."
            ),
            20: (
                "**Respuesta:** En las repeticiones, OLS asigna a la primera variable un peso medio de 1.07 con desviación de 1.85. Ridge lo mantiene cerca de 0.98 con desviación de 0.07. "
                "La suma de los dos pesos es estable incluso en OLS: ronda 2 con desviación de 0.09, porque las variables contienen casi la misma información. "
                "Ridge prefiere repartir el efecto porque $1^2+1^2=2$ cuesta menos que concentrarlo como $2^2+0^2=4$."
            ),
            26: (
                "**Respuesta:** Lasso lleva varios coeficientes exactamente a cero, a diferencia del encogimiento suave de Ridge. `LassoCV` deja 29 variables activas: 9 reales y 20 de ruido. "
                "Al multiplicar $\\alpha$ por cuatro quedan 6 variables, todas reales y sin falsos positivos, pero el RMSE sube de 3.74 a 5.44 y se pierden tres variables reales adicionales. "
                "Que Lasso seleccione una variable solo indica que aporta a la predicción dentro de esta muestra. La correlación entre variables, los factores no observados o una asociación indirecta impiden interpretarla como causa."
            ),
            31: (
                "**Respuesta:** Ganó `l1_ratio = 1.0`, equivalente a Lasso. Tiene sentido porque la señal real es dispersa. "
                "Dentro de los grupos correlacionados, Lasso tiende a concentrar el peso en unas cuantas variables. Elastic Net con 0.5 lo reparte de forma más uniforme. "
                "Ese reparto deja 64 variables activas frente a 29 de Lasso y eleva el RMSE de prueba de 3.74 a 4.20."
            ),
            34: (
                "**Respuesta:** El orden por RMSE de prueba es Elastic Net (3.73), Lasso (3.74), Ridge (5.36) y OLS (6.01). OLS obtiene 0.00 en entrenamiento porque, con más variables que observaciones, puede interpolar la muestra. "
                "Lasso usa 29 variables y encuentra 9 de las 10 reales. Elastic Net usa 32 y encuentra las 10. "
                "La diferencia de 0.01 entre ambos no es suficiente para declarar un ganador con una sola muestra de 100 casos. Harían falta repeticiones o intervalos para distinguirlos."
            ),
            38: (
                "**Respuesta:** Con verdad dispersa, Lasso obtiene el menor RMSE medio, 3.67, casi empatado con Elastic Net en 3.68. Con verdad densa gana Ridge con 4.56. "
                "Lasso pierde en el caso denso porque elimina muchos efectos pequeños que, sumados, sí aportan a la predicción. "
                "Si no conociera la estructura, elegiría Elastic Net con `l1_ratio` y $\\alpha$ ajustados por validación. Puede acercarse a una solución dispersa o conservar grupos de variables cuando la señal está repartida."
            ),
            39: (
                "**Respuesta:**\n"
                "- Empezaría con Elastic Net y ajustaría $\\alpha$ junto con `l1_ratio` mediante validación cruzada.\n"
                "- Estandarizaría las variables dentro del pipeline para que la penalización sea comparable.\n"
                "- En estos datos esperaría un RMSE cercano a 3.73, frente a 6.01 de OLS.\n"
                "- El método reduce el sobreajuste y puede conservar grupos de variables correlacionadas.\n"
                "- Aun así, puede incluir falsos positivos y no garantiza identificar causas.\n"
                "- Si la verdad fuera muy dispersa, Lasso sería igual de competitivo. Si fuera densa, Ridge resultaría más conveniente.\n"
                "- Reservaría la prueba hasta el final y haría toda transformación dentro del pipeline para evitar fuga de información."
            ),
            42: (
                "**Respuesta:** Con escalado, Lasso obtiene RMSE 3.74, deja 29 variables activas y conserva 9 reales. Sin escalado, el RMSE sube a 6.94, quedan 59 activas y solo 6 de las reales. "
                "La penalización actúa sobre el tamaño numérico del coeficiente. Una variable medida en una escala grande necesita un coeficiente pequeño y recibe menos castigo, mientras otra de escala pequeña necesita un coeficiente mayor y puede desaparecer aunque sea importante."
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

    nb = read(datos["origen"], as_version=4)
    agrega_estudiante(nb)
    for indice, reemplazos in datos["codigo"].items():
        for anterior, nuevo in reemplazos.items():
            nb.cells[indice].source = nb.cells[indice].source.replace(anterior, nuevo)
    actualiza_respuestas(nb, datos["respuestas"])
    write(nb, destino)

    cliente = NotebookClient(
        nb,
        timeout=3600,
        kernel_name="python3",
        resources={"metadata": {"path": str(destino.parent)}},
    )
    cliente.execute()
    for celda in nb.cells:
        celda.metadata.pop("execution", None)
    write(nb, destino)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--practica", choices=["lineal", "regularizada", "todas"], default="todas")
    parser.add_argument("--solo-respuestas", action="store_true")
    args = parser.parse_args()
    os.environ.update(
        OPENBLAS_NUM_THREADS="1",
        OMP_NUM_THREADS="1",
        MKL_NUM_THREADS="1",
        NUMEXPR_NUM_THREADS="1",
    )
    seleccion = PRACTICAS if args.practica == "todas" else {args.practica: PRACTICAS[args.practica]}
    for practica in seleccion:
        prepara(practica, args.solo_respuestas)
