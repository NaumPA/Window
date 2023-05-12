import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QGridLayout
# from style import style
from test2 import SecondWindow
from sqlalchemy import *
from captcha import CaptchaDialog


class MainWindow(QMainWindow):

    def quit(self):
        quit()
    def __init__(self):
        super().__init__()
        self.setFixedSize(400,250)
        self.layout = QVBoxLayout()
        lbl = QLabel("Введите логин")
        self.Line = QLineEdit()
        lbl_2 = QLabel("Введите пароль")
        self.Line_2 = QLineEdit()
        self.lbl_3 = QLabel ("Неправильный логин или пароль")
        btn = QPushButton("Вход")
        btn_ss = QPushButton("Выход")
        lbl.setObjectName("lbl")
        btn_ss.clicked.connect(self.quit)
        btn.clicked.connect(self.btn_click)
        self.layout.addWidget(lbl)
        self.layout.addWidget(self.Line)
        self.layout.addWidget(lbl_2)
        self.layout.addWidget(self.Line_2)
        self.layout.addWidget(btn)
        self.layout.addWidget(btn_ss)
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)


    def btn_click(self):
        self.sw = SecondWindow()
        if self.Line.text() == "1" and self.Line_2.text() == "1":
            self.sw.show()

        else:
            self.window4 = CaptchaDialog()
            self.window4.show()





app = QApplication(sys.argv)
window = MainWindow()
window1 = SecondWindow()
window2 = CaptchaDialog()
window.show()
# app.setStyleSheet(style)
with open("style.css", "r") as wh:
    window.setStyleSheet(wh.read())
app.exec()
