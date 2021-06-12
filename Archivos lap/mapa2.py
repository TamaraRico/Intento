import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv ('911.csv')
BBox = (df.lng.min(), df.lng.max(),df.lat.min(), df.lat.max())       


ruh_m = plt.imread ('map.png')
fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(df.lng, df.lat, zorder=1, alpha= 1, c='b', s=10)
ax.set_title('Incidentes del 911 en Pensilvania')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')
plt.show()