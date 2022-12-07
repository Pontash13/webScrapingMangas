import os
import random
import string
from pathlib import Path

# Cria uma pasta temporária para cada capitulo
def cria_pasta(caminho):
    pasta = Path(caminho)
    if not pasta.exists():
        pasta.mkdir()


def exclui_pasta(caminho):
    pasta = Path(caminho)
    if pasta.exists():
        pasta.rmdir()


def limpa_pasta(caminho):
    pasta = Path(caminho)
    if pasta.exists():
        for arquivo in pasta.iterdir():
            arquivo.unlink()


def pasta_atual():
    return os.getcwd()

def pasta_documentos():
    return str(Path.home()) + '\\Documents'

def gerar_nome_aleatorio():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(25))


#tamanho do arquivo para avisar que não é possível enviar por email -- gmail só aceita até 25mb
def obtem_tamanho_arquivo(caminho):
    arquivo = Path(caminho)
    if arquivo.exists():
        return arquivo.stat().st_size
    else:
        return 0
