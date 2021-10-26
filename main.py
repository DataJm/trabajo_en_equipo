import pandas as pd

# Necesitamos un archivo config.py donde venga
# la llave de la api
try:
    import gkey from config
except:
    print("Necesitas un archivo config.py con tu gkey")

datos = pd.DraFrame([1,2,3,4,5])

datos.to_csv("data_previa.csv")

print('Jesus Monroy')

print('aqui va el codigo')

import requests
# ups!
datos_api = requests.get("whatever").json()