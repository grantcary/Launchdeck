import ast
import os

hotkeys = ast.literal_eval(open("HotKeys.txt").read())

def opentab(key_num, url):
    hotkeys[key_num] = f"webbrowser.get(chrome_path).open('{str(url)}')"

def shortkeys(key_num, kbsc):
    hotkeys[key_num] = f"keyboard.press_and_release('{str(kbsc)}')"

def openexe(key_num, exepath):
    address = r"C:\Users\Grant\Documents\GitHub\Launchdeck".replace("\\", "/")
    hotkeys[key_num] = f"subprocess.Popen(['{str(address)}'])"
