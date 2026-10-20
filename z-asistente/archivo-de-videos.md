# Archivo personal de videos

Cada grabación se conserva en la misma carpeta que su clase con el prefijo `z-video-`. Su
transcripción lleva el prefijo `z-transcripcion-`. Los MP4 y el ZIP final están excluidos de GitHub.

Al terminar el curso se ejecutará:

```bash
python z-asistente/herramientas/preparar-archivo-videos.py
```

El comando validará cada pareja y generará localmente
`archivo-videos/aprendizaje-supervisado-videos.zip`. Ese ZIP será para Drive, no para una entrega ni
para GitHub.
