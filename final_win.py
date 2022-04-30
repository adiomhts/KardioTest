from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

from instr import *





class FinalWin(QWidget):
    def __init__(self, your_years, your_test1, your_test2, your_test3):
        super().__init__()
        self.index = self.count(your_test1, your_test2, your_test3)
        self.heart = self.heart_(your_years, self.index)
        self.set_appear()
        self.initUI()
        self.show()


    def count(self,your_test1, your_test2, your_test3):
        index = ((4 * (your_test1 + your_test2 + your_test3) - 200) / 10)
        return index
    def heart_(self, your_years, index):
        if your_years >= 15:
            if index >= 15:
                heart = txt_res1
            if index >= 11 and index < 15:
                heart = txt_res2
            if index >= 6 and index < 11:
                heart = txt_res3
            if index >= 0.5 and index < 6:
                heart = txt_res4
            if index < 0.5:
                heart = txt_res5

        if your_years < 15 and your_years >= 13:
            if index >= 16.5:
                heart = txt_res1
            if index >= 12.5 and index < 16.5:
                heart = txt_res2
            if index >= 7.5 and index < 12.5:
                heart = txt_res3
            if index >= 2 and index < 7.5:
                heart = txt_res4
            if index < 2:
                heart = txt_res5

        if your_years < 13 and your_years >= 11:
            if index >= 18:
                heart = txt_res1
            if index >= 14 and index < 18:
                heart = txt_res2
            if index >= 9 and index < 14:
                heart = txt_res3
            if index >= 3.5 and index < 9:
                heart = txt_res4
            if index < 3.5:
                heart = txt_res5

        if your_years < 11 and your_years >= 9:
            if index >= 19.5:
                heart = txt_res1
            if index >= 15.5 and index < 19.5:
                heart = txt_res2
            if index >= 10.5 and index < 15.5:
                heart = txt_res3
            if index >= 5 and index < 10.5:
                heart = txt_res4
            if index < 5:
                heart = txt_res5

        if your_years < 9:
            if index >= 21:
                heart = txt_res1
            if index >= 17 and index < 21:
                heart = txt_res2
            if index >= 12 and index < 17:
                heart = txt_res3
            if index >= 6.5 and index < 12:
                heart = txt_res4
            if index < 6.5:
                heart = txt_res5
        return heart
        



    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.text1 = QLabel(txt_index + str(self.index))
        self.text2 = QLabel(txt_workheart + self.heart)

        self.v_line = QVBoxLayout()

        self.v_line.addWidget(self.text1, alignment=Qt.AlignCenter)
        self.v_line.addWidget(self.text2, alignment=Qt.AlignCenter)

        self.setLayout(self.v_line)





