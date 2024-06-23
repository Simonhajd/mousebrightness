import pyautogui
import osascript
import tkinter
from pynput import keyboard
import subprocess
user_selection = None
x = input("\nEnter S for Spotify | Enter A for Apple Music\n")

def on_press(key, selection):
    try:
        if key == keyboard.Key.space:
            subprocess.run(("open -a "+selection), shell=True)
    except Exception as e:
        print(f"Error: {e}")
if x == "S":
    x = "Spotify"
    print("Opening Spotify")
if x == "A":
    x = "Music"
    print("Opening Apple Music")
listener = keyboard.Listener(on_press=on_press(selection=x))
listener.start()

while True: 
    x, y = pyautogui.position()
    positionStr = ('X' + str(x)).rjust(4)
    y = 100 - (y/9.55)
    x = 100 - (x/14.69)
    print(positionStr, end='')
    osascript.osascript("set volume output volume "+str(y))
    print('\b' * len(positionStr), end='', flush=True) 