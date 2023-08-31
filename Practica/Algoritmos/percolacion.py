import random

tam=20
matriz=[ [ None for y in range(tam) ] for x in range(tam) ]
probabilidad=0.5

def percolar(posx: int, posy: int):
	# Condiciones de salida (Que los valores de "x" e "y" excedan el tama?o de la matriz o que la matriz en la posici?n dada sea != 0)
	if (posx < 0 or posy < 0 or posx >= tam or posy >= tam or matriz[posx][posy] != 0):
		return
	
	# Asignamos un valor 2 en la posici?n "x" e "y" de la matriz que sera representado como agua
	matriz[posx][posy] = 2

	#Pasamos a las posiciones adyacentes
	percolar(posx, posy + 1)
	percolar(posx + 1, posy)
	percolar(posx - 1, posy)
	percolar(posx, posy - 1)


def main():
	for i in range(0,tam):
		for j in range(0, tam):
			#Genera un numero aleatorio entre 0 y 10 que dividido 10 nos da un valor entre 0 y 1
			if(random.randrange(0, 10)/10.0 <= probabilidad):
				matriz[i][j] = 0
			else:
				matriz[i][j] = 1
	
	for elemento in matriz:
		print(elemento)
	
	for i in range(0, tam):
		if (matriz[0][i] == 0):
			percolar(0, i)
	
	print("\n\n\n\n\n")
	
	for elemento in matriz:
		print(elemento)

if __name__=='__main__':
	main()