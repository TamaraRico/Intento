# -*- coding: utf-8 -*-
import pandas as pd
import os
import json
import csv
from matplotlib import pyplot as plt
from scipy.cluster import hierarchy
#from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np

#del df.index.name


myFile = open('911.csv','w')
with myFile:
  writer = csv.writer(myFile)
  writer.writerows(tabla)

df = pd.read_csv("911.csv")
df = df.set_index('911 accidents')
# del df.index.name
df

# Calculate the distance between each sample
Z = hierarchy.linkage(df, 'ward')
print(Z)

# Plot with Custom leaves
hierarchy.dendrogram(Z, leaf_rotation=90, leaf_font_size=8, labels=df.index)
plt.axis('on')

#plt.title('Clasificacion de la redes respecto a su uso')
plt.xlabel('Accidentes')
plt.ylabel('Cantidad')
plt.show()


df = pd.read_csv("Blackpink.csv")
df = df.set_index('followers')
# del df.index.name
df

# Calculate the distance between each sample
Z = hierarchy.linkage(df, 'ward')
print(Z)

# Plot with Custom leaves
hierarchy.dendrogram(Z, leaf_rotation=90, leaf_font_size=8, labels=df.index)
plt.axis('on')

#plt.title('Clasificacion de la redes respecto a su uso')
plt.xlabel('seguidores')
plt.ylabel('Valores')
plt.show()
