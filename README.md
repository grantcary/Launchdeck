# Launchdeck
<img src='https://github.com/grantcary/Launchdeck/blob/main/img/LD.ico' alt='icon' width='200'>

Launchdeck is a simple GUI application that lets you set custom buttons on your launchpad midi controller

## Setup
```
git clone https://github.com/grantcary/Launchdeck.git
cd Launchdeck
pip3 install -r requirements.txt
```

## Usage
```
usage:
    cd src
    python gui.py
```

### Support
- Partial support for both Windows and Linux (full support comming soon for each)
- Compatible midi controllers: Novation Launchpad (MK1, MK2)

To reset all assigned keys, run:
```
cd src
python generate_empty_keymap.py
```
### Features:
- open executable file
- open browser tab
- assign hot keys
- play sound
- virtual midi passthrough

### How to Use:
1. Connect your Novation Launchpad into your computer
2. Run GUI
3. Right click button you want to assign and select function from list
4. Complete prompts for chosen function
5. Test button function by left clicking the desired button
6. Start Launchpad Midi input by pressing "Start"
7. Stop Midi input by pressing "Stop"

### To use the Virtual Midi passthrough:
1. On your DAW of choice, select midi input 'Launchdeck:RtMidi virtual output'
2. Click the blue button on the upper right corner
3. Press "Start"
* *you can't use default midi functions while passthrough mode is in use and viceversa*

- *keyboard shortcut example: "command", "control + s", "left", "up", "command + space"*
- *hover over the button to check its assignment (tooltip)*