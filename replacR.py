import ast
import os
import json

try:
    hotkeys = ast.literal_eval(open("HotKeys.txt").read())
except:
    print("Not a valid file")

def openexe(key_num, exepath):
    address = r"C:\Users\Grant\Documents\GitHub\Launchdeck".replace("\\", "/")
    hotkeys[key_num] = f"subprocess.Popen(['{str(address)}'])"

def opentab(key_num, url):
    hotkeys[key_num] = f"webbrowser.get(chrome_path).open('{str(url)}')"
    file = open("HotKeys.txt","r+")
    file.truncate(0)
    file.close()
    with open("HotKeys.txt", "w") as writedict:
        writedict.write(json.dumps(hotkeys))
    print(f"Changed key {key_num} to {url}")

def shortkeys(key_num, kbsc):
    hotkeys[key_num] = f"keyboard.press_and_release('{str(kbsc)}')"
    file = open("HotKeys.txt","r+")
    file.truncate(0)
    file.close()
    with open("HotKeys.txt", "w") as writedict:
        writedict.write(json.dumps(hotkeys))
    print(f"Changed key {key_num} to {kbsc}")
