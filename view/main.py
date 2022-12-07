import threading
from tkinter import *
from src import utilManga, utilFormatt, utilSystem

class App:

    #consts para manipulacao
    mangas_encontrados = {}
    capitulos_encontrados = {}
    manga_selecionado = ""
    infos_manga = None
    link_manga = ""

    # constante para a tela de carregando
    root_carregando = None

    def __init__(self):
        self.root = Tk()
        self.root.title("Mangas Downloader")
        self.root.geometry("400x450")
        self.root.resizable(False, False)
        # criar no meio da tela
        self.root.eval('tk::PlaceWindow . center')


        #cria o menu
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.menu.add_command(label="Configurações")
        self.menu.add_command(label="Sobre")

        #cria um label
        self.label_cabecalho = Label(self.root, text="\nDigite o nome do manga:")
        self.label_cabecalho.config(font=("Arial", 20))
        self.label_cabecalho.pack()

        #cria um input para o nome do manga
        self.input_nome_manga = Entry(self.root)
        self.input_nome_manga.config(font=("Arial", 20))
        self.input_nome_manga.pack()
        self.input_nome_manga.bind("<Return>", lambda event: self.procura_manga(self.input_nome_manga.get()))

        #cria um botão para pesquisar
        self.botao_pesquisar = Button(self.root, text="Pesquisar", command=lambda: self.procura_manga(self.input_nome_manga.get()))
        self.botao_pesquisar.config(font=("Arial", 12))
        self.botao_pesquisar["bg"] = "green"
        self.botao_pesquisar.pack()

        #cria um label para mostrar os mangas encontrados
        self.label_mangas_encontrados = Label(self.root, text="\nMangas encontrados:")
        self.label_mangas_encontrados.config(font=("Arial", 14))
        self.label_mangas_encontrados.pack()

        #cria lista para mostrar os mangas encontrados
        self.lista_mangas = Listbox(self.root)
        self.lista_mangas.config(font=("Arial", 12))
        self.lista_mangas.config(height=10)
        self.lista_mangas.config(width=30)
        #retorna posição do item selecionado
        self.lista_mangas.bind("<<ListboxSelect>>", lambda event: self.procura_capitulos(self.lista_mangas.curselection()))
        self.lista_mangas.pack()

        #cria grid para mostrar os capitulos encontrados
        self.label_capitulos = Label(self.root, text="\nCapitulos encontrados:")
        self.label_capitulos.config(font=("Arial", 14))

        #cria lista para mostrar os capitulos encontrados
        self.lista_capitulos = Listbox(self.root, selectmode=MULTIPLE)
        self.lista_capitulos.config(font=("Arial", 12))
        self.lista_capitulos.config(height=10)
        self.lista_capitulos.config(width=30)

        #cria o botão para baixar os capitulos
        self.botao_baixar_capitulos = Button(self.root, text="Baixar", command=lambda: self.baixar_capitulos())
        self.botao_baixar_capitulos.config(font=("Arial", 12))
        self.botao_baixar_capitulos["bg"] = "green"

        #cria o botão para selecionar todos os capitulos
        self.botao_selecionar_tudo = Button(self.root, text="Selecionar todos", command=lambda: self.selecionar_todos())
        #ao clicar no botão seleciona todos os capitulos
        self.botao_selecionar_tudo.config(font=("Arial", 12))
        self.botao_selecionar_tudo["bg"] = "blue"



    #funções do programa

    def alerta_carregando(self):
        self.root = Tk()
        #retira a barra de titulo
        self.root.overrideredirect(True)
        self.root.geometry("200x100")
        self.root.resizable(False, False)
        self.root.title("...")
        #criar no meio da tela
        self.root.eval('tk::PlaceWindow . center')

        self.label_carregando = Label(self.root, text="Carregando...")
        self.label_carregando.config(font=("Arial", 20))
        self.label_carregando.pack()


        return self.root




    def selecionar_todos(self):
        self.lista_capitulos.select_set(0, END)

    def procura_manga(self, nome):

        #cria uma nova janela para mostrar que está carregando
        self.root_carregando= self.alerta_carregando()


        #cria uma thread para não travar a interface
        thread = threading.Thread(target=self.procura_manga_thread, args=(nome,))
        thread.daemon = True
        thread.start()


    def procura_manga_thread(self, nome):
        self.mangas_encontrados = utilManga.procura_manga(nome)
        self.lista_mangas.delete(0, END)
        for manga in self.mangas_encontrados:
            self.lista_mangas.insert(END, manga)

        #fecha a janela de carregando
        self.root_carregando.destroy()


    def procura_capitulos(self, nome):
            self.manga_selecionado = (list(self.mangas_encontrados.keys())[nome[0]])
            self.infos_manga = utilManga.obtem_infos_manga(self.manga_selecionado)
            self.link_manga = self.mangas_encontrados[list(self.mangas_encontrados.keys())[nome[0]]]
            self.capitulos_encontrados = utilManga.procura_capitulos(self.link_manga)
            self.lista_mangas.delete(0, END)

            #desfaço os label e lista
            self.lista_mangas.pack_forget()
            self.label_mangas_encontrados.pack_forget()

            #crio os novos label e lista
            self.label_capitulos.pack()
            self.lista_capitulos.pack()
            self.botao_baixar_capitulos.pack()
            self.botao_selecionar_tudo.pack()

            for capitulo in self.capitulos_encontrados:
                self.lista_capitulos.insert(END, capitulo)

    def baixar_capitulos(self):
        #cria um thread para baixar os capitulos
        thread = threading.Thread(target=self.baixar_capitulos_thread)
        thread.start()

    def baixar_capitulos_thread(self):
        # inativar o botão de baixar
        self.botao_baixar_capitulos["state"] = "disabled"
        # inativar o botão de selecionar todos
        self.botao_selecionar_tudo["state"] = "disabled"
        # inativar a lista de capitulos
        self.lista_capitulos["state"] = "disabled"

        #pega os capitulos selecionados na lista
        selecionados = self.lista_capitulos.curselection()

        for selecionado in selecionados:
            pasta_cache = utilSystem.pasta_atual()
            pasta_temp = utilSystem.gerar_nome_aleatorio() #nome aleatorio para a pasta
            pasta_capitulo = pasta_cache + '\\cache\\' + pasta_temp

            utilSystem.cria_pasta(pasta_capitulo) #cria a pasta
            utilManga.baixa_capa(self.manga_selecionado, pasta_capitulo)
            paginas = utilManga.procura_paginas(self.capitulos_encontrados[list(self.capitulos_encontrados.keys())[selecionado]])
            utilManga.baixa_paginas(paginas, pasta_capitulo)
            nome_capitulo = list(self.capitulos_encontrados.keys())[selecionado]
            #transorma em um epub
            utilFormatt.cria_epub(self.infos_manga, nome_capitulo, pasta_capitulo)
            utilSystem.limpa_pasta(pasta_capitulo) #limpa a pasta


        #ativa o botão de baixar
        self.botao_baixar_capitulos["state"] = "normal"
        #ativa o botão de selecionar todos
        self.botao_selecionar_tudo["state"] = "normal"
        #ativa a lista de capitulos
        self.lista_capitulos["state"] = "normal"

    def run(self): #inicia o programa
        self.root.mainloop()


root = App()
root.run()


