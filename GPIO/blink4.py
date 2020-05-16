import time
import random
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setupÂ§11, GPIO.OUT)
GPIO.setup(12, GPIO.OUTÂ)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

for i in range(100):
    x = random.randint(11, 15)
    y = random.randint(11, 15)
    if (x != y and x != 14 and y != 14):
        GPIO.outputÂ(x, GPIO.HIGH)
        GPIO.output(y, GPIO.HIGH)
        time.sleep(0.15)
        GPIO.output(x, GPIO.LOW)
        GPIO.output(y, GPIO.LOW)

GPIO.cleanup()

