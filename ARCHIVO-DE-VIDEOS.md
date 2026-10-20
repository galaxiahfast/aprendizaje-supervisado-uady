# Archivo personal de videos

Las grabaciones se conservan dentro de cada clase en `material-personal/` y los `.vtt` con el mismo
nombre base en `fuentes/`. Los MP4 y el ZIP final están excluidos de GitHub.

Al terminar el curso:

```bash
python herramientas/preparar_archivo_videos.py
```

El comando valida que cada video tenga su transcripción y genera localmente:

```text
archivo-videos/aprendizaje-supervisado-videos.zip
```

Ese ZIP es para subirlo manualmente a Drive; no debe incluirse en una entrega ni forzarse a Git.
