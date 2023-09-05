import pyautogui
import pydirectinput
import keyboard
import random
import time
import threading

keys = ['w', 'a', 's', 'd']
delay_between_keys = 0.1
paused = False 
Epressed = False
Ppressed = False

def simulate_keys():
    global paused
    while True:
        if not paused:
            key_to_press = random.choice(keys)
            pydirectinput.keyDown(key_to_press)
            time.sleep(delay_between_keys)
            pydirectinput.keyUp(key_to_press)
            if Epressed:
                print("Paused")
                paused = True
        if paused:
            if not Epressed:
                print("Unpaused")
                paused = False
        if Ppressed:
            break

def Key():
    global Epressed
    global Ppressed
    while True:
        if not Ppressed:
            if keyboard.is_pressed('p'):
                print("off")
                Ppressed = True
                break
        if not Epressed:
            time.sleep(0.1)
            if keyboard.is_pressed('e'):
                Epressed = True
                print("pressed")
        if Epressed:
            time.sleep(0.1)    
            if keyboard.is_pressed('e'):
                Epressed = False
                print("unpressed")



script_thread = threading.Thread(target=simulate_keys)
script_thread.start()
Key_thread = threading.Thread(target=Key)
Key_thread.start()


try:
    script_thread.join()
except KeyboardInterrupt:
    pass



