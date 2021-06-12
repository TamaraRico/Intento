#Liberías necesarias para el dendograma
import plotly.figure_factory as ff
import pandas as pd
import numpy as np
import os

#Acceso al archivo con la base de datos
filepath = str(os.path.dirname(os.path.realpath(__file__))) + "\\Datos911.csv"

#Dendograma para la distribución de los tipos de emergencias en cada ciudad 
X = pd.read_csv(filepath)
X.rename(columns={X.columns[0]:"# of incidents"}, inplace= True)
X.set_index("# of incidents")
X.replace(np.nan, 0, inplace= True)
incidentes = list(X["# of incidents"])
del X["# of incidents"]
#del X["Origin"]

#CREACION DEL DENDOGRAMA 
fig = ff.create_dendrogram(X, labels=incidentes)
fig.update_layout(autosize=False, width=1000, height=800)
fig.show()