from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit
from style import style
from PyQt6.QtGui import QPixmap
import time

a = "SVK2D"

class Captcha(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(200,200)

        self.layout = QVBoxLayout()
        lbl1 = QLabel("Введите каптчу : ")
        self.lbl = QLineEdit()
        photo = QLabel()
        pix = QPixmap("captcha.png")
        photo.setPixmap(pix)
        btn = QPushButton("Готово")
        self.lbl5 = QLabel("При вводе неправильной катпчи, потоврный ввод доступен только через 5 секунд")

        self.lbl.setObjectName("lbl_sw")

        self.layout.addWidget(lbl1)
        self.layout.addWidget(self.lbl)
        self.layout.addWidget(btn)
        self.layout.addWidget(photo)
        btn.clicked.connect(self.quit)
        self.layout.addWidget(self.lbl5)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
    def quit(self):
        if self.lbl.text() == a:
            self.close()
        else:
            time.sleep(5)

# class Capthalogin(QWidget):
#     counter = 0
#     acess = True
#     def update_timer(self, timer):
#         self.attempt.setText(f"Ваша программа заблокированна на {self.total_seconds} секунд")
#         if self.total_seconds == timer:
#             self.attempt.setText("")
#             self.timeq.stop()
#             self.acess = True
#         self.total_seconds -=1

#     def captha_timer(self, timer):
#         self.total_seconds = timer
#         self.timeq = QTimer (self)
#         self.timeq.setInterval(1000)
#         self.timeq.timeout.connect(functools.partial(self.update_timer, 0))
#         self.timeq.start()


#     def quit(self, captcha):
#         if self.acess:
#             self.timer =3

#         else:
#             self.counter +=1
#             if self.counter == 2:
#                 self.timer = 3
#             elif self.counter == 3:
#                 self.timer = 5
#             elif self.counter > 3:
#                 self.timer = 10
#         if self.timer > 0:
#             self.acess = False
#             self.captha_timer(self.timer)

#     def closeEvent(self,e):
#         if(not self.acess):
#             e.ignore()


