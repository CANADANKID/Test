import os #imports the os library

directory_path = "C:/Python/Cv2 test/Renames"  #Replace the directory with the directory with the outputted files
file_list = os.listdir(directory_path) #List all files in the directory

for file_name in file_list: #starts a loop thats to go through all the files it found
    file_path = os.path.join(directory_path, file_name) #joins the directory with the file
    try: #starts a try gaurd to handle errors better
        if os.path.isfile(file_path): #Makes sure it can access the file
            os.remove(file_path) #removes the file
            print(f"Removed: {file_path}") #prints a success message
    except Exception as e: #catches any errors
        print(f"Error removing {file_path}: {e}") #prints the error

print(directory_path) #prints the directory
print(file_list) #prints the file list