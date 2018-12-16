from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication, QPushButton, QCheckBox
import sys
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PySide2 import QtGui
from time import sleep


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        uic.loadUi('тест на темперамент.ui', self)
        self.n = 1

    def initUI(self):
        self.setWindowTitle('тест')
       # self.color.clicked.connect(self.change_color())

    def change_color(self):
        self.n += 1
        if self.n % 4 == 0:
            self.setBackground(QtGui.QColor('000000', 100))
            self.start_buton.setBackground(QtGui.QColor('2f4f4f', 100))
            self.start_buton.setFont(QtGui.QColor('ffa07a', 100))
            self.Messanges.setFont(QtGui.QColor('ffa07a', 100))
        elif self.n % 3 == 0:
            self.setBackground(QtGui.QFont('f4a460', 100))
            self.start_buton.setBackground(QtGui.QColor('b22222', 100))
            self.start_buton.setFont(QtGui.QColor('White', 100))
            self.Messanges.setFont(QtGui.QColor('White', 100))
        elif self.n % 2 == 0:
            self.setBackground(QtGui.QColor('1e90ff', 10))
            self.start_buton.setBackground(QtGui.QColor('da70d6', 100))


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
ex.change_color()
