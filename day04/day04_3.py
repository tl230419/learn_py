'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

'''
from PyQt5.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)
w = QWidget()
w.show()
sys.exit(app.exec())
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import sys

app = QApplication(sys.argv)
w = QWidget()
#w.setWindowTitle('黑马窗口')
#icon = QIcon('qq.png')
#w.setWindowIcon(icon)
w.setWindowTitle('气泡提示窗口')
w.setToolTip('这是一个气泡提示的窗口')
w.show()
sys.exit(app.exec())


