from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randint
import sys


class Main(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.button.clicked.connect(self.yellow_orbs)

    def yellow_orbs(self):
        self.repaint()

    def paintEvent(self, event):
        if self.sender() == self.button:
            paint = QPainter()
            paint.begin(self)
            paint.setPen(QColor(255, 255, 0))
            for i in range(10):
                radius = randint(0, 100)
                paint.drawEllipse(randint(0, 640), randint(0, 640), radius, radius)
            paint.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Main()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
