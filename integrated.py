import tkinter
from tkinter import *
import os
import numpy as np
import random
import matplotlib.pyplot as plt

class IALetterReconizer:
    def __init__(self):
        self.threshold = 0.0
        os.chdir(r'/home/esdras/Documents/PROJETOS PESSOAIS/IA/IA-Adaline-letter-recognizer')
        self.x = np.loadtxt('letterArrayValues.txt')
        self.target = np.loadtxt('results.txt')
        (self.samples, self.inputs) = np.shape(self.x)
        (self.numResults, self.numExamples) = np.shape(self.target)
        self.v = np.zeros((self.inputs, self.numResults))
        self.v0 = np.zeros(self.numResults)

    def trainAI(self, alpha, toleratedError):
        self.alpha = alpha
        self.toleratedError = toleratedError

        yin = np.zeros((self.numResults, 1))
        y = np.zeros((self.numResults, 1))

        error = 5
        cycle = 0

        chartCycleAxis = []
        chartErrorAxis = []

        ## SPECIFY THE PARAMETERS OS THE LERNING STEP ##
        for i in range(self.inputs):
            for j in range(self.numResults):
                # v -> SYNAPTIC WEIGHTS
                self.v[i][j] = random.uniform(-0.1, 0.1)

        for i in range(self.numResults):
            # V0 -> BIAS PARAMETER
            self.v0[j] = random.uniform(-0.1, 0.1)

        ## LOOP OF LEARNING STEP ##
        while error > self.toleratedError:
            # INCREMENT CYCLE
            cycle = cycle + 1
            error = 0
            for i in range(self.samples):
                # Xaux -> The input values of only the current row
                Xaux = self.x[i, :]
                for j in range(self.numResults):
                    sum = 0
                    for k in range(self.inputs):
                        # the sum to be used to determinate the output index
                        sum = sum + Xaux[k] * self.v[k][j]
                    # The initial input index that is determinated by the sum plus the bias
                    yin[j] = sum + self.v0[j]

                for j in range(self.numResults):
                    # Y -> the output index that is compared with treshold.
                    if yin[j] > self.threshold:
                        y[j] = 1.0
                    else:
                        y[j] = -1.0

                for j in range(self.numResults):
                    # calculation of error, using the formula of slide 10
                    error = error + 0.5 * ((self.target[j][i] - y[j]) ** 2)

                # here we need the previous V to use in the formula of next weight
                previousV = self.v

                for j in range(self.inputs):
                    for k in range(self.numResults):
                        # Calculation of new weights using the formula of slide 13
                        self.v[j][k] = previousV[j][k] + self.alpha * (self.target[k][i] - y[k]) * Xaux[j]

                # here we need the previous V0 to use in the formula of next bias
                previousV0 = self.v0

                for j in range(self.numResults):
                    # Calculation of new bias using the formula of slide 13
                    self.v0[j] = previousV0[j] + self.alpha * (self.target[j][i] - y[j])

            ## Insert the cycle and error to the respectiver arrays that will be showed in plot ##
            chartCycleAxis.append(cycle)
            chartErrorAxis.append(error)

            ## Plotting the value ##
            # plt.scatter(chartCycleAxis, chartErrorAxis, marker='.', color='red')
            # plt.xlabel('cycle')
            # plt.ylabel('error')

            # plt.pause(0.0001)
            # plt.clf()
            # plt.plot(chartCycleAxis, chartErrorAxis)
            # plt.draw()

        # Make the graph stay static in screen
        # plt.scatter(chartCycleAxis, chartErrorAxis, marker='.', color='red')
        # plt.xlabel('cycle')
        # plt.ylabel('error')
        # plt.show()

    def testIA(self, letterTest):
        yin = np.zeros((self.numResults, 1))
        y = np.zeros((self.numResults, 1))

        for iTest in range(self.numResults):
            sum = 0
            for jTest in range(self.inputs):
                # the sum to be used to determinate the output index
                sum = sum + letterTest[jTest] * self.v[jTest][iTest]
            # The initial input index that is determinated by the sum plus the bias
            yin[iTest] = sum + self.v0[iTest]
        for j in range(self.numResults):
            # Y -> the output index that is compared with treshold.
            if yin[j] >= self.threshold:
                y[j] = 1.0
            else:
                y[j] = -1.0

        # RESULT LOGS
        print("\nARRAY DE RECONHECIMENTO:")
        print(y)

        print()
        if y[0] == 1:
            print("A LETRA RECONHECIDA FOI A LETRA: A")
        elif y[1] == 1:
            print("A LETRA RECONHECIDA FOI A LETRA: B")
        elif y[2] == 1:
            print("A LETRA RECONHECIDA FOI A LETRA: C")
        elif y[3] == 1:
            print("A LETRA RECONHECIDA FOI A LETRA: D")
        elif y[4] == 1:
            print("A LETRA RECONHECIDA FOI A LETRA: E")
        elif y[5] == 1:
            print("A LETRA RECONHECIDA FOI A LETRA: J")
        elif y[6] == 1:
            print("A LETRA RECONHECIDA FOI A LETRA: K")
        else:
            print("NÃO FOI POSSÍVEL RECONHECER NENHUMA LETRA")

def submit_button_event():
    taxa =  float(input_taxa.get())
    tolerated_error = float(input_tolerated_error.get())
    if taxa > 0.00 and tolerated_error >0.00:
        skynet.trainAI(taxa,tolerated_error)

def test_button_event():
    selectedchecks=[]
    for i, row in enumerate(checkboxes):
        for j, var in enumerate(row):
            if checkboxes[i][j].get() ==0:
                selectedchecks.append(-1)
            else:
                selectedchecks.append(1)
    print(selectedchecks)
    skynet.testIA(selectedchecks)



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
skynet= IALetterReconizer()
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
variable.trace("w", lambda name, index, mode, variable=variable: on_select(variable.get(),checkboxes,skynet.x))
option_menu.place(x=250, y=200)

window.mainloop()