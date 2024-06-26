import pandas as pd
from pandas import Series, DataFrame
#Clientes
clientes_df = pd.read_excel('clientes.xlsx')
print(clientes_df.head())

# suma de nulos
print("\nSuma de valores nulos:")
print(clientes_df.isnull().sum())

def rellenar_valores_faltantes(df):
    # RFC Generico
    df['RFC'].fillna('XAXX010101000', inplace=True)
    
    # nulos de nombre por desconocido
    df['NOMBRE'].fillna('Desconocido', inplace=True)
    
    return df

if __name__ == "__main__":
    clientes_df = rellenar_valores_faltantes(clientes_df)
    

    clientes_df.to_csv('clientes_RFCNull.csv', index=False)
    print("\nInformación después de limpiar:")
    print(clientes_df.info())
    print(clientes_df.head())