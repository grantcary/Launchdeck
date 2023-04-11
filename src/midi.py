#!/usr/bin/env python3

from time import sleep
import multiprocessing
import platform
import json

import pygame.midi

import evaluate as ev

PLATFORM_SYSTEM_MAP = {
    'Windows': 1,
    'Linux': 3
}

SYSTEM = PLATFORM_SYSTEM_MAP.get(platform.system())
MAP_PATH = 'keymap.json'

class Midi:
  def open_file(self, path: str) -> dict:
    with open(path, 'r') as d:
      return json.load(d)

  def new_process(self, func: str) -> None:
    newthread = multiprocessing.Process(target=ev.play_sound, args=(func,))
    newthread.start()

  def execute_func(self, data: str, func: str) -> None:
    if func == 'open_tab': ev.open_tab(data)
    elif func == 'short_key': ev.shortcut(data)
    elif func == 'open_exe': ev.exe(data)
    elif func == 'store_sound': self.new_process(data)

  def stop(self) -> None:
    self.run = False

  def start(self) -> None:
    pygame.midi.init()
    # Linux: pygame.midi.Input(3)
    # Windows: pygame.midi.Input(1)
    self.midi_in = pygame.midi.Input(SYSTEM)
    midi_start_time = pygame.midi.time()

    map = self.open_file(MAP_PATH)

    self.run = True
    while self.run:
      while(pygame.midi.Input.poll(self.midi_in) == False):
        if self.run == False:
          pygame.midi.Input.close(self.midi_in)
          pygame.midi.quit()
          return
        sleep(0.1)
              
      midi_data = pygame.midi.Input.read(self.midi_in, 1)
      midi_note, timestamp = midi_data[0]
      # velocity == 127 for downstroke, velocity == 0 for upstroke
      _, keynum, velocity, _ = midi_note
      
      key = str(keynum)
      data, func = map[key][0], map[key][2]

      # delays registering midi input until 300ms after starting function because of odd buffer behavior
      if key in map and velocity == 127 and timestamp > (midi_start_time+300):         
        self.execute_func(data, func)

    pygame.midi.Input.close(self.midi_in)
    pygame.midi.quit()