import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("page.ui", self)
        self.setGeometry(200, 200, 500, 500)
        self.pushButton.clicked.connect(self.start)

    def start(self):
        self.update()

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.draw_circle()
        self.qp.end()

    def draw_circle(self):
        x, y, r = random.randint(1, 500), random.randint(1, 500), random.randint(10, 200)
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse(x, y, r, r)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    style = """
            QPushButton{
                color: white;
                background: #0577a8;
                border: 1px #DADADA solid;
                padding: 5px 10px;
                border-radius: 2px;
                font-weight: bold;
                font-size: 9pt;
                outline: none;
            }
            QPushButton:hover{
                border: 1px #C6C6C6 solid;
                background: #0892D0;
            }
        """
    app.setStyleSheet(style)
    ex = Example()
    ex.show()
    sys.exit(app.exec())