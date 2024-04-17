import pandas as pd
from pandas import Series, DataFrame
     
clientes = pd.read_excel('clientes.xlsx', index_col=0)
devoluciones = pd.read_excel('devoluciones.xlsx', index_col=0)
facturacion = pd.read_excel('facturacion.xlsx', index_col=0)
notas_credito = pd.read_excel('notas_credito.xlsx', index_col=0)
precios = pd.read_excel('precios_productos.xlsx', index_col=0)
#gastos_20 = pd.read_excel('gastos_costos2020.xlsx', index_col=0)
#gastos_21 = pd.read_excel('gastos_costos2021.xlsx', index_col=0)
#gastos_22 = pd.read_excel('gastos_costos2022.xlsx', index_col=0)
#gastos_23 = pd.read_excel('gastos_costos2023.xlsx', index_col=0)

#Detalle de precios y Productos fabricados
precios.info()

#Facturacion
facturacion.info()
facturacion=facturacion.fillna({'FECHA_CANCELA':'--','CVE_VEND':'--','FECHA_ENTREGA':'--'})
facturacion.isnull().sum()

#Devoluciones
devoluciones.info()
devoluciones=devoluciones.fillna({'DOC_ANT':'--', 'CVE_PEDI':'--', 'FECHA_CANCELA':'--','CVE_VEND':'--'})
devoluciones.isnull().sum()

#Clientes
clientes.info()
clientes=clientes.fillna({'RFC':'--','NOMBRE':'--'})
clientes.isnull().sum()

#Notas de Crédito
notas_credito.info()
notas_credito=notas_credito.fillna({'CVE_PEDI':'--','FECHA_CANCELA':'--','CVE_VEND':'--'})
notas_credito.isnull().sum()


