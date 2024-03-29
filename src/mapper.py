#!/usr/bin/env python3

from urllib.parse import urlparse
import ast
import os
import json

MAP_PATH = 'keymap.json'

def path_reformat(path: str) -> str: return path.replace('\\', '/')

def write_to_file(map: dict) -> None:
  with open(MAP_PATH, "w") as out_file:
    json.dump(map, out_file)

def openmap() -> dict: return ast.literal_eval(open(MAP_PATH).read())

def openexe(key: str, exepath: str) -> None:
  map = openmap()
  address = path_reformat(exepath)
  map[key] = [str(address), "Open program: " + os.path.basename(address), 'open_exe']
  write_to_file(map)

def storesound(key: str, soundpath: str) -> None:
  map = openmap()
  address = path_reformat(soundpath)
  filename = os.path.basename(soundpath)
  map[key] = [address, "Play sound: " + filename, 'store_sound']
  write_to_file(map)

def opentab(key: str, url: str) -> None:
  map = openmap()
  map[key] = [str(url), "Open tab: " + urlparse(url).netloc, 'open_tab']
  write_to_file(map)

def shortkeys(key: str, keyshort: str) -> None:
  map = openmap()
  map[key] = [str(keyshort), "Hotkey: " + str(keyshort), 'short_key']
  write_to_file(map)

def reset(key: str) -> None:
  map = openmap()
  map[key] = ['', 'None', '']
  write_to_file(map)