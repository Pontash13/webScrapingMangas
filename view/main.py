from tkinter import *
from src import utilManga

class App:

    #consts para manipulacao
    mangas_encontrados = {}
    capitulos_encontrados = {}

    def __init__(self):
        self.root = Tk()
        self.root.title("Mangas Downloader")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        #cria o menu
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.menu.add_command(label="Confirações")
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


    #funções do programa
    def procura_manga(self, nome):
        self.mangas_encontrados = utilManga.procura_manga(nome)
        self.lista_mangas.delete(0, END)
        for manga in self.mangas_encontrados:
            self.lista_mangas.insert(END, manga)

    def procura_capitulos(self, nome):
        selecionado = self.mangas_encontrados[list(self.mangas_encontrados.keys())[nome[0]]]
        self.capitulos_encontrados = utilManga.procura_capitulos(selecionado)
        self.lista_mangas.delete(0, END)

        #desfaço os label e lista
        self.lista_mangas.pack_forget()
        self.label_mangas_encontrados.pack_forget()

        #crio os novos label e lista
        self.label_capitulos.pack()
        self.lista_capitulos.pack()
        self.botao_baixar_capitulos.pack()

        for capitulo in self.capitulos_encontrados:
            self.lista_capitulos.insert(END, capitulo)




    def run(self):
        self.root.mainloop()


root = App()
root.run()


