'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

'''
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import sys

app = QApplication(sys.argv)
w = QWidget()

w.setWindowTitle('单行输入框')

edit = QLineEdit()
edit.setText('张三')
text = edit.text()

edit.setMaxLength(10)
edit.setParent(w)

w.show()

sys.exit(app.exec())
'''

from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import sys

app = QApplication(sys.argv)
w = QWidget()


w.setWindowTitle('多行输入框')

edit = QTextEdit()
edit.setPlainText('武汉疫情')
edit.clear()

edit.setParent(w)

w.show()

sys.exit(app.exec())