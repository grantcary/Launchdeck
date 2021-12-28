from pydub import AudioSegment
from pydub.playback import play
import time
import pygame
import pygame.midi
import multiprocessing
import webbrowser
import subprocess
import keyboard
import ast

def evaluate(func):
    eval(func)

def getthreaded(func):
    newthread = multiprocessing.Process(target=evaluate, args=(func,))
    newthread.start()

def runMidi():
    try:
        pygame.midi.init()
        midi_in = pygame.midi.Input(1)
        
        print("Diagnostics -------------")
        print(f"MIDI Device Connected: {pygame.midi.get_init()}")
        print(f"Number of MIDI Devices Connected: {pygame.midi.get_count()}")
        for i in range(pygame.midi.get_count()):
            print(pygame.midi.get_device_info(i), i)
        print("--------------------------")

        try:
            AudioSegment.converter = r"C:\\ffmpeg\\bin\\ffmpeg.exe"
            AudioSegment.ffmpeg = r"C:\\ffmpeg\\bin\\ffmpeg.exe"
            AudioSegment.ffprobe = r"C:\\ffmpeg\\bin\\ffprobe.exe"

            settings = ast.literal_eval(open("txtfiles/settings.txt").read())
            chrome_path = settings['1'] 
            
            hotkeys = ast.literal_eval(open("txtfiles/HotKeys.txt").read())
            global x
            x = True
            while x:
                while(pygame.midi.Input.poll(midi_in) == False):
                    if x == False:
                        pygame.midi.Input.close(midi_in)
                        pygame.midi.quit()
                        print("Terminated")
                        quit()
                    time.sleep(0.1)
                midi_data = pygame.midi.Input.read(midi_in, 1)
                midi_note, timestamp = midi_data[0]
                note_status, keynum, velocity, unused = midi_note
                print("Midi Note: \n\tNote Status: ", note_status, " Key Number: ", keynum," Velocity: " , velocity, "\n\tTime Stamp: ", timestamp)
                if note_status == 144:
                    key_down = True
                elif note_status == 128: 
                    key_down = False
                else:
                    print("Unknown status!")

                if str(keynum) in hotkeys and velocity == 127:
                    try:
                        if "Play sound:" in hotkeys[str(keynum)][1]:
                            getthreaded(hotkeys[str(keynum)][0])
                        else:
                            eval(hotkeys[str(keynum)][0])
                    except:
                        print("Invalid cmd")

            pygame.midi.Input.close(midi_in)
            pygame.midi.quit()
            print("Terminated")
        except:
            print("Not a valid file")
    except:
        print("Midi not connected")

        # if str(keynum) == "19":
        #     x = False

# runMidi()