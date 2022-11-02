from src import utilFormatt, utilManga
import os


def main():

    print(os.system('cls'))
    nome = input("Digite o nome do manga: ").lower().strip()
    if (nome == ''):
        print(os.system('cls'))
        input('Nome inválido... Tente novamente')
        main()

    print(os.system('cls'))
    print("Procurando mangas...")
    mangas_encontrados = utilManga.procura_manga(nome)


    #verifica se o manga não foi encontrado
    if len(mangas_encontrados) == 0:
        print(os.system('cls'))
        input('Nenhum manga encontrado.. tente novamente')
        main()

    print(os.system('cls'))
    print("Mangas encontrados: ")
    for manga in mangas_encontrados:
        index = list(mangas_encontrados).index(manga)
        print(index + 1, manga)

    manga_escolhido = int(input("\nDigite o número do manga que deseja baixar: ")) - 1 # -1 para ajustar o index

    print(os.system('cls'))
    print("Listando capitulos...")
    capitulos_encontrados = utilManga.procura_capitulos(mangas_encontrados[list(mangas_encontrados)[manga_escolhido]])

    print(os.system('cls'))
    print("Capitulos encontrados: ")
    for capitulo in capitulos_encontrados:
        index = list(capitulos_encontrados).index(capitulo)
        print('(',index + 1 ,')', "----", capitulo)


    capitulo_escolhido = int(input("Digite o número do capitulo que deseja baixar: ")) - 1 # -1 para ajustar o index



    print(os.system('cls'))
    print("Listando paginas...")
    paginas_encontradas = utilManga.procura_paginas(capitulos_encontrados[list(capitulos_encontrados)[capitulo_escolhido]])


    print(os.system('cls'))
    print("Baixando imagens...")
    utilManga.baixa_paginas(paginas_encontradas)

    print(os.system('cls'))
    print("Imagens baixadas com sucesso!")

    #nome do manga
    utilFormatt.transforma_pdf(list(mangas_encontrados)[manga_escolhido], str(capitulo_escolhido + 1))




if __name__ == '__main__':
    main()
    input('Pressione qualquer tecla para sair...')



