from datetime import datetime
import pandas as pd
def alistarData():
    bdEstructura = pd.read_excel('xlsxS/BD_CGSM_ESTRUCTURA_LABSIS_2021.12.03.xlsx', sheet_name='BD_Estructura')
    bdEstructura.columns = [
    'FECHA','AÑO','ESTACION',
    'CÓDIGO_ESTACION','TRANSECTO',
    'PARCELA','ESPECIE',
    'IDENTIFICADOR','TAG',
    'ROTULO','ESTADO','TIPO',
    'NEW','ALTURA','DAP',
    'CATEGORÍA_DIAMETRICA',
    'OBSERVACIONES','AB'
    ]
    bdEstructura['ESTACION_BD'] = bdEstructura['ESTACION'] + "-" + bdEstructura['TRANSECTO'].map(str) 
    bdEstructura['ESTACION_BD'] = bdEstructura['ESTACION_BD'].str.replace(' ','')
    #Asignamos los id segun la bd
    bdEstructura['ID_ESTACION'] = bdEstructura['ESTACION_BD']
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('AguasNegras-1','45924')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('AguasNegras-2','45926')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('AguasNegras-3','45928')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('CañoGrande-1','45930')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('CañoGrande-2','45932')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('CañoGrande-3','45934')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Km22-1','45907')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Km22-2','45910')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Km22-3','45912')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Luna-1','45922')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Luna-2','47837')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Luna-3','47839')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Rinconada-1','45914')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Rinconada-2','45916')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Rinconada-3','45920')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Sevillano-1','50089')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Sevillano-2','50091')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Sevillano-3','50093')
    
    #generamos los id_muestreo
    bdEstructura['ROTULO'] = bdEstructura['ROTULO'].map(int)
    print(bdEstructura.info())
    bdEstructura['FECHA'] = bdEstructura['FECHA'].dt.date
    bdEstructura['ID_MUESTREO'] = bdEstructura['FECHA'].map(str).str.replace('-','') + bdEstructura['ID_ESTACION']
    bdEstructura['ID_MUESTRA'] = bdEstructura['ID_MUESTREO'] + bdEstructura['ROTULO'].map(str)
    # bdEstructura['ID_MUESTRA'] = bdEstructura['ID_MUESTRA'].map(float)
    # bdEstructura['ID_MUESTRA'] = bdEstructura['ID_MUESTRA'].map(int)
    
    # print(bdEstructura['ESTACION_BD'].unique())
    # for row in bdEstructura:
        # row['ESTACION_BD'] = concat(row['ESTACION'], row['TRANSECTO']) 
        
    
    bdEstructura[['FECHA','AÑO','TRANSECTO','ROTULO','ALTURA','DAP','AB','ID_MUESTRA']] = bdEstructura[['FECHA','AÑO','TRANSECTO','ROTULO','ALTURA','DAP','AB','ID_MUESTRA']].astype(str)
    
    print(bdEstructura.info())
    print(bdEstructura)
    bdEstructura.to_excel('xlsxS/BD_2239_3-toUpload.xlsx',index=False)

# GENERAR MUESTRAS
def generarAGD_MUESTRAS():
    bdEstructura = pd.read_excel('xlsxS/BD_2239_3-toUpload.xlsx')
    muestras = pd.DataFrame(columns = ['ID_MUESTRA','ID_MUESTREO','NOTAS','ES_REPLICA'])
    muestras['ID_MUESTRA'] = bdEstructura['ID_MUESTRA'].map(str)
    muestras['ID_MUESTREO'] = bdEstructura['ID_MUESTREO'].map(str)
    muestras['NOTAS'] = bdEstructura['OBSERVACIONES']
    muestras['ES_REPLICA'] = 1 #siempre es 1??
    print(muestras.info())
    print(muestras)
    muestras.to_excel('xlsxS/2239_3-toUpload/BD_2239_3-ToUpload(muestras).xlsx',index=False)
    
# GENERAR MUESTREOS
def generarAGD_MUESTREOS():
    bdEstructura = pd.read_excel('xlsxS/BD_2239_3-toUpload.xlsx')
    muestreos = pd.DataFrame(columns = ['ID_MUESTREO','ID_ESTACION','ID_PROYECTO','ID_METODOLOGIA','ID_TEMATICAS','FECHA','NOTAS','FECHASIS'])
    result_bdEstructura = bdEstructura.drop_duplicates(subset=['ID_MUESTREO'])
    muestreos['ID_MUESTREO'] = result_bdEstructura['ID_MUESTREO'].map(str)
    muestreos['ID_ESTACION'] = result_bdEstructura['ID_ESTACION'].map(str)
    muestreos['ID_PROYECTO'] = 2239
    muestreos['ID_METODOLOGIA'] = 3
    muestreos['ID_TEMATICAS'] = 224
    muestreos['FECHA'] = result_bdEstructura['FECHA']
    muestreos['FECHASIS'] = datetime.now().date()
    print(muestreos.info())
    print(muestreos)
    muestreos.to_excel('xlsxS/2239_3-toUpload/BD_2239_3-ToUpload(muestreos).xlsx',index=False)
    
# GENERAR MUESTRAS VARIABLES(aca se guarda dap)
def generarAGD_MUESTREOS_PARAMETROS():
    1+1
# GENERAR MUESTREOS PARAMETROS (ID_MUESTREO ID_PARAMETRO ID_METODOLOGIA ID_UNIDAD_MEDIDA VALOR)
def generarAGD_MUESTREOS_PARAMETROS():
    bdEstructura = pd.read_excel('xlsxS/BD_2239_3-toUpload.xlsx')
    muestreos_parametros = pd.DataFrame(columns = ['ID_MUESTREO','ID_PARAMETRO','ID_METODOLOGIA','ID_UNIDAD_MEDIDA','VALOR'])
    result_bdEstructura = bdEstructura.drop_duplicates(subset=['ID_MUESTREO'])
    result_bdEstructura['ID_MUESTREO'] = result_bdEstructura['ID_MUESTREO'].map(str)
    for i, row in result_bdEstructura.iterrows():
        muestreos_parametros = muestreos_parametros.append({'ID_MUESTREO':row['ID_MUESTREO'], 'ID_PARAMETRO':860,'ID_METODOLOGIA':3, 'ID_UNIDAD_MEDIDA':109,'VALOR':100}, ignore_index=True)
        # muestreos_parametros = muestreos_parametros.append({'ID_MUESTREO':row['ID_MUESTREO'], 'ID_PARAMETRO':860,'ID_METODOLOGIA':3, 'ID_UNIDAD_MEDIDA':109,'VALOR':100}, ignore_index=True)
    
    print(muestreos_parametros.info())
    print(muestreos_parametros)
    muestreos_parametros.to_excel('xlsxS/2239_3-toUpload/BD_2239_3-ToUpload(muestreos_parametros).xlsx',index=False)

# 860	Area	A
# 901	Subparcelas muestreadas	SuPM
# 1055	Versión plantilla	1055
# 1170	Archivo fuente	1170

# GENERAR MUESTRAS VARIABLES
# GENERAR AUTORIAS



#GENERAR SQLS
"""
def generate_sqls():
    muestreos = pd.read_excel('xlsxS/2239_3-toUpload/BD_2239_3-ToUpload(muestreos).xlsx')
    muestreos['ID_PROYECTO'] = muestreos['ID_PROYECTO'].map(str)
    muestreos['ID_METODOLOGIA'] = muestreos['ID_METODOLOGIA'].map(str)
    muestreos['ID_TEMATICAS'] = muestreos['ID_TEMATICAS'].map(str)
    print(muestreos.info())
    columns = list(muestreos)
    query = "INSERT INTO datosdecampo.AGD_MUESTREOS ("
    values = ""
    for i, row in muestreos.iterrows():
        for col in columns:
            query = query + col +","
           
        query=" INSERT INTO datosdecampo.AGD_MUESTREOS (ID_MUESTREO,ID_ESTACION,ID_PROYECTO,ID_METODOLOGIA,ID_TEMATICAS,FECHA,NOTAS,FECHASIS) VALUES ("+row['ID_MUESTREO']+","+row['ID_ESTACION']+","+row['ID_PROYECTO']+","+row['ID_METODOLOGIA']+","+row['ID_TEMATICAS']+","+row['FECHA']+","+row['NOTAS']+","+row['FECHASIS']+");"
        
        
        print(query,"\n")
"""   
#    ID_MUESTREO ID_ESTACION  ID_PROYECTO  ID_METODOLOGIA  ID_TEMATICAS       FECHA NOTAS    FECHASIS
    


# alistarData()
# generarAGD_MUESTREOS()
# generarAGD_MUESTRAS()
generarAGD_MUESTREOS_PARAMETROS()

