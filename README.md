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
Only Windows is officially supported
Supported midi controllers:
- Novation Launchpad MK2

### Features:
- open executable file
- open browser tab
- hot keys
- play sound

### How to Use:
1. Connect your Novation Launchpad into your computer
2. Run GUI
3. Select a button you desire to change, then select "Change Func"
4. Select your button function from the dropdown menu and complete the prompts
5. Start Launchpad Midi input by pressing "Start"
6. Stop Midi input by pressing "Stop"

- *keyboard shortcut example: "command", "control + s", "left", "up", "command + space"*
- *hover over the button to check its assignment*