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
		self.multi = QPushButton()
		self.parti = QPushButton()
		self.le = QLineEdit()
		self.lb_bool = QLabel()
		
		self.setWindowTitle("Basic Calculator")
		self.setGeometry(300, 300, 300, 200)

		self.plus.setText("+")
		self.minus.setText("-")
		self.multi.setText("*")
		self.parti.setText("/")
		
		self.plus.setMaximumWidth(50)
		self.plus.setMinimumHeight(50)
		self.minus.setMaximumWidth(50)
		self.minus.setMinimumHeight(50)
		self.multi.setMaximumWidth(50)
		self.multi.setMinimumHeight(50)
		self.parti.setMaximumWidth(50)
		self.parti.setMinimumHeight(50)

		self.lay1 = QBoxLayout(QBoxLayout.TopToBottom)
		self.lay2 = QBoxLayout(QBoxLayout.LeftToRight)
		self.lay3 = QBoxLayout(QBoxLayout.LeftToRight)
		
		self.lay0 = QBoxLayout(QBoxLayout.LeftToRight)
		self.lay1.addLayout(self.lay0)

		self.plus.clicked.connect(self.Plus)
		self.minus.clicked.connect(self.Minus)
		self.multi.clicked.connect(self.Multi)
		self.parti.clicked.connect(self.Parti)

		self.lay0.addWidget(self.lb)
		self.lay0.addWidget(self.lb_bool)
		self.lay1.addWidget(self.le)
		self.lay2.addWidget(self.plus)
		self.lay2.addWidget(self.minus)
		self.lay3.addWidget(self.multi)
		self.lay3.addWidget(self.parti)

		form_lbx = QBoxLayout(QBoxLayout.TopToBottom, self)
		self.setLayout(form_lbx)
		form_lbx.addLayout(self.lay1)
		form_lbx.addLayout(self.lay2)
		form_lbx.addLayout(self.lay3)

	def Plus(self):
		try:
			self.cnt = self.cnt + float(self.le.text())
			self.lb.setText("ans : " + str(self.cnt))
			self.lb_bool.setText("")
			self.le.setText("")
		except ValueError:
			self.lb_bool.setText("enter correct value")
			self.le.setText("")

	def Minus(self):
		try:
			self.cnt = self.cnt - float(self.le.text())
			self.lb.setText("ans : " + str(self.cnt))
			self.lb_bool.setText("")
			self.le.setText("")
		except ValueError:
			self.lb_bool.setText("enter correct value")
			self.le.setText("")

	def Multi(self):
		try:
			self.cnt = self.cnt * float(self.le.text())
			self.lb.setText("ans : " + str(self.cnt))
			self.lb_bool.setText("")
			self.le.setText("")
		except ValueError:
			self.lb_bool.setText("enter correct value")
			self.le.setText("")

	def Parti(self):
		try:
			self.cnt = self.cnt / float(self.le.text())
			self.lb.setText("ans : " + str(self.cnt))
			self.lb_bool.setText("")
			self.le.setText("")
		except ValueError:
			self.lb_bool.setText("enter correct value")
			self.le.setText("")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())
