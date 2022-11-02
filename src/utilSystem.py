import os
from pathlib import Path


def limpa_pasta(caminho):
    pasta = Path(caminho)
    if pasta.exists():
        for arquivo in pasta.iterdir():
            arquivo.unlink()

