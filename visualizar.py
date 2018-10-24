#-*- coding: utf-8 -*-
print("Importando paquetes...")
import pandas as pd
import matplotlib.pyplot as plt
import sys
print("Listo!")

print("Leyendo datos...")
df = pd.read_csv('datos.csv')
print(df[:3])

# Organiza el DataFrame por experimento y por generacion
df = df.sort_values(['Experimento','Generacion'], ascending=[True, True])

print(u"Obteniendo promedios última generación...")

aux = []
for key, grp in df.groupby('Experimento'):
    ultimaGeneracion = grp.Generacion.unique()[-1]
    # print(grp.groupby('Generacion').get_group(ultimaGeneracion)['Score'].mean())
    dict = {}
    dict['Experimento'] = key
    dict['meanScore'] = grp.groupby('Generacion').get_group(ultimaGeneracion)['Score'].mean()
    dict['meanBoldness'] = grp.groupby('Generacion').get_group(ultimaGeneracion)['Boldness'].mean()
    dict['meanVengefulness'] = grp.groupby('Generacion').get_group(ultimaGeneracion)['Vengefulness'].mean()
    aux.append(dict)

data = pd.DataFrame(aux)

print(data)

fig, ax = plt.subplots()

data[['meanBoldness', 'meanVengefulness']].plot(kind='scatter', x='meanBoldness', y='meanVengefulness',  ax=ax)

fig.savefig('prueba.pdf')

sys.exit()

for label, grp in df.groupby('Experimento'):
    grp.groupby('Generacion')['Score'].mean().plot(ax=ax, label=label)

fig.savefig('prueba.pdf')

# for g in grpExp:
#     aux = pd.DataFrame(grpExp.get_group(g))
#     promedio = aux.groupby('Generacion').get_group(ultimaGeneracion)['Score'].mean()
#     print("Promedio: ", promedio)
