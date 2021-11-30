import PyQt5.QtWidgets as qtw
import threading
import Midi_Input as mi
import replacR as rr
import sys
import os

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Launchdeck')
        self.setWindowOpacity(0.99)
        self.setFixedWidth(400)
        self.setFixedHeight(400)
        self.setStyleSheet("background-color: #1f1f1f;")
        # self.setStyleSheet("background-color: rgba(31, 31, 31, 50);")
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setStyleSheet("QPushButton {color: #bababa;}")
        self.setLayout(qtw.QVBoxLayout())
        self.topgrid()
        self.buttongrid()

        self.show()

    def topgrid(self, parent=None):
        container2 = qtw.QWidget()
        container2.setLayout(qtw.QGridLayout())
        container2.setStyleSheet("padding: 8px; QInputDialog {background-color: #bababa;}")
        
        settings = qtw.QPushButton('Settings', clicked = self.settings)
        btn_func = qtw.QPushButton('Change func', clicked = self.onActivated)
        self.btn_start = qtw.QPushButton('Start', clicked = self.execute)
        btn_stop = qtw.QPushButton('Stop', clicked = self.stop)

        container2.layout().addWidget(settings, 0, 0)
        container2.layout().addWidget(btn_func, 0, 1)       
        container2.layout().addWidget(self.btn_start, 0, 2)
        container2.layout().addWidget(btn_stop, 0, 3)

        self.layout().addWidget(container2)
        
    def buttongrid(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())
        # container.setStyleSheet("background-color: #171717; border-radius: 5px;")
        container.setStyleSheet("background-color: #171717; padding: 10px;")
        
        self.prevbtn = None
        self.btn_11 = qtw.QPushButton(clicked = lambda: self.buttonselect("11", self.btn_11, self.prevbtn))
        self.btn_12 = qtw.QPushButton(clicked = lambda: self.buttonselect('12', self.btn_12, self.prevbtn))
        self.btn_13 = qtw.QPushButton(clicked = lambda: self.buttonselect('13', self.btn_13, self.prevbtn))
        self.btn_14 = qtw.QPushButton(clicked = lambda: self.buttonselect('14', self.btn_14, self.prevbtn))
        self.btn_15 = qtw.QPushButton(clicked = lambda: self.buttonselect('15', self.btn_15, self.prevbtn))
        self.btn_16 = qtw.QPushButton(clicked = lambda: self.buttonselect('16', self.btn_16, self.prevbtn))
        self.btn_17 = qtw.QPushButton(clicked = lambda: self.buttonselect('17', self.btn_17, self.prevbtn))
        self.btn_18 = qtw.QPushButton(clicked = lambda: self.buttonselect('18', self.btn_18, self.prevbtn))
        self.btn_19 = qtw.QPushButton(clicked = lambda: self.buttonselect('19', self.btn_19, self.prevbtn))
        self.btn_21 = qtw.QPushButton(clicked = lambda: self.buttonselect('21', self.btn_21, self.prevbtn))
        self.btn_22 = qtw.QPushButton(clicked = lambda: self.buttonselect('22', self.btn_22, self.prevbtn))
        self.btn_23 = qtw.QPushButton(clicked = lambda: self.buttonselect('23', self.btn_23, self.prevbtn))
        self.btn_24 = qtw.QPushButton(clicked = lambda: self.buttonselect('24', self.btn_24, self.prevbtn))
        self.btn_25 = qtw.QPushButton(clicked = lambda: self.buttonselect('25', self.btn_25, self.prevbtn))
        self.btn_26 = qtw.QPushButton(clicked = lambda: self.buttonselect('26', self.btn_26, self.prevbtn))
        self.btn_27 = qtw.QPushButton(clicked = lambda: self.buttonselect('27', self.btn_27, self.prevbtn))
        self.btn_28 = qtw.QPushButton(clicked = lambda: self.buttonselect('28', self.btn_28, self.prevbtn))
        self.btn_29 = qtw.QPushButton(clicked = lambda: self.buttonselect('29', self.btn_29, self.prevbtn))
        self.btn_31 = qtw.QPushButton(clicked = lambda: self.buttonselect('31', self.btn_31, self.prevbtn))
        self.btn_32 = qtw.QPushButton(clicked = lambda: self.buttonselect('32', self.btn_32, self.prevbtn))
        self.btn_33 = qtw.QPushButton(clicked = lambda: self.buttonselect('33', self.btn_33, self.prevbtn))
        self.btn_34 = qtw.QPushButton(clicked = lambda: self.buttonselect('34', self.btn_34, self.prevbtn))
        self.btn_35 = qtw.QPushButton(clicked = lambda: self.buttonselect('35', self.btn_35, self.prevbtn))
        self.btn_36 = qtw.QPushButton(clicked = lambda: self.buttonselect('36', self.btn_36, self.prevbtn))
        self.btn_37 = qtw.QPushButton(clicked = lambda: self.buttonselect('37', self.btn_37, self.prevbtn))
        self.btn_38 = qtw.QPushButton(clicked = lambda: self.buttonselect('38', self.btn_38, self.prevbtn))
        self.btn_39 = qtw.QPushButton(clicked = lambda: self.buttonselect('39', self.btn_39, self.prevbtn))
        self.btn_41 = qtw.QPushButton(clicked = lambda: self.buttonselect('41', self.btn_41, self.prevbtn))
        self.btn_42 = qtw.QPushButton(clicked = lambda: self.buttonselect('42', self.btn_42, self.prevbtn))
        self.btn_43 = qtw.QPushButton(clicked = lambda: self.buttonselect('43', self.btn_43, self.prevbtn))
        self.btn_44 = qtw.QPushButton(clicked = lambda: self.buttonselect('44', self.btn_44, self.prevbtn))
        self.btn_45 = qtw.QPushButton(clicked = lambda: self.buttonselect('45', self.btn_45, self.prevbtn))
        self.btn_46 = qtw.QPushButton(clicked = lambda: self.buttonselect('46', self.btn_46, self.prevbtn))
        self.btn_47 = qtw.QPushButton(clicked = lambda: self.buttonselect('47', self.btn_47, self.prevbtn))
        self.btn_48 = qtw.QPushButton(clicked = lambda: self.buttonselect('48', self.btn_48, self.prevbtn))
        self.btn_49 = qtw.QPushButton(clicked = lambda: self.buttonselect('49', self.btn_49, self.prevbtn))
        self.btn_51 = qtw.QPushButton(clicked = lambda: self.buttonselect('51', self.btn_51, self.prevbtn))
        self.btn_52 = qtw.QPushButton(clicked = lambda: self.buttonselect('52', self.btn_52, self.prevbtn))
        self.btn_53 = qtw.QPushButton(clicked = lambda: self.buttonselect('53', self.btn_53, self.prevbtn))
        self.btn_54 = qtw.QPushButton(clicked = lambda: self.buttonselect('54', self.btn_54, self.prevbtn))
        self.btn_55 = qtw.QPushButton(clicked = lambda: self.buttonselect('55', self.btn_55, self.prevbtn))
        self.btn_56 = qtw.QPushButton(clicked = lambda: self.buttonselect('56', self.btn_56, self.prevbtn))
        self.btn_57 = qtw.QPushButton(clicked = lambda: self.buttonselect('57', self.btn_57, self.prevbtn))
        self.btn_58 = qtw.QPushButton(clicked = lambda: self.buttonselect('58', self.btn_58, self.prevbtn))
        self.btn_59 = qtw.QPushButton(clicked = lambda: self.buttonselect('59', self.btn_59, self.prevbtn))
        self.btn_61 = qtw.QPushButton(clicked = lambda: self.buttonselect('61', self.btn_61, self.prevbtn))
        self.btn_62 = qtw.QPushButton(clicked = lambda: self.buttonselect('62', self.btn_62, self.prevbtn))
        self.btn_63 = qtw.QPushButton(clicked = lambda: self.buttonselect('63', self.btn_63, self.prevbtn))
        self.btn_64 = qtw.QPushButton(clicked = lambda: self.buttonselect('64', self.btn_64, self.prevbtn))
        self.btn_65 = qtw.QPushButton(clicked = lambda: self.buttonselect('65', self.btn_65, self.prevbtn))
        self.btn_66 = qtw.QPushButton(clicked = lambda: self.buttonselect('66', self.btn_66, self.prevbtn))
        self.btn_67 = qtw.QPushButton(clicked = lambda: self.buttonselect('67', self.btn_67, self.prevbtn))
        self.btn_68 = qtw.QPushButton(clicked = lambda: self.buttonselect('68', self.btn_68, self.prevbtn))
        self.btn_69 = qtw.QPushButton(clicked = lambda: self.buttonselect('69', self.btn_69, self.prevbtn))
        self.btn_71 = qtw.QPushButton(clicked = lambda: self.buttonselect('71', self.btn_71, self.prevbtn))
        self.btn_72 = qtw.QPushButton(clicked = lambda: self.buttonselect('72', self.btn_72, self.prevbtn))
        self.btn_73 = qtw.QPushButton(clicked = lambda: self.buttonselect('73', self.btn_73, self.prevbtn))
        self.btn_74 = qtw.QPushButton(clicked = lambda: self.buttonselect('74', self.btn_74, self.prevbtn))
        self.btn_75 = qtw.QPushButton(clicked = lambda: self.buttonselect('75', self.btn_75, self.prevbtn))
        self.btn_76 = qtw.QPushButton(clicked = lambda: self.buttonselect('76', self.btn_76, self.prevbtn))
        self.btn_77 = qtw.QPushButton(clicked = lambda: self.buttonselect('77', self.btn_77, self.prevbtn))
        self.btn_78 = qtw.QPushButton(clicked = lambda: self.buttonselect('78', self.btn_78, self.prevbtn))
        self.btn_79 = qtw.QPushButton(clicked = lambda: self.buttonselect('79', self.btn_79, self.prevbtn))
        self.btn_81 = qtw.QPushButton(clicked = lambda: self.buttonselect('81', self.btn_81, self.prevbtn))
        self.btn_82 = qtw.QPushButton(clicked = lambda: self.buttonselect('82', self.btn_82, self.prevbtn))
        self.btn_83 = qtw.QPushButton(clicked = lambda: self.buttonselect('83', self.btn_83, self.prevbtn))
        self.btn_84 = qtw.QPushButton(clicked = lambda: self.buttonselect('84', self.btn_84, self.prevbtn))
        self.btn_85 = qtw.QPushButton(clicked = lambda: self.buttonselect('85', self.btn_85, self.prevbtn))
        self.btn_86 = qtw.QPushButton(clicked = lambda: self.buttonselect('86', self.btn_86, self.prevbtn))
        self.btn_87 = qtw.QPushButton(clicked = lambda: self.buttonselect('87', self.btn_87, self.prevbtn))
        self.btn_88 = qtw.QPushButton(clicked = lambda: self.buttonselect('88', self.btn_88, self.prevbtn))
        self.btn_89 = qtw.QPushButton(clicked = lambda: self.buttonselect('89', self.btn_89, self.prevbtn))
        self.btn_104 = qtw.QPushButton(clicked = lambda: self.buttonselect('104', self.btn_104, self.prevbtn))
        self.btn_105 = qtw.QPushButton(clicked = lambda: self.buttonselect('105', self.btn_105, self.prevbtn))
        self.btn_106 = qtw.QPushButton(clicked = lambda: self.buttonselect('106', self.btn_106, self.prevbtn))
        self.btn_107 = qtw.QPushButton(clicked = lambda: self.buttonselect('107', self.btn_107, self.prevbtn))
        self.btn_108 = qtw.QPushButton(clicked = lambda: self.buttonselect('108', self.btn_108, self.prevbtn))
        self.btn_109 = qtw.QPushButton(clicked = lambda: self.buttonselect('109', self.btn_109, self.prevbtn))
        self.btn_110 = qtw.QPushButton(clicked = lambda: self.buttonselect('110', self.btn_110, self.prevbtn))
        self.btn_111 = qtw.QPushButton(clicked = lambda: self.buttonselect('111', self.btn_111, self.prevbtn))
        lab_1 = qtw.QLabel("")
        lab_2 = qtw.QLabel("")

        container.layout().addWidget(self.btn_104, 0, 0)
        container.layout().addWidget(self.btn_105, 0, 1)
        container.layout().addWidget(self.btn_106, 0, 2)
        container.layout().addWidget(self.btn_107, 0, 3)
        container.layout().addWidget(self.btn_108, 0, 4)
        container.layout().addWidget(self.btn_109, 0, 5)
        container.layout().addWidget(self.btn_110, 0, 6)
        container.layout().addWidget(self.btn_111, 0, 7)
        container.layout().addWidget(lab_1, 1, 0)
        container.layout().addWidget(self.btn_81, 2, 0)
        container.layout().addWidget(self.btn_82, 2, 1)
        container.layout().addWidget(self.btn_83, 2, 2)
        container.layout().addWidget(self.btn_84, 2, 3)
        container.layout().addWidget(self.btn_85, 2, 4)
        container.layout().addWidget(self.btn_86, 2, 5)
        container.layout().addWidget(self.btn_87, 2, 6)
        container.layout().addWidget(self.btn_88, 2, 7)
        container.layout().addWidget(lab_2, 2, 8)
        container.layout().addWidget(self.btn_89, 2, 9)
        container.layout().addWidget(self.btn_71, 3, 0)
        container.layout().addWidget(self.btn_72, 3, 1)
        container.layout().addWidget(self.btn_73, 3, 2)
        container.layout().addWidget(self.btn_74, 3, 3)
        container.layout().addWidget(self.btn_75, 3, 4)
        container.layout().addWidget(self.btn_76, 3, 5)
        container.layout().addWidget(self.btn_77, 3, 6)
        container.layout().addWidget(self.btn_78, 3, 7)
        container.layout().addWidget(lab_2, 3, 8)
        container.layout().addWidget(self.btn_79, 3, 9)
        container.layout().addWidget(self.btn_61, 4, 0)
        container.layout().addWidget(self.btn_62, 4, 1)
        container.layout().addWidget(self.btn_63, 4, 2)
        container.layout().addWidget(self.btn_64, 4, 3)
        container.layout().addWidget(self.btn_65, 4, 4)
        container.layout().addWidget(self.btn_66, 4, 5)
        container.layout().addWidget(self.btn_67, 4, 6)
        container.layout().addWidget(self.btn_68, 4, 7)
        container.layout().addWidget(lab_2, 4, 8)
        container.layout().addWidget(self.btn_69, 4, 9)
        container.layout().addWidget(self.btn_51, 5, 0)
        container.layout().addWidget(self.btn_52, 5, 1)
        container.layout().addWidget(self.btn_53, 5, 2)
        container.layout().addWidget(self.btn_54, 5, 3)
        container.layout().addWidget(self.btn_55, 5, 4)
        container.layout().addWidget(self.btn_56, 5, 5)
        container.layout().addWidget(self.btn_57, 5, 6)
        container.layout().addWidget(self.btn_58, 5, 7)
        container.layout().addWidget(lab_2, 5, 8)
        container.layout().addWidget(self.btn_59, 5, 9)
        container.layout().addWidget(self.btn_41, 6, 0)
        container.layout().addWidget(self.btn_42, 6, 1)
        container.layout().addWidget(self.btn_43, 6, 2)
        container.layout().addWidget(self.btn_44, 6, 3)
        container.layout().addWidget(self.btn_45, 6, 4)
        container.layout().addWidget(self.btn_46, 6, 5)
        container.layout().addWidget(self.btn_47, 6, 6)
        container.layout().addWidget(self.btn_48, 6, 7)
        container.layout().addWidget(lab_2, 6, 8)
        container.layout().addWidget(self.btn_49, 6, 9)
        container.layout().addWidget(self.btn_31, 7, 0)
        container.layout().addWidget(self.btn_32, 7, 1)
        container.layout().addWidget(self.btn_33, 7, 2)
        container.layout().addWidget(self.btn_34, 7, 3)
        container.layout().addWidget(self.btn_35, 7, 4)
        container.layout().addWidget(self.btn_36, 7, 5)
        container.layout().addWidget(self.btn_37, 7, 6)
        container.layout().addWidget(self.btn_38, 7, 7)
        container.layout().addWidget(lab_2, 7, 8)
        container.layout().addWidget(self.btn_39, 7, 9)
        container.layout().addWidget(self.btn_21, 8, 0)
        container.layout().addWidget(self.btn_22, 8, 1)
        container.layout().addWidget(self.btn_23, 8, 2)
        container.layout().addWidget(self.btn_24, 8, 3)
        container.layout().addWidget(self.btn_25, 8, 4)
        container.layout().addWidget(self.btn_26, 8, 5)
        container.layout().addWidget(self.btn_27, 8, 6)
        container.layout().addWidget(self.btn_28, 8, 7)
        container.layout().addWidget(lab_2, 8, 8)
        container.layout().addWidget(self.btn_29, 8, 9)
        container.layout().addWidget(self.btn_11, 9, 0)
        container.layout().addWidget(self.btn_12, 9, 1)
        container.layout().addWidget(self.btn_13, 9, 2)
        container.layout().addWidget(self.btn_14, 9, 3)
        container.layout().addWidget(self.btn_15, 9, 4)
        container.layout().addWidget(self.btn_16, 9, 5)
        container.layout().addWidget(self.btn_17, 9, 6)
        container.layout().addWidget(self.btn_18, 9, 7)
        container.layout().addWidget(lab_2, 9, 8)
        container.layout().addWidget(self.btn_19, 9, 9)

        self.layout().addWidget(container)

    def stop(self):
        mi.x = False
        self.btn_start.setEnabled(True)
        self.btn_start.setStyleSheet("background-color: #1f1f1f")
        self.btn_start.setText("Start")

    def buttonselect(self, text, button, prevbtn):
        if prevbtn != None and prevbtn != button: 
            prevbtn.setStyleSheet("background-color: #171717")
            button.setStyleSheet("background-color: #3c85cf")
            self.prevbtn = button
            self.bNum = text
            print(self.bNum)
        elif prevbtn == button and self.bNum == text:
            button.setStyleSheet("background-color: #171717")
            self.prevbtn = button
            self.bNum = None
            print(self.bNum)
        else:
            button.setStyleSheet("background-color: #3c85cf")
            self.prevbtn = button
            self.bNum = text
            print(self.bNum)

    def onActivated(self):
        msg = qtw.QMessageBox()
        msg.setStyleSheet("background-color: #1f1f1f; color: #bababa")
        selectlist = ["Select Function", "Open File", "Open Tab", "Keyboard Shortcut"]
        try:
            if isinstance(int(self.bNum), int) == True:
                taskselect, tsbool = qtw.QInputDialog.getItem(self, "Select Function", f"Select Function for key {self.bNum}", selectlist, 0, False)
                if taskselect == "Select Function":
                    pass
                elif taskselect == "Open File":
                    self.getFileDir("1")
                    print("Finished")
                elif taskselect == "Open Tab":
                    urlInput, ok = qtw.QInputDialog.getText(self, "Open Tab", "Enter url:")
                    if urlInput and ok:
                        rr.opentab(self.bNum, urlInput)
                        print("Finished")
                elif taskselect == "Keyboard Shortcut":
                    cmdInput, ok = qtw.QInputDialog.getText(self, "Keyboard Shortcut", "Enter keyboard shortcut:")
                    if cmdInput and ok:
                        rr.shortkeys(self.bNum, cmdInput)
                        print("Finished")
        except:
            msg.setText("Select a button you want to change function of first")
            retval = msg.exec_()

    def settings(self):
        selectlist = ["Select setting", "Chrome path"]
        taskselect, tsbool = qtw.QInputDialog.getItem(self, "Select setting", "Select setting", selectlist)
        if taskselect == "Chrome path":
            self.getFileDir("2")
            print("Finished")   

    def getFileDir(self, func):
        file_filter = "Executable (*.exe)"
        response, ok = qtw.QFileDialog.getOpenFileName(
            parent=self,
            caption="Select File",
            directory=os.getcwd(),
            filter=file_filter
        )
        if func == "1":
            rr.openexe(self.bNum, response)
            print(func)
        elif func == "2":
            rr.chromepath(response)
            print(func)

    def execute(self):
        self.btn_start.setEnabled(False)
        self.btn_start.setStyleSheet("background-color: #3c85cf")
        self.btn_start.setText("Running")
        newthread = threading.Thread(target=mi.runMidi)
        newthread.start()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    app.setStyle(qtw.QStyleFactory.create('Fusion'))
    app.setStyleSheet("QPushButton, QLabel, QLineEdit, QComboBox, QAbstractItemView, QMessageBox {color: #c7c7c7;}")
    # app.setStyleSheet("border-radius : 50; border : 2px solid black")
    app.exec_()