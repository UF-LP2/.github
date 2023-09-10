import sys
from PyQt6.QtWidgets import QApplication
from src.percolacion import Window

'''
Ejecución del programa
'''
if __name__=="__main__":
	app = QApplication(sys.argv)

	window = Window()
	window.show()
	sys.exit(app.exec())