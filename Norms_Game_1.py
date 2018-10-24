#-*- coding: utf-8 -*-
# Semillero en división de la labor cognitiva
# Octubre de 2018

import numpy as np
import matplotlib.pyplot as plt
import random
import scipy as sp
import sys
import time

random.seed(time.time())

# *******************************************************************
# DEFINICIONES DE OBJETOS Y FUNCIONES
# *******************************************************************

class Jugadores():
    # Se define un objeto jugadores con tres atributos
    # Score, que es el puntaje resultado de sus acciones y las de los demás participantes
    # Boldness, que es su propensidad a transgredir la norma (número entre 0 y 1)
    # Vengefulness, que es su propensidad a castigar una transgresión de la norma
    def __init__(self, S, B, V):
        self.Score = S
        self.Boldness = B
        self.Vengefulness = V

def Imprimir_Jugador(j, Personas):
    # Imprime los atributos del jugador j-ésimo en la lista Personas
    # Input: - j, índice
    #        - Personas, lista de jugadores
    # Output: None
    print("Score: " + str(Personas[j].Score))
    print("Boldness: " + str(Personas[j].Boldness))
    print("Vengefulness: " + str(Personas[j].Vengefulness))

def Iteracion(Poblacion):
    # Cuatro rondas del juego definido por Axelrod (1986)
    # Input: Poblacion, lista de jugadores
    # Output: - Poblacion, lista de jugadores con score actualizado
    #         - Corrompe_norma, lista de oportunidades de transgresión de la norma
    Corrompe_norma=[] # Guarda 0 si la norma fue transgredida; 1 si no
    s = uniform(0,1) # Probabilidad de ser visto
    for u in range(len(Poblacion)):
        #Le damos a cada habitante 4 oportunidades para no cumplir la norma
        for k in range(0,4):
            b = Poblacion[u].Boldness
            if s < b: # Si True, el jugador u-esimo transgrede la norma
                Poblacion[u].Score +=3 # Aumenta su puntaje en 3 unidades
                Corrompe_norma.append(0) # Se pone un 0 porque hubo una transgreción de la norma
                for y in range(len(Poblacion)): # Para los demás jugadores
                    if y!=u:
                        Poblacion[y].Score += -1 # La transgresión disminuye su puntaje en 1 unidad
                        if s < Poblacion[y].Vengefulness: # Si True, el agente y-ésimo ve la transgresión
                            Poblacion[u].Score += -9 # Castiga al transgresor
                            Poblacion[y].Score += -2 # Sufre al castigar
            else:
                Corrompe_norma.append(1) # No hubo transgresión de la norma
    return Poblacion, Corrompe_norma

def Experimento():
    # Inicializamos las variables
    Personas = []
    Scores =[]
    Boldness_1 =[]
    Vengefulness_1 = []
    Corrompe_norma_1 = []

    # Creamos la poblacion inicial donde cada habitante tiene un nivel aleatorio de boldness y vengefulness
    for i in range(0,20):
        Bold = randint(0,7)
        Prob_Bold= float(Bold)/7
        Veng = randint(0,7)
        Prob_Veng = float(Veng)/7
        Personas.append(Jugadores(0, Prob_Bold, Prob_Veng))

    #Creamos un bucle para iterar 100 nuevas generaciones
    print("Corriendo iteraciones...")
    for y in range(0, NumGeneraciones):

        # Actualizamos los scores siguiendo la dinámica de Axelrod
        Personas, aux = Iteracion(Personas)

        Scores.append([u.Score for u in Personas]) # Guarda los scores en esta generación
        # print "i: " + str(y) + " Scores: ", Scores
        Boldness_1.append([u.Boldness for u in Personas]) # Guarda Boldness en esta generación
        Vengefulness_1.append([u.Vengefulness for u in Personas]) # Guarda Vengefulness en esta generación
        Corrompe_norma_1.append(aux) # Guarda opciones de transgreción en esta generación

        # Halla el promedio del Score y su desvacion estándar
        M = np.mean(Scores[-1])
        # print "El promedio de scores es: " + str(M)
        std_deviation = np.std(Scores[-1])
        # print "La desv. est. de scores es: " + str(std_deviation)

        # M = np.mean(Boldness_1)
        # print "El promedio de boldness es: " + str(M)
        #
        # M = np.mean(Vengefulness_1)
        # print "El promedio de vengefulness es: " + str(M)

        # Identifica a los jugadores buenos y a los regulares
        Personas_nuevas =[]

        # Se actualiza la población dependiendo de la descendencia de los buenos y los regulares
        for i in range(len(Personas)):
            x = (Personas[i].Score-M)/std_deviation
            if (x) >= 1:
                Personas_nuevas.append(Jugadores(0, Personas[i].Boldness, Personas[i].Vengefulness))
                Personas_nuevas.append(Jugadores(0, Personas[i].Boldness, Personas[i].Vengefulness))
            elif x > -1:
                Personas_nuevas.append(Jugadores(0, Personas[i].Boldness, Personas[i].Vengefulness)) # los regulares son aquellos quienes estan en (-1,1)

        # print "Lista de buenos (tamano " + str(len(indices_buenos)) + ")"
        # print indices_buenos
        # print "Lista de regulares (tamano " + str(len(indices_regulares)) + ")"
        # print indices_regulares
        # print "Tamano de los nuevos regulares: " + str(len(Personas_nuevas))

        # Revisamos si faltan jugadores para completar 20
        if len(Personas_nuevas)<=20:
            Personas = Personas_nuevas
            x = 20 - len(Personas)
            for i in range(x):
                Bold = randint(0,7)
                Prob_Bold= float(Bold)/7 #int(round(x)) redondea el numero decimal al entero mas cercano

                Veng = randint(0,7)
                Prob_Veng = float(Veng)/7

                Personas.append(Jugadores(0, Prob_Bold, Prob_Veng))
        else:
            Personas = Personas_nuevas[:20]

        #Mutación
        for i in range(len(Personas)):
            mutation = uniform(0,1)
            if mutation <0.01:
                Bold = randint(0,7)
                Prob_Bold= float(Bold)/7
                Veng = randint(0,7)
                Prob_Veng = float(Veng)/7
                Personas[i].Boldness = Prob_Bold
                Personas[i].Vengefulness = Prob_Veng

    return Scores,Boldness_1,Vengefulness_1,Corrompe_norma_1

# *******************************************************************
# PARAMETROS DEL MODELO
# *******************************************************************

NumExp = 10
NumGeneraciones = 100

# *******************************************************************

X = []
Y = []
Z = []
U = []
Boldness_Av = []
Vengefulness_Av = []

# Esto dentro de un bucle
for i in range(NumExp):
    print("Comenzando experimento " + str(i) + u"-ésimo")
    Scores,Boldness_1,Vengefulness_1,Corrompe_norma_1 = Experimento()
    # for i in range(len(x)):
    #     print "i: " + str(i) + " x: " + str(x[i])
    x = [np.mean(u) for u in Scores]
    y = [np.mean(u) for u in Boldness_1]
    z = [np.mean(u) for u in Vengefulness_1]
    u = [np.mean(u) for u in Corrompe_norma_1]
    X.append(x)
    Y.append(y)
    Z.append(z)
    U.append(u)

# Grafica Axelrod Básica

ultimaGeneracionBoldness = []
ultimaGeneracionVengefulness = []
for g in Y:
    ultimaGeneracionBoldness.append(np.mean(g[-1]))
    ultimaGeneracionVengefulness.append(np.mean(g[-1]))

plt.xlabel("Boldness")
plt.ylabel("Vengefullness")
plt.title('Norms Game Dynamics')
plt.ylim([0.0, 1.0])
plt.xlim([0.0, 1.0])
plt.plot(ultimaGeneracionBoldness,ultimaGeneracionVengefulness,'D',color = 'grey')
plt.show()

sys.exit()

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


#Graficar Vengefullnes Y Boldness Unico // Solo estamos graficando el ultimo experimento ojo !
fig, ax = plt.subplots()

ax.plot(z,color = 'grey',label = "Boldness")
ax.plot(y,color = 'black' , linestyle = '--',label = "Vengefulness")

plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.ylim([0.0, 1.0])
plt.yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
plt.xlim([0.0, NumGeneraciones])
plt.show()

# print Corrompe_norma_1
# print "Listo!"

print("Dibujando...")
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
