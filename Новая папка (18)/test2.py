from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QComboBox, QVBoxLayout, QWidget,
                            QHBoxLayout, QGridLayout, QApplication, QWidget, QLabel, QRadioButton, QPushButton, QStackedLayout,QStackedWidget)


class SecondWindow(QWidget,QStackedLayout):
    def __init__(self):
        super().__init__()
        self.resize(300, 220)

        self.question_label = QLabel(self)
        self.answer1_radio = QRadioButton(self)
        self.answer2_radio = QRadioButton(self)
        self.answer3_radio = QRadioButton(self)
        self.check_button = QPushButton(self)
        self.next_button = QPushButton(self)
        self.back_button = QPushButton(self)
        self.initUI()

    def initUI(self):

        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Теcт на знание марок телефонов")

        self.question_label.setGeometry(50, 50, 500, 100)
        self.question_label.setText('Вопрос 1: Логотипом какой компании является Яблоко?')
        self.question_label.setWordWrap(True)

        self.answer1_radio.setGeometry(100, 150, 400, 30)
        self.answer1_radio.setText('A. Samsung')
        self.answer1_radio.setChecked(False)

        self.answer2_radio.setGeometry(100, 200, 400, 30)
        self.answer2_radio.setText('B. Apple')
        self.answer2_radio.setChecked(False)

        self.answer3_radio.setGeometry(100, 250, 400, 30)
        self.answer3_radio.setText('C. Xiaomi')
        self.answer3_radio.setChecked(False)

        self.check_button.setGeometry(200, 350, 200, 30)
        self.check_button.setText('Проверить')
        self.check_button.clicked.connect(self.checkAnswer)


        self.next_button.setGeometry(400,350,200,30)
        self.next_button.setText('Далее')
        self.next_button.clicked.connect(self.next)

        self.back_button.setGeometry(0, 350, 200, 30)
        self.back_button.clicked.connect(self.back)
        self.back_button.setText('Назад')




    def checkAnswer(self):
        if self.answer2_radio.isChecked():
            self.question_label.setText('Ответ верный')

        else:
            self.question_label.setText('Ответ неверный')

    def next(self):
        if self.answer2_radio.isChecked():
            self.question_label.setText('Ответ верный')
            self.stacklayout = QStackedLayout()
            rd = QRadioButton("12321")
            self.stacklayout.addWidget(rd)
            self.stacklayout.setCurrentIndex(1)
        else:
            self.question_label.setText('Ошибка')

    def back(self):
        pass
