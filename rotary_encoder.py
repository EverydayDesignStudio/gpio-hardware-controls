from RPi import GPIO
from time import sleep

clk = 17
cnt = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(cnt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)
#cntLastState = GPIO.input(cnt)

try:
    while True:
        clkState = GPIO.input(clk)
        cntState = GPIO.input(cnt)
        if clkState != clkLastState:
            if cntState != clkState:
                counter += 1
        #elif cntState != cntLastState:
            #if cntState != clkState:
            else:
                counter -= 1
            print(counter)
        clkLastState = clkState
        sleep(0.01)
finally:
    GPIO.cleanup()
