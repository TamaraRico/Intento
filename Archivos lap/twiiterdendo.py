# -*- coding: utf-8 -*-
import os
import tweepy as tw
import pandas as pd
import json
import csv
from matplotlib import pyplot as plt
from scipy.cluster import hierarchy
import numpy as np

consumer_key= "jfeq9Y0DorR0RnOFn92393Qbb"
consumer_secret= "iYUk6r7xddcJaQ6kyXVTM6HDX22mBKViu3VGQ3Fy1nNexHxYLo"
access_token= "1313220507223744512-USHklyLV9FiYdkABMnqXJoMdHQik21"
access_token_secret="jsdzm4g8NYxvGNdd2RiDwj6Bg2kPH9JCaDQbZ1w89lqfL"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
# tabla = {'bts_bighit':["0","0","0"], 'BTS_twt':["0","0","0"], 'BTS_ARMY':["0","0","0"], 'choi_bts2':["0","0","0"]}
# tabla = [["bts_bighit","0","0","0","0","0","0"], ["BTS_twt","0","0","0","0","0","0"], ["BTS_ARMY","0","0","0","0","0","0"], ["choi_bts2","0","0","0","0","0","0"]]
tabla = [["0","0","0","0","0","0"], ["0","0","0","0","0","0"], ["0","0","0","0","0","0"], ["0","0","0","0","0","0"]]
asiaLista =['Republic of the Philippines', 'Somewhere in Philippines', 'DKI Jakarta, Indonesia', 'Zamboanga City, Zamboanga Peni', 'Ibaraki-ken, Japan', 'Jombang, Jawa Timur', 'South Korean', 'Mumbai, India', 'Kalimantan Timur, Indonesia', 'Chittagong, Bangladesh', 'Papua Barat, Indonesia', 'Bengaluru South, India', 'Selangor, Malaysia', 'Davao City, Davao Region', 'Karachi, Pakistan']
americaLista = ['New Mexico, USA', 'Argentina ', 'Peru']
europaLista = ['Somewhere in the northen italy', 'Banyoles, Espa\xc3\xb1a']
africaLista = ['Cairo, Egypt']


cuentas = ['bts_bighit','BTS_twt','BTS_ARMY','choi_bts2']
datos =['followers','friends','asia', 'america', 'europa', 'africa']

for i in range(4):
  data = api.get_user(cuentas[i])
  tabla[i][0] = data.followers_count
  tabla[i][1] = data.friends_count
  # print(cuentas[i],"followers:", tabla[i][0], "friends:", tabla[i][1], "location", tabla[i][2])
  # print(json.dumps(data._json, indent=2))
  i = 0
  asia = 0
  america = 0
  europa = 0
  africa = 0
  for user in tw.Cursor(api.followers, screen_name=cuentas[i]).items(20):
    print((user.location).encode("utf-8"))
    if (((user.location).encode("utf-8")) in asiaLista):
      asia += 1
    elif (((user.location).encode("utf-8")) in europaLista):
      europa += 1
    elif (((user.location).encode("utf-8")) in americaLista):
      america += 1
    elif (((user.location).encode("utf-8")) in africaLista):
      africa += 1
  tabla[i][2] = str(asia)
  tabla[i][3] = str(america)
  tabla[i][4] = str(europa)
  tabla[i][5] = str(africa)
    

tabla.insert(0,datos)

print(tabla)

myFile = open('Blackpink.csv','w')
with myFile:
  writer = csv.writer(myFile)
  writer.writerows(tabla)

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