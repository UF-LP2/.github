def mayor(lista: list[int]) -> int:
	"""Mayor es una funcion vortice para llamar a la funcion recursiva mayorDyV
	con los parametros de entrada inicio=1 y fin=largo del vector.

	Args:
		lista (list[int]): Lista de n elementos enteros.

	Returns:
		int: Mayor elemento de la lista
	"""

	if (len(lista)>0):
		# Llamada al Algoritmo "Divide y Venceras". retorno del resultado.
		return mayorDyV(lista, 1, len(lista))
	else:
		return 0


def mayorDyV(lista: list[int], inicio: int, fin: int) -> int:
	"""Función recursiva (DyV) para obtener el número mas grande del subvector dado.

	Args:
		lista (list[int]): Lista de n elementos enteros.
		inicio (int): inicio de la sublista
		fin (int): fin de la sublista

	Returns:
		int: Mayor elemento de la sublista
	"""

	# Se evalúa en inicio-1 o fin-1 porque recuerden que las posiciones de los arreglos inician en 0 y terminan en largo-1
	# y nuestras posiciones de inicio y fin van desde 1 hasta el largo, esto es para poder realizar el cálculo de la mitad de forma correcta.
	
	# Caso base Nro 1: Que sea un único elemento en la rama a analizar.
	if (fin-inicio == 0):
		return lista[inicio-1]
	# Caso base Nro 2: Que queden 2 elementos en la rama a analizar.
	elif (fin-inicio == 1):
		if (lista[inicio-1] >= lista[fin-1]):
			return lista[inicio-1]
		else: return lista[fin-1]
	
	# Si no se cumple ninguno de los dos casos bases
	# entonces vuelvo a dividir a la mitad
	# obteniendo otra subrama izquierda y otra derecha.
	
	mitad: int = int(((fin-inicio)/2)+inicio) # En python tengo que castear el resultado de la división para quedarme con la parte entera.
	aux1: int = mayorDyV(lista, inicio, mitad)
	aux2: int = mayorDyV(lista, mitad+1, fin)
	
	# Cuando vuelvo de las llamadas anteriores
	# comparo el resultado de ambas ramas y devuelvo el mayor.
	if (aux1 > aux2):
		return aux1
	else:
		return aux2

def main() -> int:
	mi_lista=[1, 8, 1, 10, 40, 2, 31, 14, 38]
	
	print(str(mi_lista)+"\nEl mayor es: "+str(mayor(mi_lista)))
	
	return 0

if __name__=='__main__':
	main()