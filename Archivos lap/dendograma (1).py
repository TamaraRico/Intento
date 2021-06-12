import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

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
width = 0.1

fig, ax = plt.subplots()

#Generamos las barras para el conjunto de hombres
barraproductos = ax.bar(x, cantProductos.values(), width, label='Ventas')
#Generamos las barras para el conjunto de mujeres



#Añadimos las etiquetas de identificacion de valores en el grafico
ax.set_ylabel('Accidentes por categoria')
ax.set_title('Aciddentes')
ax.set_xticks(x)
ax.set_xticklabels(productos)
#Añadimos un legen() esto permite mmostrar con colores a que pertence cada valor.
ax.legend()



def autolabel(rects):
    """Funcion para agregar una etiqueta con el valor en cada barra"""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

#Añadimos las etiquetas para cada barra
autolabel(barraproductos)


fig.tight_layout()
# plt.savefig('GraficasDiarias/'+fecha+'.png')
#Mostramos la grafica con el metodo show()
plt.show()

