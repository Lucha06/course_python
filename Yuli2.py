#importamos librerias
import pandas as pd
import geopandas as gp
# Trabajamos con la libreria pysal
from pysal.model.spint import Gravity, Production, Attraction, Doubly


base1 = gp.read_file('C:\Users\lucer\OneDrive\SEMESTRE 2024A\Matriz.xlsx')
base1.plot()
base2 = pd.read_csv('C:\Users\lucer\OneDrive\SEMESTRE 2024A\Matriz.csv')
print(base2.head())

# # Creamos un arreglo de vectores para el formato de nuestra baseenv
# base2 = base2[base2['Origen'] != base2['Destino']]
#
# flujos = base2['Data'].values
# oi = base2['oi'].values
# dj = base2['dj'].values
# dij = base2['dij'].values
# Origen = base2['Origen'].values
# Destino = base2['Destino'].values
#
#
#
# # creamos un modelo basico de gravitacion sin restringir
#
# mg = Gravity(flujos, oi, dj, dij, 'exp')
# print(mg.params)
#
# # creamos un modelo restringido para el origen
# mp = Production(flujos, Origen, dj, dij, 'exp')
# print (mp.params[-2:])
#
# # Creamos un modelo restringido para el destino
#
# ma = Attraction(flujos, Destino, oi, dij, 'exp')
# print(ma.params[-2:])
#
# # Construimos el modelo para ambos destino y origen
# mf = Doubly(flujos,Origen, Destino, dij, 'exp')
# print(mf.params[-1:])
#
# print(mp.params[-2:])
#
# # ajustamos el modelo para que sea una regression de poisson
#
# mg = Gravity(flujos, oi, dj, dij, 'exp')
# print(mg.params)