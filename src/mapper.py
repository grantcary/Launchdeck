from urllib.parse import urlparse
from shutil import copyfile
import ast
import os
import json

KEYMAP = 'keymap.json'

def path_reformat(path): return path.replace('\\', '/')

def write_to_file(path, f):
    with open(path, "w") as d:
        json.dumps(f, d)

def openmap(): return ast.literal_eval(open(KEYMAP).read())

def openexe(key, exepath):
    map = openmap()
    address = path_reformat(exepath)
    map[key] = [str(address), "Open program: " + os.path.basename(address)]
    write_to_file(KEYMAP, map)

def storesound(key, soundpath):
    map = openmap()
    address = path_reformat(soundpath)
    filename = os.path.basename(soundpath)
    
    copyfile(soundpath, f'soundfiles/{filename}')
    map[key] = [str(filename), "Play sound: " + filename]
    write_to_file(KEYMAP, map)

def opentab(key, url):
    map = openmap()
    map[key] = [str(url), "Open tab: " + urlparse(url).netloc]
    write_to_file(KEYMAP, map)

def shortkeys(key, keyshort):
    map = openmap()
    map[key] = [str(keyshort), "Hotkey: " + str(keyshort)]
    write_to_file(KEYMAP, map)

# file = open(KEYMAP,"r+")
# file.truncate(0)
# file.close()