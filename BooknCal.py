import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class CalTab(QWidget):
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
		
		self.lb.setFont(QFont("Ubuntu",20))
		self.lb_bool.setFont(QFont("Ubuntu",15))

		self.plus.setText("+")
		self.minus.setText("-")
		self.multi.setText("*")
		self.parti.setText("/")
		
		self.plus.setFont(QFont("Ubuntu",70))
		self.minus.setFont(QFont("Ubuntu",70))
		self.multi.setFont(QFont("Ubuntu",70))
		self.parti.setFont(QFont("Ubuntu",70))
	
	
		self.plus.setFixedWidth(100)
		self.plus.setFixedHeight(100)
		self.minus.setFixedWidth(100)
		self.minus.setFixedHeight(100)
		self.multi.setFixedWidth(100)
		self.multi.setFixedHeight(100)
		self.parti.setFixedWidth(100)
		self.parti.setFixedHeight(100)

		self.lay1 = QBoxLayout(QBoxLayout.TopToBottom)
		self.lay2 = QBoxLayout(QBoxLayout.LeftToRight)
		
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
		self.lay2.addWidget(self.multi)
		self.lay2.addWidget(self.parti)

		form_lbx = QBoxLayout(QBoxLayout.TopToBottom, self)
		self.setLayout(form_lbx)
		form_lbx.addLayout(self.lay1)
		form_lbx.addLayout(self.lay2)

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



def CurrentTime():			#	현재 시간
	cur = time.gmtime(time.time())
	real = str(cur.tm_year) + '/' + str(cur.tm_mon) + '/' + str(cur.tm_mday) + ' ' + str(cur.tm_hour) + ':' + str(cur.tm_mday) + ':' + str(cur.tm_sec)
	return real

def CurrentDay(fake):			#	현재 날짜
	return fake.split(' ')[0]

class HouseBookTab(QWidget):	#	가계부 탭
	def __init__(self):
		super(HouseBookTab, self).__init__()
		self.init_widget()

	def init_widget(self):
		self.ivalerr = 0
		self.ovalerr = 0
	
		pb_1 = QPushButton()
		pb_2 = QPushButton()
		pb_1.setText("등록")
		pb_2.setText("등록")
		
		pb_1.setMaximumWidth(50)
		pb_2.setMaximumWidth(50)

		self.le_1 = QLineEdit()
		self.le_2 = QLineEdit()
		
		self.le_3 = QLineEdit()
		self.le_4 = QLineEdit()

		self.le_1.setMaximumWidth(200)
		self.le_2.setMaximumWidth(200)
		self.le_3.setMaximumWidth(200)
		self.le_4.setMaximumWidth(200)
		
		lb_1 = QLabel()
		lb_2 = QLabel()
		lb_3 = QLabel()
		lb_4 = QLabel()
		lb_5 = QLabel()
		lb_6 = QLabel()
		self.lb_7 = QLabel()
		self.lb_8 = QLabel()
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
		
		layout_1 = QBoxLayout(QBoxLayout.LeftToRight, self)
		layout_2 = QBoxLayout(QBoxLayout.TopToBottom)
		self.layout_3 = QBoxLayout(QBoxLayout.TopToBottom)
		
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
		
		self.layout_3.addWidget(self.lb_7)
		self.layout_3.addWidget(self.tw_1)
		self.layout_3.addWidget(pb_1)
		self.layout_3.addWidget(self.lb_8)
		self.layout_3.addWidget(self.tw_2)
		self.layout_3.addWidget(pb_2)
		
		layout_1.addLayout(layout_2)
		layout_1.addLayout(self.layout_3)
		
		self.twadd()
		
		pb_1.clicked.connect(self.income)
		pb_1.clicked.connect(self.twadd)
		pb_2.clicked.connect(self.outcome)
		pb_2.clicked.connect(self.twadd)

	def twadd(self):
		moneysum = 0
		self.root_1 = self.tw_1.invisibleRootItem()
		f = open("income.txt","r")
		for i in f:
			item = QTreeWidgetItem()
			fdate, text, money = i.split(',')
			date = CurrentDay(fdate)
			item.setText(0, date)
			item.setText(1, text)
			item.setText(2, money)
			self.root_1.addChild(item)
			moneysum += int(money)
		if(self.ivalerr == 1):
			self.lb_7.setText("enter correct money")
		else:
			self.lb_7.setText("수입 총액 : +{}".format(moneysum))
		f.close()

		moneysum = 0
		self.root_2 = self.tw_2.invisibleRootItem()
		t = open("outcome.txt","r")
		for j in t:
			item = QTreeWidgetItem()
			fdate, text, money = j.split(',')
			date = CurrentDay(fdate)
			item.setText(0, date)
			item.setText(1, text)
			item.setText(2, money)
			self.root_2.addChild(item)
			moneysum += int(money)
		if(self.ovalerr == 1):
			self.lb_8.setText("enter correct money")
		else:
			self.lb_8.setText("지출 총액 : -{}".format(moneysum))
		t.close()

	def income(self):
		try:
			int(self.le_3.text())
		except ValueError:
			self.le_1.setText("")
			self.le_3.setText("")
			self.ivalerr = 1
			return
		
		self.ivalerr = 0
		f = open("income.txt","a")
		text = CurrentTime() + "," + self.le_1.text() + "," + self.le_3.text() + "\n"
		f.write(text)
		f.close()
		self.le_1.setText("")
		self.le_3.setText("")

	def outcome(self):
		try:
			int(self.le_4.text())
		except ValueError:
			self.le_2.setText("")
			self.le_4.setText("")
			self.ovalerr = 1
			return
		
		self.ovalerr = 0
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
		self.setWindowTitle("가계부와 계산기")
		
		form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
		self.setLayout(form_lbx)
		form_lbx.addWidget(self.tab)

		self.tab.addTab(HouseBookTab(), "가계부")
		self.tab.addTab(CalTab(), "계산기")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())
