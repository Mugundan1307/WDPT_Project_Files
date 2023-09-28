import time
import threading
import os
import cv2

from picamera2 import Picamera2
from picamera2.encoders import MJPEGEncoder
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
from picamera2 import Picamera2, Preview
from picamera2 import MappedArray
from time import sleep

picam2 = Picamera2()
picam2.video_configuration.controls.FrameRate = 90.0
mp4_output = "Testing_WDPT.mp4"

#Adding Timestamp while recording the video
colour = (0, 0, 0) #Black
origin = (0, 30)
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 0.7
thickness = 1

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
time.sleep(10)
picam2.stop_recording()
