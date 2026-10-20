# Aprendizaje Supervisado

Repositorio de trabajo de la asignatura **Aprendizaje Supervisado**. Aquí se concentran apuntes,
materiales de clase, actividades, entregables y una ruta corta para estudiar las grabaciones sin
tener que verlas completas.

## Lo más importante

- El curso consta de **14 sesiones de 2 horas**: 28 horas presenciales.
- El flujo completo va de los datos crudos a modelos evaluados y listos para producción.
- La calificación se divide en laboratorios (30 %), miniproyecto de regresión (35 %) y
  miniproyecto de clasificación (35 %).
- La [Actividad 1 de EDA](unidades/01-preparacion-de-datos/actividades/01-eda-california-housing/)
  ya está resuelta, ejecutada y separada de los archivos personales de la clase.
- Las fechas que no aparecen en los documentos oficiales se marcan como **no publicadas**; no se
  inventan plazos.

## Accesos rápidos

- [Entregas y estado](ENTREGAS.md)
- [Calendario temático de las 14 sesiones](CALENDARIO.md)
- [Ruta rápida de las grabaciones](RUTA-RAPIDA-CLASES.md)
- [Programa oficial](recursos/programa-oficial/planeacion-didactica.pdf)
- [Unidades](unidades/)

## Organización del curso

| Unidad | Sesiones | Contenido | Evidencia principal |
| --- | ---: | --- | --- |
| [1. Preparación de datos](unidades/01-preparacion-de-datos/) | 1-3 | EDA, preprocesamiento, ingeniería y selección de variables | Laboratorios |
| [2. Modelos de regresión](unidades/02-modelos-de-regresion/) | 4-7 | Regresión lineal, regularización, SVR y árboles | Miniproyecto de regresión |
| [3. Modelos de clasificación](unidades/03-modelos-de-clasificacion/) | 8-12 | Logística, kNN, Bayes, árboles, SVM, MLP y evaluación | Miniproyecto de clasificación |
| [4. Métodos de ensamble](unidades/04-metodos-de-ensamble/) | 13-14 | Bagging, bosques aleatorios y boosting | Laboratorios del curso |

## Estructura

```text
.
├── README.md
├── ENTREGAS.md
├── CALENDARIO.md
├── RUTA-RAPIDA-CLASES.md
├── unidades/
│   ├── 01-preparacion-de-datos/
│   │   ├── apuntes/
│   │   ├── clases/
│   │   ├── actividades/
│   │   └── materiales/
│   ├── 02-modelos-de-regresion/
│   ├── 03-modelos-de-clasificacion/
│   └── 04-metodos-de-ensamble/
├── recursos/
└── herramientas/
```

Cada clase guarda su resumen, minutos clave, `.vtt` y referencias en una carpeta propia. Los videos
se conservan localmente junto a la clase, pero `*.mp4` está bloqueado por `.gitignore` para que nunca
se suba a GitHub ni se mezcle con una entrega.

## Forma de trabajo

1. Guardar cada nueva clase dentro de su unidad y conservar el `.vtt` con fecha y número de sesión.
2. Resumir conceptos, decisiones del profesor, actividad mencionada y minutos que vale la pena ver.
3. Resolver las evidencias según el documento oficial y dejar la plantilla original separada.
4. Ejecutar todo desde cero y registrar la verificación en el README de la actividad.
5. Actualizar `ENTREGAS.md` únicamente con fechas y estados comprobados.
6. Hacer commits pequeños y subir cada bloque terminado a `main`.

## Fuente del curso

Los nombres, temas, ponderaciones y actividades se contrastan con el
[repositorio oficial del curso](https://github.com/clirlab/supervised-learning-course). El trabajo de
este repositorio usa explicaciones y decisiones propias; no modifica los materiales originales.
