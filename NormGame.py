#-*- coding: utf-8 -*-
from random import uniform
from random import randint
import numpy as np
class Jugadores():
    def __init__(self, S, B, V):
        self.Score = S
        self.Boldness = B
        self.Vengefulness = V

def Imprimir_Jugador(j, Personas):
    print("Score: " + str(Personas[j].Score))
    print("Boldness: " + str(Personas[j].Boldness))
    print("Vengefulness: " + str(Personas[j].Vengefulness))

Personas = []
Scores =[]
for i in range(0,20):
    Personas.append(Jugadores(0, uniform(0,1),uniform(0,1)))
def Inicializar(Poblacion):
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
Inicializar(Personas)

for j in range(0,20):                            
    Imprimir_Jugador(j, Personas)

def Anadir_scores():
    for u in Personas:
        Scores.append(float(u.Score))
    


Anadir_scores()
print(Scores)
mean = np.mean(Scores)

std_deviation = np.std(Scores)
print(std_deviation)

Personas_2 = []
for i in Personas:
    if ((i.Score-mean)/std_deviation)<1:
        for u in range(0,1):
            Personas_2.append(Jugadores(0, uniform(0,1),uniform(0,1)))
    elif ((i.Score-mean)/std_deviation)<1 and ((i.Score-mean)/std_deviation)> -1:
        Personas_2.append(Jugadores(0, uniform(0,1),uniform(0,1)))



print(len(Personas_2))
