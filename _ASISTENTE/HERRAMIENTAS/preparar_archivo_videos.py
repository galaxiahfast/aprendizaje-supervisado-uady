"""Crea el ZIP personal de grabaciones y transcripciones al cerrar el curso."""

from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


RAIZ = Path(__file__).resolve().parents[2]


def pares_de_clase() -> list[tuple[Path, Path, str]]:
    pares: list[tuple[Path, Path, str]] = []
    patron = "U*/_FUENTES_CLASE/_VIDEO_LOCAL/*.mp4"
    for video in sorted((RAIZ / "01_CLASES_APRENDIZAJE_SUPERVISADO").glob(patron)):
        carpeta_clase = video.parents[2]
        fuentes = carpeta_clase / "_FUENTES_CLASE"
        vtt_es = fuentes / f"{video.stem}_RETRANSCRIPCION_ES.vtt"
        vtt_original = fuentes / f"{video.stem}_ORIGINAL.vtt"
        vtt = vtt_es if vtt_es.exists() else vtt_original
        if not vtt.exists():
            raise FileNotFoundError(f"Falta el VTT correspondiente a {video}")
        ruta_zip = f"{carpeta_clase.name}/{video.stem}"
        pares.append((video, vtt, ruta_zip))
    return pares


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--salida",
        type=Path,
        default=RAIZ / "archivo-videos" / "aprendizaje-supervisado-videos.zip",
    )
    args = parser.parse_args()

    pares = pares_de_clase()
    if not pares:
        raise SystemExit("No se encontraron grabaciones organizadas.")

    args.salida.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(args.salida, "w", compression=ZIP_DEFLATED, compresslevel=1) as archivo:
        for video, vtt, base in pares:
            archivo.write(video, f"{base}.mp4")
            archivo.write(vtt, f"{base}.vtt")
            print(f"Incluidos: {base}.mp4 y {base}.vtt")
    print(args.salida)


if __name__ == "__main__":
    main()
