"""Genera una transcripción local en español a partir de una grabación.

Dependencia opcional:
    python -m pip install faster-whisper
"""

from __future__ import annotations

import argparse
import html
from pathlib import Path

from faster_whisper import WhisperModel


def marca_tiempo(segundos: float) -> str:
    milisegundos = round(segundos * 1000)
    horas, resto = divmod(milisegundos, 3_600_000)
    minutos, resto = divmod(resto, 60_000)
    segundos_enteros, milisegundos = divmod(resto, 1000)
    return f"{horas:02}:{minutos:02}:{segundos_enteros:02}.{milisegundos:03}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("entrada", type=Path)
    parser.add_argument("salida", type=Path, help="Ruta base, sin extensión")
    parser.add_argument("--modelo", default="small")
    parser.add_argument("--beam-size", type=int, default=5)
    parser.add_argument("--cpu-threads", type=int, default=0)
    parser.add_argument("--sin-contexto", action="store_true")
    args = parser.parse_args()

    opciones_modelo = {"device": "cpu", "compute_type": "int8"}
    if args.cpu_threads:
        opciones_modelo["cpu_threads"] = args.cpu_threads
    modelo = WhisperModel(args.modelo, **opciones_modelo)
    segmentos, informacion = modelo.transcribe(
        str(args.entrada),
        language="es",
        beam_size=args.beam_size,
        best_of=1,
        vad_filter=True,
        condition_on_previous_text=not args.sin_contexto,
    )

    args.salida.parent.mkdir(parents=True, exist_ok=True)
    ruta_vtt = args.salida.with_suffix(".vtt")
    ruta_txt = args.salida.with_suffix(".txt")

    with ruta_vtt.open("w", encoding="utf-8", newline="\n") as vtt, ruta_txt.open(
        "w", encoding="utf-8", newline="\n"
    ) as texto:
        vtt.write("WEBVTT\n\n")
        for indice, segmento in enumerate(segmentos, start=1):
            contenido = segmento.text.strip()
            if not contenido:
                continue
            inicio = marca_tiempo(segmento.start)
            fin = marca_tiempo(segmento.end)
            vtt.write(f"{indice}\n{inicio} --> {fin}\n{html.escape(contenido)}\n\n")
            texto.write(f"[{inicio}] {contenido}\n")
            if indice % 100 == 0:
                vtt.flush()
                texto.flush()
                print(f"Progreso: {inicio}", flush=True)

    print(
        f"Idioma: {informacion.language} "
        f"(probabilidad {informacion.language_probability:.3f})"
    )
    print(ruta_vtt)
    print(ruta_txt)


if __name__ == "__main__":
    main()
