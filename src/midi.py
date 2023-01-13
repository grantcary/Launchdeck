from time import sleep
import multiprocessing
import evaluate as ev
import pygame.midi
import json

KEYMAP = 'keymap.json'

class Midi:
  def open_file(self, path: str) -> dict:
      with open(path, 'r') as d:
          return json.load(d)

  def new_process(self, func: str) -> None:
      newthread = multiprocessing.Process(target=ev.play_sound, args=(func,))
      newthread.start()

  def execute_func(self, data: str, func: str) -> None:
    match func:
      case 'open_tab': ev.open_tab(data)
      case 'short_key': ev.shortcut(data)
      case 'open_exe': ev.exe(data)
      case 'store_sound': self.new_process(data)

  def stop(self) -> None:
    self.run = False

  def start(self) -> None:
    pygame.midi.init()
    # Linux: pygame.midi.Input(3)
    self.midi_in = pygame.midi.Input(1)
    midi_start_time = pygame.midi.time()

    map = self.open_file(KEYMAP)

    self.run = True
    while self.run:
      while(pygame.midi.Input.poll(self.midi_in) == False):
        if self.run == False:
          pygame.midi.Input.close(self.midi_in)
          pygame.midi.quit()
          print("Terminated")
          return
        sleep(0.1)
              
      midi_data = pygame.midi.Input.read(self.midi_in, 1)
      midi_note, timestamp = midi_data[0]
      # velocity == 127 for downstroke, velocity == 0 for upstroke
      _, keynum, velocity, _ = midi_note
      
      key = str(keynum)
      data, desc, func = map[key][0], map[key][1], map[key][2]

      # delays registering midi input until 300ms after starting function because of odd buffer behavior
      if key in map and velocity == 127 and timestamp > (midi_start_time+300):         
        self.execute_func(data, func)

    pygame.midi.Input.close(self.midi_in)
    pygame.midi.quit()