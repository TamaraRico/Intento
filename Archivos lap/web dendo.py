import pandas as pd

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

ciudades={'MONTGOMERY': 0, 'UPPER PROVIDENCE': 0, 'LOWER POTTSGROVE': 0, 'POTTSTOWN': 0}
filtro = pd.read_excel('911.xls')
i = 0
while (i < (filtro.shape[0])):
  tipo = filtro['title'][i]
  if tipo[:4] == 'MONTGOMERY:':
    cantProductos['MONTGOMERY'] += 1
  elif tipo[:5] == 'LOWER POTTSGROVE:':
    cantProductos['LOWER POTTSGROVE'] += 1
  elif tipo[:8] == 'LOWER POTTSGROVE:':
    cantProductos['LOWER POTTSGROVE'] += 1
  elif tipo[:] == 'POTTSTOWN:':
    cantProductos['POTTSTOWN'] += 1
  i += 1

accidentes = pd.DataFrame(cantProductos, ciudades)

from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, dendrogram

distanceMatrix = pdist(accidentes)
dend = dendrogram(linkage(distanceMatrix, method='complete'), 
              color_threshold=4, 
              leaf_font_size=10)