#-*- coding: utf-8 -*-
# Semillero en división de la labor cognitiva
# Octubre de 2018

print("Importando paquetes...")
from random import randint
from random import uniform
import numpy as np
import matplotlib.pyplot as plt
import random
import scipy as sp
import sys
import time
import pandas as pd
print("Listo!")

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
    # Le damos a cada habitante 4 oportunidades para no cumplir la norma
    for u in range(len(Poblacion)):
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
    # Corremos la dinámica cuatro veces
    # for k in range(0,4):
    #     for u in range(len(Poblacion)):
    #         b = Poblacion[u].Boldness
    #         if s < b: # Si True, el jugador u-esimo transgrede la norma
    #             Poblacion[u].Score +=3 # Aumenta su puntaje en 3 unidades
    #             Corrompe_norma.append(0) # Se pone un 0 porque hubo una transgreción de la norma
    #             for y in range(len(Poblacion)): # Para los demás jugadores
    #                 if y!=u:
    #                     Poblacion[y].Score += -1 # La transgresión disminuye su puntaje en 1 unidad
    #                     if s < Poblacion[y].Vengefulness: # Si True, el agente y-ésimo ve la transgresión
    #                         Poblacion[u].Score += -9 # Castiga al transgresor
    #                         Poblacion[y].Score += -2 # Sufre al castigar
            else:
                Corrompe_norma.append(1) # No hubo transgresión de la norma
    return Poblacion, Corrompe_norma

def Experimento(numGeneraciones):
    # Inicializamos las variables
    Personas = []
    Scores =[]
    Boldness_1 =[]
    Vengefulness_1 = []
    Corrompe_norma_1 = []

    # Creamos la poblacion inicial donde cada habitante tiene un nivel aleatorio de boldness y vengefulness
    for i in range(0,numJugadores):
        Bold = randint(0,7)
        Prob_Bold= float(Bold)/7
        # print("Prob_Bold", Prob_Bold)
        Veng = randint(0,7)
        Prob_Veng = float(Veng)/7
        # print("Prob_Veng", Prob_Veng)
        Personas.append(Jugadores(0, Prob_Bold, Prob_Veng))

    Scores.append([u.Score for u in Personas]) # Guarda los scores en esta generación
    Boldness_1.append([u.Boldness for u in Personas]) # Guarda Boldness en esta generación
    Vengefulness_1.append([u.Vengefulness for u in Personas]) # Guarda Vengefulness en esta generación
    Corrompe_norma_1.append([np.nan] * numJugadores) # Guarda opciones de transgreción en esta generación

    #Creamos un bucle para iterar 100 nuevas generaciones
    print("Corriendo iteraciones...")
    for y in range(0, numGeneraciones):

        # Actualizamos los scores siguiendo la dinámica de Axelrod
        Personas, aux = Iteracion(Personas)

        Scores.append([u.Score for u in Personas]) # Guarda los scores en esta generación
        Boldness_1.append([u.Boldness for u in Personas]) # Guarda Boldness en esta generación
        Vengefulness_1.append([u.Vengefulness for u in Personas]) # Guarda Vengefulness en esta generación
        Corrompe_norma_1.append(aux) # Guarda opciones de transgreción en esta generación

        # Halla el promedio del Score y su desvacion estándar
        puntajes = [x.Score for x in Personas]
        M = np.mean(puntajes)
        print("El promedio de scores es: ", M)
        std_deviation = np.std(puntajes)
        print("La desv. est. de scores es: ", std_deviation)

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
                Personas_nuevas.append(Jugadores(0, Personas[i].Boldness, Personas[i].Vengefulness)) # los regulares son aquellos que están en (-1,1)

        # print "Lista de buenos (tamano " + str(len(indices_buenos)) + ")"
        # print indices_buenos
        # print "Lista de regulares (tamano " + str(len(indices_regulares)) + ")"
        # print indices_regulares
        # print "Tamano de los nuevos regulares: " + str(len(Personas_nuevas))

        # Revisamos si faltan jugadores para completar numJugadores
        if len(Personas_nuevas)<=numJugadores:
            Personas = Personas_nuevas
            x = numJugadores - len(Personas)
            for i in range(x):
                Bold = randint(0,7)
                Prob_Bold= float(Bold)/7 #int(round(x)) redondea el numero decimal al entero mas cercano

                Veng = randint(0,7)
                Prob_Veng = float(Veng)/7

                Personas.append(Jugadores(0, Prob_Bold, Prob_Veng))
        else:
            Personas = Personas_nuevas[:numJugadores]

        #Mutación
        for i in range(len(Personas)):
            mutation = uniform(0,1)
            if mutation < 0.01:
                print(u"Hubo mutación!")
                Bold = randint(0,7)
                Prob_Bold= float(Bold)/7
                Veng = randint(0,7)
                Prob_Veng = float(Veng)/7
                Personas[i].Boldness = Prob_Bold
                Personas[i].Vengefulness = Prob_Veng

    return Scores, Boldness_1, Vengefulness_1, Corrompe_norma_1

# *******************************************************************
# PARAMETROS DEL MODELO
# *******************************************************************

numJugadores = 20
numExp = 5
numGeneraciones = 100

# *******************************************************************

# Para pasar los datos a pandas DataFrame
datos = []

for i in range(numExp):
    print("Comenzando experimento " + str(i + 1) + u"-ésimo")
    Scores, Boldness_1, Vengefulness_1, Corrompe_norma_1 = Experimento(numGeneraciones)
    for g in range(numGeneraciones + 1):
        for j in range(numJugadores):
            dict = {}
            dict['Experimento'] = i + 1
            dict['Generacion'] = g
            dict['Jugador'] = j
            dict['Score'] = Scores[g][j]
            dict['Boldness'] = Boldness_1[g][j]
            dict['Vengefulness'] = Vengefulness_1[g][j]
            dict['Follows_norm'] = Corrompe_norma_1[g][j]
            datos.append(dict)

df = pd.DataFrame(datos)

df.to_csv('datos.csv')
print("Datos guardados en datos.csv")

print(df[:3])

print("Terminado!")
