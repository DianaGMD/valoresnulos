import pandas as pd

df = pd.read_excel('precios_productos.xlsx')
print(df.head())

def rellenar_valores_faltantes(df):
    df['NOMBRE_VENDEDOR'].fillna("Sin Asignar", inplace=True)
    return df

df = rellenar_valores_faltantes(df)
df.to_csv('precio_productos_tratado(limpio).csv', index=False)
print("\nLimpieza de valores nulos:")
print(df.info())
print(df.head())