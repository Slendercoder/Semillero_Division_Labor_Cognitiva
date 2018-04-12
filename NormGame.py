from random import uniform
from random import randint

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

for i in range(0,20):
    Personas.append(Jugadores(0, uniform(0,1),uniform(0,1)))

for u in Personas:
    s = uniform(0,1)
    b = u.Boldness
    if s<b:
        u.Score +=3
        for y in Personas:
            if y!=u:
                y.Score += -1
                



