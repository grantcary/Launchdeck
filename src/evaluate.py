#!/usr/bin/env python3

import webbrowser
import keyboard
import subprocess
import platform

from pydub import AudioSegment
from pydub.playback import play

PLATFORM_SYSTEM_MAP = {
    'Windows': r"C:\\ffmpeg\\bin\\ffmpeg.exe",
    'Linux': r'/usr/bin/ffmpeg'
}

SYSTEM = PLATFORM_SYSTEM_MAP.get(platform.system())

# Linux: r'/usr/bin/ffmpeg'
# Windows: r"C:\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.converter = SYSTEM

def shortcut(key: str) -> None: keyboard.send(str(key))
def open_tab(url: str) -> None: webbrowser.open_new_tab(url)
def play_sound(f: str, vol: int = 0) -> None: play(AudioSegment.from_mp3(f) + vol)
def exe(addr: str) -> None: subprocess.call([str(addr)])