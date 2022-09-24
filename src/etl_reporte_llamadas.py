# Pseudo codigo
# main()
#   datos = get_data(filename)
#   reporte = generate_report(datos)
#   save_data(reporte)

from argparse import RawDescriptionHelpFormatter
import os
import pandas as pd
from pathlib import Path

root_dir = Path (".")

def get_data(filename):

    filename = 'llamadas123_julio_2022.csv'
    root_dir = Path('.').resolve()
    data_dir = 'raw'
    datos = get_data(filename)
    file_path = os.path.join(root_dir, 'data',data_dir,filename)
    
    datos = pd.read_csv(file_path, sep=';', encoding='latin-1')
    print('get_data')
    print('la tabla contiene', datos.shape[0], 'filas',datos.shape[1],'columnas')
    return datos

def generate_report(datos):
    #Crear diccionario vacio
    dict_resumen = dict()

    for col in datos.columns:
    valores_unicos =datos [col].unique()
    n_valores = len(valores_unicos)
    dict_resumen[col] = n_valores

    reporte = pd.DataFrame.from_dict(dict_resumen, orient='index')
    reporte.rename({0:'conteo'},axis=1,inplace=True)

    print('generate_reprt')
    print(report.head)
    return reporte

def save_data(reporte, filename):
    out_name = 'resumen_' + filename
    out_path = 


def main():

    filename = "llamadas123_julio_2022.csv"
    datos = get_data (filename)
    reporte = generate_report (datos)
    save_data(reporte,filename)

if __name__ == '__main__':
    main()