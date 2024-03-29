import time
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def CurrentTime():			#	현재 시간
	cur = time.gmtime(time.time())
	real = str(cur.tm_year) + '/' + str(cur.tm_mon) + '/' + str(cur.tm_mday) + ' ' + str(cur.tm_hour) + ':' + str(cur.tm_mday) + ':' + str(cur.tm_sec)
	return real

def CurrentDay(fake):			#	현재 날짜
	return fake.split(' ')[0]

class FirstTab(QWidget):	#	가계부 탭
	def __init__(self):
		super(FirstTab, self).__init__()
		self.init_widget()

	def init_widget(self):
		pb_1 = QPushButton()
		pb_2 = QPushButton()
		pb_1.setText("등록")
		pb_2.setText("등록")
		
		self.le_1 = QLineEdit()
		self.le_2 = QLineEdit()
		
		self.le_3 = QLineEdit()
		self.le_4 = QLineEdit()
		
		self.le_1.setMaximumWidth(400)
		self.le_2.setMaximumWidth(400)	
		
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
		
		self.tw_1 = QTreeWidget(self)
		self.tw_1.setColumnCount(3)
		self.tw_1.setHeaderLabels(["Date","Contents","Money"])
		self.tw_2 = QTreeWidget(self)
		self.tw_2.setColumnCount(3)
		self.tw_2.setHeaderLabels(["Date","Contents","Money"])
		self.root_1 = self.tw_1.invisibleRootItem()
		self.root_2 = self.tw_2.invisibleRootItem()
		
		layout_1 = QBoxLayout(QBoxLayout.LeftToRight, self)
		layout_2 = QBoxLayout(QBoxLayout.TopToBottom)
		layout_3 = QBoxLayout(QBoxLayout.TopToBottom)
		
		layout_2.addWidget(lb_1)
		layout_2.addWidget(lb_3)
		layout_2.addWidget(self.le_1)
		layout_2.addWidget(lb_4)
		layout_2.addWidget(self.le_3)
		layout_2.addWidget(lb_2)
		layout_2.addWidget(lb_5)
		layout_2.addWidget(self.le_2)
		layout_2.addWidget(lb_6)
		layout_2.addWidget(self.le_4)
		
		layout_3.addWidget(self.tw_1)
		layout_3.addWidget(pb_1)
		layout_3.addWidget(self.tw_2)
		layout_3.addWidget(pb_2)
		
		layout_1.addLayout(layout_2)
		layout_1.addLayout(layout_3)
		
		self.twadd()
		
		pb_1.clicked.connect(self.income)
		pb_1.clicked.connect(self.twadd)
		pb_2.clicked.connect(self.outcome)
		pb_2.clicked.connect(self.twadd)

	def twadd(self):
		f = open("income.txt","r")
		for i in f:
			item = QTreeWidgetItem()
			fdate, text, money = i.split(',')
			date = CurrentDay(fdate)
			item.setText(0, date)
			item.setText(1, text)
			item.setText(2, money)
			self.root_1.addChild(item)
		
		f.close()
		t = open("outcome.txt","r")
		for j in t:
			item = QTreeWidgetItem()
			fdate, text, money = j.split(',')
			date = CurrentDay(fdate)
			item.setText(0, date)
			item.setText(1, text)
			item.setText(2, money)
			self.root_2.addChild(item)

		t.close()

	def income(self):
		f = open("income.txt","a")
		text = CurrentTime() + "," + self.le_1.text() + "," + self.le_3.text() + "\n"
		f.write(text)
		f.close()
		self.le_1.setText("")
		self.le_3.setText("")

	def outcome(self):
		f = open("outcome.txt","a")
		text = CurrentTime() + "," + self.le_2.text() + "," + self.le_4.text() + "\n"
		f.write(text)
		f.close()
		self.le_2.setText("")
		self.le_4.setText("")


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
