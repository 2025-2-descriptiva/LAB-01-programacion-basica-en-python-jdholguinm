"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    letras = []
    numeros = []

    with open(r"files/input/data.csv", "r", encoding="utf-8") as data:
        for linea in data:
            lista = linea.strip().split("\t")
            letras.append(lista[0])   
            numeros.append(int(lista[1]))

    resultado = {}
    for letra_unica in set(letras):
        suma = 0
        for i in range(len(letras)):
            if letras[i] == letra_unica:
                suma += numeros[i]
        resultado[letra_unica] = suma
    
    # resultado ={letra_unica: sum(numeros[i] for i in range(len(letras)) if letras[i] == letra_unica) for letra_unica in set(letras)}
    """ Este es una version mas compacta usando comprension de diccionarios la lógica es la siguiente:
    letra_unica: clave del diccionario
    sum(numeros...): valor del diccionario, que es la suma de los numeros correspondientes a la letra_unica
    el if dentro del sum filtra los indices donde la letra en la lista letras coincide con letra_unica
    Después el for itera sobre cada letra única en el conjunto de letras para construir el diccionario completo.
    La sintaxis sería: {clave: valor for item in iterable if condicion} """

    resultado = sorted(resultado.items())
    
    return resultado

# resultado = pregunta_03()
# print(resultado)

if __name__ == "__main__":
    print(pregunta_03())

