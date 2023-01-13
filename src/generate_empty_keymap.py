import json
MAP_PATH = 'keymap.json'

keymap = {}
for i in range(11, 112):
  if i not in range(90, 104):
    keymap[str(i)] = ['', 'None', '']
keymap['Null'] = ['', 'None', '']

with open(MAP_PATH, 'w') as w:
  json.dump(keymap, w)