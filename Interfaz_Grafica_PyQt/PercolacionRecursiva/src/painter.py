from PyQt6.QtWidgets import QWidget, QSizePolicy
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import Qt

class Painter(QWidget):
	"""Widget que dibuja una matriz"""

	__matriz=[[None]]
	
	def __init__(self):
		super().__init__()

		self.setSizePolicy(
			QSizePolicy.Policy.MinimumExpanding,
			QSizePolicy.Policy.MinimumExpanding
		)
		self.__painter=QPainter()
		self.__painter.setPen(QPen(QColor(0,0,0), 1))
		
	def setMatriz(self, mat):
		"""Seter de la matriz

		Args:
			mat ([[int]]): Matriz a dibujar
		"""
		self.__matriz=mat
		self.update()

	def paintEvent(self, e):
		"""paintEvent es un evento que se llama automaticamente cuando se realiza un update del widget

		Args:
			e (_type_): recibe un QPaintEvent
		"""

		# Obtengo el largo de mi matriz
		largo=len(self.__matriz)

		# Chequeo el alto y el ancho del widget para obtener
		# la proporcion que debene tener mis cuadrados
		# para que se muestren en la ventana y se pueda hacer un resize
		if (self.width() > self.height()):
			tamSize = int(self.height() / largo)
		else:
			tamSize = int(self.width() / largo)

		# Dibujo mi matriz
		self.__painter.begin(self)
		for i in range(0,largo):
			for j in range(0,largo):
				self.__painter.drawRect(tamSize*i,tamSize*j,tamSize,tamSize)
				if(self.__matriz[i][j]==1):
					self.__painter.fillRect(tamSize*i+1, tamSize*j+1, tamSize-1, tamSize-1, Qt.GlobalColor.black)
				elif(self.__matriz[i][j]==2):
					self.__painter.fillRect(tamSize*i+1, tamSize*j+1, tamSize-1, tamSize-1, Qt.GlobalColor.blue)
		self.__painter.end()