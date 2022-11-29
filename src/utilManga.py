import requests
import bs4
from AnilistPython import Anilist

#definicao de variaveis globais
url_site = "https://unionleitor.top/"


#procura o manga na pagina do site
def procura_manga(nome_manga):
    dict_manga = {}  # dicionario para armazenar os mangas encontrados
    response = requests.get(url_site + 'busca/' + nome_manga.strip() + '/1').text
    soup = bs4.BeautifulSoup(response, 'html.parser')
    containers = soup.find_all('div', attrs={'class': "col-md-3 col-xs-6 text-center bloco-manga"})
    for container in containers:
        dict_manga[container.select('a')[1].text] = container.select('a')[0].get('href')

    return dict_manga

#procura o capitulo do manga
def procura_capitulos(manga):
    dict_capitulos = {}
    response = requests.get(manga).text
    soup = bs4.BeautifulSoup(response, 'html.parser')
    containers = soup.find_all('div', attrs={'class': "row capitulos"})
    for container in containers:
        dict_capitulos[container.select('a')[0].text] = container.select('a')[0].get('href')

    #inverte o dicionario para que os capitulos fiquem em ordem decrescente
    dict_capitulos = dict(reversed(list(dict_capitulos.items())))

    return dict_capitulos

#procura as paginas do capitulo
def procura_paginas(capitulo):
    dict_paginas = {}
    response = requests.get(capitulo).text
    soup = bs4.BeautifulSoup(response, 'html.parser')
    containers = soup.find_all('img', attrs={'class': "img-manga"})
    for container in containers:
        dict_paginas[container.get('pag')] = container.get('src')

    return dict_paginas

def baixa_paginas(paginas):
    for pagina in paginas:
        response = requests.get(paginas[pagina])
        with open('cache/' + pagina + '.jpg', 'wb') as f:
            f.write(response.content)

def baixa_capa(manga_nome):
    anilist = Anilist()
    capa_link = anilist.get_manga(manga_nome)['cover_image']
    response = requests.get(capa_link)
    with open('cache/cover.jpg', 'wb') as f:
        f.write(response.content)

#obtem de uma api informações sobre o manga para criar o epub
def obtem_infos_manga(manga_nome):
    anilist = Anilist()
    infos_manga = anilist.get_manga(manga_nome)
    return infos_manga