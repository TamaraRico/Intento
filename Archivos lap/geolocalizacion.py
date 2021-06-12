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
G.add_node('Horsham', pos=(40.1821, -75.1479.), score=9, ems=5)
G.add_node('East Greenville', pos=(40.4058, -75.5061), score=3, ems=1)
G.add_node('Abington', pos=(40.1238, -75.1148), score=25, ems=14)
G.add_node('Pottstown', pos=(40.2506,-75.6435 ), score=13, ems=9)
G.add_node('Ambler', pos=( 40.1564, -75.2214), score=3, ems=3)
G.add_node('Jenkintown', pos=(40.098, -75.1078), score=2, ems=1)
G.add_node('Skippack', pos=(40.210846, -75.4397957), score=2, ems=2)
G.add_node('Upper Merion', pos=(40.1025527, -75.3678382), score=8, ems=15)
G.add_node('Whitpain', pos=(40.1552833, -75.2642296), score=5, ems=3)
G.add_node('Lower Salford', pos=(40.2890267	-75.3995896), score=4, ems=2)
G.add_node('Plymouth', pos=(40.1023985	-75.2914577), score=11, ems=1)
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
G.add_node('Chile', pos=(-35.675147, -71.542969), score=6.444, GPD_per_capita=1.159, ss=1.369, healthy_life=0.92, freedom=0.357, generosity=0.187, corruption=0.056)
G.add_node('Guatemala', pos=(15.783471, -90.230759), score=6.436, GPD_per_capita=0.8, ss=1.269, healthy_life=0.746, freedom=0.535, generosity=0.175, corruption=0.078)
G.add_node('Saudi Arabia', pos=(24.2669, 45.1078), score=6.375, GPD_per_capita=1.403, ss=1.357, healthy_life=0.795, freedom=0.439, generosity=0.08, corruption=0.132)
G.add_node('Qatar', pos=(25.3271, 51.1967), score=6.374, GPD_per_capita=1.684, ss=1.313, healthy_life=0.871, freedom=0.555, generosity=0.22, corruption=0.167)
G.add_node('Spain', pos=(40.463667, -3.74922), score=6.354, GPD_per_capita=1.256, ss=1.484, healthy_life=1.062, freedom=0.362, generosity=0.153, corruption=0.079)
G.add_node('Panama', pos=(8.537981, -80.782127), score=6.321, GPD_per_capita=1.149, ss=1.442, healthy_life=0.91, freedom=0.516, generosity=0.109, corruption=0.054)
G.add_node('Brazil', pos=(14.2350, 51.9253), score=6.3, GPD_per_capita=1.004, ss=1.439, healthy_life=0.802, freedom=0.39, generosity=0.099, corruption=0.086)
G.add_node('Uruguay', pos=(-32.522779, -55.765835), score=6.293, GPD_per_capita=1.124, ss=1.465, healthy_life=0.891, freedom=0.523, generosity=0.127, corruption=0.15)
G.add_node('Singapore', pos=(1.290270, 103.851959), score=6.262, GPD_per_capita=1.572, ss=1.463, healthy_life=1.141, freedom=0.556, generosity=0.271, corruption=0.453)
G.add_node('El Salvador', pos=(13.794185, -88.89653), score=6.253, GPD_per_capita=0.794, ss=1.242, healthy_life=0.789, freedom=0.43, generosity=0.093, corruption=0.074)
G.add_node('Italy', pos=(41.8719, 12.5674), score=6.223, GPD_per_capita=1.294, ss=1.488, healthy_life=1.039, freedom=0.253, generosity=0.158, corruption=0.03)
G.add_node('Bahrain', pos=(25.9434, 50.6015), score=6.199, GPD_per_capita=1.362, ss=1.368, healthy_life=0.871, freedom=0.536, generosity=0.255, corruption=0.11)
G.add_node('Slovakia', pos=(48.6737532, 19.696058), score=6.198, GPD_per_capita=1.246, ss=1.504, healthy_life=0.881, freedom=0.334, generosity=0.121, corruption=0.014)
G.add_node('Trinidad & Tobago', pos=(10.536421, -61.311951), score=6.192, GPD_per_capita=1.231, ss=1.477, healthy_life=0.713, freedom=0.489, generosity=0.185, corruption=0.016)
G.add_node('Poland', pos=(51.9189, 19.1344), score=6.182, GPD_per_capita=1.206, ss=1.438, healthy_life=0.884, freedom=0.483, generosity=0.117, corruption=0.05)
G.add_node('Uzbekistan', pos=(41.3812, 64.5736), score=6.174, GPD_per_capita=0.745, ss=1.529, healthy_life=0.756, freedom=0.631, generosity=0.322, corruption=0.24)
G.add_node('Lithuania', pos=(55.1736, 23.8948), score=6.149, GPD_per_capita=1.238, ss=1.515, healthy_life=0.818, freedom=0.291, generosity=0.043, corruption=0.042)
G.add_node('Colombia', pos=(4.570868, -74.297333), score=6.125, GPD_per_capita=0.985, ss=1.41, healthy_life=0.841, freedom=0.47, generosity=0.099, corruption=0.034)
G.add_node('Slovenia', pos=(46.1492, 14.9860), score=6.118, GPD_per_capita=1.258, ss=1.523, healthy_life=0.953, freedom=0.564, generosity=0.144, corruption=0.057)
G.add_node('Nicaragua', pos=(12.865416, -85.207229), score=6.105, GPD_per_capita=0.694, ss=1.325, healthy_life=0.835, freedom=0.435, generosity=0.2, corruption=0.127)
G.add_node('Kosovo', pos=(42.6639, 21.0961), score=6.1, GPD_per_capita=0.882, ss=1.232, healthy_life=0.758, freedom=0.489, generosity=0.262, corruption=0.006)
G.add_node('Argentina', pos=(-38.416097, -63.616672), score=6.086, GPD_per_capita=1.092, ss=1.432, healthy_life=0.881, freedom=0.471, generosity=0.066, corruption=0.05)
G.add_node('Romania', pos=(45.9443, 25.0094), score=6.07, GPD_per_capita=1.162, ss=1.232, healthy_life=0.825, freedom=0.462, generosity=0.083, corruption=0.005)
G.add_node('Cyprus', pos=(35.095192, 33.203430), score=6.046, GPD_per_capita=1.263, ss=1.223, healthy_life=1.042, freedom=0.406, generosity=0.19, corruption=0.41)
G.add_node('Ecuador', pos=(-1.7929665, -78.1368875), score=6.028, GPD_per_capita=0.912, ss=1.312, healthy_life=0.868, freedom=0.498, generosity=0.126, corruption=0.087)

score = nx.get_node_attributes(G, 'score')
ems= nx.get_node_attributes(G, 'ems')

G.nodes(data=True)

node_color = [float(ems[v]) for v in G]
node_size = [float(score[v]) for v in G]

vmin, vmax = min(node_color), max(node_color)
cmap = plt.cm.rainbow
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
#cmap = plt.cm.rainbow

nx.draw(G, nx.get_node_attributes(G, 'pos'), font_size=3, with_labels=False, node_size=node_size,
        edge_cmap=cmap)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(node_color))
sm._A = []
plt.colorbar(sm)
plt.show()
