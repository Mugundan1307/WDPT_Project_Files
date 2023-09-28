#!/usr/bin/python3
import time
import threading
import os
import cv2

from time import sleep
# Initialize the camera
cap = cv2.VideoCapture('/dev/video0')  # Change to 1 if the camera is the second camera (usually USB)
# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can change the codec as needed
out = cv2.VideoWriter('imx179_recorded_video.avi', fourcc, 20.0, (640, 480))  # Adjust resolution if needed

start_time = time.time()
record_duration = 10
# Record video
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Write the frame to the output video
    out.write(frame)

    cv2.imshow('Recording', frame)
    
    # Press 'q' to stop recording
    if cv2.waitKey(45) & 0xFF == ord('q'):
#     or (time.time() - start_time) >=record_duration:
        break

out.release()
cap.release()
cv2.destroyAllWindows() 
