#Algoritmo iterativo para saber si la raiz de un numero es un numero entero.
#  O sea, si es un CUADRADO PERFECTO.

def esCuadradoPerfectoIterativo(n)-> bool:
    # Se empieza con numero impar numero 1
    impar = 1
 
    # loop hasta que n sea 0 o negativo
    while n > 0:
        n = n - impar        
        impar = impar + 2      
 
    # si n=0, es porque es un cuadrado perfecto!
    return n == 0
#Orden O(n)
# Algoritmo de busqueda binaria (BB) 


def esCuadradoPerfectoBB(n) -> bool:
    # Seteo de busqueda entre [0, n].
    min, max = 0, n
    while min <= max:
        medio= int(min + ((max - min) / 2))        # Calculo del valor medio 
        # Si medio * medio == n, ya esta
        if medio * medio == n:
            return True
        # Si medio * medio < n, se actualiza el minimo a medio + 1
        if medio * medio < n:
            min = medio + 1
        # Si medio * medio > n, se actualiza el max a medio - 1 
        else:
            max = medio - 1
 
    # si min>max, sale del while y no es cuadrado perfecto
    return False

# De que orden es este algoritmo?
 #O(log (n))

if __name__ == '__main__':
    n =25
    print(esCuadradoPerfectoIterativo(n))

