import webbrowser
import keyboard
import subprocess

from pydub import AudioSegment
from pydub.playback import play

# Linux: r'/usr/bin/ffmpeg'
AudioSegment.converter = r"C:\\ffmpeg\\bin\\ffmpeg.exe"

def shortcut(key: str) -> None: keyboard.send(str(key))
def open_tab(url: str) -> None: webbrowser.open_new_tab(url)
def play_sound(f: str, vol: int = 0) -> None: play(AudioSegment.from_mp3(f) + vol)
def exe(addr: str) -> None: subprocess.call([str(addr)])