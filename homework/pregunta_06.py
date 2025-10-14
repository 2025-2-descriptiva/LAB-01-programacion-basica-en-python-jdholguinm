"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    matriz = []
    with open(r"files/input/data.csv", "r", encoding="utf-8") as data:
        for fila in data:
            columnas = fila.strip().split("\t")
            matriz.append(columnas)
    
    # Diccionario final: clave -> lista de valores
    diccionario = {}

    # Recorremos cada fila
    for fila in matriz:
        pares = fila[4].split(",")  # columna 4 tiene los pares clave:valor

        for par in pares:
            clave, valor = par.split(":")
            valor = int(valor)

            # Crear y agregar el valor a la lista de esa clave
            if clave not in diccionario:
                diccionario[clave] = [valor]
            else:
                diccionario[clave].append(valor)
    
    diccionario = dict(sorted(diccionario.items()))
     # Convertir las listas de valores en tuplas (min, max)
    diccionario = {k: (min(v), max(v)) for k, v in diccionario.items()}
    resultado = list((k, v[0], v[1]) for k, v in diccionario.items())   

    # return diccionario
    return resultado

if __name__ == "__main__":
    print(pregunta_06())

# for fila in pregunta_06():
#     print(fila)