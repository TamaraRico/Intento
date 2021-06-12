from geopy.geocoders import Nominatim
import pandas as pd
import pylab 
import networkx as nx
import pickle


geolocator = Nominatim(user_agent="Nominatim")

cantProductos = {'ems': 0, 'trafico': 0, 'fire': 0}

filtro = pd.read_excel('911.xls')
i = 0
direcciones = []
incidentestipo = []
while (i < filtro.shape[0]):
  tipo = filtro['title'][i]
  raw = (geolocator.reverse(str(filtro['lat'][i])+','+str(filtro['lng'][i]))).raw
  try:
    direcciones.append(raw['address']['city'])
  except:
   direcciones.append("???")
  
  if tipo[:4] == 'EMS:':
    cantProductos['ems'] += 1
    incidentestipo.append('EMS')
  elif tipo[:5] == 'Fire:':
    incidentestipo.append('Fire')
    cantProductos['fire'] += 1
  elif tipo[:8] == 'Traffic:':
    incidentestipo.append('Traffic')
    cantProductos['trafico'] += 1
  i += 1
  print(i)

for i in range(len(direcciones)):
  direcciones[i] = direcciones[i].replace(" ","")

arch = open("soda.txt", "w")
for i in range(len(direcciones)):
  arch.write(incidentestipo[i] + " " + direcciones[i])
  arch.write("\n")
arch.close()

G=nx.read_weighted_edgelist('soda.txt', create_using=nx.MultiGraph())

custom_node_color={}
custom_node_color['0'] = 'black'

nx.draw(G, with_labels = True, node_size = [G.degree(i) * 35 for i in G.nodes()])

#Archivo con el dato del promedio del grado de clusterizacion por nodo

avg_node_degree = nx.average_neighbor_degree(G)
vString = str(avg_node_degree)

pylab.show()
