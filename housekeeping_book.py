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

class FirstTab(QWidget):	#	가계부 탭
	def __init__(self):
		super(FirstTab, self).__init__()
		self.init_widget()

	def init_widget(self):
		pb_1 = QPushButton()
		pb_2 = QPushButton()
		pb_1.setText("등록")
		pb_2.setText("등록")

		le_1 = QLineEdit()
		le_2 = QLineEdit()
		
		le_3 = QLineEdit()
		le_4 = QLineEdit()
	
		le_1.setMaximumWidth(400)
		le_2.setMaximumWidth(400)	

		lb_1 = QLabel()
		lb_2 = QLabel()
		lb_3 = QLabel()
		lb_4 = QLabel()
		lb_5 = QLabel()
		lb_6 = QLabel()
		lb_1.setText("----------------  수입")
		lb_2.setText("----------------  지출")
		lb_3.setText("내용  ")
		lb_4.setText("금액  ")
		lb_5.setText("내용  ")
		lb_6.setText("금액  ")
		lb_3.setMaximumHeight(30)
		
		blank_1 = QLabel()
		blank_2 = QLabel()

		layout_1 = QBoxLayout(QBoxLayout.LeftToRight, self)
		layout_2 = QBoxLayout(QBoxLayout.TopToBottom)
		layout_3 = QBoxLayout(QBoxLayout.TopToBottom)
		
		layout_2.addWidget(lb_1)
		layout_2.addWidget(lb_3)
		layout_2.addWidget(le_1)
		layout_2.addWidget(lb_4)
		layout_2.addWidget(le_3)
		layout_2.addWidget(lb_2)
		layout_2.addWidget(lb_5)
		layout_2.addWidget(le_2)
		layout_2.addWidget(lb_6)
		layout_2.addWidget(le_4)

		layout_3.addWidget(blank_1)
		layout_3.addWidget(pb_1)
		layout_3.addWidget(blank_2)
		layout_3.addWidget(pb_2)
		
		layout_1.addLayout(layout_2)
		layout_1.addLayout(layout_3)
		
		layout_4 = QBoxLayout(QBoxLayout.LeftToRight)
		


"""

class SecondTab(QWidget):
	def __init__(self):
		super(SecondTab, self).__init__()
		self.inc = 0
		self.outc = 0
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

	def outcome(self):
				
"""

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


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())
