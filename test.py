import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtCore import QTimer

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.targetBtn = QPushButton('target', self)
        self.targetBtn.move(100, 50)
        self.targetBtn.clicked.connect(self.sleep5sec)

        self.target2 = QPushButton('target2', self)
        self.target2.move(100, 100)
        self.target2.clicked.connect(self.stop)


        self.setGeometry(100, 100, 300, 300)
        self.show()

    def sleep5sec(self):
        self.targetBtn.setEnabled(False)

    def stop(self):
        self.targetBtn.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())