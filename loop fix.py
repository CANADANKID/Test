import threading
import keyboard
import time

on = True
x = 1
xing = False

def smth():
    global xing
    time.sleep(0.1) #if you don't have this wait
    while on:
        if xing:
            print("grapes")

def go():
    global x
    global on
    global xing
    print("circle")
    while True:
        if on:
            print(x)
            x += 1
            if x > 10:
                x = 1
        if keyboard.is_pressed('esc'):
            on = False
            break
        if keyboard.is_pressed ('p'): # this will cause the code to freeze
            if xing:
                xing = False
                print("flainfing")
            else:
                xing = True
                print("truen")

threading.Thread(target=smth).start()
threading.Thread(target=go).start()