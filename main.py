import pyautogui
import osascript
import tkinter
from pynput import keyboard
import subprocess
import os
from playsound import playsound

user_selection = None
service = input("\nEnter S for Spotify | Enter A for Apple Music\n")
subprocess.Popen(["python3", "controltest.py"])
controller = keyboard.Controller()
def on_press(key):
    global x
    try:
        if key == keyboard.Key.space:
            print(service)
            subprocess.run(("open -a "+service), shell=True)
    except Exception as e:
        print(f"Error: {e}")
if service == "S" or service == "s": 
    service = "Spotify"
    print("Opening Spotify")
if service == "A" or service == "a":
    service = "Music"
    print("Opening Apple Music")
listener = keyboard.Listener(on_press=on_press)
listener.start()

while True: 
    x, y = pyautogui.position()
    positionStr = ('X' + str(x)).rjust(4)
    y = 100 - (y/9.55)
    x = 100 - (x/14.69)
    print(positionStr, end='')
    osascript.osascript("set volume output volume "+str(y))
    print('\b' * len(positionStr), end='', flush=True) 
    print("| x: ", x, end='\r')
    if x <= 2:
        print("Skip detected")
        playsound('funk.aiff', block=False)
        print("Sound played")
        # Use pynput for next track
        controller.press(keyboard.Key.media_next)
        print("key pressed")
        controller.release(keyboard.Key.media_next)
        print("key released")
        pyautogui.moveTo(734, None)
        print("Moved mouse")
        print("Next")
        
    if x >= 98:
        os.system(f'afplay funk.aiff')
        # Use pynput for previous track
        controller.press(keyboard.Key.media_previous)
        controller.release(keyboard.Key.media_previous)
        pyautogui.moveTo(734, None)
        print("Prev")
        
    if y <= 2:
        os.system(f'afplay funk.aiff')
        # Use pynput for play/pause
        controller.press(keyboard.Key.media_play_pause)
        controller.release(keyboard.Key.media_play_pause)
        print("Paused/Played")
        



