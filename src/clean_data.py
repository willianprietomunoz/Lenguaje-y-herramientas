#main()
#   datos = leer datos(obre del archivo:str) -- pd.dataframe
#   datos = remover_duplicados_y_nulo(datos: pd.dataframe) -- pd.dataframe
#   datos = covertir_str_a_num(datos, col='EDAD') -- pd.dataframe
#   datos = corregir_fechas(datos, col='FECHA1') -- pd.dataframe
#   datos = corregir_fechas(datos, col='FECHA2') -- pd.dataframe
#   save_data()

import pandas as pd 

def remover_duplicados_y_nulos(data:pd.DataFrame):
    print ('forma inicial',data.shape)
    data = data.drop_duplicates() 
    data.reset_index(inplace=True, drop=True) 
    print('forma final', data.shape)
    return data




#Tratamiento de valores nulos
#nulo de string = sin_dato - n/a
#nulo numeros = numpy utilizar funcion nan(not_asigned_name) (np.nan)
#nulo de fechas = nat (not_asigned_time)

import pandas as pd 
import os
from pathlib import Path 
import numpy as np


root_dir = Path('.').resolve().parent
filename = 'llamadas123_julio_2022.csv'
data_dir = 'raw'


file_path = os.path.join(root_dir,'data','raw',filename)
data = pd.read_csv(file_path, sep=';', encoding='latin-1')

print ('forma inicial',data.shape)
data = data.drop_duplicates() 
data.reset_index(inplace=True, drop=True) 
print('forma final', data.shape)

col = 'UNIDAD'
data [col].fillna('SIN_DATO', inplace=True)
data [col].value_counts(dropna=False, normalize=True)

fecha = '2022-07-01 00:08:59'
pd.to_datetime(fecha)

col = 'FECHA_INICIO_DESPLAZAMIENTO_MOVIL'
data[col]

fecha = ' 0000-00-00 00:00:00'
pd.to_datetime(fecha, errors='coerce', format= '%Y/%m/%d')

col = 'FECHA_INICIO_DESPLAZAMIENTO_MOVIL'
data[col] = pd.to_datetime (data[col], errors='coerce')

col = 'EDAD'
data[col].replace({'SIN_DATO': np.nan}, inplace=True)

str_num = '28'
f = lambda x: x if pd.isna(x) else int(x)

data[col] = data[col].apply(f)

from dateutil.parser import parse 
fecha = 'may 29th 2021'
parse(fecha)

fechas = lambda x: parse(x)
list_fechas = list()

for fecha in data[col]:
    try:
        new_fecha = parse(fecha)
    except Exception as e:
        new_fecha = pd.to_datetime(fecha, errors='coerce')
    list_fechas.append(new_fecha)
    
data ['RECEPCION_Corregida'] = list_fechas





