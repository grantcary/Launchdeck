#!/usr/bin/env python3

import mido
import rtmidi
import time

# Set up the backend
mido.set_backend('mido.backends.rtmidi')

start_time = time.time()

# Find available input and output ports
input_ports = mido.get_input_names()
output_ports = mido.get_output_names()

# These are the ports that are available on my system:
# Input ports: ['Midi Through:Midi Through Port-0 14:0', 'Launchpad MK2:Launchpad MK2 MIDI 1 28:0', 'Midi Through:Midi Through Port-0 14:0', 'Launchpad MK2:Launchpad MK2 MIDI 1 28:0']
# Output ports: ['Midi Through:Midi Through Port-0 14:0', 'Launchpad MK2:Launchpad MK2 MIDI 1 28:0', 'Midi Through:Midi Through Port-0 14:0', 'Launchpad MK2:Launchpad MK2 MIDI 1 28:0', 'LMMS:TripleOscillator 128:0']

# print("Input ports:", input_ports)
# print("Output ports:", output_ports)

input_port_name = input_ports[1]
output_port_name = output_ports[1]

inport = mido.open_input(input_port_name)
timeout = 0.1  # Timeout in seconds for buffer flushing
start_time = time.time()

# flush the buffer
while time.time() - start_time < timeout:
  inport.poll()
  if inport.poll():
    inport.receive()

class VirtualMidi:
  def __init__(self):
    self.inport = mido.open_input(input_port_name)
    self.rtmidi_output = rtmidi.MidiOut(name='Launchdeck')
    self.outport = self.rtmidi_output.open_virtual_port()
    self.run = False

  def stop(self):
    self.run = False

  def start(self):
    self.run = True

    while self.run:
      msg = self.inport.poll()
      if msg:
        self.outport.send_message(msg.bytes())
        msg = self.inport.receive()
        self.outport.send_message(msg.bytes())