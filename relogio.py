''' Código para criar um relógio digital em Python
    Autor: Carlos Reis
    Data: 20/07/2021
    Versão: 1.0'''

# importa as bibliotecas necessárias
from tkinter import *   
import tkinter  
from datetime import datetime   

import pyglet   // importa a biblioteca pyglet
pyglet.font.add_file(r"C:\Users\carlo\OneDrive\ANALYTICS\0001_caixa_ferramentas\0001_python_para_tudo\relogio\arquivos\skyfont\Skyfont.otf")


# cores de fundo e da fonte
cor1 = "#3d3d3d"  # preta   
cor2 = "#fafcff"  # branca  
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul

# define as cores nas variáveis
fundo = cor1
cor = cor5

# cria a janela do programa
janela = Tk()
janela.title("")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1)
l1 = Label

# função para atualizar o relógio
def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%B")
    ano = tempo.strftime("%Y")

    l1.config(text = hora)
    l1.after(180, relogio)
    l2.config(text = dia_semana + ", " + str(dia) + "/" + str(mes) + "/" + str(ano))

l1 = Label(janela, text = "", font=("Skyfont 80"), bg = fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, text = "", font=("Skyfont 22"), bg = fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop() // loop infinito