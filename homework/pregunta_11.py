"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    resultado = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as data:
        for linea in data:
            columnas = linea.strip().split("\t")

            col_1 = int(columnas[1])
            col_3 = columnas[3].split(",")

            for letra in col_3:
                if letra not in resultado:
                    resultado[letra] = 0
                resultado[letra] += col_1

    # Ordenar alfabéticamente las claves antes de retornar
    resultado_ordenado = dict(sorted(resultado.items()))

    return resultado_ordenado


if __name__ == "__main__":
    print(pregunta_11())