import cv2 #imports the OpenCV library we will be using

cap = cv2.VideoCapture(0) #replace the 0 with the number of the camera you want to use
cap.set(cv2.CAP_PROP_FPS, 2) #replace the number with the number of frames per second you want to capture

framenum = 0 #starts the frame number at 0
savepath = "C:/Python/Cv2 test/Frames/" #replace the directory with where you want to save the frames

while True: #starts the loop
    ret, frame = cap.read() #reads the frame, ret is whether the frame was read, frame is the frame
    if not ret: #checks ret to see if the frame was read
        break #ends the loop
    cv2.imwrite(f'{savepath}frame_{framenum}.png', frame) #saves the frame
    framenum += 1 #increments the frame number
    if framenum > 10: #checks if the frame number is greater than 10
        break  #ends the loop
    if cv2.waitKey(100) == ord('p'): #waits 100 miliseconds and checks if the 'p' key was pressed
        break #ends the loop
cap.release() #releases the camera