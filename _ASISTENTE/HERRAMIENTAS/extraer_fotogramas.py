"""Extrae fotogramas puntuales de una grabación para revisar diapositivas.

Dependencias opcionales:
    python -m pip install av pillow
"""

from __future__ import annotations

import argparse
from pathlib import Path

import av


def segundos(valor: str) -> float:
    partes = [float(parte) for parte in valor.split(":")]
    if len(partes) == 3:
        return partes[0] * 3600 + partes[1] * 60 + partes[2]
    if len(partes) == 2:
        return partes[0] * 60 + partes[1]
    return partes[0]


def nombre_tiempo(valor: float) -> str:
    total = round(valor)
    horas, resto = divmod(total, 3600)
    minutos, segundos_restantes = divmod(resto, 60)
    return f"{horas:02}-{minutos:02}-{segundos_restantes:02}.jpg"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("entrada", type=Path)
    parser.add_argument("salida", type=Path)
    parser.add_argument("marcas", nargs="+", help="Marcas SS, MM:SS o HH:MM:SS")
    args = parser.parse_args()

    args.salida.mkdir(parents=True, exist_ok=True)
    with av.open(str(args.entrada)) as contenedor:
        video = contenedor.streams.video[0]
        for marca in args.marcas:
            destino_segundos = segundos(marca)
            posicion = int(destino_segundos / float(video.time_base))
            contenedor.seek(posicion, stream=video, backward=True)
            for fotograma in contenedor.decode(video):
                if fotograma.time is None or fotograma.time + 0.05 < destino_segundos:
                    continue
                ruta = args.salida / nombre_tiempo(destino_segundos)
                fotograma.to_image().save(ruta, quality=88)
                print(ruta)
                break


if __name__ == "__main__":
    main()
