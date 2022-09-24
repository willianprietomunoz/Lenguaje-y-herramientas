# Pseudo codigo
# main()
#   datos = get_data(filename)
#   reporte = generate_report(datos)
#   save_data(reporte)

import os
from pathlib import Path
import pandas as pd

root_dir = Path('.').resolve()


def get_data(filename):
    data_dir = 'raw'
    file_path = os.path.join(root_dir, 'data', data_dir, filename)
    datos = pd.read_csv(file_path, sep=';', encoding='latin-1')

    print('get_data')
    print('La tabla contiene', datos.shape[0],
          'filas', datos.shape[1], 'columnas')
    return datos


def generate_report(datos):
    dict_resumen = dict()

    for col in datos.columns:
        valores_unicos = datos[col].unique()
        n_valores = len(valores_unicos)
        dict_resumen[col] = n_valores

    reporte = pd.DataFrame.from_dict(dict_resumen, orient='index')
    reporte.rename({0: 'Conteo'}, axis=1, inplace=True)

    print('generate_report')
    print(reporte.head())
    return reporte


def save_data(reporte, filename, step='resumen'):

    out_name = step + '_' + filename
    out_path = os.path.join(root_dir, 'data', 'processed', out_name)
    reporte.to_csv(out_path)


def main():
    filename = 'llamadas123_julio_2022.csv'
    datos = get_data(filename)
    reporte = generate_report(datos)
    save_data(reporte, filename)


if __name__ == '__main__':
    main()