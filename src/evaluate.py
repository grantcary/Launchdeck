import webbrowser
import keyboard
import subprocess

from pydub import AudioSegment
from pydub.playback import play

# Linux: r'/usr/bin/ffmpeg'
AudioSegment.converter = r"C:\\ffmpeg\\bin\\ffmpeg.exe"

def shortcut(key): keyboard.send(str(key))
def open_tab(url): webbrowser.open_new_tab(url)
def play_sound(f, vol=0): play(AudioSegment.from_mp3(f) + vol)
def exe(addr): subprocess.Popen([str(addr)])
