import tkinter
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("IA-TRABALHO-GRUPO-ESDRAS-JOAO-OTAVIO-FELIPE MENDES")
window.geometry('1920x1080')
window.configure(background="gray");

form_label_taxa = tkinter.Label(window, text="Digite a Taxa de Aprendizagem:")
form_label_tolerated_error = tkinter.Label(window, text="Digite o Erro Tolerado:")

input_taxa=tkinter.Entry()
input_tolerated_error=tkinter.Entry()


def submit():
    taxa=input_taxa.get()
    tolerated_error=input_tolerated_error.get()

    print("TAXA ",taxa)
    print("ERRO TOLERADO ",tolerated_error)





submit_button = tkinter.Button(window, text="Submit", command=submit)


form_label_taxa.grid(row=0, column=0,padx=10,pady=10)
input_taxa.grid(row=0, column=1,padx=10,pady=10)
form_label_tolerated_error.grid(row=1, column=0,padx=10,pady=10)
input_tolerated_error.grid(row=1, column=1,padx=10,pady=10)
submit_button.grid(row=2, column=1,padx=10,pady=10)



window.mainloop()
