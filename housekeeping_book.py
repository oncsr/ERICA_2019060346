import time
import sys
#from PyQt5.QtWidgets import QWidget
#from PyQt5.QtWidgets import QLabel
#from PyQt5.QtWidgets import QLineEdit
#from PyQt5.QtWidgets import QBoxLayout
#from PyQt5.QtWidgets import QPushButton
#from PyQt5.QtWidgets import QTabWidget
#from PyQt5.QtWidgets import QApplication

#from PyQt5.QtCore import Qt
#from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def CurrentTime():			#	현재 시간
	cur = time.gmtime(time.time())
	real = str(cur.tm_year) + '/' + str(cur.tm_mon) + '/' + str(cur.tm_mday) + ' ' + str(cur.tm_hour) + ':' + str(cur.tm_mday) + ':' + str(cur.tm_sec)
	return real

class FirstTab(QWidget):	#	입력 탭
	def __init__(self):
		super(FirstTab, self).__init__()
		self.init_widget()

	def init_widget(self):
		pb_1 = QPushButton()
		pb_2 = QPushButton()

		le_1 = QLineEdit()
		le_2 = QLineEdit()

		lb_1 = QLabel()
		lb_2 = QLabel()

		pb_1.setText("등록")
		pb_2.setText("등록")

		lb_1.setText("지출")
		lb_2.setText("수입")
		
		blank_1 = QLabel()
		blank_2 = QLabel()

		layout_1 = QBoxLayout(QBoxLayout.LeftToRight, self)
		layout_2 = QBoxLayout(QBoxLayout.TopToBottom)
		layout_3 = QBoxLayout(QBoxLayout.TopToBottom)
		
		layout_2.addWidget(lb_1)
		layout_2.addWidget(le_1)
		layout_2.addWidget(lb_2)
		layout_2.addWidget(le_2)

		layout_3.addWidget(blank_1)
		layout_3.addWidget(pb_1)
		layout_3.addWidget(blank_2)
		layout_3.addWidget(pb_2)
		
#		layout_3.addWidget(blank_1)
#		layout_3.addWidget(blank_2)

		layout_1.addLayout(layout_2)
		layout_1.addLayout(layout_3)

class SecondTab(QWidget):
	def __init__(self):
		super(SecondTab, self).__init__()
		self.init_widget()

	def init_widget(self):
		lb_1 = QLabel()
		lb_2 = QLabel()
		cur_time_lb = QLabel()
		cur_time_lb.setText("{}".format(CurrentTime()))
		lb_1.setText("지출 : ")
		lb_2.setText("수입 : ")

		layout_1 = QBoxLayout(QBoxLayout.LeftToRight, self)
		layout_2 = QBoxLayout(QBoxLayout.TopToBottom)
		layout_3 = QBoxLayout(QBoxLayout.TopToBottom)
		
		layout_2.addWidget(cur_time_lb)
		layout_2.addWidget(lb_1)
		layout_2.addWidget(lb_2)

		layout_1.addLayout(layout_2)
		layout_1.addLayout(layout_3)


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)
		self.setFixedWidth(640)
		self.setFixedHeight(480)
		self.tab = QTabWidget()
		
		self.init_widget()

	def init_widget(self):
		self.setWindowTitle("가계부")
		
		form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
		self.setLayout(form_lbx)
		form_lbx.addWidget(self.tab)

		self.tab.addTab(FirstTab(), "입력")
		self.tab.addTab(SecondTab(), "내역 확인")


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())
