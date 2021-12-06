import pandas as pd

bdEstructura = pd.read_excel('xlsxS/BD_CGSM_ESTRUCTURA_LABSIS_2021.12.03.xlsx', sheet_name='BD_Estructura')

bdEstructura.columns = [
'FECHA',
'AÑO',
'ESTACION',
'CÓDIGO_ESTACION',
'TRANSECTO',
'PARCELA',
'ESPECIE',
'IDENTIFICADOR',
'TAG',
'ROTULO',
'ESTADO',
'TIPO',
'NEW',
'ALTURA',
'DAP',
'CATEGORÍA_DIAMETRICA',
'OBSERVACIONES',
'AB'
]
bdEstructura['ROTULO'] = bdEstructura['ROTULO'].map(int)
bdEstructura[['FECHA','AÑO','TRANSECTO','ROTULO','ALTURA','DAP','AB']] = bdEstructura[['FECHA','AÑO','TRANSECTO','ROTULO','ALTURA','DAP','AB']].astype(str)
print(bdEstructura.info())
bdEstructura.to_excel('xlsxS/BD_2239_3-toUpload.xlsx',index=False)

# GENERAR INSERT FOR MUESTRAS
# GENERAR INSERT FOR MUESTREOS
# GENERAR MUESTRAS VARIABLES