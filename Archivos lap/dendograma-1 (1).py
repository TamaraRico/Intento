import plotly.figure_factory as ff
import pandas as pd
import numpy as np
import os


filepath = str(os.path.dirname(os.path.realpath(__file__))) + "\\dendo - Hoja 3.csv"

#DENDOGRAMA PARA LA CANTIDAD DE PERSONAS QUE HABLAN EL IDIOMA
X = pd.read_csv(filepath)
X.rename(columns={X.columns[0]:"Language"}, inplace= True)
X.set_index("Language")
X.replace(np.nan, 0, inplace= True)

languages = list(X["Language"])

del X["Language"]
#del X["Origin"]

#<------ USO DE PLOTLY ---------->

#CREACION DEL DENDOGRAMA DE IDIOMAS
fig = ff.create_dendrogram(X, labels=languages)
fig.update_layout(autosize=False, width=1220, height=800)
fig.show()