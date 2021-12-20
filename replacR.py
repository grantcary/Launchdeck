from pydub import AudioSegment
from pydub.playback import play
from urllib.parse import urlparse
from shutil import copyfile
import ast
import os
import json

def opentxt():
    try:
        global hotkeys
        hotkeys = ast.literal_eval(open("txtfiles/HotKeys.txt").read())
        return hotkeys
    except:
        print("Not a valid file")

def opensettings():
    try:
        global settings
        settings = ast.literal_eval(open("txtfiles/settings.txt").read())
        return settings
    except:
        print("Not a valid file")

def openexe(key_num, exepath):
    opentxt()
    address = exepath.replace("\\", "/")

    x = 0
    y = ""
    for i in address[::-1]:
        if i == ".":
            x += 1
        elif i == "/":
            break
        elif x != 0:
            y += i

    appendList = [f"subprocess.Popen(['{str(address)}'])", "Open program: " + y[::-1].capitalize()]
    hotkeys[key_num] = appendList
    file = open("txtfiles/HotKeys.txt","r+")
    file.truncate(0)
    file.close()
    with open("txtfiles/HotKeys.txt", "w") as writedict:
        writedict.write(json.dumps(hotkeys))
    print(f"Changed key {key_num} to {address}")

def storesound(key_num, exepath):
    opentxt()
    address = exepath.replace("\\", "/")
    
    y = ""
    for i in address[::-1]:
        if i == "/":
            break
        y += i

    # print("sound mark 1")
    # # copyfile(exepath, f"/soundfiles/{y[::-1]}")
    # print("sound mark 2")

    appendList = [f"play(AudioSegment.from_mp3('''{str(address)}''') - 25)", "Play sound: " + y[::-1].capitalize()]
    hotkeys[key_num] = appendList
    file = open("txtfiles/HotKeys.txt","r+")
    file.truncate(0)
    file.close()
    with open("txtfiles/HotKeys.txt", "w") as writedict:
        writedict.write(json.dumps(hotkeys))
    print(f"Changed key {key_num} to {address}")

def opentab(key_num, url):
    opentxt()
    tempurl = urlparse(url).netloc
    print(tempurl)
    appendList = [f"webbrowser.get(chrome_path).open('{str(url)}')", "Open tab: " + tempurl]
    hotkeys[key_num] = appendList
    file = open("txtfiles/HotKeys.txt","r+")
    file.truncate(0)
    file.close()
    with open("txtfiles/HotKeys.txt", "w") as writedict:
        writedict.write(json.dumps(hotkeys))
    print(f"Changed key {key_num} to {url}")

def shortkeys(key_num, kbsc):
    opentxt()
    appendList = [f"keyboard.press_and_release('{str(kbsc)}')", "Keyboard shortcut: " + str(kbsc)]
    hotkeys[key_num] = appendList
    file = open("txtfiles/HotKeys.txt","r+")
    file.truncate(0)
    file.close()
    with open("txtfiles/HotKeys.txt", "w") as writedict:
        writedict.write(json.dumps(hotkeys))
    print(f"Changed key {key_num} to {kbsc}")

def chromepath(chrome):
    opensettings()
    address = chrome.replace("\\", "/")
    address = f"{str(address)} %s"
    settings['1'] = str(address)
    file = open("txtfiles/settings.txt","r+")
    file.truncate(0)
    file.close()
    with open("txtfiles/settings.txt", "w") as writedict:
        writedict.write(json.dumps(settings))
    print(f"Changed key chrome path to {address}")
