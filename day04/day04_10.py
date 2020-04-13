'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import sys

def func(checked):
    #状态变化的槽函数
    #:param checked: 是否被选中
    #:return:
    print('状态变化', checked)

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('单选框')

layout = QHBoxLayout()
w.setLayout(layout)

rb1 = QRadioButton('男')
rb2 = QRadioButton('女')
rb1.setChecked(True)
layout.addWidget(rb1)
layout.addWidget(rb2)

rb1.toggled.connect(func)

w.show()

sys.exit(app.exec())
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import sys

def func(state):
    if state == 2:
        print('选中')
    else:
        print('取消选中')

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('复选框')

layout = QHBoxLayout()
w.setLayout(layout)

label = QLabel()
label.setText('爱好：')
ck1 = QCheckBox('抽烟')
ck2 = QCheckBox('喝酒')
ck3 = QCheckBox('烫头')

layout.addWidget(label)
layout.addWidget(ck1)
layout.addWidget(ck2)
layout.addWidget(ck3)

ck1.stateChanged.connect(func)

w.show()

sys.exit(app.exec())