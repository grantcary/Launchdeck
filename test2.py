import sys
from PyQt5.QtWidgets import QWidget, QPushButton,QHBoxLayout, QGridLayout, QApplication

class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.addButton = QPushButton("add")
        #once click the addButton, call add() function
        self.addButton.clicked.connect(self.add)

        self.layout = QGridLayout()
        self.layout.addWidget(self.addButton, 0, 0)

        self.setLayout(self.layout)

        self.setWindowTitle('add')
        self.show()

    def add(self):
        Button1 = QPushButton("1")
        self.layout.addWidget(Button1, 0, 1)

        Button2 = QPushButton("2")
        self.layout.addWidget(Button2, 1, 0)

        Button3 = QPushButton("3")
        self.layout.addWidget(Button3, 1, 1)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())