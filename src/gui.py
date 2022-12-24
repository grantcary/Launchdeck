import threading
import json
import sys
import os

import PyQt5.QtGui as Qg
import PyQt5.QtCore as Qt
import PyQt5.QtWidgets as Qw
# from qtwidgets import AnimatedToggle
        
import midi as mi
import mapper as rr


class MainWindow(Qw.QWidget):
    def __init__(self):
        self.start_flag = False

        super().__init__()
        self.setWindowTitle('Launchdeck')
        self.setWindowOpacity(0.99)
        # self.setWindowIcon(Qw.QIcon('LD.ico')) FIX THIS
        self.setStyleSheet("background-color: #1f1f1f;")
        # self.setStyleSheet("background-color: rgba(31, 31, 31, 50);")
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setStyleSheet("QPushButton {color: #bababa;}")
        self.setLayout(Qw.QVBoxLayout())
        self.topgrid()
        self.button_generator()
        self.show()

    def topgrid(self, parent=None):
        container2 = Qw.QWidget()
        container2.setLayout(Qw.QGridLayout())
        container2.setStyleSheet("padding: 8px; QInputDialog {background-color: #bababa;}")
        container2.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

        self.btn_start = Qw.QPushButton('Start', clicked = self.run)
        self.btn_start.setToolTip("Start Launchpad")
        self.btn_start.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)
        
        self.btn_stop = Qw.QPushButton('Stop', clicked = self.stop)
        self.btn_stop.setToolTip("Stop Launchpad")
        self.btn_stop.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

        arr = []
        arr.append(self.btn_start)
        arr.append(self.btn_stop)
        for i in arr:
            action1 = Qw.QAction("First Action", self)

            self.buttonMenu = Qw.QMenu(i)
            self.buttonMenu.addAction(action1)
            self.buttonMenu.addAction("Option 2")
            self.buttonMenu.addAction("Option 3")

            action1.triggered.connect(lambda: print("clicked"))

            i.installEventFilter(self)
            self.buttonMenu.installEventFilter(self)
        
        container2.layout().addWidget(self.btn_start, 0, 1)
        container2.layout().addWidget(self.btn_stop, 0, 2)

        self.layout().addWidget(container2, stretch=1)
        
    def eventFilter(self, source, event):
        if event.type() == Qt.QEvent.ContextMenu:
            if source == self.btn_start:
                self.buttonMenu.exec_(event.globalPos())
                return True
            elif source == self.btn_stop:
                self.buttonMenu.exec_(event.globalPos())
                return True

        return super().eventFilter(source, event)
    
    def button_generator(self):
        # https://stackoverflow.com/questions/54927194/python-creating-buttons-in-loop-in-pyqt5
        # https://www.reddit.com/r/learnpython/comments/dvdfp5/add_qpushbuttons_in_loop_with_different_names/
        # https://stackoverflow.com/questions/19837486/lambda-in-a-loop
        # https://stackoverflow.com/questions/18836291/lambda-function-returning-false

        container = Qw.QWidget()
        container.setLayout(Qw.QGridLayout())
        container.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)
        container.setStyleSheet("background-color: #171717; padding: 10px;")

        self.prev = None
        self.buttons = {}
        spacer = Qw.QSpacerItem(40, 30)

        with open('keymap.json', 'r') as d:
            hkparse = json.load(d)

        size = 10
        for btn_row in range(size):
            if btn_row == 1: container.layout().addItem(spacer, 1, 0)
            else:
                column_cnt = 0
                for btn_column in range(size):
                    tens, ones = size-btn_row, column_cnt+1
                    num = (tens*10)+ones
                    pos = str(num+3) if (btn_row==0) else str(num)

                    if btn_column == 8: container.layout().addItem(spacer, btn_row, btn_column)
                    else:
                        if pos != '112':
                            self.buttons[pos] = Qw.QPushButton(clicked = lambda ignore, x=pos: self.button_select(x))
                            self.buttons[pos].setToolTip(hkparse[pos][1])
                            container.layout().addWidget(self.buttons[pos], btn_row, btn_column)
                            column_cnt+=1
                        else: pass

        self.layout().addWidget(container, stretch=4)

    def button_select(self, text):        
        if self.prev != None and self.prev != text: 
            self.buttons[self.prev].setStyleSheet("background-color: #171717")
            self.buttons[text].setStyleSheet("background-color: #3c85cf")
            self.prev = text
            self.bNum = text
        
        elif self.prev == text and self.bNum == text:
            self.buttons[text].setStyleSheet("background-color: #171717")
            self.prev = text
            self.bNum = None
        
        else:
            self.buttons[text].setStyleSheet("background-color: #3c85cf")
            self.prev = text
            self.bNum = text

        if isinstance(self.bNum, str):
            print(self.bNum)

    # def remap_menu(self, self.buttons[text]):        
    #     self.buttonMenu = Qw.QMenu(self.buttons[text])
    #     self.buttonMenu.addAction("Option 1") # Open File
    #     self.buttonMenu.addAction("Option 2") # Play Sound
    #     self.buttonMenu.addAction("Option 3") # Open Tab
    #     self.buttonMenu.addAction("Option 4") # Keyboard Shortcut

    #     self.buttons[text].installEventFilter(self)
    #     self.buttonMenu.installEventFilter(self)

    def onActivated(self):
        msg = Qw.QMessageBox()
        msg.setStyleSheet("background-color: #1f1f1f; color: #bababa")
        selectlist = ["Select Function", "Open File", "Play Sound", "Open Tab", "Keyboard Shortcut"]
        
        try:
            if isinstance(int(self.bNum), int):
                taskselect, _ = Qw.QInputDialog.getItem(self, "Select Function", f"Select Function for key {self.bNum}", selectlist, 0, False)
          
                if taskselect == "Select Function":
                    pass
          
                elif taskselect == "Open File":
                    self.getFileDir("1")
                    print("Finished")
          
                elif taskselect == "Play Sound":
                    self.getSoundFile()
                    print("Finished")
          
                elif taskselect == "Open Tab":
                    url, ok = Qw.QInputDialog.getText(self, "Open Tab", "Enter url:")
                    
                    if url and ok:
                        rr.opentab(self.bNum, url)
                        print("Finished")
                
                elif taskselect == "Keyboard Shortcut":
                    shortkey, ok = Qw.QInputDialog.getText(self, "Keyboard Shortcut", "Enter keyboard shortcut:")
                
                    if shortkey and ok:
                        rr.shortkeys(self.bNum, shortkey)
                        print("Finished")
            
            self.tooltip()
        
        except:
            msg.setText("Select a self.buttons[text] you want to change function of first")
            retval = msg.exec_()

    def settings(self):
        selectlist = ["Select setting", "Chrome path"]
        taskselect, _ = Qw.QInputDialog.getItem(self, "Select setting", "Select setting", selectlist)
        if taskselect == "Chrome path":
            self.getFileDir("2")
            print("Finished")
            
    def getFileDir(self):
        file_filter = "Executable (*.exe)"
        response, _ = Qw.QFileDialog.getOpenFileName(
            parent=self,
            caption="Select File",
            directory=os.getcwd(),
            filter=file_filter
        )

        rr.openexe(self.bNum, response)

    def getSoundFile(self):
        file_filter = "MP3 File (*.mp3)"
        response, ok = Qw.QFileDialog.getOpenFileName(
            parent=self,
            caption="Select File",
            directory=os.getcwd(),
            filter=file_filter
        )
        rr.storesound(self.bNum, response)
        print("Store Sound Stored")

    def stop(self):
        if self.start_flag == True:
            self.m.stop()
            self.start_flag = False

            self.btn_start.setEnabled(True)
            self.btn_start.setStyleSheet("background-color: #1f1f1f")
            self.btn_start.setText("Start")

    def run(self):
        self.btn_start.setEnabled(False)
        self.btn_start.setStyleSheet("background-color: #3c85cf")
        self.btn_start.setText("Running")

        self.start_flag = True

        self.m = mi.Midi()
        try:
            self.newthread = threading.Thread(target=self.m.start)
            self.newthread.start()
        except:
            print("Midi not connected")


if __name__ == "__main__":
    app = Qw.QApplication(sys.argv)
    mw = MainWindow()

    # screenGeometry = Qw.QDesktopWidget().screenGeometry(-1)
    # screenGeometry = Qw.QDesktopWidget().primaryScreen()
    # size = mw.geometry()
    # print(screenGeometry)
    # print(size)

    mw.setMinimumSize(400, 400)
    mw.setMaximumSize(600, 600)

    # mw.setFixedSize(screenGeometry.width()*0.1564, screenGeometry.height()*0.2779)
    # mw.showMaximized()
    
    app.setStyle(Qw.QStyleFactory.create('Fusion'))
    app.setStyleSheet("QPushButton, QLabel, QLineEdit, QComboBox, QAbstractItemView, QMessageBox, QToolTip {color: #c7c7c7;}")
    app.exec_()
    app.quit()