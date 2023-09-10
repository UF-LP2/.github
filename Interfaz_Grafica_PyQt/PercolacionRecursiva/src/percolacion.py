from PyQt6.QtWidgets import QMainWindow, QSpinBox, QWidget, QPushButton, QGridLayout, QSlider, QLabel
from PyQt6.QtCore import Qt
from src.painter import Painter
import random

class Window(QMainWindow):
	"""Widget que representa mi ventana principal"""

	# Declaración de los widgets
	__SBTam=None
	__painter=None
	__botonGenerarMatriz=None
	__SLProbabilidad=None
	__botonPercolar=None
	__labelPercolacion=None
	__labelProbabilidad=None
	__labelTamMatriz=None

	# Declaración de las variables
	__title=None
	__top=None
	__left=None
	__width=None
	__height=None
	__matriz=None
	__tam=0

	def __init__(self):
		super().__init__()

		# Inicializacion de variables
		self.__title="Percolación"
		self.__top=150
		self.__left=150
		self.__width=500
		self.__height=350

		# Inicializacion de widgets
		self.__SBTam=QSpinBox()
		self.__painter=Painter()
		self.__botonGenerarMatriz=QPushButton()
		self.__botonPercolar=QPushButton()
		self.__SLProbabilidad=QSlider()
		self.__labelPercolacion=QLabel("")
		self.__labelTamMatriz=QLabel("Tamaño de la matriz:")
		self.__labelProbabilidad=QLabel("Probabilidad:")

		# Geometria de la ventana principal
		self.setWindowTitle(self.__title)
		self.setGeometry(self.__top, self.__left, self.__width, self.__height)

		# declaro e inicializo el widget central y el layout
		widgetCentral=QWidget(self)
		layout=QGridLayout()

		# Configuracion del layout
		layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

		# Configuraciones del SpinBox tamaño matriz
		self.__SBTam.setGeometry(500-120, 0, 120, 20)
		self.__SBTam.setMaximum(50)
		self.__SBTam.setMinimum(10)

		# Configuraciones del slider probabilidad
		self.__SLProbabilidad.setOrientation(Qt.Orientation.Horizontal)
		self.__SLProbabilidad.setMaximum(10)
		self.__SLProbabilidad.setMinimum(1)
		self.__SLProbabilidad.setPageStep(1)
		self.__SLProbabilidad.setMinimumSize(120, 20)
		self.__SLProbabilidad.setMaximumSize(400, 20)
		self.__SLProbabilidad.setValue(4)

		# Configuraciones del label percolacion
		self.__labelPercolacion.setMaximumSize(500,20)

		# Configuraciones del label tamaño matriz
		self.__labelTamMatriz.setMaximumSize(150,20)

		# Configuraciones del label probabilidad
		self.__labelProbabilidad.setMaximumSize(150,20)

		# Configuraciones del painter
		self.__painter.setGeometry(0, 0, 300, 300)

		# Configuraciones del botonGenerarMatriz
		self.__botonGenerarMatriz.setGeometry(500-120, 35, 120, 20)
		self.__botonGenerarMatriz.setText("Generar Matriz")

		# Configuraciones del botonPercolar
		self.__botonPercolar.setMaximumSize(400, 20)
		self.__botonPercolar.setMinimumSize(120, 20)
		self.__botonPercolar.setText("Percolar")
		self.__botonPercolar.setEnabled(False)

		# Conexiones
		self.__botonGenerarMatriz.clicked.connect(self._BotonGenerarMatriz)
		self.__botonPercolar.clicked.connect(self._BotonPercolar)

		# Agrego los widgets al layout
		layout.addWidget(self.__painter, 0, 0, 7, 1)
		layout.addWidget(self.__labelPercolacion, 8, 0, 1, 1)
		layout.addWidget(self.__labelTamMatriz, 0, 1, 1, 1)
		layout.addWidget(self.__SBTam, 1, 1, 1, 1)
		layout.addWidget(self.__labelProbabilidad, 2, 1, 1, 1)
		layout.addWidget(self.__SLProbabilidad, 3, 1, 1, 1)
		layout.addWidget(self.__botonGenerarMatriz, 4, 1, 1, 1)
		layout.addWidget(self.__botonPercolar, 5, 1, 1, 1)
		layout.setColumnStretch(0, 3)
		layout.setRowStretch(6, 0)

		# Configuraciones del widget central y del layout
		widgetCentral.setLayout(layout)
		self.setCentralWidget(widgetCentral)

	def __percolar(self, posx: int, posy: int):
		# Condiciones de salida (Que los valores de "x" e "y" excedan el tama?o de la matriz o que la matriz en la posici?n dada sea != 0)
		if (posx < 0 or posy < 0 or posx >= self.__tam or posy >= self.__tam or self.__matriz[posx][posy] != 0):
			return

		# Asignamos un valor 2 en la posici?n "x" e "y" de la matriz que sera representado como agua
		self.__matriz[posx][posy] = 2

		#Pasamos a las posiciones adyacentes
		self.__percolar(posx, posy + 1)
		self.__percolar(posx + 1, posy)
		self.__percolar(posx - 1, posy)
		self.__percolar(posx, posy - 1)

	def _BotonGenerarMatriz(self):
		self.__tam=self.__SBTam.value()
		self.__matriz=[ [ None for y in range(self.__tam) ] for x in range(self.__tam) ]
		probabilidad=self.__SLProbabilidad.value()/10

		for i in range(0,self.__tam):
			for j in range(0, self.__tam):
				#Genera un numero aleatorio entre 0 y 10 que dividido 10 nos da un valor entre 0 y 1
				if(random.randrange(0, 10)/10.0 <= probabilidad):
					self.__matriz[i][j] = 0
				else:
					self.__matriz[i][j] = 1

		self.__painter.setMatriz(self.__matriz)

		self.__labelPercolacion.setText("")

		self.__botonPercolar.setEnabled(True)

	def _BotonPercolar(self):
		for i in range(0, self.__tam):
			if (self.__matriz[i][0] == 0):
				self.__percolar(i, 0)

		self.__painter.update()

		flag=False
		for i in range(0, len(self.__matriz)):
			if(self.__matriz[i][-1]==2):
				flag=True

		if(flag):
			self.__labelPercolacion.setStyleSheet("color: green; font-weight: bold")
			self.__labelPercolacion.setText("Hay percolación ✓")
		else:
			self.__labelPercolacion.setStyleSheet("color: red; font-weight: bold")
			self.__labelPercolacion.setText("No hay percolación ❌")

		self.__botonPercolar.setEnabled(False)