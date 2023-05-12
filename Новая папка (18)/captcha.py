from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QDialog, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QTimer
import time

a = "svk2d"

# class Captcha(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.resize(200,200)

#         self.layout = QVBoxLayout()
#         lbl1 = QLabel("Введите каптчу : ")
#         self.lbl = QLineEdit()
#         # photo = QLabel()
#         # pix = QPixmap("captcha.png")
#         # photo.setPixmap(pix)
#         btn = QPushButton("Готово")
#         self.lbl5 = QLabel("При вводе неправильной катпчи, потоврный ввод доступен только через 5 секунд")

#         self.lbl.setObjectName("lbl_sw")

#         self.layout.addWidget(lbl1)
#         self.layout.addWidget(self.lbl)
#         self.layout.addWidget(btn)
#         # self.layout.addWidget(photo)
#         btn.clicked.connect(self.quit)
#         self.layout.addWidget(self.lbl5)

#         widget = QWidget()
#         widget.setLayout(self.layout)
#         self.setCentralWidget(widget)
#     # def quit(self):
#     #     if self.lbl.text() == a:
#     #         self.close()
#     #     # else:
#     #     #     time.sleep(5)

#         self.captcha_dialog = CaptchaDialog(parent=self)
#         self.captcha_dialog.setModal(True)

#     def quit(self):
#         if self.lbl.text() == a:
#             self.close()
#         else:

#             self.captcha_dialog.start_timer()

#             if self.captcha_dialog.exec() == QDialog.DialogCode.Accepted:
#                 QMessageBox.information(self, "Успех", "Вход выполнен после капчи")

#             else:
#                 QMessageBox.warning(self, "Ошибка", "Неверные данные и капча")
#                 self.login_attempts = 0


class CaptchaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        photo = QLabel()
        pix = QPixmap("captcha.png")
        photo.setPixmap(pix)
        self.setWindowTitle("Капча")
        self.label = QLabel("Введите капчу:")
        self.textbox = QLineEdit()
        self.button = QPushButton("Проверить")
        self.button.clicked.connect(self.verify_captcha)

        self.timer_label = QLabel("Таймер: 10")
        self.timer_counter = 10
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)

        layout = QVBoxLayout()
        layout.addWidget(photo)
        layout.addWidget(self.label)
        layout.addWidget(self.textbox)
        layout.addWidget(self.timer_label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def verify_captcha(self):
        captcha = self.textbox.text()
        print("Проверка капчи:", captcha)

        if captcha.lower() == a:
            self.close()
        else:
            self.textbox.setDisabled(True)
            self.timer_counter = 11
            self.timer.start()
            QMessageBox.critical(self, "Ошибка", "Неправильная капча")

    def start_timer(self):
        self.timer_counter = 10
        self.timer.start()

    def update_timer(self):
        self.timer_counter -= 1
        self.timer_label.setText(f"Таймер: {self.timer_counter}")

        if self.timer_counter == 0 :
            self.timer.stop()
            self.textbox.setDisabled(False)
# window2 = CaptchaDialog()

# with open("style.css", "r") as wh2:
#     window2.setStyleSheet(wh2.read())
