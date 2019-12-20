import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)
		self.cnt = 0
		self.lb = QLabel(str(self.cnt))
		self.plus = QPushButton()
		self.minus = QPushButton()
		self.le = QLineEdit()
		
		self.setWindowTitle("Basic Calculator")
		self.setGeometry(300, 300, 300, 200)

		self.plus.setText("+")
		self.minus.setText("-")
		
		self.plus.setMaximumWidth(50)
		self.plus.setMinimumHeight(50)
		self.minus.setMaximumWidth(50)
		self.minus.setMinimumHeight(50)

		self.lay1 = QBoxLayout(QBoxLayout.TopToBottom)
		self.lay2 = QBoxLayout(QBoxLayout.LeftToRight)
		
		self.plus.clicked.connect(self.Plus)
		self.minus.clicked.connect(self.Minus)

		self.lay1.addWidget(self.lb)
		self.lay1.addWidget(self.le)
		self.lay2.addWidget(self.plus)
		self.lay2.addWidget(self.minus)

		form_lbx = QBoxLayout(QBoxLayout.TopToBottom, self)
		self.setLayout(form_lbx)
		form_lbx.addLayout(self.lay1)
		form_lbx.addLayout(self.lay2)

	def Plus(self):
		self.cnt = self.cnt + float(self.le.text())
		self.lb.setText("ans : " + str(self.cnt))

	def Minus(self):
		self.cnt = self.cnt - float(self.le.text())
		self.lb.setText("ans : " + str(self.cnt))
	

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())
