import sys
import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


def long_running_function(update_ui):
    # Doing something
    time.sleep(1)
    update_ui(percent=25)

    # Doing something else
    time.sleep(1)
    update_ui(percent=50)

    # Another long thing
    time.sleep(1)
    update_ui(percent=75)

    # Almost done
    time.sleep(1)
    update_ui(percent=100)


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        # Here we pass the update_progress (uncalled!)
        # function to the long_running_function:
        long_running_function(self.update_progress)
        self.finished.emit()

    def update_progress(self, percent):
        self.progress.emit(percent)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        layout = QVBoxLayout()
        self.progress = QProgressBar()
        self.button = QPushButton("Start")
        layout.addWidget(self.progress)
        layout.addWidget(self.button)

        self.button.clicked.connect(self.execute)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)
        self.show()

    def execute(self):
        self.update_progress(0)
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.update_progress)

        self.thread.start()
        self.button.setEnabled(False)

    def update_progress(self, progress):
        self.progress.setValue(progress)
        self.button.setEnabled(progress == 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()