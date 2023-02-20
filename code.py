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

            # Plotting the value ##
            plt.scatter(chartCycleAxis, chartErrorAxis, marker='.', color='red')
            plt.xlabel('cycle')
            plt.ylabel('error')

            plt.pause(0.0001)
            plt.clf()
            plt.plot(chartCycleAxis, chartErrorAxis)
            plt.draw()


        plt.scatter(chartCycleAxis, chartErrorAxis, marker='.', color='red')
        plt.xlabel('cycle')
        plt.ylabel('error')
        plt.show()

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

teste = IALetterReconizer()
teste.trainAI(0.001, 0.0001)
teste.testIA(teste.x[3, :])


########################################################## TRAINING ##########################################################

## READ TXT ARCHIVES THAT CONTAINS THE VALUES AND RESULTS ##
# TODO: HERE YOU NEED TO PUT THE ABSOLUTE PATH WHERE IS THE DIRECTORY OF "IA-Adaline-letter-recognizer"
# os.chdir(r'C:\Users\joao_\Desktop\FACUL 2023\IA\Trabalhos\trab2\IA-Adaline-letter-recognizer')

# x=np.loadtxt('letterArrayValues.txt')
# (samples, inputs)=np.shape(x)

# target=np.loadtxt('results.txt')
# (numResults, numExamples)=np.shape(target)

# ## SPECIFY THE PARAMETERS OS THE LERNING STEP ##
# threshold=0.0
# alpha=0.001
# toleratedError=0.0001

# ## CREATE VARIABLES OF PLOT, WEIGHTS, OUTPUTS, ERROR AND CYCLE ##
# chartCycleAxis = []
# chartErrorAxis = []

# v=np.zeros((inputs, numResults))
# v0=np.zeros(numResults)

# yin = np.zeros((numResults, 1))
# y = np.zeros((numResults, 1))

# error = 5
# cycle=0

# ## SPECIFY THE PARAMETERS OS THE LERNING STEP ##
# for i in range(inputs):
#     for j in range(numResults):
#         #v -> SYNAPTIC WEIGHTS
#         v[i][j]=random.uniform(-0.1, 0.1)

# for i in range(numResults):
#     #V0 -> BIAS PARAMETER
#     v0[j]=random.uniform(-0.1, 0.1)

# ## LOOP OF LEARNING STEP ##
# while error>toleratedError:
#     #INCREMENT CYCLE
#     cycle=cycle+1
#     error=0
#     for i in range(samples):
#         #Xaux -> The input values of only the current row
#         Xaux = x[i,:]
#         for j in range(numResults):
#             sum=0
#             for k in range(inputs):
#                 #the sum to be used to determinate the output index
#                 sum=sum+Xaux[k]*v[k][j]
#             #The initial input index that is determinated by the sum plus the bias
#             yin[j]=sum+v0[j]

#         for j in range(numResults):
#             # Y -> the output index that is compared with treshold.
#             if yin[j]>threshold:
#                 y[j]=1.0
#             else:
#                 y[j]=-1.0

#         for j in range(numResults):
#             # calculation of error, using the formula of slide 10
#             error=error+0.5*((target[j][i]-y[j])**2)

#         #here we need the previous V to use in the formula of next weight
#         previousV = v

#         for j in range(inputs):
#             for k in range(numResults):
#                 #Calculation of new weights using the formula of slide 13
#                 v[j][k] = previousV[j][k]+alpha*(target[k][i]-y[k])*Xaux[j]

#         #here we need the previous V0 to use in the formula of next bias
#         previousV0=v0

#         for j in range(numResults):
#             #Calculation of new bias using the formula of slide 13
#             v0[j]=previousV0[j]+alpha*(target[j][i]-y[j])

#     ## Insert the cycle and error to the respectiver arrays that will be showed in plot ##
#     chartCycleAxis.append(cycle)
#     chartErrorAxis.append(error)

#     ## Plotting the value ##
#     plt.scatter(chartCycleAxis, chartErrorAxis, marker='.', color='red')
#     plt.xlabel('cycle')
#     plt.ylabel('error')

#     plt.pause(0.0001)
#     plt.clf()
#     plt.plot(chartCycleAxis, chartErrorAxis)
#     plt.draw()

# ##############################################################################################################################
# ########################################################## TESTING ###########################################################

# #Variable that contains the row of array that was tested
# letterTest = x[15, :]
# for iTest in range(numResults):
#     sum=0
#     for jTest in range(inputs):
#         #the sum to be used to determinate the output index
#         sum=sum+letterTest[jTest]*v[jTest][iTest]
#     #The initial input index that is determinated by the sum plus the bias
#     yin[iTest]=sum+v0[iTest]
# for j in range(numResults):
#     # Y -> the output index that is compared with treshold.
#     if yin[j]>=threshold:
#         y[j]=1.0
#     else:
#         y[j]=-1.0

# # RESULT LOGS
# print("\nARRAY DE RECONHECIMENTO:")
# print(y)

# print()
# if y[0]==1:
#     print("A LETRA RECONHECIDA FOI A LETRA: A")
# if y[1]==1:
#     print("A LETRA RECONHECIDA FOI A LETRA: B")
# if y[2]==1:
#     print("A LETRA RECONHECIDA FOI A LETRA: C")
# if y[3]==1:
#     print("A LETRA RECONHECIDA FOI A LETRA: D")
# if y[4]==1:
#     print("A LETRA RECONHECIDA FOI A LETRA: E")
# if y[5]==1:
#     print("A LETRA RECONHECIDA FOI A LETRA: J")
# if y[6]==1:
#     print("A LETRA RECONHECIDA FOI A LETRA: K")

# #Make the graph stay static in screen
# plt.scatter(chartCycleAxis, chartErrorAxis, marker='.', color='red')
# plt.xlabel('cycle')
# plt.ylabel('error')
# plt.show()

##############################################################################################################################