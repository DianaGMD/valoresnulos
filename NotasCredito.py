import pandas as pd
df = pd.read_excel('notas_credito.xlsx')
print(df.head())

def rellenar_valores_faltantes(df):
    # Valores nulos 
    #'CVE_VEND' con "Sin Asignar"
    df['CVE_VEND'].fillna("Sin Asignar", inplace=True)

    # 'CVE_PEDI' con "No disponible"
    df['CVE_PEDI'].fillna("No disponible", inplace=True)

    # 'FECHA_CANCELA' con "No cancelado"
    df['FECHA_CANCELA'].fillna("No cancelado", inplace=True)

    return df
df = rellenar_valores_faltantes(df)

df.to_csv('notas_credito_limpiado.csv', index=False)
print("\nLimpieza de valores nulos:")
print(df.info())
print(df.head())