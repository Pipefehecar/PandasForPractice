import numpy as np
from numpy import float64
import pandas as pd 
import math as mt

def importarDatos():
    excel = pd.read_excel('sigma_estructura_bd - copia.xlsx',sheet_name='DATA_EXCEL')
    bd = pd.read_excel('sigma_estructura_bd - copia.xlsx',sheet_name='DATA_BD')
    bd.to_excel("sigmaEstructura_bd.xlsx", sheet_name='DATA_BD',index=False)
    excel.to_excel("sigmaEstructura_excel.xlsx", sheet_name='DATA_EXCEL',index=False)
def verExcel():
    excel = pd.read_excel('sigma_estructura_bd - copia.xlsx',sheet_name='DATA_EXCEL')
    bd = pd.read_excel('sigma_estructura_bd - copia.xlsx',sheet_name='DATA_BD')
    print("-----------------------------------------------------BD------------------------------------")
    print(bd)
    print("-----------------------------------------------------EXCEL------------------------------------")
    print(excel)
      
def igualarColumnas():#col deben tener el mismo nombre y los registros deben estar descritos de la misma forma
    bd = pd.read_excel("sigmaEstructura_bd.xlsx", sheet_name='DATA_BD')
    excel = pd.read_excel("sigmaEstructura_excel.xlsx", sheet_name='DATA_EXCEL')
    
    excel.dropna(subset=['IDENTIFICADOR'], inplace=True)
    bd.dropna(subset=['IDENTIFICADOR'], inplace=True)
    
    #cambiamos la descripcion de los registros
    excel['ESTADO'] = excel['ESTADO'].str.replace('VI', '6')
    excel['ESTADO'] = excel['ESTADO'].str.replace('PA', '5')
    excel['ESTADO'] = excel['ESTADO'].str.replace('MU', '4')
    excel['ESTADO'] = excel['ESTADO'].str.replace('ME', '3')
    excel['ESTADO'] = excel['ESTADO'].str.replace('CO', '2')
    excel['ESTADO'] = excel['ESTADO'].str.replace('CA', '1')
    #excel = excel.astype(float64)
    excel[['TIPO']] = excel[['TIPO']].astype(str)
    #excel['TIPO'] = excel['TIPO'].map(str)
    excel['TIPO'] = excel['TIPO'].str.replace('R', '7')
    excel['TIPO'] = excel['TIPO'].str.replace('T', '8')
    
    #cambiamos los nombres de las colas de la misma
    excel = excel.rename(columns={'DAP (cm)': 'DAP', 'ALTURA (m)': 'ALTURA_METROS','ROTULO ÁRBOL        (ID)':'ROTULO_ARBOL_ID','TIPO':'ID_TIPO'})
    # excel[['ALTURA (m)', 'DAP (cm)','TIPO','AB','ROTULO ÁRBOL        (ID)']] = excel[['ALTURA (m)', 'DAP (cm)','TIPO','AB','ROTULO ÁRBOL        (ID)']].astype(str)
    
    #excel.columns['FECHA','ANO','IDENTIFICADOR','ESTACION','CODIGO_ESTACION','TRANSECTO','PARCELA','ESPECIE','ROTULO_ARBOL_ID','TAG','ESTADO', 'ID_TIPO','NEW_TAG','ALTURA_METROS','DAP','CATEGORIA_DIAMETRICA','OBSERVACIONES','AB']
    
    print('EXC\n',excel.info())
    print('bd\n',bd.info())
    bd.to_excel("sigmaEstructura_bd.xlsx", sheet_name='DATA_BD',index=False)
    excel.to_excel("sigmaEstructura_excel.xlsx", sheet_name='DATA_EXCEL',index=False)
    
    
    
def alistarIdentificadores():
    bd = pd.read_excel("sigmaEstructura_bd.xlsx", sheet_name='DATA_BD')
    excel = pd.read_excel("sigmaEstructura_excel.xlsx", sheet_name='DATA_EXCEL')
    excel.dropna(subset=['IDENTIFICADOR'], inplace=True)
    bd.dropna(subset=['IDENTIFICADOR'], inplace=True)
    
   
    #creamoos nueva col IDENTIFICADOR(FECHA-ESTACION-TRANSECTO-ROTULO ÁRBOL(ID)) para comparar con la BD
    #bd['FECHA'] =pd.to_datetime(bd['FECHA'])
    excel['ROTULO_ARBOL_ID'] = list(map(int,excel['ROTULO_ARBOL_ID']))
    excel['IDENTIFICADOR'] = excel['FECHA'].map(str) + excel['ESTACION'].map(str) + excel['TRANSECTO'].map(str) + excel['ROTULO_ARBOL_ID'].map(str)
    excel['IDENTIFICADOR'] = excel['IDENTIFICADOR'].str.replace(' ', '')
    excel['IDENTIFICADOR'] = excel['IDENTIFICADOR'].str.replace('-', '')
    excel['IDENTIFICADOR'] = excel['IDENTIFICADOR'].str.replace('00:00:00', '')
   
    #creamoos nueva col IDENTIFICADOR(FECHA-NOM_ESTACION-ROTULO_ARBOL_ID) para comparar con el excel
    #bd['FECHA'] =pd.to_datetime(bd['FECHA']).dt.normalize()
    bd['ROTULO_ARBOL_ID'] = list(map(int,bd['ROTULO_ARBOL_ID']))
    bd['IDENTIFICADOR'] = bd['FECHA'].map(str) + bd['NOM_ESTACION'].map(str) + bd['ROTULO_ARBOL_ID'].map(str)
    bd['IDENTIFICADOR'] = bd['IDENTIFICADOR'].str.replace(' ', '')
    bd['IDENTIFICADOR'] = bd['IDENTIFICADOR'].str.replace('-', '')
    bd['IDENTIFICADOR'] = bd['IDENTIFICADOR'].str.replace('Kilómetro','Km')
    bd['IDENTIFICADOR'] = bd['IDENTIFICADOR'].str.replace('Cañoa', 'Caño')
    bd['IDENTIFICADOR'] = bd['IDENTIFICADOR'].str.replace('CañoGrandeE', 'CañoGrande')
    bd['IDENTIFICADOR'] = bd['IDENTIFICADOR'].str.replace('00:00:00', '')
    
    print(bd)
    print(excel)
    bd.to_excel("sigmaEstructura_bd.xlsx", sheet_name='DATA_BD',index=False)
    excel.to_excel("sigmaEstructura_excel.xlsx", sheet_name='DATA_EXCEL',index=False)
    
def dap_cap():
    bd = pd.read_excel("sigmaEstructura_bd.xlsx", sheet_name='DATA_BD')
    for i, row in bd.iterrows():
        if np.isnan(row['DAP']):
            if not(np.isnan(row['CAP'])):
                bd['DAP']=bd['CAP'].apply(lambda x: x/mt.pi)
                # print("nan dap---",row['IDENTIFICADOR'])
        # if np.isnan(row['CAP']):
        #     if not(np.isnan(row['DAP'])):
        #         bd['CAP']=bd['DAP'].apply(lambda x: x*mt.pi)
        #         print("nan cap---",row['IDENTIFICADOR'])
            
    bd.to_excel("sigmaEstructura_bd.xlsx", sheet_name='DATA_BD',index=False)       
def contarVacias(columName):
    bd = pd.read_excel("sigmaEstructura_bd.xlsx", sheet_name='DATA_BD')
    print(bd[columName].isnull().sum())    

def registrosParaActualizacion():
    bd = pd.read_excel("sigmaEstructura_bd.xlsx", sheet_name='DATA_BD')
    excel = pd.read_excel("sigmaEstructura_excel.xlsx", sheet_name='DATA_EXCEL', nrows=1000)
    #print(bd.loc[bd['IDENTIFICADOR']=='19961120Km2211477'])
    # if(bd['IDENTIFICADOR'].isin(['19961120Km2211477']).any()):
    #     print('exito')
    especie=0  
    rotulo=0
    id_tipo=0
    altura=0

    for i, row in excel.iterrows():
        # print(row['DAP'])
        # if(bd.loc[bd['IDENTIFICADOR']==row['IDENTIFICADOR']].bool()):
        if(bd['IDENTIFICADOR'].isin([row['IDENTIFICADOR']]).any()):
            muestra = bd.loc[bd['IDENTIFICADOR']==row['IDENTIFICADOR']]
            
            if (muestra['ESPECIE'] != row['ESPECIE']).any() :
                # print(muestra['ID_MUESTREOTX'])
                especie += 1
            if (muestra['ROTULO_ARBOL_ID'] != row['ROTULO_ARBOL_ID']).any() :
                # print(muestra['ID_MUESTREOTX'])
                rotulo += 1
            if (muestra['ID_TIPO'] != row['ID_TIPO']).any() :
                # print(muestra['ID_MUESTREOTX'])
                id_tipo += 1
            if (muestra['ALTURA_METROS'] != row['ALTURA_METROS']).any() :
                # print(muestra['ID_MUESTREOTX'])
                altura += 1
            if (muestra['DAP'] != row['DAP']).any() :
                # print(muestra['ID_MUESTREOTX'])
                altura += 1
    print("especie: ", especie)
    print("rotulo: ", rotulo)
    print("id_tipo: ", id_tipo)
    print("altura: ", altura)


# importarDatos()
# igualarColumnas()
# alistarIdentificadores()
# dap_cap()
# verExcel()
# contarVacias('CAP')#1=dap,2=cap
registrosParaActualizacion()