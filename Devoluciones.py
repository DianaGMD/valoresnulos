import pandas as pd

df = pd.read_excel('devoluciones.xlsx')
print(df.head())

def rellenar_valores_faltantes(df):
    #Sustitucion de valores
    # 'CVE_VEND' con "Sin Asignar"
    df['CVE_VEND'].fillna("Sin Asignar", inplace=True)

    # 'CVE_PEDI' con "No disponible"
    df['CVE_PEDI'].fillna("No disponible", inplace=True)

    # 'FECHA_CANCELA' con "No cancelado"
    df['FECHA_CANCELA'].fillna("No cancelado", inplace=True)

    # 'DOC_ANT' con "No especificado"
    df['DOC_ANT'].fillna("No especificado", inplace=True)
    return df

df = rellenar_valores_faltantes(df)
df.to_csv('devoluciones_sinnull.csv', index=False)

print("\nLimpieza de valores nulos:")
print(df.info())
print(df.head())