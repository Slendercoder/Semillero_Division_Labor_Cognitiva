
#-*- coding: utf-8 -*-
from random import uniform
from random import randint
import numpy as np
import matplotlib.pyplot as plt
import random
import scipy as sp

# *******************************************************************
# DEFINICIONES DE OBJETOS Y FUNCIONES
# *******************************************************************

class Jugadores():
    def __init__(self, S, B, V):
        self.Score = S
        self.Boldness = B
        self.Vengefulness = V

def Imprimir_Jugador(j, Personas):
    print("Score: " + str(Personas[j].Score))
    print("Boldness: " + str(Personas[j].Boldness))
    print("Vengefulness: " + str(Personas[j].Vengefulness))

def Iteracion(Poblacion):
    Corrompe_norma=[]
    # for u in Poblacion:
    #     #Le damos a cada habitante 4 oportunidades para no cumplir la norma
    #     for k in range(0,4):
    #         s = uniform(0,1)
    #         b = u.Boldness
    #         if s < b:
    #             u.Score +=3
    #             Corrompe_norma.append(0)
    #             for y in Poblacion:
    #                 if y!=u:
    #                     y.Score += -1
    #                     s1 = uniform(0,1)
    #                     if s1 < s:
    #                         r = uniform(0,1)
    #                         if r < y.Vengefulness:
    #                             u.Score += -9
    #                             y.Score += -2
    for u in range(len(Poblacion)):
        #Le damos a cada habitante 4 oportunidades para no cumplir la norma
        for k in range(0,4):
            s = uniform(0,1)
            b = Poblacion[u].Boldness
            if s < b:
                Poblacion[u].Score +=3
                Corrompe_norma.append(0)
                for y in range(len(Poblacion)):
                    if y!=u:
                        Poblacion[y].Score += -1
                        if s < Poblacion[y].Vengefulness:
                            Poblacion[u].Score += -9
                            Poblacion[y].Score += -2
            else:
                Corrompe_norma.append(1)
    return Poblacion, Corrompe_norma

def Experimento(Boldness_inicial, Vengefulness_inicial):
    # Inicializamos las variables
    Personas = []
    Scores =[]
    Boldness_1 =[]
    Vengefulness_1 = []
    Corrompe_norma_1 = []

    # Creamos la poblacion inicial donde cada habitante tiene un nivel aleatorio de boldness y vengefulness
    for i in range(0,20):
        Bold = sp.random.normal(Boldness_inicial, 0.2, 1)[0]
        if Bold > 1:
            Bold = 1
        elif Bold < 0:
            Bold = 0

        Veng = sp.random.normal(Vengefulness_inicial, 0.2, 1)[0]
        if Veng > 1:
            Veng = 1
        elif Veng < 0:
            Veng = 0

        Personas.append(Jugadores(0, Bold, Veng))

    #Creamos un bucle para iterar 100 nuevas generaciones
    print "Corriendo iteraciones..."
    for y in range(0,NumGeneraciones):

        Personas, aux = Iteracion(Personas)

        Scores.append([u.Score for u in Personas])
        # print "i: " + str(y) + " Scores: ", Scores
        Boldness_1.append([u.Boldness for u in Personas])
        Vengefulness_1.append([u.Vengefulness for u in Personas])
        Corrompe_norma_1.append(aux)

        # Halla el promedio del Score y su desvacion estándar
        M = np.mean(Scores)
        # print "El promedio de scores es: " + str(M)
        std_deviation = np.std(Scores)
        # print "La desv. est. de scores es: " + str(std_deviation)

        # M = np.mean(Boldness_1)
        # print "El promedio de boldness es: " + str(M)
        #
        # M = np.mean(Vengefulness_1)
        # print "El promedio de vengefulness es: " + str(M)


        # Identifica a los buenos y a los regulares
        indices_buenos = []
        indices_regulares = []

        for i in range(len(Personas)):
            x = (Personas[i].Score-M)/std_deviation
            if (x) >= 1: indices_buenos.append(i)
            elif x > -1: indices_regulares.append(i)

        # print "Lista de buenos (tamano " + str(len(indices_buenos)) + ")"
        # print indices_buenos
        # print "Lista de regulares (tamano " + str(len(indices_regulares)) + ")"
        # print indices_regulares

        # Se crea una nueva lista dependiendo de la descendencia de los buenos y los 			regulares
        Personas_nuevas =[]
        for i in indices_buenos:
            Personas_nuevas.append(Personas[i])
            Personas_nuevas.append(Personas[i])

        # print "tamano de los nuevos buenos: " + str(len(Personas_nuevas))

        for i in indices_regulares:
            Personas_nuevas.append(Personas[i])

        # print "Tamano de los nuevos regulares: " + str(len(Personas_nuevas))

        if len(Personas_nuevas)<=20:
            Personas = Personas_nuevas
            x = 20 - len(Personas)
            for i in range(x):
                Bold = sp.random.normal(Boldness_inicial, 0.2, 1)[0]
                if Bold > 1:
                    Bold = 1
                elif Bold < 0:
                    Bold = 0
                Veng = sp.random.normal(Vengefulness_inicial, 0.2, 1)[0]
                if Veng > 1:
                    Veng = 1
                elif Veng < 0:
                    Veng = 0
                Personas.append(Jugadores(0, Bold, Veng))
        else:
            Personas = Personas_nuevas[:20]

    x = [np.mean(u) for u in Scores]
    y = [np.mean(u) for u in Boldness_1]
    z = [np.mean(u) for u in Vengefulness_1]
    u = [np.mean(u) for u in Corrompe_norma_1]

    return x, y, z, u

# *******************************************************************
# PARAMETROS DEL MODELO
# *******************************************************************

NumExp = 50
NumGeneraciones = 300
Boldness_inicial = 0.9
Vengefulness_inicial = 0.6

# *******************************************************************

X = []
Y = []
Z = []
U = []

# Esto dentro de un bucle
for i in range(NumExp):
    print "Comenzando experimento " + str(i) + "esimo"
    x, y, z, u = Experimento(Boldness_inicial, Vengefulness_inicial)
    # for i in range(len(x)):
    #     print "i: " + str(i) + " x: " + str(x[i])
    X.append(x)
    Y.append(y)
    Z.append(z)
    U.append(u)

# Hallamos los promedios por experimento
x = []
for i in range(NumGeneraciones):
    gen = [e[i] for e in X]
    x.append(np.mean(gen))

y = []
for i in range(NumGeneraciones):
    gen = [e[i] for e in Y]
    y.append(np.mean(gen))

z = []
for i in range(NumGeneraciones):
    gen = [e[i] for e in Z]
    z.append(np.mean(gen))

u = []
for i in range(NumGeneraciones):
    gen = [e[i] for e in U]
    u.append(np.mean(gen))


# print Corrompe_norma_1
# print "Listo!"

print "Dibujando..."
# f, axarr = plt.subplots(4, sharex=True)
f, axarr = plt.subplots(4)


axarr[0].set_ylabel('Score')
axarr[1].set_ylabel('Boldness')
axarr[1].set_ylim(-0.1, 1.1)
axarr[2].set_ylabel('Vengefulness')
axarr[2].set_ylim(-0.1, 1.1)
axarr[3].set_ylabel('Norma')
axarr[3].set_ylim(-0.1, 1.1)
axarr[3].set_xlabel('Generation')

axarr[0].plot(x)
axarr[1].plot(y)
axarr[2].plot(z)
axarr[3].plot(u)
# axarr[1].plot( y, 'y--', linewidth = 1)
# axarr[2].plot( z, 'r-.', linewidth = 1)
axarr[0].set_title('Boldness =' + str(Boldness_inicial) + ' Vengefulness =' + str(Vengefulness_inicial))

# axarr[1].scatter(x, y)
plt.show()

# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# #ax1.set_title("Temperatura del panal vs. tiempo")
# # ax1.set_xlabel('t (time)')
# # ax1.set_ylabel('T (temperature)')
# # ax1.set_ylim([29, 33])
# ax1.plot([np.mean(u) for u in Scores], marker="v", ls='-') # , 'x', c = 'black', linewidth=4)
# ax1.plot([np.mean(u) for u in Boldness_1], marker="o",ls='-') # , 'x', c = 'black', linewidth=4)
# plt.show()
# #ax1.plot(Tp, c='black')
