from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from random import randint
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.design = Design()
        self.design.hide_q.connect(self.circle)

    def circle(self):
        x, y = [randint(10, 500) for _ in range(2)]
        w, h = [randint(10, 100) for _ in range(2)]
        painter = QPainter(self.design.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(*[randint(0, 255) for _ in range(3)]))
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, h)
        painter.end()
        self.update()


class Design(QWidget):
    hide_q = pyqtSignal()

    def __init__(self):
        super(Design, self).__init__()
        self.setGeometry(500, 100, 700, 700)
        self.hide_q = pyqtSignal()

        self.label = QLabel(self)
        self.pushButton = QPushButton('Create', self)
        self.pushButton.setFixedSize(50, 50)
        self.pushButton.move(300, 0)
        canvas = QPixmap(600, 600)
        self.label.setPixmap(canvas)
        self.label.move(50, 50)
        self.pushButton.clicked.connect(self.signal)

    def signal(self):
        self.hide_q.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Design()
    ex.show()
    sys.exit(app.exec())