import webbrowser
import keyboard
import subprocess

from pydub import AudioSegment
from pydub.playback import play

AudioSegment.converter = r'/usr/bin/ffmpeg'

def shortcut(key): keyboard.send(str(key))
def open_tab(url): webbrowser.open_new_tab(url)
def play_sound(f, vol=0): play(AudioSegment.from_mp3(f) + vol)
def exe(addr): subprocess.Popen([str(addr)])
