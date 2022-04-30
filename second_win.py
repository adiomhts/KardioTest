from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QFont 

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



        self.line_h.addLayout(self.line_v1)
        self.line_h.addLayout(self.line_v2)

        self.setLayout(self.line_h)

    def next_click(self):

        self.hide()
        self.fw = FinalWin(int(self.years_enter.text()), int(self.test1_enter.text()), int(self.test2_1enter.text()), int(self.test2_2enter.text()))

    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.time1Event)
        self.timer.start(1000)

    def time1Event(self):
        global time
        time = time.addSecs(-1)
        self.seconds.setText(time.toString("hh:mm:ss"))
        self.seconds.setFont(QFont("Times", 40, QFont.Bold))
        self.seconds.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def time_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.time2Event)
        self.timer.start(1500)

    def time2Event(self):
        global time
        time = time.addSecs(-1)
        self.seconds.setText(time.toString("hh:mm:ss")[6:8])
        self.seconds.setFont(QFont("Times", 40, QFont.Bold))
        self.seconds.setStyleSheet("color: rgb(0, 0, 0)")
        if (time.toString("hh:mm:ss")[6:8]) == "00":
            self.timer.stop()

    def time_last(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.time3Event)
        self.timer.start(1000)

    def time3Event(self):
        global time
        time = time.addSecs(-1)
        self.seconds.setText(time.toString("hh:mm:ss"))
        self.seconds.setFont(QFont("Times", 40, QFont.Bold))
        self.seconds.setStyleSheet("color: rgb(0, 0, 0)")
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.seconds.setStyleSheet("color: rgb(0, 255, 0)")
        if int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.seconds.setStyleSheet("color: rgb(0, 255, 0)")
        if (time.toString("hh:mm:ss")) == "00:00:00":
            self.timer.stop()


    def connects(self):
        self.button_1.clicked.connect(self.timer_test)
        self.button_2.clicked.connect(self.time_sits)
        self.button_3.clicked.connect(self.time_last)
        self.button_4.clicked.connect(self.next_click)











