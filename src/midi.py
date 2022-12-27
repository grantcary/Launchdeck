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
    if func == 'open_tab': ev.open_tab(data)
    elif func == 'short_key': ev.shortcut(data)
    elif func == 'open_exe': ev.exe(data)
    elif func == 'store_sound': self.new_process(data)

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

# closing the thread manually does not stop from piling up input stream
# the function does terminate once conditions are reached
# deleting variable that stores the class instance does nothing
# importing the module only once prompted to start doesn't fix the problem
# if i close the gui window before stoping midi input, midi input continues to run
# very bad bug. open gui, run, press buttons, stop, press buttons, close window, re-open gui, press start, button presses registered from previous instance of gui
# it has something to do with the event loop i think. because even when the program is closed, there is a back log of registered events in queue
# in one gui instance, if you start and stop then start again the event loop, it just continues the previous event, based on the timestamps
# button presses registered before starting loop have timestamps that coincide with timestamps after starting the loop
# so aparently i was somewhat right, it doesn't have anything to do with threading, but i don't think it has to do with the event loop any more
# it must have something to do with a driver or something queuing up button presses once midi device is instantized
# i don't think this is a problem i can fix without a hacky solution, like giving a 3 second count down before allowing button presses, freeing up queue
# hacky fix by adding 300ms of delay before starting to register button presses
