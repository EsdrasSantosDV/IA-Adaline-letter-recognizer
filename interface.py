import tkinter
from tkinter import *
import os
import numpy as np
import random
import matplotlib.pyplot as plt


def submit_button_event():
    taxa = input_taxa.get()
    tolerated_error = input_tolerated_error.get()
    print(taxa)
    print(tolerated_error)
    # logica do submit

def test_button_event():
    selectedchecks=[]
    for i, row in enumerate(checkboxes):
        for j, var in enumerate(row):
            if checkboxes[i][j].get() ==0:
                selectedchecks.append(-1)
            else:
                selectedchecks.append(1)




def on_select(value,checkboxes,x):
    index = options.index(value)
    row_values = x[index, :]

    k=0
    for i in range(9):
        for j in range(7):
            if(row_values[k]==1.0):
                checkboxes[i][j].set(1)
            else:
                checkboxes[i][j].set(0)
            k=k+1



window = Tk()

window.title("IA-TRABALHO-GRUPO-ESDRAS-JOAO-OTAVIO-FELIPE MENDES")
window.geometry('1920x1080')
window.configure(background="gray")
form_label_taxa = tkinter.Label(window, text="Digite a Taxa de Aprendizagem:")
form_label_tolerated_error = tkinter.Label(window, text="Digite o Erro Tolerado:")
input_taxa = tkinter.Entry(window)
input_tolerated_error = tkinter.Entry(window)
submit_button = tkinter.Button(window, text="Realizar Aprendizado", command=submit_button_event)
form_label_taxa.place(x=100, y=50)
input_taxa.place(x=350, y=50)
form_label_tolerated_error.place(x=100, y=100)
input_tolerated_error.place(x=350, y=100)
submit_button.place(x=350, y=150)
checkboxes = []
for i in range(9):
    row = []
    for j in range(7):
        var = IntVar()
        checkbox = Checkbutton(window, variable=var)
        checkbox.place(x=320 + j * 30, y=200 + i * 25)
        row.append(var)
    checkboxes.append(row)
button_test = tkinter.Button(window, text="Realizar Teste", command=test_button_event)
button_test.place(x=5 + j * 60, y=200 + i * 30)
options = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1', 'D2', 'D3', 'E1', 'E2', 'E3', 'J1', 'J2', 'J3',
           'K1', 'K2', 'K3']
variable = tkinter.StringVar()
option_menu = tkinter.OptionMenu(window, variable, *options)
variable.trace("w", lambda name, index, mode, variable=variable: on_select(variable.get(),checkboxes,x))
option_menu.place(x=250, y=200)

window.mainloop()
