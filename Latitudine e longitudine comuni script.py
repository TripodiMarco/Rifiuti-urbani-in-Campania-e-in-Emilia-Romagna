import pandas as pd
import numpy as np
from geopy.geocoders import ArcGIS


df = pd.read_csv('Comuni Emilia-Romagna.csv', index_col="COMUNE")
df = df.drop("Stato", axis=1)
df = df.drop("Regione", axis=1)
df["Latitudine"]=np.nan
df["Longitudine"]=np.nan


comuni = ArcGIS()
for comune, provincia in zip(df.index,df["PROVINCIA"]):
    latitudine = comuni.geocode(f"{comune}, {provincia}, Italia").latitude
    longitudine = comuni.geocode(f"{comune}, {provincia}, Italia").longitude
    df.loc[comune, "Latitudine"] = latitudine
    df.loc[comune, "Longitudine"] = longitudine
df = df.drop("PROVINCIA", axis=1)
df.to_csv("Latitudine e longitudine comuni Emilia-Romagna.csv")

