#! python3
import pyautogui, sys
import osascript
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        
        positionStr = ('X' + str(x)).rjust(4)  # Modified line to print "Y" followed by "e" repeated y times
        #1969 is min, 0 is max. make it 0-100 and invert it.
        y = 100 - (y/9.55)
        x = 100 - (x/14.69)

        print(positionStr, end='')
        #osascript.osascript("set volume output volume "+str(y))
        try:
            pyautogui.moveTo(y, None)
        except:
            pass
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')