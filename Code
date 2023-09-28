#!/usr/bin/python3
import time
import threading
import board
import adafruit_veml7700
import os
import cv2
import RPi.GPIO as GPIO

from picamera2 import Picamera2
from picamera2.encoders import MJPEGEncoder
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
from picamera2 import Picamera2, Preview
from picamera2 import MappedArray

from time import sleep

IO = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(IO, GPIO.OUT)
GPIO.output(IO,GPIO.LOW)

picam2 = Picamera2()
#picam2.start(show_preview=True)
#picam2.start_preview(Preview.QTGL)
#preview_config = picam2.create_preview_configuration()
#picam2.configure(preview_config)
 
mp4_output = "testing_wdpt.mp4"

colour = (0, 255, 0)
origin = (0, 30)
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 0.7
thickness = 2

def apply_timestamp(request):
    timestamp = time.strftime("%m-%d-%Y %X")
    with MappedArray(request, "main") as m:
        cv2.putText(m.array, timestamp, origin, font, scale, colour, thickness)

picam2.pre_callback = apply_timestamp

picam2.video_configuration.size = (1920, 1080)
encoder = H264Encoder(bitrate=20000000)
output = FfmpegOutput(mp4_output)

picam2.start()
picam2.start_recording(encoder, output)
time.sleep(5)

GPIO.output(IO, GPIO.HIGH)
delay_in_sec = 0.01
time.sleep(delay_in_sec)
GPIO.output(IO, GPIO.LOW)
time.sleep(5)

picam2.stop_recording()

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
# cv2.waitKey(50) for 20fps
#cap.release()
out.release()
cap.release()
cv2.destroyAllWindows()

i2c = board.I2C()  
veml7700 = adafruit_veml7700.VEML7700(i2c) 
while True:
     print("Lux:", veml7700.lux)
     print("Ambient Light:", veml7700.light)
     time.sleep(1)
    
GPIO.cleanup()
