from random import uniform
from random import randint
class Jugadores():
    def __init__(self, S, B, V):
        self.Score = S
        self.Boldness = B
        self.Vengefulness = V



Personas = []

for i in range(0,21):
    Personas.append(Jugadores(0, uniform(0,1),uniform(0,1)))


for j in Personas:
    s = uniform(0,1)
    b = Personas[j].Boldness
    if s<b:
        print(Personas[j].Score)
        Personas[j].Score +=3
        print(Personas[j].Score)
        for y in Personas and y!=j:
            Personas[y].Score += -1
            print(Personas[y].Score)





       


