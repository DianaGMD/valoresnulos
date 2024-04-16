import pandas as pd
import numpy as np
df=pd.read_csv("ventas_totales.csv")
df.head()
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())

#Quitar nulos en columna salon ventas
df['salon_ventas'] = df['salon_ventas'].fillna(round(df['salon_ventas'].mean(),1))
#valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Quitar valores nulos de columna tarjeta debito, sustituimos con mediana
df['tarjetas_debito'] = df['tarjetas_debito'].fillna(round(df['tarjetas_debito'].median(),1))
#valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Quitar nulos de columna tarjeta de credito
df['tarjetas_credito'] = df['tarjetas_credito'].fillna(round(df['tarjetas_credito'].median(),1))
#valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Quitar valor nulo con un valor númerico en la columna otros medios
print(df['otros_medios'].describe())
df['otros_medios']=df['otros_medios'].fillna(6922148.759)
#valores_nulos=df.isnull().sum()
#print(valores_nulos)

#ffill En subtotal de alimentos y bebidas decidí rellenarlo con los valores no nulos hacía adelante. Ya que son 10 valores nulos y así pueden ser sustituidos con valores anteriores
df['subtotal_ventas_alimentos_bebidas'] =df['subtotal_ventas_alimentos_bebidas'].fillna(method='ffill')
#valores_nulos=df.isnull().sum()
#print(valores_nulos)

#bfill
df['almacen'] =df['almacen'].fillna(method='bfill')
#valores_nulos=df.isnull().sum()
#print(valores_nulos)

#sustituir el nulo con 0
df['panaderia'] =df['panaderia'].fillna(0)
valores_nulos=df.isnull().sum()
print(valores_nulos)

#Convertir DataFrame a CSV
df.to_csv('Ventas_totales_limpio.csv')
     

