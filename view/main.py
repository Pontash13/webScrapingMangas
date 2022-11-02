#hello world tkinter
from tkinter import *
from src import utilManga

#instanciar utilManga


#criando a janela e definindo seu comportamento
root = Tk()
root.title("Mangas Downloader")
root.geometry("600x400")

#não pode mudar o tamanho
root.resizable(False, False)

#cria menu principal e adiciona já algumas funcionalidades
menu = Menu(root, tearoff=0)
menu.add_command(label="Configurações")
menu.add_command(label="Sobre", command=root.quit)
menu.add_command(label="Sair", command=root.quit)


root.config(menu=menu)

#cria o label principal
label = Label()
label.config(font=("Arial MT", 11))
label.config(text="\nProcure por um manga:\n")
label.pack()

#cria caixa de texto para o usuario digitar o nome do manga e adiciona um botão para pesquisar ao lado
caixa = Entry(root, width=50)
caixa.pack()
botao = Button(root, text="Pesquisar")
#on click do botao, chama a função pesquisar

botao.config(bg="yellow")
botao.pack()

#cria um label para mostrar os resultados
label_resultados = Label()
label_resultados.config(font=("Arial MT", 11))
label_resultados.config(text="\nResultados:")
label_resultados.pack()
#
#cria uma lista para mostrar os resultados
lista = Listbox(root, width=50)
lista.pack()


#Roda tudo
root.mainloop()