import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
for i in range(9):
    GPIO.output(21, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(21, GPIO.LOW)
    time.sleep(0.5)
