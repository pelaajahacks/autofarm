from pynput.keyboard import Controller as pnkb
from pynput.keyboard import Key
from pynput.mouse import Controller as pnms
from pynput.mouse import Button
from time import sleep as sp
from random import randint as ri
import threading
from pynput import keyboard as kb

layers = input("How many layers? >>> ")
keyboard = pnkb()
mouse = pnms()


def farm(layers):
    mouse.press(Button.left)
    for i in range(int(layers)//2):
        keyboard.press("a")
        sp(ri(265, 275)/10)
        keyboard.release("a")
        sp(ri(10, 25)/100)
        keyboard.press("d")
        sp(ri(265, 275)/10)
        keyboard.release("d")
        print("Layer", i+1, "done")
        
    mouse.release(Button.left)
    print("Done")

def stop():
    
    keyboard.release("d")
    keyboard.release("s")
    mouse.release(Button.left)
    raise SystemExit(0)
def on_press(key):
    try:
        if key.char == "f": threading.Thread(target=farm, args=(layers,)).start()
        elif key.char == "c": stop()
    except AttributeError as ex:
        print(ex)
        
def wait_for_user_input():
    listener = kb.Listener(on_press=on_press)
    listener.start()
    listener.join() # wait till listener will stop
    # other stuff
    
wait_for_user_input()