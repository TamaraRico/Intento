#!/usr/bin/python
# -*- coding: utf-8 -*-
# from pylab import figure
# from mpl_toolkits.basemap import Basemap
import pylab
import networkx as nx
import pickle
import matplotlib.pyplot as plt
from random import randint
import scipy
import numpy as np
import math

G = nx.Graph()
# AGEB

G.add_node('Lower Merion', pos=(40.0096, 75.28), score=21, ems=10)
G.add_node('Montgomery', pos=(32.36681, -86.29997), score=11, ems=11) 
G.add_node('Norristown', pos=( 40.1226,-75.3396), score=22, ems=21)
G.add_node('Horsham', pos=(40.1821, -75.1479), score=9, ems=5)
G.add_node('East Greenville', pos=(40.4058, -75.5061), score=3, ems=1)
G.add_node('Abington', pos=(40.1238, -75.1148), score=25, ems=14)
G.add_node('Pottstown', pos=(40.2506,-75.6435 ), score=13, ems=9)
G.add_node('Ambler', pos=( 40.1564, -75.2214), score=3, ems=3)
G.add_node('Jenkintown', pos=(40.098, -75.1078), score=2, ems=1)
G.add_node('Skippack', pos=(40.210846, -75.4397957), score=2, ems=2)
G.add_node('Upper Merion', pos=(40.1025527, -75.3678382), score=8, ems=15)
G.add_node('Whitpain', pos=(40.1552833, -75.2642296), score=5, ems=3)
G.add_node('Lower Salford', pos=(40.2890267, -75.3995896), score=4, ems=2)
G.add_node('Plymouth', pos=(40.1023985, -75.2914577), score=11, ems=1)
G.add_node('Upper Moreland', pos=(40.1741312, -75.0984907), score=10, ems=4)
G.add_node('Cheltenham', pos=(40.062974, -75.135914), score=13, ems=4)
G.add_node('Lansdale', pos=(40.2432578, -75.2865516), score=9, ems=6)
G.add_node('New Hanover', pos=(40.3121807, -75.5742598), score=1, ems=1)
G.add_node('West Norriton', pos=(40.123193, -75.3829629), score=7, ems=4)
G.add_node('Whitemarsh', pos=(40.1098315, -75.2719513), score=6, ems=1)
G.add_node('Limerick', pos=(40.2149774, -75.4997122), score=15, ems=7)
G.add_node('Lower Moreland', pos=(40.1430862, -75.0605932), score=6, ems=4)
G.add_node('Towamencin', pos=(40.2497608, -75.3484526), score=4, ems=3)
G.add_node('Upper Providence', pos=(40.1795657, -75.5273502), score=7, ems=3)
G.add_node('Springfield', pos=(40.1049255, -75.2132496), score=3, ems=1)
G.add_node('Hatfield Township', pos=(40.2984302, -75.2841346), score=4, ems=0)
G.add_node('Lower Pottsgrove', pos=(40.249191, -75.5909541), score=4, ems=1)
G.add_node('Upper Gwynedd', pos=(40.2074035, -75.3137919), score=3, ems=2)
G.add_node('Perkiomen', pos=(40.2255371, -75.4716175), score=1, ems=1)
G.add_node('Lower Providence', pos=(40.156807, -75.4423234), score=9, ems=7)
G.add_node('Conshohocken', pos=(40.0817953, -75.2996401), score=3, ems=2)
G.add_node('North Wales', pos=(40.2109404, -75.2782317), score=2, ems=2)
G.add_node('Douglass', pos=(40.3082416, -75.6006932), score=3, ems=2)
G.add_node('Souderton', pos=(40.3071113, -75.3230319), score=3, ems=1)
G.add_node('Lower Gwynedd', pos=(40.2020579, -75.2554801), score=6, ems=3)
G.add_node('Upper Dublin', pos=(40.116985, -75.1694856), score=6, ems=4)
G.add_node('Royersford', pos=(40.1876645, -75.532277), score=3, ems=1)
G.add_node('Telford', pos=(40.3309982, -75.3304253), score=2, ems=2)
G.add_node('West Conshohocke', pos=(40.0700952, -75.3178667), score=1, ems=1)
G.add_node('Hatboro', pos=(40.188666, -75.1007192), score=2, ems=1)
G.add_node('Red Hill', pos=(40.3760733, -75.4870743), score=1, ems=1)
G.add_node('Lower Frederick', pos=(40.2750408, -75.476455), score=4, ems=0)
G.add_node('Bridgeport', pos=(40.105308, -75.341987), score=2, ems=2)
G.add_node('East Norriton', pos=(40.1280087, -75.3181112), score=6, ems=4)
G.add_node('Bryn Athyn', pos=(40.1317717, -75.0582548), score=2, ems=0)
G.add_node('Collegeville', pos=(40.1930534, -75.4623315), score=2, ems=2)
G.add_node('Franconia', pos=(40.2927598, -75.3230399), score=2, ems=1)
G.add_node('Delaware county', pos=(40.0252992, -75.3365305), score=1, ems=0)
G.add_node('Upper Hanover', pos=(40.4106035, -75.4736714), score=1, ems=1)

score = nx.get_node_attributes(G, 'score')
ems= nx.get_node_attributes(G, 'ems')

G.nodes(data=True)


node_color = [float(ems[v]) for v in G]
node_size = [float(score[v]) for v in G] 

vmin, vmax = min(node_color), max(node_color)

cmap = plt.cm.rainbow
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
cmap = plt.cm.rainbow

nx.draw(G, nx.get_node_attributes(G, 'pos'), font_size=3, with_labels=False, node_size=node_size,
        edge_cmap=cmap)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(node_color))
sm._A = []
plt.colorbar(sm)
plt.show()
