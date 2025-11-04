"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    resultado = []

    with open("files/input/data.csv", "r", encoding="utf-8") as data:
        for linea in data:
            columnas = linea.strip().split("\t")

            col_0 = columnas[0]
            col_3 = columnas[3]
            col_4 = columnas[4]

            # Contar los elementos separados por coma
            num_col3 = len(col_3.split(","))
            num_col4 = len(col_4.split(","))

            # Crear la tupla
            resultado.append((col_0, num_col3, num_col4))

    return resultado

if __name__ == "__main__":
    print(pregunta_10())