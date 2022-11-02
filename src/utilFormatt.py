import re
from pathlib import Path
from PIL import Image
import os

#tranforma pasta de imagens em pdf
def transforma_pdf(nome, capitulo):
    #pasta documentos do usuario
    local = os.path.expanduser('~') + '\\Documents\\Mangas\\'
    # regex para remover caracteres invalidos
    nome = re.sub('[^A-Za-z0-9]+', '', nome)
    #pasta com arquivos em cache
    pasta_cache = Path(os.getcwd() + '\\' + 'cache')

    #cria pasta para o manga
    pasta = Path(local + nome)
    if not pasta.exists():
        pasta.mkdir()


    pasta_cache = Path(os.getcwd() + '\\' + 'cache')
    images = list(pasta_cache.glob('*.jpg'))
    # ordena as paginas
    images.sort(key=lambda x: int(x.stem))

    # cria o pdf com fundo branco

    pdf = Image.open(str(images[0].absolute())).convert('RGB')


    #adiciona capa ao pdf

    pdf.save(local + '\\' +nome + '\\' + capitulo + '.pdf', save_all=True,
             append_images=[Image.open(str(image.absolute())) for image in images[1:]], background=Image.new('RGB', pdf.size, (255, 255, 255)))





