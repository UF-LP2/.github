def percolar(matriz: [[int]])->(bool, [[int]]):
	"""Ejecuta el algoritmo de percolacion

	Args:
		matriz ([[int]]): Matriz a percolar

	Returns:
		bool: Retorna si True si hay percolación y False en caso contrario
		[[int]]: Retorna La matriz percolada
	"""
	def __percolar(posx: int, posy: int):
		# Condiciones de salida (Que los valores de "x" e "y" excedan el tama?o de la matriz o que la matriz en la posici?n dada sea != 0)
		if (posx < 0 or posy < 0 or posx >= len(matriz) or posy >= len(matriz[0]) or matriz[posx][posy] != 0):
			return

		# Asignamos un valor 2 en la posici?n "x" e "y" de la matriz que sera representado como agua
		matriz[posx][posy] = 2

		#Pasamos a las posiciones adyacentes
		__percolar(posx, posy + 1)
		__percolar(posx + 1, posy)
		__percolar(posx - 1, posy)
		__percolar(posx, posy - 1)
	
	for i in range(0, len(matriz)):
		if (matriz[i][0] == 0):
			__percolar(i, 0)

	flag=False
	for i in range(0, len(matriz)):
		if(matriz[i][-1]==2):
			flag=True
	return flag, matriz