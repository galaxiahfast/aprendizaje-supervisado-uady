"""Crea el ZIP personal de grabaciones y transcripciones al cerrar el curso."""

from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


RAIZ = Path(__file__).resolve().parents[1]


def pares_de_clase() -> list[tuple[Path, Path, str]]:
    pares: list[tuple[Path, Path, str]] = []
    for video in sorted((RAIZ / "unidades").glob("*/clases/*/material-personal/*.mp4")):
        carpeta_clase = video.parents[1]
        vtt = carpeta_clase / "fuentes" / f"{video.stem}.vtt"
        if not vtt.exists():
            raise FileNotFoundError(f"Falta el VTT correspondiente a {video}")
        unidad = carpeta_clase.parents[1].name
        ruta_zip = f"{unidad}/{video.stem}"
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
