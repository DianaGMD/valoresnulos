import pandas as pd
import numpy as np
df=pd.read_csv("ventas_totales.csv")
df.head()
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())

#Quitar nulos en columna salon ventas
df['salon_ventas'] = df['salon_ventas'].fillna(round(df['salon_ventas'].mean(),1))
valores_nulos=df.isnull().sum()
print(valores_nulos)

