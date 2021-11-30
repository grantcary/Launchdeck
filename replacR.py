import ast
import os
import json

def opentxt():
    try:
        global hotkeys
        hotkeys = ast.literal_eval(open("HotKeys.txt").read())
        return hotkeys
    except:
        print("Not a valid file")

def opensettings():
    try:
        global settings
        settings = ast.literal_eval(open("settings.txt").read())
        return settings
    except:
        print("Not a valid file")

def openexe(key_num, exepath):
    opentxt()
    address = exepath.replace("\\", "/")
    hotkeys[key_num] = f"subprocess.Popen(['{str(address)}'])"
    file = open("HotKeys.txt","r+")
    file.truncate(0)
    file.close()
    with open("HotKeys.txt", "w") as writedict:
        writedict.write(json.dumps(hotkeys))
    print(f"Changed key {key_num} to {address}")

def opentab(key_num, url):
    opentxt()
    hotkeys[key_num] = f"webbrowser.get(chrome_path).open('{str(url)}')"
    file = open("HotKeys.txt","r+")
    file.truncate(0)
    file.close()
    with open("HotKeys.txt", "w") as writedict:
        writedict.write(json.dumps(hotkeys))
    print(f"Changed key {key_num} to {url}")

def shortkeys(key_num, kbsc):
    opentxt()
    hotkeys[key_num] = f"keyboard.press_and_release('{str(kbsc)}')"
    file = open("HotKeys.txt","r+")
    file.truncate(0)
    file.close()
    with open("HotKeys.txt", "w") as writedict:
        writedict.write(json.dumps(hotkeys))
    print(f"Changed key {key_num} to {kbsc}")

def chromepath(chrome):
    opensettings()
    address = chrome.replace("\\", "/")
    address = f"{str(address)} %s"
    settings['1'] = str(address)
    file = open("settings.txt","r+")
    file.truncate(0)
    file.close()
    with open("settings.txt", "w") as writedict:
        writedict.write(json.dumps(settings))
    print(f"Changed key chrome path to {address}")
