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

def delete_user():
    result = QMessageBox.question(w, '提示', '确认要删除好基友吗？',
        QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)
    if result == QMessageBox.Ok:
        print('确认删除')
    elif result == QMessageBox.Cancel:
        print('取消删除')

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('对话框')

btn = QPushButton('删除用户')
btn.setParent(w)
btn.clicked.connect(delete_user)

w.show()

sys.exit(app.exec())
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import sys

def func():
    str,success = QInputDialog.getText(w, '提示', '请输入角色名称')
    if success:
        edit.setText(str)

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('输入提示框')

layout = QHBoxLayout()
w.setLayout(layout)

btn = QPushButton('创建角色')
btn.clicked.connect(func)
edit = QLineEdit()
layout.addWidget(btn)
layout.addWidget(edit)

w.show()

sys.exit(app.exec())