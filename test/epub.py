import random
import urllib

import requests
from AnilistPython import Anilist
from pathlib import Path
from ebooklib import epub


#todo corrigir esse caminho chumbado
pasta_cache = 'C:\\Users\\alyss\\PycharmProjects\\pythonProject\\cache'

def ler_arquivos_pasta_temp(pasta):
    pasta_cache = Path(pasta)
    images = list(pasta_cache.glob('*.jpg'))
    images.remove(pasta_cache / 'cover.jpg')

    # ordena as paginas
    images.sort(key=lambda x: int(x.stem))

    return images


def cria_epub(manga_infos, cap):
    list_capitulos = []
    imagens = ler_arquivos_pasta_temp(pasta_cache)


    book = epub.EpubBook()
    book.set_identifier('id' + str(random.randint(0, 1000000)))
    book.set_title(manga_infos['name_english'])
    book.set_language('jp')

    book.add_author('Gera_epub_python')

    # add cover image
    book.set_cover("cover.jpg", open(pasta_cache + '\\cover.jpg', 'rb').read())
    book.set_direction('rtl')


    for imagem in imagens:
        count = imagens.index(imagem) + 1
        file_name = 'image' + str(count) + '.jpg'

        c = epub.EpubHtml(title='Page %s' % count, file_name='page_%s.xhtml' % count, lang='pt')
        i = epub.EpubItem(uid='image%s' % count, file_name=file_name, media_type='image/jpeg', content= open(imagem, 'rb').read())
        c.content = u'<html><body><img src="%s" /></body></html>' % file_name

        book.add_item(i)
        book.add_item(c)
        list_capitulos.append(c)

    # add default NCX and Nav file (required)
    book.toc = tuple(list_capitulos)

    #page progression direction
    book.spine = ['nav'] + list_capitulos
    print(book.spine)


    epub.write_epub(manga_infos['name_english'] + '_cap' + cap + '.epub', book, {})




def obtem_infos_manga(manga_nome):
    anilist = Anilist()
    infos_manga = anilist.get_manga(manga_nome)
    return infos_manga


cria_epub(obtem_infos_manga('One Piece'), 'teste')