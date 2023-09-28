import time
import threading
import os
import cv2
import RPi.GPIO as GPIO

from time import sleep

IO = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(IO, GPIO.OUT)
GPIO.output(IO,GPIO.LOW)

time.sleep(5)

GPIO.output(IO, GPIO.HIGH)
delay_in_sec = 0.005 #5ms
time.sleep(delay_in_sec)
GPIO.output(IO, GPIO.LOW)
time.sleep(5)

GPIO.cleanup()
