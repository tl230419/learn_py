'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

'''
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import sys

app = QApplication(sys.argv)
w = QWidget()
#w.setWindowTitle('水平布局')
w.setWindowTitle('竖直布局')

btn1 = QPushButton('1')
btn2 = QPushButton('2')
btn3 = QPushButton('3')
btn4 = QPushButton('4')
btn5 = QPushButton('5')

#layout = QHBoxLayout()
layout = QVBoxLayout()
w.setLayout(layout)
layout.addWidget(btn1)
layout.addWidget(btn2)
layout.addWidget(btn3)
layout.addWidget(btn4)
layout.addWidget(btn5)

w.show()

sys.exit(app.exec())
'''

'''
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit, QPushButton,QFormLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import sys

def func():
    name = name_edit.text()
    age = int(age_edit.text())
    phone = phone_edit.text()
    print('姓名：%s,年纪：%d,电话：%s'%(name, age, phone))

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('表单布局')

layout = QFormLayout()
w.setLayout(layout)

name_edit = QLineEdit()
age_edit = QLineEdit()
phone_edit = QLineEdit()
btn = QPushButton('发送')

layout.addRow('姓名', name_edit)
layout.addRow('年纪', age_edit)
layout.addRow('电话', phone_edit)
layout.addRow('', btn)

btn.clicked.connect(func)

w.show()

sys.exit(app.exec())
'''

from PyQt5.QtWidgets import QApplication,QWidget, QPushButton,QHBoxLayout,QVBoxLayout,QFormLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import sys

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('嵌套布局')

whole_layout = QHBoxLayout()
w.setLayout(whole_layout)

layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()
layout4 = QVBoxLayout()
layout5 = QVBoxLayout()

whole_layout.addLayout(layout1)
whole_layout.addLayout(layout2)
whole_layout.addLayout(layout3)
whole_layout.addLayout(layout4)
whole_layout.addLayout(layout5)

btn1 = QPushButton('1')
btn2 = QPushButton('2')
btn3 = QPushButton('3')
btn4 = QPushButton('4')
btn5 = QPushButton('5')
btn6 = QPushButton('6')
btn7 = QPushButton('7')
btn8 = QPushButton('8')
btn9 = QPushButton('9')
btn10 = QPushButton('10')
btn11 = QPushButton('11')
btn12 = QPushButton('12')

layout1.addWidget(btn1)
layout1.addWidget(btn2)

layout2.addWidget(btn3)
layout2.addWidget(btn4)

layout3.addWidget(btn5)
layout3.addWidget(btn6)

layout4.addWidget(btn7)
layout4.addWidget(btn8)

layout5.addWidget(btn9)
layout5.addWidget(btn10)

layout5.addWidget(btn11)
layout5.addWidget(btn12)

w.show()

sys.exit(app.exec())
