from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

from instr import *





class FinalWin(QWidget):
    def __init__(self, index, heart):
        super().__init__()
        self.index = index
        self.heart = heart
        self.set_appear()
        self.initUI()
        self.show()

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





