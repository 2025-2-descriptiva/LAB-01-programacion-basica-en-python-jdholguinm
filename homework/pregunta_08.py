"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """

    resultado = {}

    with open(r"files/input/data.csv", "r", encoding="utf-8") as data:
        for linea in data:
            columnas = linea.strip().split("\t")
            col_0 = columnas[0]          # letra
            col_1 = int(columnas[1])     # número (convertido a entero)


            if col_1 not in resultado:
                resultado[col_1] = set()
            resultado[col_1].add(col_0)

    # Convertir cada conjunto en lista ordenada. Acá el for ayuda a ordenar los set (conjunto)
    lista_tuplas = []
    for clave, conjunto in resultado.items():
        lista_tuplas.append((clave, sorted(conjunto)))

    # Ordenar por clave numérica y retornar
    return sorted(lista_tuplas)

if __name__ == "__main__":
    print(pregunta_08())