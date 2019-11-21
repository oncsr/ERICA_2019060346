import sys
from PyQt5 import QtWidgets ,uic

class Form(QtWidgets.QDialog):
	def __init__(self):
		super().__init__()
		self.ui = uic.loadUi("myfirst.ui")
		self.ui.show()

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	w = Form()
	sys.exit(app.exec())
