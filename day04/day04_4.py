'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

'''
from PyQt5.QtWidgets import QWidget,QApplication,QLabel
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import sys

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('文本展示')
label = QLabel()
label.setText('第一个文本')
label.setParent(w)
w.show()
sys.exit(app.exec())
'''

from PyQt5.QtWidgets import QWidget,QApplication,QLabel
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon,QPixmap
import sys

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('图片展示')
label = QLabel()
pixmap = QPixmap('i.jpg')
label.setPixmap(pixmap)
label.setParent(w)
w.resize(pixmap.width(),pixmap.height())
w.show()
sys.exit(app.exec())