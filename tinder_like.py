from importlib import machinery
from tkinter import Button
import pynput.keyboard
import pynput.mouse
from pynput.mouse import Button
from pynput.keyboard import Key, Controller
import keyboard
import time

kb = Controller()
stop = True
run = True
def onkeypress(event):
    global stop
    global run
    if event.name == '0':
        if stop:
            stop = False
        else:
            stop = True
    if event.name == '1':
        if run:
            run = False
        else:
            run = True

# ---------> hook event handler
keyboard.on_press(onkeypress)
# --------->
while run:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        
        if stop:  # if key '0' is pressed 
            print('Press 0 to Start!')
            #break  # finishing the loop
        else:
            time.sleep(0.3)
            kb.press(Key.right)
            time.sleep(0.2)
            kb.release(Key.right)
    except:
        print('Error')
