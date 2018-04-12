from random import uniform
from random import randint

class Jugadores():
    def __init__(self, S, B, V):
        self.Score = S
        self.Boldness = B
        self.Vengefulness = V

def Imprimir_Jugador(j, Personas):
    print "Score: " + str(Personas[j].Score)
    print "Boldness: " + str(Personas[j].Boldness)
    print "Vengefulness: " + str(Personas[j].Vengefulness)



Personas = []

for i in range(0,20):
    Personas.append(Jugadores(0, uniform(0,1),uniform(0,1)))


Imprimir_Jugador(19, Personas)

for j in Personas:
    s = uniform(0,1)
    b = j.Boldness
    if s<b:
        print(Personas[j].Score)
        Personas[j].Score +=3
        print(Personas[j].Score)
        for y in Personas and y!=j:
            Personas[y].Score += -1
            print(Personas[y].Score)
