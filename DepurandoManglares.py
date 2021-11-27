import pandas as pd 

def importarDatos():
    excel = pd.read_excel('sigma_estructura_bd - copia.xlsx',sheet_name='DATA_EXCEL')
    bd = pd.read_excel('sigma_estructura_bd - copia.xlsx',sheet_name='DATA_BD')
    bd.to_excel("sigmaEstructura_bd.xlsx", sheet_name='DATA_BD',index=False)
    excel.to_excel("sigmaEstructura_excel.xlsx", sheet_name='DATA_EXCEL',index=False)
   
def igualarColumnas():#col deben tener el mismo nombre y los registros deben estar descritos de la misma forma
    bd = pd.read_excel("sigmaEstructura_bd.xlsx", sheet_name='DATA_BD')
    excel = pd.read_excel("sigmaEstructura_excel.xlsx", sheet_name='DATA_EXCEL')
    #cambiamos la descripcion de los registros
   
    #cambiamos los nombres de las colas de la misma
    excel.columns['FECHA',  'AÑO',  'IDENTIFICADOR' 'ESTACION', 'CÓDIGOESTACIÓN',   'TRANSECTO',    'PARCELA',  'ESPECIE    ROTULO ÁRBOL        (ID)',  'TAG',  'ESTADO',   'TIPO', 'NEW TAG o INDIV',  'ALTURA (m) DAP (cm)',  'CATEGORÍA DIAMÉTRICA', 'OBSERVACIONES',    'AB'
]
    # bd.columns[]
   

importarDatos()