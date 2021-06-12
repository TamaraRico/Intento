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

G.add_node('Finland', pos=(64.9417, 26.0673), score=7.769, GPD_per_capita=1.34, healthy_life=0.986, freedom=0.596, generosity=0.153, corruption=0.393)
G.add_node('Denmark', pos=(55.9397, 9.5156), score=7.6, GPD_per_capita=1.383, ss=1.573, healthy_life=0.996, freedom=0.592, generosity=0.252, corruption=0.41)
G.add_node('Norway', pos=(60.472, 8.4689), score=7.554, GPD_per_capita=1.488, ss=1.582, healthy_life=1.028, freedom=0.603, generosity=0.271, corruption=0.341)
G.add_node('Iceland', pos=(64.9312762, 19.0211697), score=7.494, GPD_per_capita=1.38, ss=1.624, healthy_life=1.026, freedom=0.591, generosity=0.354, corruption=0.118)
G.add_node('Netherlands', pos=(52.2130, 5.2794), score=7.488, GPD_per_capita=1.396, ss=1.522, healthy_life=0.999, freedom=0.557, generosity=0.322, corruption=0.298)
G.add_node('Switzerland', pos=(46.8182, 8.2275), score=7.48, GPD_per_capita=1.452, ss=1.526, healthy_life=1.052, freedom=0.572, generosity=0.263, corruption=0.343)
G.add_node('Sweden', pos=(60.1282, 18.6435), score=7.343, GPD_per_capita=1.387, ss=1.487, healthy_life=1.009, freedom=0.574, generosity=0.267, corruption=0.373)
G.add_node('New Zealand', pos=(-43.3745, 172.4663), score=7.307, GPD_per_capita=1.303, ss=1.557, healthy_life=1.026, freedom=0.585, generosity=0.33, corruption=0.38)
G.add_node('Canada', pos=(56.130366, -106.346771), score=7.278, GPD_per_capita=1.365, ss=1.505, healthy_life=1.039, freedom=0.584, generosity=0.285, corruption=0.308)
G.add_node('Austria', pos=(47.6965, 13.3457), score=7.247, GPD_per_capita=1.376, ss=1.475, healthy_life=1.016, freedom=0.532, generosity=0.244, corruption=0.226)
G.add_node('Australia', pos=(-25.274398, 133.775136), score=7.228, GPD_per_capita=1.372, ss=1.548, healthy_life=1.036, freedom=0.557, generosity=0.332, corruption=0.29)
G.add_node('Costa Rica', pos=(9.748917, -83.753428), score=7.167, GPD_per_capita=1.034, ss=1.441, healthy_life=0.963, freedom=0.558, generosity=0.144, corruption=0.093)
G.add_node('Israel', pos=(31.7833, 35.2167), score=7.139, GPD_per_capita=1.276, ss=1.455, healthy_life=1.029, freedom=0.371, generosity=0.261, corruption=0.082)
G.add_node('Luxembourg', pos=(49.611622, 6.131935), score=7.09, GPD_per_capita=1.609, ss=1.479, healthy_life=1.012, freedom=0.526, generosity=0.194, corruption=0.316)
G.add_node('United Kingdom', pos=(55.378051, -3.435973), score=7.054, GPD_per_capita=1.333, ss=1.538, healthy_life=0.996, freedom=0.45, generosity=0.348, corruption=0.278)
G.add_node('Ireland', pos=(53.1424, 7.6921), score=7.021, GPD_per_capita=1.499, ss=1.553, healthy_life=0.999, freedom=0.516, generosity=0.298, corruption=0.31)
G.add_node('Germany', pos=(51.1657, 10.4515), score=6.985, GPD_per_capita=1.373, ss=1.454, healthy_life=0.987, freedom=0.495, generosity=0.261, corruption=0.265)
G.add_node('Belgium', pos=(50.5011, 4.4765), score=6.923, GPD_per_capita=1.356, ss=1.504, healthy_life=0.986, freedom=0.473, generosity=0.16, corruption=0.21)
G.add_node('United States', pos=(37.09024, -95.712891), score=6.892, GPD_per_capita=1.433, ss=1.457, healthy_life=0.874, freedom=0.454, generosity=0.28, corruption=0.128)
G.add_node('Czech Republic', pos=(49.8038, 15.4749), score=6.852, GPD_per_capita=1.269, ss=1.487, healthy_life=0.92, freedom=0.457, generosity=0.046, corruption=0.036)
G.add_node('United Arab Emirates', pos=(24.3506, 53.9396), score=6.825, GPD_per_capita=1.503, ss=1.31, healthy_life=0.825, freedom=0.598, generosity=0.262, corruption=0.182)
G.add_node('Malta', pos=(35.917973, 35.917973), score=6.726, GPD_per_capita=1.3, ss=1.52, healthy_life=0.999, freedom=0.564, generosity=0.375, corruption=0.151)
G.add_node('Mexico', pos=(23.634501, -102.552784), score=6.595, GPD_per_capita=1.07, ss=1.323, healthy_life=0.861, freedom=0.433, generosity=0.074, corruption=0.073)
G.add_node('France', pos=(46.7111, 1.7191), score=6.592, GPD_per_capita=1.324, ss=1.472, healthy_life=1.045, freedom=0.436, generosity=0.111, corruption=0.183)
G.add_node('Taiwan', pos=(23.5531, 121.0211), score=6.446, GPD_per_capita=1.368, ss=1.43, healthy_life=0.914, freedom=0.351, generosity=0.242, corruption=0.097)
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
GDP = nx.get_node_attributes(G, 'GDP_per_capita')
ss = nx.get_node_attributes(G, 'ss')
healthy_life = nx.get_node_attributes(G, 'healthy_life')
freedom = nx.get_node_attributes(G, 'generosity')
corruption = nx.get_node_attributes(G, 'corruption')
G.nodes(data=True)

node_color = [float(GDP[v]) for v in G]
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









