import random
import re
from pathlib import Path
from ebooklib import epub

#todo corrigir esse caminho chumbado
pasta_cache = 'C:\\Users\\alyss\\PycharmProjects\\pythonProject\\cache'


#Le os arquivos da pasta temporaria e devolve uma lista
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
    book.set_identifier('id' + str(random.randint(0, 1000)))
    book.set_title(manga_infos['name_english'])
    book.set_language('en')

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

    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # define CSS style
    style = 'BODY {color: white;}'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

    # add CSS file
    book.add_item(nav_css)

    # basic spine
    book.spine = ['nav'] + list_capitulos



    epub.write_epub(manga_infos['name_english'] + '_' + cap + '.epub', book, {})


