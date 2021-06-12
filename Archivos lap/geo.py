#!/usr/bin/python
# -*- coding: utf-8 -*-
#from pylab import figure
#from mpl_toolkits.basemap import Basemap
import pylab 
import networkx as nx
import pickle
import matplotlib.pyplot as plt
from random import randint
import scipy
import numpy as np
import math

G = nx.Graph()
#AGEB

#G.add_node('Playas de Rosarito', pos= (1170322,	322032), population=	65278, escolaridad =8.8, pea=27850)

G.add_node('Lower Merion', pos=(40.0096, 75.28), score=21, ems=10)
G.add_node('Montgomery', pos=(32.36681, -86.29997), score=11, ems=11) 
G.add_node('Norristown', pos=( 40.1226,-75.3396), score=22, ems=21)
G.add_node('Horsham', pos=(40.1821, -75.1479), score=9, ems=5)
G.add_node('East Greenville', pos=(40.4058, -75.5061), score=3, ems=1)
G.add_node('Abington', pos=(40.1238, -75.1148), score=25, ems=14)
G.add_node('Pottstown', pos=(40.2506,-75.6435 ), score=13, ems=9)
G.add_node('Ambler', pos=( 40.1564, -75.2214), score=3, ems=3)


score=nx.get_node_attributes(G,'score')
ems=nx.get_node_attributes(G,'ems')
#pea=nx.get_node_attributes(G,'pea')

G.nodes(data=True)

node_color=[float(score[v]) for v in G]
node_size=[float(ems[v]) for v in G]



cmap = plt.cm.rainbow
nx.draw(G, nx.get_node_attributes(G,'pos'), font_size=10, with_labels=False, node_size=node_size, node_color=node_color, edge_cmap=cmap)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(node_color))
sm._A = []
plt.colorbar(sm)
plt.show()

# nx.draw(H1, nx.get_node_attributes(H1, 'pos'), node_color='b', edge_color='blue', node_size=60, font_size=8, with_labels=False)
# nx.draw(H2, nx.get_node_attributes(H2, 'pos'), node_color='g', node_size=30,edge_color='green',  font_size=8, with_labels=False)
# nx.draw(H3, nx.get_node_attributes(H3, 'pos'), node_color='y', node_size=90, edge_color='yellow',font_size=8, with_labels=False)

# pylab.show()




 



