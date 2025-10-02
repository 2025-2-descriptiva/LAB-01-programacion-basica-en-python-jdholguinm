"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214

    """
    total = 0
    # with open(r"D:\Ensayos Python\files\data.csv", "r", encoding="utf-8") as data:
    with open(r"files/input/data.csv", "r", encoding="utf-8") as data:
        for fila in data:
            columna = fila.strip().split("\t")
            total += int(columna[1])
        
    return total


if __name__ == "__main__":
    print(pregunta_01())
