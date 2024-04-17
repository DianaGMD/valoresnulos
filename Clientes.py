import pandas as pd
from pandas import Series, DataFrame
#Clientes
clientes_df = pd.read_excel('clientes.xlsx')
print(clientes_df.head())

# Verificando la suma de valores nulos por columna
print("\nSuma de valores nulos por columna:")
print(clientes_df.isnull().sum())

def fill_missing_values(df):
    # Sustituyendo valores nulos en la columna 'RFC' con el RFC genérico nacional 'XAXX010101000'
    df['RFC'].fillna('XAXX010101000', inplace=True)
    
    # Sustituyendo valores nulos en la columna 'NOMBRE' con 'Desconocido'
    df['NOMBRE'].fillna('Desconocido', inplace=True)
    
    return df

if __name__ == "__main__":
    # Llamando a la función para tratar valores nulos
    clientes_df = fill_missing_values(clientes_df)
    
    # Guardando el DataFrame limpio como un archivo CSV
    clientes_df.to_csv('clientes_clean.csv', index=False)
    
    # Mostrando información del DataFrame para confirmar que no hay valores nulos
    print("\nInformación después de limpiar:")
    print(clientes_df.info())
    print(clientes_df.head())