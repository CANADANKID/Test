import os #imports the os library
import time #imports the time library
import keyboard #imports the keyboard library
import threading #imports the threading library
import subprocess #imports the subprocess library

namenum = 0 #numbers the renamed files
framenum = 0 #numbers the files it pulling



subprocess.run(["python", "C:\Python\Cv2 test\collect.py"]) #runs the collect.py script


def rename_files(): #creates a function
    global framenum #uses the global framenum 
    global namenum #uses the global namenum
    while framenum <= 10: #creates a loop that ends when the framenum variable is greater than 10
        try: #starts a try gaurd to keep the program running in case of errors
            current_name = f"C:/Python/Cv2 test/Frames/frame_{framenum}.png" #sets the name of the file being renamed
            new_name = f"C:/Python/Cv2 test/Renames/named_{namenum}.png" #set the new name of the file
            os.rename(current_name, new_name) #renames the current file
            framenum += 1 #increments the framenum
            namenum += 1 #increments the namenum
            print("success")  #prints a success message
            time.sleep(0.1) #waits 100 miliseconds 
        except Exception as e: #catches any errors
            print(e) #prints the error
            if keyboard.is_pressed('p'): #checks if the 'p' key was pressed
                break #ends the loop
            framenum += 1 #increments the framenum
            namenum += 1 #increments the namenum
            print("failed") #prints a failed message
            time.sleep(0.5) #waits 500 miliseconds
            continue #continues the loop

rename = threading.Thread(target=rename_files) #creates a thread out of the rename_files function
rename.start() #starts the thread


while True: #starts the loop
    if keyboard.is_pressed('l'): #checks if the 'L' key was pressed
        subprocess.run(["python", "C:\Python\Cv2 test\delete.py"]) #runs the delete.py script
    if keyboard.is_pressed('esc'): #checks if the 'escape' key was pressed
        break #ends the loop



