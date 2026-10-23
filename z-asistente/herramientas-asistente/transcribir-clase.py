"""Genera una transcripción local en español a partir de una grabación.

Dependencia opcional:
    python -m pip install faster-whisper
"""

from __future__ import annotations

import argparse
import html
from pathlib import Path
import subprocess
import tempfile

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
    parser.add_argument(
        "--duracion-tramo-minutos",
        type=int,
        default=0,
        help="Divide grabaciones largas en tramos para reducir el uso de memoria",
    )
    args = parser.parse_args()

    opciones_modelo = {"device": "cpu", "compute_type": "int8"}
    if args.cpu_threads:
        opciones_modelo["cpu_threads"] = args.cpu_threads
    modelo = WhisperModel(args.modelo, **opciones_modelo)
    args.salida.parent.mkdir(parents=True, exist_ok=True)
    ruta_vtt = args.salida.with_suffix(".vtt")
    ruta_txt = args.salida.with_suffix(".txt")

    def transcribir(entrada: Path):
        return modelo.transcribe(
            str(entrada),
            language="es",
            beam_size=args.beam_size,
            best_of=1,
            vad_filter=True,
            condition_on_previous_text=not args.sin_contexto,
        )

    temporales = None
    entradas = [args.entrada]
    duracion_tramo = 0
    if args.duracion_tramo_minutos:
        import imageio_ffmpeg

        duracion_tramo = args.duracion_tramo_minutos * 60
        temporales = tempfile.TemporaryDirectory(prefix="transcripcion-clase-")
        patron = Path(temporales.name) / "tramo-%03d.mp3"
        subprocess.run(
            [
                imageio_ffmpeg.get_ffmpeg_exe(),
                "-hide_banner",
                "-loglevel",
                "error",
                "-i",
                str(args.entrada),
                "-vn",
                "-ac",
                "1",
                "-ar",
                "16000",
                "-f",
                "segment",
                "-segment_time",
                str(duracion_tramo),
                "-reset_timestamps",
                "1",
                str(patron),
            ],
            check=True,
        )
        entradas = sorted(Path(temporales.name).glob("tramo-*.mp3"))

    with ruta_vtt.open("w", encoding="utf-8", newline="\n") as vtt, ruta_txt.open(
        "w", encoding="utf-8", newline="\n"
    ) as texto:
        vtt.write("WEBVTT\n\n")
        indice = 0
        idiomas = []
        for numero_tramo, entrada in enumerate(entradas):
            segmentos, informacion = transcribir(entrada)
            idiomas.append((informacion.language, informacion.language_probability))
            desplazamiento = numero_tramo * duracion_tramo
            for segmento in segmentos:
                contenido = segmento.text.strip()
                if not contenido:
                    continue
                indice += 1
                inicio = marca_tiempo(segmento.start + desplazamiento)
                fin = marca_tiempo(segmento.end + desplazamiento)
                vtt.write(f"{indice}\n{inicio} --> {fin}\n{html.escape(contenido)}\n\n")
                texto.write(f"[{inicio}] {contenido}\n")
                if indice % 100 == 0:
                    vtt.flush()
                    texto.flush()
                    print(f"Progreso: {inicio}", flush=True)

    if temporales is not None:
        temporales.cleanup()
    idioma, probabilidad = max(idiomas, key=lambda dato: dato[1])
    print(f"Idioma: {idioma} (probabilidad {probabilidad:.3f})")
    print(ruta_vtt)
    print(ruta_txt)


if __name__ == "__main__":
    main()
