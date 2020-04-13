'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import sys

def func():
    pass

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('普通按钮')

btn = QPushButton()
btn.setText('登录')
btn.setToolTip('登录按钮')
btn.setParent(w)

w.show()

sys.exit(app.exec())