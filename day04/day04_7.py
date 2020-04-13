'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

'''
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import sys

def click():
    print('hello')

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('信号和槽的绑定')

btn = QPushButton()
btn.setText('点我')
btn.setParent(w)
btn.clicked.connect(lambda :print('hello'))

w.show()

sys.exit(app.exec())
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import sys

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('使用系统的槽函数')

btn = QPushButton()
btn.setText('关闭窗口')
btn.setParent(w)
btn.clicked.connect(QApplication.quit)

w.show()

sys.exit(app.exec())