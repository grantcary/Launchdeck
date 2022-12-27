from urllib.parse import urlparse
from shutil import copyfile
import ast
import os
import json

KEYMAP = 'keymap.json'

def path_reformat(path): return path.replace('\\', '/')

def write_to_file(map: dict) -> None:
    with open(KEYMAP, "w") as out_file:
        json.dump(map, out_file)

def openmap() -> ast: return ast.literal_eval(open(KEYMAP).read())

def openexe(key, exepath):
    map = openmap()
    address = path_reformat(exepath)
    map[key] = [str(address), "Open program: " + os.path.basename(address)]
    write_to_file(map)

def storesound(key, soundpath):
    map = openmap()
    address = path_reformat(soundpath)
    filename = os.path.basename(soundpath)
    
    copyfile(soundpath, f'soundfiles/{filename}')
    map[key] = [str(filename), "Play sound: " + filename]
    write_to_file(map)

def opentab(key, url):
    map = openmap()
    map[key] = [str(url), "Open tab: " + urlparse(url).netloc]
    write_to_file(map)

def shortkeys(key, keyshort):
    map = openmap()
    map[key] = [str(keyshort), "Hotkey: " + str(keyshort)]
    write_to_file(map)

# file = open(KEYMAP,"r+")
# file.truncate(0)
# file.close()

opentab('12', 'https://news.ycombinator.com/')