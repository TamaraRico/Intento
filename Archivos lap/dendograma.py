import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster import hierarchy

cantProductos = {'ems': 0, 'trafico': 0, 'fire': 0}

filtro = pd.read_excel('911.xls')
i = 0
while (i < (filtro.shape[0])):
  tipo = filtro['title'][i]
  if tipo[:4] == 'EMS:':
    cantProductos['ems'] += 1
  elif tipo[:5] == 'Fire:':
    cantProductos['fire'] += 1
  elif tipo[:8] == 'Traffic:':
    cantProductos['trafico'] += 1

  i += 1

productos = ['Emergencia Medica', 'Accidentes de trafico', 'Incendios']


#Obtenemos la posicion de cada etiqueta en el eje de X
x = np.arange(len(productos))
#tamaño de cada barra


df = pd.read_csv("Blackpink.csv")
df = df.set_index('followers')

#Generamos las barras para el conjunto de hombres
barraproductos = ax.bar(x, cantProductos.values(), width, label='Ventas')
#Generamos las barras para el conjunto de mujeres



# Calculate the distance between each sample
Z = hierarchy.linkage(df, 'ward')
print(Z)

# Plot with Custom leaves
hierarchy.dendrogram(Z, leaf_rotation=90, leaf_font_size=8, labels=df.index)
plt.axis('on')

#plt.title('Clasificacion de la redes respecto a su uso')
plt.xlabel('Accidentes')
plt.ylabel('Valores')
plt.show()
#Mostramos la grafica con el metodo show()


