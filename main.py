import pandas as pd

datos = pd.DraFrame([1,2,3,4,5])

datos.to_csv("data_previa.csv")


import requests


datos_api = requests.get("whatever").json()

