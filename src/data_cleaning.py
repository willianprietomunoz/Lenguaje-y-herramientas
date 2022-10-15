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
from etl_reporte_llamadas import save_data
from dateutil.parser import parse
import csv


root_dir = Path('.').resolve()


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
    datos['UNIDAD'].fillna('SIN_DATO').value_counts(dropna=True)
    datos = datos.fillna('SIN_DATO')
    return(datos)


def convertir_str_a_num(datos, col='EDAD'):
    """ Modifica el formato de la columna edad de str a num'

    Args:
        columna (EDAD): numero de edad de la persona que solicita el servicio

    Returns:
        dataframe: (Cambio de formato de la columna edad)
    """

    datos['EDAD'] = datos['EDAD'].replace({'SIN_DATO': np.nan})
    datos['EDAD'] = datos['EDAD'].astype('float')
    return(datos)


def corregir_fechas_1(datos, col='FECHA_INICIO_DESPLAZAMIENTO_MOVIL'):
    datos[col] = pd.to_datetime(datos[col], errors='coerce')
    return (datos)


def corregir_fechas_2(datos, col='RECEPCION'):
    datos[col] = pd.to_datetime(
        datos[col], errors='coerce', format='%Y-%m-%d %H:%M:%S')
    return (datos)


def generar_reporte(datos):
    return (datos)


def save_datos(datos, filename, step='Limpieza_datos'):

    out_name = step + '_' + 'llamadas123_julio_2022.csv'
    out_path = os.path.join(root_dir, 'data', 'processed', out_name)
    datos.to_csv(out_path)


def main():

    filename = 'llamadas123_julio_2022.csv'
    datos = get_data(filename)
    datos = remover_duplicados_y_nulos(datos)
    datos = convertir_str_a_num(datos)
    datos = corregir_fechas_1(datos)
    datos = corregir_fechas_2(datos)
    datos.info()
    datos = generar_reporte(datos)
    datos = save_datos(datos, filename='llamadas123_julio_2022.csv')


main()
