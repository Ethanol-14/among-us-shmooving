import keyboard
from pynput.keyboard import Key, Controller
import time

keypress = Controller()

delay = 1/30

while True:
    if keyboard.is_pressed('t'):
        keypress.press('w')
        time.sleep(delay)
        keypress.release('w')
        time.sleep(delay)
        print("detected t")

    if keyboard.is_pressed('g'):
        keypress.press('s')
        time.sleep(delay)
        keypress.release('s')
        time.sleep(delay)
        print("detected g")

    if keyboard.is_pressed('f'):
        keypress.press('a')
        time.sleep(delay)
        keypress.release('a')
        time.sleep(delay)
        print("detected f")

    if keyboard.is_pressed('h'):
        keypress.press('d')
        time.sleep(delay)
        keypress.release('d')
        time.sleep(delay)
        print("detected h")

    #horizontal shmoove
    if keyboard.is_pressed('r'):
        keypress.press('a')
        time.sleep(delay)
        keypress.release('a')
        keypress.press('d')
        time.sleep(delay)
        keypress.release('d')
        print("detected r")

    #vertical shmoove
    if keyboard.is_pressed('y'):
        keypress.press('w')
        time.sleep(delay)
        keypress.release('w')
        keypress.press('s')
        time.sleep(delay)
        keypress.release('s')
        print("detected y")

    #general shmoove
    if keyboard.is_pressed('v'):
        keypress.press('a')
        time.sleep(delay)
        keypress.release('a')
        keypress.press('d')
        time.sleep(delay)
        keypress.release('d')
        keypress.press('w')
        time.sleep(delay)
        keypress.release('w')
        keypress.press('s')
        time.sleep(delay)
        keypress.release('s')
        print("detected v")
