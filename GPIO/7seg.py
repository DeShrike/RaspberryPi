import RPi.GPIO as GPIO
import time

# sn74hc595n
# SMA42056 common cathode

DATA = 4    # connect to pin 14 SER
CLOCK = 17  # connect to pin 11 SRCLCK
LATCH = 22  # connect to pin 12 RCLCK
CLEAR = 19  # connect to pin 10 SRCLR (enabled low)

GPIO.setmode(GPIO.BCM)

GPIO.setup(DATA,GPIO.OUT)
GPIO.setup(CLOCK,GPIO.OUT)
GPIO.setup(LATCH,GPIO.OUT)
GPIO.setup(CLEAR,GPIO.OUT)

# Segments

A = 1 << 0
B = 1 << 1
C = 1 << 2
D = 1 << 3
E = 1 << 4
F = 1 << 6
G = 1 << 5
DP = 1 << 7

TOP = A
CENTER = G
BOTTOM = D
LEFT = E | F
RIGHT = B | C

# Digits

digits = {
    '0': A | B | C | D | E | F,
    '1': B | C,
    '2': A | B | G | D | E,
    '3': A | B | C | D | G,
    '4': B | C | F | G,
    '5': A | C | D | F | G,
    '6': A | C | D | E | F | G,
    '7': A | B | C,
    '8': A | B | C | D | E | F| G, 
    '9': A | B | C | D | F | G, 
    'A': A | B | C | E | F | G, 
    'B': C | D | E | F | G, 
    'C': A | D | E | F,
    'D': B | C | D | E | G, 
    'E': A | D | E | F | G, 
    'F': A | E | F | G
}


def pulsePin(pin):
    # Pulse a pin high then low
    # the latch and the clock pins
    # need this to load in and output data
    GPIO.output(pin, 1)
    time.sleep(0.01)
    GPIO.output(pin, 0)


def outputValue(value):
    # Convert a decimal value to a binary one
    # then load that onto the shift register, one bit at a time
    # by setting the datapin high for 1, low for zero
    # Pulse the clock pin until all 16 bits have been loaded
    # on to the shift register
    # then pulse the latch pin to output the data

    sbin = "{0:08b}".format(value)
    print ("binary for %s is %s " % (value, sbin))
    # step through one bit at a time
    for bit in sbin:
        print "bit  == ", bit
        if bit == "1":
            GPIO.output(DATA, 1)
        else:
            GPIO.output(DATA, 0)
        pulsePin(CLOCK)
    time.sleep(0.01)
    # all bits loaded, now output them
    pulsePin(LATCH)

def showChar(char):
    value = digits[char]
    print(char, value)
    outputValue(value)

def run():
    for i in range(0, 256):
        outputValue(i)
        time.sleep(0.01)

def loop(delay):
    for l in range(0, 10):
        outputValue(A)
        time.sleep(delay)
        outputValue(B)
        time.sleep(delay)
        outputValue(C)
        time.sleep(delay)
        outputValue(D)
        time.sleep(delay)
        outputValue(E)
        time.sleep(delay)
        outputValue(F)
        time.sleep(delay)

    outputValue(0)
    time.sleep(1)

    for l in range(0, 10):
        outputValue(TOP)
        time.sleep(delay)
        outputValue(CENTER)
        time.sleep(delay)
        outputValue(BOTTOM)
        time.sleep(delay)
        outputValue(CENTER)
        time.sleep(delay)

    outputValue(0)
    time.sleep(1)

    for l in range(0, 10):
        outputValue(LEFT)
        time.sleep(delay)
        outputValue(RIGHT)
        time.sleep(delay)

    outputValue(0)
    time.sleep(1)

    for l in range(0, 10):
        for ix in range(0,10):
            ch = str(ix)
            print(ch)
            showChar(ch)
            time.sleep(delay)

    outputValue(DP)

def wait():
    outputValue(DP)
    while True:
        time.sleep(1)

def flash():
    for i in range(0, 10):
        outputValue(0)
        time.sleep(0.001)
        outputValue(DP)
        time.sleep(0.001)

def test():
    print('A')
    showChar('A')
    time.sleep(1)
    showChar('B')
    time.sleep(1)
    showChar('C')
    time.sleep(1)
    showChar('D')
    time.sleep(1)
    showChar('E')
    time.sleep(1)
    showChar('F')
    time.sleep(1)

if __name__ == "__main__":
    try:
        outputValue(0)
        time.sleep(3)
        
        run()
        test()
        flash()
        loop(0.01)
        
        wait()
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()


