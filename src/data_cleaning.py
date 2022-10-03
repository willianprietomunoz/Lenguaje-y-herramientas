# pseudo codigo
# main()
#   datos = leer_datos(nombre del archivo : str) -- pd.dataframe
#   datos = remover_duplicados_y_nulos(datos : pd.dataframe) --pd.dataframe
#   datos = convertir_str_a_num(datos,col='EDAD') --pd.dataframe
#   datos = corregir_fechas (datos,col='FECHA1') --pd.dataframe
#   datos = convertir_formato_fechas (datos,col='FECHA2') --pd.dataframe
#   save_data(datos)


import numpy as np
import pandas as pd
import os
from pathlib import Path
from etl_reporte_llamadas import get_data
from dateutil.parser import parse
import csv

root_dir = Path('.').resolve()
filename = 'llamadas123_julio_2022.csv'


def remover_duplicados_y_nulos(datos):
    """ Remueve valor duplicados del DF y reemplaza valores nulos en colum 'unidad'

    Args:
        dataframe (datos): llamadas123_julio_2022
        columna (UNIDAD): medida de referecia de colum 'EDAD'

    Returns:
        dataframe: (forma inicial (rows, columns), forma final (rows, columns))
    """

    print('forma inicial', datos.shape)
    datos = datos.drop_duplicates()
    print('forma final', datos.shape)
    datos.fillna('SIN_DATO').value_counts(dropna=True)
    datos = datos.fillna('SIN_DATO')
    print(datos)


def convertir_str_a_num(datos, col='EDAD'):
    datos['EDAD'] = datos['EDAD'].replace({'SIN_DATO': np.nan})
    x = '0'
    def f(x): return x if pd.isna(x) == True else int(x)
    f(x)
    datos['EDAD'] = datos['EDAD'].apply(f)
    datos.info()


def corregir_fechas_1(datos, col='FECHA_INICIO_DESPLAZAMIENTO_MOVIL'):
    col = 'FECHA_INICIO_DESPLAZAMIENTO_MOVIL'
    datos[col] = pd.to_datetime(datos[col], errors='coerce')
    datos.info()
    return datos


def generar_reporte(datos):
    return datos


def save_data(datos, filename, step='Limpieza_datos'):

    out_name = step + '_' + 'llamadas123_julio_2022.csv'
    out_path = os.path.join(root_dir, 'data', 'processed', out_name)
    datos.to_csv(out_path)


def main():
    datos = get_data(filename='llamadas123_julio_2022.csv')
    datos = remover_duplicados_y_nulos(datos) or convertir_str_a_num(
        datos) or corregir_fechas_1(datos)
    datos = generar_reporte(datos)
    datos = save_data(datos, filename='llamadas123_julio_2022.csv')


main()
