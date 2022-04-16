from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout
from time import sleep

from instr import *
from final_win import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):

        self.button_1 = QPushButton(txt_starttest1)
        self.button_2 = QPushButton(txt_starttest2)
        self.button_3 = QPushButton(txt_starttest3)
        self.button_4 = QPushButton(txt_sendresults)

        self.surname = QLabel(txt_name)
        self.years = QLabel(txt_age)
        self.lay = QLabel(txt_test1)
        self.sit_ups = QLabel(txt_test2)
        self.lay_again = QLabel(txt_test3)
        self.seconds = QLabel('00:00:00')

        self.surname_enter = QLineEdit(txt_hintname)
        self.years_enter = QLineEdit(txt_hintage)
        self.test1_enter = QLineEdit(txt_hinttest1)
        self.test2_1enter = QLineEdit(txt_hinttest2)
        self.test2_2enter = QLineEdit(txt_hinttest3)

        self.line_v1 = QVBoxLayout()
        self.line_h = QHBoxLayout()
        self.line_v2 = QVBoxLayout()

        self.line_v2.addWidget(self.seconds, alignment=Qt.AlignCenter)
        self.line_v1.addWidget(self.surname, alignment=Qt.AlignLeft)
        self.line_v1.addWidget(self.surname_enter, alignment=Qt.AlignLeft)
        self.line_v1.addWidget(self.years, alignment=Qt.AlignLeft)
        self.line_v1.addWidget(self.years_enter, alignment=Qt.AlignLeft)
        self.line_v1.addWidget(self.lay, alignment=Qt.AlignLeft)
        self.line_v1.addWidget(self.button_1, alignment=Qt.AlignLeft)
        self.line_v1.addWidget(self.test1_enter, alignment=Qt.AlignLeft)
        self.line_v1.addWidget(self.sit_ups, alignment=Qt.AlignLeft)
        self.line_v1.addWidget(self.button_2, alignment=Qt.AlignLeft)
        self.line_v1.addWidget(self.lay_again, alignment=Qt.AlignLeft)
        self.line_v1.addWidget(self.button_3, alignment=Qt.AlignLeft)
        self.line_v1.addWidget(self.test2_1enter, alignment=Qt.AlignLeft)
        self.line_v1.addWidget(self.test2_2enter, alignment=Qt.AlignLeft)
        self.line_v1.addWidget(self.button_4, alignment=Qt.AlignCenter)

        self.your_surname = self.surname_enter.text()
        self.your_years = int(self.years_enter.text())
        self.your_test1 = int(self.test1_enter.text())
        self.your_test2 = int(self.test2_1enter.text())
        self.your_test3 = int(self.test2_2enter.text())

        self.line_h.addLayout(self.line_v1)
        self.line_h.addLayout(self.line_v2)

        self.setLayout(self.line_h)

    def next_click(self):

        self.index = ((4 * (self.your_test1 + self.your_test2 + self.your_test3) - 200) / 10)


        if self.your_years >= 15:
            if self.index >= 15:
                self.heart = txt_res1
            if self.index >= 11 and self.index < 15:
                self.heart = txt_res2
            if self.index >= 6 and self.index < 11:
                self.heart = txt_res3
            if self.index >= 0.5 and self.index < 6:
                self.heart = txt_res4
            if self.index < 0.5:
                self.heart = txt_res5

        if self.your_years < 15 and self.your_years >= 13:
            if self.index >= 16.5:
                self.heart = txt_res1
            if self.index >= 12.5 and self.index < 16.5:
                self.heart = txt_res2
            if self.index >= 7.5 and self.index < 12.5:
                self.heart = txt_res3
            if self.index >= 2 and self.index < 7.5:
                self.heart = txt_res4
            if self.index < 2:
                self.heart = txt_res5

        if self.your_years < 13 and self.your_years >= 11:
            if self.index >= 18:
                self.heart = txt_res1
            if self.index >= 14 and self.index < 18:
                self.heart = txt_res2
            if self.index >= 9 and self.index < 14:
                self.heart = txt_res3
            if self.index >= 3.5 and self.index < 9:
                self.heart = txt_res4
            if self.index < 3.5:
                self.heart = txt_res5

        if self.your_years < 11 and self.your_years >= 9:
            if self.index >= 19.5:
                self.heart = txt_res1
            if self.index >= 15.5 and self.index < 19.5:
                self.heart = txt_res2
            if self.index >= 10.5 and self.index < 15.5:
                self.heart = txt_res3
            if self.index >= 5 and self.index < 10.5:
                self.heart = txt_res4
            if self.index < 5:
                self.heart = txt_res5

        if self.your_years < 9:
            if self.index >= 21:
                self.heart = txt_res1
            if self.index >= 17 and self.index < 21:
                self.heart = txt_res2
            if self.index >= 12 and self.index < 17:
                self.heart = txt_res3
            if self.index >= 6.5 and self.index < 12:
                self.heart = txt_res4
            if self.index < 6.5:
                self.heart = txt_res5

        self.hide()
        self.fw = FinalWin(self.index, self.heart)


    def timer_15(self):
        number = 0
        self.seconds.setText('00:00:' + (str(number)))
        for i in range(15):
            sleep(1)
            number += 1
            self.seconds.setText('00:00:' + (str(number)))

    def situps(self):
        number = 0
        self.seconds.setText(str(number))
        for i in range(30):
            sleep(1.5)
            number += 1
            self.seconds.setText(str(number))

    def timer_60(self):
        number = 0
        self.seconds.setStyleSheet('color: green')
        self.seconds.setText('00:00:' + (str(number)))
        for i in range(15):
            sleep(1)
            number += 1
            self.seconds.setText('00:00:' + (str(number)))
        self.seconds.setStyleSheet('color: black')
        for i in range(30):
            sleep(1)
            number += 1
            self.seconds.setText('00:00:' + (str(number)))
        self.seconds.setStyleSheet('color: green')
        for i in range(15):
            sleep(1)
            number += 1
            self.seconds.setText('00:00:' + (str(number)))

    def connects(self):
        self.button_1.clicked.connect(self.timer_15)
        self.button_2.clicked.connect(self.situps)
        self.button_3.clicked.connect(self.timer_60)
        self.button_4.clicked.connect(self.next_click)











