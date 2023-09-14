from datetime import datetime
import math
import random

"""
Se necesita diseñar el algoritmo Distancia-Maxima (X,Y), que dado un conjunto de coordenadas (x,y)
que representan puntos en el plano, muestre la distancia máxima entre cada par de puntos.
(X,Y) son dos array de la misma longitud y representan las coordenadas de cada punto respectivamente.

a)	¿Cómo resolvería el problema?  
b)	¿Cuál es su complejidad?
c)	Explique cómo su algoritmo exhibe comportamiento óptimo local (Opcional)
"""

def Distancia(a: tuple[int, int], b: tuple[int, int]) -> float:
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def MaximaDistancia(arr_i: list[int, int], arr_ii: list[int, int]) -> float:
    maxima: float = Distancia(arr_i[0], arr_ii[0])
    j: int = 1
    
    while(len(arr_i) > 0):
        distancia: float = Distancia(arr_i[0], arr_ii[j])
        if distancia > maxima:
            maxima = distancia
        j += 1
        if j == len(arr_ii) - 1:
            arr_i.pop(0)
            j = 0

    return maxima

def MaximaDistancia_RI(arr_i: list[int, int], arr_ii: list[int, int]) -> float:
    if len(arr_i) == 0:
        return 0

    resultado: float = MaximaDistancia_RI(arr_i[1:], arr_ii)
    temp: list[float] = []
    for i in range(len(arr_ii)):
        temp.append(Distancia(arr_i[0], arr_ii[i]))

    return resultado if resultado > max(temp) else max(temp)

def MaximaDistancia_IDC(arr_i: list[int, int], arr_ii: list[int, int]) -> float:
    def Distancias_DC(valor: tuple[int, int], arreglo: list[int,int]) -> float:
        if len(arreglo) == 1:
            return Distancia(valor, arreglo[0])
        else:
            return max(Distancias_DC(valor, arreglo[:len(arreglo)//2]), Distancias_DC(valor, arreglo[len(arreglo)//2:]))

    distancias: list[float] = []
    for i in range(len(arr_i)):
        distancias.append(Distancias_DC(arr_i[i-1], arr_ii))

    return max(distancias)

def MaximaDistancia_DP(arr_i: list[int, int], arr_ii: list[int, int]) -> float:
    matriz: list[list[float]] = [[0 for _ in range(len(arr_ii))] for _ in range(len(arr_i))]
    distancias: list[float] = []

    for i in range(len(arr_i)):
        for j in range(len(arr_ii)):
            matriz[i][j] = Distancia(arr_i[i], arr_ii[j])
        distancia: int = max(matriz[i])
        distancias.append(distancia)

    maxima: float = max(distancias)
    return maxima

if __name__ == "__main__":
    """puntos_i:  list[int, int] = [(1, 2), (3, 4), (5, 6)]
    puntos_ii: list[int, int] = [(7, 8), (9, 10), (11, 12)]"""

    """puntos_i:  list[int, int] = [(36, 47), (-6, -24), (24, -50), (47, -21), (-2, -10), (29, -31), (47, 13), (-34, 9), (-40, 2), (11, 20), (41, -1), (14, -38), (-4, -18), (10, -21), (-24, -14), (3, -38)]
    puntos_ii: list[int, int] = [(-37, -31), (46, -39), (-36, -21), (40, -27), (-12, -44), (24, -2), (37, 19), (-1, 7), (-31, 49), (-16, 44), (-39, 34), (-30, 46), (-34, -30), (1, -3), (-41, -5), (33, -3)]"""

    """ Generamos arrays de tamaño N con valores aleatorios en R2 """
    longitud = random.randrange(100, 900)
    puntos_i:  list[int, int] = [ ((random).randrange(-500,500), (random).randrange(-50,50)) for _ in range(longitud) ]
    puntos_ii: list[int, int] = [ ((random).randrange(-500,500), (random).randrange(-50,50)) for _ in range(longitud) ]
    
    print("Los arrays tienen", longitud, "elementos")

    """print("Puntos i",  puntos_i)
    print("Puntos ii", puntos_ii)"""

    resultados: list[float, float] = []
    
    copia_puntos_i = [ x for x in puntos_i]
    start = datetime.now()
    aux = MaximaDistancia(copia_puntos_i, puntos_ii)
    end = datetime.now()
    resultados.append((aux, end - start))

    copia_puntos_i = puntos_i
    start = datetime.now()
    aux = MaximaDistancia_RI(copia_puntos_i, puntos_ii)
    end = datetime.now()
    resultados.append((aux, end - start))
    
    copia_puntos_i = puntos_i
    start = datetime.now()
    aux = MaximaDistancia_IDC(copia_puntos_i, puntos_ii)
    end = datetime.now()
    resultados.append((aux, end - start))

    copia_puntos_i = puntos_i
    start = datetime.now()
    aux = MaximaDistancia_DP(copia_puntos_i, puntos_ii)
    end = datetime.now()
    resultados.append((aux, end - start))

    print("Mayor distancia con Iterativo:", resultados[0][0], "Tiempo:", resultados[0][1])
    print("Mayor distancia con Recursivo + Iterativo:", resultados[1][0], "Tiempo:", resultados[1][1])
    print("Mayor distancia con Iterativo + D&C:", resultados[2][0], "Tiempo:", resultados[2][1])
    print("Mayor distancia con Dynamic Programming:", resultados[3][0], "Tiempo:", resultados[3][1])
