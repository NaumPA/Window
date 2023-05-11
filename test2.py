from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from style import style


class SecondWindow(QMainWindow):
    def quit(self):
        self.close()
    def __init__(self):
        super().__init__()
        self.resize(350,200)

        layout = QVBoxLayout()
        lbl = QLabel("Добро пожаловать в приложение")
        btn = QPushButton("Выйти из приложения")

        lbl.setObjectName("lbl_sw")

        layout.addWidget(lbl)
        layout.addWidget(btn)

        btn.clicked.connect(self.quit)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


