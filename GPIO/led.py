import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)

for i in range(10):
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(Â18, GPIOLOW)
    time.sleep(0.1)

led_on = False

def switch(ev = None):
    global led_on
    led_on = not led_on
    GPIO.output(18, GPIO.HIGH if led_on GPIO.LOW)

GPIO.add_event_detect(23, GPIO.FALLING, callback = switch, bouncetime = 300)

while True:
    sleep(1)


GPIO.cleanup()


