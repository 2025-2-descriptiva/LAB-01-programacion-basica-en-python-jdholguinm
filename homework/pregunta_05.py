"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    letras = []
    numeros = []
    max_min = {}

    with open(r"files/input/data.csv", "r", encoding="utf-8") as data:
        for linea in data:
            lista = linea.strip().split("\t")
            letras.append(lista[0])   
            numeros.append(int(lista[1]))


        for letra in set(letras):
            max_min[letra] = [float('-inf'), float('inf')]
            for i in range(len(letras)):
                if letras[i] == letra:
                    max_min[letra][0] = max(max_min[letra][0], numeros[i])
                    max_min[letra][1] = min(max_min[letra][1], numeros[i])

    resultado = sorted(list((letra, max_min[letra][0], max_min[letra][1]) for letra in max_min))

    return resultado

# resultado = pregunta_05()
# print(resultado)


if __name__ == "__main__":
    print(pregunta_05())
