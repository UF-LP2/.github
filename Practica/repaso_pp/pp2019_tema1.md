# [2019] Primer Parcial - Tema 1

#### Consigna
```text
Se necesita diseñar el algoritmo Distancia-Maxima (X,Y), que dado un conjunto de coordenadas (x,y)
que representan puntos en el plano, muestre la distancia máxima entre cada par de puntos.
(X,Y) son dos array de la misma longitud y representan las coordenadas de cada punto respectivamente.

a)¿Cómo resolvería el problema?  
b)¿Cuál es su complejidad?
c)Explique cómo su algoritmo exhibe comportamiento óptimo local (Opcional)
```

### Función base
```py
def Distancia(a: tuple[int, int], b: tuple[int, int]) -> float:
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
```

## Algoritmos

### Greedy (Iterativo)
```py
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
```

### Greedy (Recursivo + Iterativo)
```py
def MaximaDistancia_RI(arr_i: list[int, int], arr_ii: list[int, int]) -> float:
    if len(arr_i) == 0:
        return 0

    resultado: float = MaximaDistancia_RI(arr_i[1:], arr_ii)
    temp: list[float] = []
    for i in range(len(arr_ii)):
        temp.append(Distancia(arr_i[0], arr_ii[i]))

    return resultado if resultado > max(temp) else max(temp)
```

### Iterativo + Divider & Conquer (Recursivo)
```py
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
```

### Programación Dinámica
```py
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
```

### Input
```py
N = 15
puntos_i   = [(36, 47), (-6, -24), (24, -50), (47, -21), (-2, -10), (29, -31), (47, 13), (-34, 9), (-40, 2), (11, 20), (41, -1), (14, -38), (-4, -18), (10, -21), (-24, -14)]
puntos_ii: = [(-37, -31), (46, -39), (-36, -21), (40, -27), (-12, -44), (24, -2), (37, 19), (-1, 7), (-31, 49), (-16, 44), (-39, 34), (-30, 46), (-34, -30), (1, -3), (-41, -5)]
```

### Output
```text
Mayor distancia con Iterativo: 113.25193155085701 Tiempo: 0:00:00.001000
Mayor distancia con Recursivo + Iterativo: 113.25193155085701 Tiempo: 0:00:00.000999
Mayor distancia con Iterativo + D&C: 113.25193155085701 Tiempo: 0:00:00.001000
Mayor distancia con Dynamic Programming: 113.25193155085701 Tiempo: 0:00:00.000999
```

Por los diseños de los algoritmos, con un 'N' menor a 16, no se nota la diferencia de tiempo, pero que pasaría si incrementamos la cantidad, puede que empiece a notarse la diferencia entre ellos?

<details>
<summary>Ejemplo con N > 16</summary>

```text
Los arrays tienen 534 elementos
Mayor distancia con Iterativo: 997.513408431185 Tiempo: 0:00:00.780156
Mayor distancia con Recursivo + Iterativo: 997.513408431185 Tiempo: 0:00:00.520010
Mayor distancia con Iterativo + D&C: 997.513408431185 Tiempo: 0:00:01.321384
Mayor distancia con Dynamic Programming: 997.513408431185 Tiempo: 0:00:00.583686
```
- ¿Qué algoritmo se comportó mejor? ¿Por qué?
- Arme las Tn(n) para cada algoritmo. calculé el T(n) = T1(n) + T2(n) + T3(n) + T4(n). Indique cual es el mejor y peor caso para T(n) y cada Tn(n).
</details>
