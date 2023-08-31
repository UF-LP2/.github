def hanoi( n, origen,  intermedio,  destino):
    if (n>=1):
        hanoi((n-1),origen,intermedio,destino)
        print("Mover plato "+str(n)+" desde "+ origen+" a "+ intermedio)
        hanoi((n-1),destino,intermedio,origen)
        print("Mover plato "+str(n)+" desde "+ intermedio+" a "+ destino)
       
        hanoi((n-1),origen,intermedio,destino)

if __name__ == '__main__':
    n = 5
    hanoi(n,"a","b","c")


