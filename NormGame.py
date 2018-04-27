
#-*- coding: utf-8 -*-
from random import uniform
from random import randint
import numpy as np

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
    for u in Poblacion:
        for y in range(0,3):
            s = uniform(0,1)
            b = u.Boldness
            if s<b:
                u.Score +=3
                for y in Personas:
                    s1= uniform(0,1)
                    if y!=u:
                        y.Score += -1
                    elif s1<s and y!=u:
                        r = uniform(0,1)
                        if r<y.Vengefulness:
                            u.Score +=-9
                            y.Score += -2
    return Poblacion

# *******************************************************************

# Inicializamos las variables
Personas = []
Scores =[]
Boldness_1 =[]
Vengefulness_1 = []
# Falta inicializar lista de Boldness y Vengefulness

# Creamos la poblacion inicial de manera aleatoria
for i in range(0,20):
    Personas.append(Jugadores(0, uniform(0,1),uniform(0,1)))
#Creamos un bucle para iterar 100 nuevas generaciones

for y in range(0,99):
# Determina el puntaje total de las personas
	Personas = Iteracion(Personas)
	# for j in range(0,20):
	#     Imprimir_Jugador(j, Personas)
	Scores.append([u.Score for u in Personas])
	Boldness_1.append([u.Boldness for u in Personas])
	Vengefulness_1.append([u.Vengefulness for u in Personas])


	# Halla los promedios de los Scores, Vengefulness y Boldness y halla la desvacion 			estándar de los Scores  
	M = np.mean(Scores)
	print "El promedio de scores es: " + str(M)
	std_deviation = np.std(Scores)
	print "La desv. est. de scores es: " + str(std_deviation)

	M = np.mean(Boldness_1)
	print "El promedio de boldness es: " + str(M)

	M = np.mean(Vengefulness)
	print "El promedio de vengefulness es: " + str(M)


	# Identifica a los buenos y a los regulares
	indices_buenos = []
	indices_regulares = []

	for i in range(len(Personas)):
	    x = (Personas[i].Score-M)/std_deviation
	    if (x) >= 1: indices_buenos.append(i)
	    elif x > -1: indices_regulares.append(i)

	print "Lista de buenos (tamano " + str(len(indices_buenos)) + ")"
	print indices_buenos
	print "Lista de regulares (tamano " + str(len(indices_regulares)) + ")"
	print indices_regulares

	# Se crea una nueva lista dependiendo de la descendencia de los buenos y los 			regulares
	Personas_nuevas =[]
	for i in indices_buenos:
	    Personas_nuevas.append(Personas[i])
	    Personas_nuevas.append(Personas[i])

	print "tamano de los nuevos buenos: " + str(len(Personas_nuevas))

	for i in indices_regulares:
	    Personas_nuevas.append(Personas[i])
	print "Tamano de los nuevos regulares: " + str(len(Personas_nuevas))

	if len(Personas_nuevas)<=20:
	    Personas = Personas_nuevas
	    x = 20 - len(Personas)
	    for i in range(x):
		Personas.append(Jugadores(0, uniform(0,1),uniform(0,1)))
	else:
		Personas = Personas_nuevas[:20]

Scores =[]
Boldness_1 =[]
Vengefulness_1 = []
