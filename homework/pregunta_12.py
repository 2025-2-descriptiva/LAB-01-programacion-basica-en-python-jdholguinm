"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    resultado = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as data:
        for linea in data:
            columnas = linea.strip().split("\t")

            col_0 = columnas[0]
            col_4 = columnas[4]
            pares = col_4.split(",")

            # Convertimos cada par "clave:valor" y sumamos los valores numéricos
            suma_valores = sum(int(par.split(":")[1]) for par in pares)

            # Acumulamos la suma total por letra
            if col_0 not in resultado:
                resultado[col_0] = 0
            resultado[col_0] += suma_valores

    # Ordenar alfabéticamente las claves
    resultado_ordenado = dict(sorted(resultado.items()))

    return resultado_ordenado

if __name__ == "__main__":
    print(pregunta_12())