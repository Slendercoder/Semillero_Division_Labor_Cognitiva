#-*- coding: utf-8 -*-
print("Importando paquetes...")
import pandas as pd
print("Listo!")

print("Leyendo datos...")
df = pd.read_csv('datos.csv')
print(df[:3])

print(u"Encontrando promedios por generación...")

for grp, key in df.groupby('Experimento'):
    print(grp['Generacion'])
    # ultimaGeneracion = grp['Generacion'].unique()
    # print(u"La última generación es: ", ultimaGeneracion)
    aux = grp.get_group(ultimaGeneracion)
    promedio = aux.Score.mean()
    print("Promedio: ", promedio)
