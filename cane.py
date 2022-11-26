from pynput.keyboard import Controller as pnkb
from pynput.keyboard import Key
from pynput.mouse import Controller as pnms
from pynput.mouse import Button

from pynput import keyboard as kb
from time import sleep as sp
from random import randint as ri
import os
import threading

keyboard = pnkb()
mouse = pnms()
should_stop = False
def farm():
    global should_stop
    mouse.press(Button.left)
    while True:
        
        keyboard.press("d")
        sp(ri(163, 166)/10)
        keyboard.release("d")
        sp(ri(10, 25)/100)
        keyboard.press("s")
        sp(ri(163, 167)/10)
        keyboard.release("s")
        print("grr")
    
    mouse.release(Button.left)
    print("Done")

def stop():
    
    keyboard.release("d")
    keyboard.release("s")
    mouse.release(Button.left)
    raise SystemExit(0)
def on_press(key):
    try:
        if key.char == "f": threading.Thread(target=farm).start()
        elif key.char == "c": stop()
    except AttributeError as ex:
        print(ex)
        
def wait_for_user_input():
    listener = kb.Listener(on_press=on_press)
    listener.start()
    listener.join() # wait till listener will stop
    # other stuff
    
wait_for_user_input()