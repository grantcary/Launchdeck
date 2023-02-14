import threading
import json
import sys
import os

import PyQt5.QtCore as Qt
import PyQt5.QtWidgets as Qw
import PyQt5.QtGui as Qg
# from qtwidgets import AnimatedToggle

import midi as mi
from mapper import opentab, shortkeys, openexe, storesound, reset

MAP_PATH = 'keymap.json'

class MainWindow(Qw.QWidget):
  def __init__(self) -> None:
    super().__init__()
    self.setWindowTitle('Launchdeck')
    self.setWindowOpacity(0.99)
    self.setWindowIcon(Qg.QIcon('..\img\LD.ico'))
    self.setStyleSheet("background-color: #0a0a0a;")
    # self.setWindowFlag(Qt.Qt.FramelessWindowHint)
    self.setLayout(Qw.QVBoxLayout())

    self.start_flag = False
    
    self.top_grid()
    self.button_generator()
    self.set_tooltip()
    self.show()

  # midi control buttons
  def top_grid(self) -> None:
    container = Qw.QWidget()
    container.setLayout(Qw.QGridLayout())
    container.setStyleSheet("padding: 8px")
    container.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

    self.btn_start = Qw.QPushButton('Start', clicked = self.run)
    self.btn_start.setStyleSheet("background-color: #171717")
    self.btn_start.setToolTip("Start Launchpad")
    self.btn_start.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)
    
    self.btn_stop = Qw.QPushButton('Stop', clicked = self.stop)
    self.btn_stop.setStyleSheet("background-color: #171717")
    self.btn_stop.setToolTip("Stop Launchpad")
    self.btn_stop.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

    container.layout().addWidget(self.btn_start, 0, 1)
    container.layout().addWidget(self.btn_stop, 0, 2)

    self.layout().addWidget(container, stretch=1)

  # generates main button grid 
  def button_generator(self) -> None:
    # https://stackoverflow.com/questions/54927194/python-creating-buttons-in-loop-in-pyqt5
    # https://www.reddit.com/r/learnpython/comments/dvdfp5/add_qpushbuttons_in_loop_with_different_names/
    # https://stackoverflow.com/questions/19837486/lambda-in-a-loop
    # https://stackoverflow.com/questions/18836291/lambda-function-returning-false

    container = Qw.QWidget()
    container.setLayout(Qw.QGridLayout())
    container.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)
    container.setStyleSheet("background-color: #171717; padding: 10px;")

    def action_menu(button: Qw.QPushButton, pos: str) -> None:
      buttonMenu = Qw.QMenu(button)
      for func in ('Change Tab', 'Change Hotkey', 'Change Application', 'Change Sound', 'Reset Button'):
        action = Qw.QAction(func, self)
        action.triggered.connect(lambda ignore, f=func, p=pos: self.change_button_func(f, p))
        buttonMenu.addAction(action)
          
      button.installEventFilter(self)
      buttonMenu.installEventFilter(self)
      return buttonMenu

    # define base variables
    self.prev = None
    self.buttons = {}
    self.action_events = {}
    spacer = Qw.QSpacerItem(40, 30)

    # starts position at 104, ends at 19
    # the tens place descends, but the ones place ascends
    # pattern: 48, 49, 31, 32........38, 39, 21, 22, etc
    size = 10
    for btn_row in range(size):
      # top row seperator
      if btn_row == 1: container.layout().addItem(spacer, 1, 0)
      else:
        column_cnt = 0
        for btn_column in range(size):
          tens, ones = size-btn_row, column_cnt+1
          num = (tens*10)+ones
          pos = str(num+3) if (btn_row==0) else str(num)

          # right side column seperator
          if btn_column == 8: container.layout().addItem(spacer, btn_row, btn_column)
          else:
            # button 112 is out of bounds, pass over and continue
            if pos != '112':
              # create button, add to widget, create action event for button
              self.buttons[pos] = Qw.QPushButton(clicked = lambda ignore, x=pos: self.button_press(x))
              self.buttons[pos].setStyleSheet("QPushButton {background-color : #171717} QPushButton::pressed {background-color : #3c85cf}")
              container.layout().addWidget(self.buttons[pos], btn_row, btn_column)
              self.action_events[pos] = action_menu(self.buttons[pos], pos)
              column_cnt+=1

    self.layout().addWidget(container, stretch=4)

  def eventFilter(self, source: Qt.QObject, event: Qt.QEvent) -> bool:
    if event.type() == Qt.QEvent.ContextMenu:
      if source in self.buttons.values():
        # checks for button number that matches the source button object id
        button_key = next((k for k, v in self.buttons.items() if v == source), None)
        self.action_events[button_key].exec_(event.globalPos())
        return True
    return super().eventFilter(source, event)

  # re-executes function everytime keymap is updated
  def set_tooltip(self) -> None:
    # opens key function dictionary
    with open(MAP_PATH, 'r') as d:
      self.hkparse = json.load(d)

      for key in self.buttons.keys():
        self.buttons[key].setToolTip(self.hkparse[key][1])

  # lets you use gui buttons without midi controller connected
  def button_press(self, text: str) -> None:
    data, _, func = self.hkparse[text]
    if data and func and self.start_flag == False:
      midi_button_press = mi.Midi()
      midi_button_press.execute_func(data, func)

  def change_button_func(self, func: str, pos: str) -> None:
    match func:
      case 'Change Tab':
        url, ok = Qw.QInputDialog.getText(self, "Open Tab", "Enter url:")
        if url and ok: opentab(pos, url)
      case 'Change Hotkey':
        shortkey, ok = Qw.QInputDialog.getText(self, "Keyboard Shortcut", "Enter keyboard shortcut:")
        if shortkey and ok: shortkeys(pos, shortkey)
      case 'Change Application':
        response, _ = Qw.QFileDialog.getOpenFileName(parent=self, caption="Select File", directory=os.getcwd(), filter="Executable (*.exe)")
        if response: openexe(pos, response)
      case 'Change Sound':
        response, _ = Qw.QFileDialog.getOpenFileName(parent=self, caption="Select File", directory=os.getcwd(), filter="MP3 File (*.mp3)")
        if response: storesound(pos, response)
      case 'Reset Button': reset(pos)
    self.set_tooltip()

  def run(self) -> None:
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

  def stop(self) -> None:
    if self.start_flag == True:
      self.m.stop()
      self.start_flag = False

      self.btn_start.setEnabled(True)
      self.btn_start.setStyleSheet("background-color: #171717")
      self.btn_start.setText("Start")

if __name__ == "__main__":
  app = Qw.QApplication(sys.argv)
  mw = MainWindow()
  mw.setMinimumSize(400, 400)
  mw.setMaximumSize(600, 600)

  # off white: #e0e0e0; light grey: #c9c9c9; dark grey: #171717
  app.setStyle(Qw.QStyleFactory.create('Fusion'))
  app.setStyleSheet("QPushButton, QLabel, QLineEdit, QComboBox, QAbstractItemView, QMessageBox, QToolTip, QMenu {color: #c7c7c7;}")
  app.exec_()
  app.quit()