from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication, QPushButton, QCheckBox
import sys
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PySide2 import QtGui



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        uic.loadUi('тест на темперамент.ui', self)

    def initUI(self):
        self.setWindowTitle('тест')