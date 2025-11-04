"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    resultado = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as data:
        for linea in data:
            columnas = linea.strip().split("\t")
            col_4 = columnas[4]
            pares = col_4.split(",")       # Estamos separando los pares clave:valor de cada fila

            for par in pares:
                clave = par.split(":")[0]  # tomamos solo la clave

                if clave not in resultado:
                    resultado[clave] = 0
                resultado[clave] += 1    # Contador de las veces que aparece

    return dict(sorted(resultado.items()))

if __name__ == "__main__":
    print(pregunta_09())