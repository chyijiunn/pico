from machine import Pin ,PWM
from utime import sleep
button_1 = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_2 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
servoPIN = PWM(Pin(16))
servoPIN.freq(50)

def servo(degrees):
    if degrees > 90: degrees=90
    if degrees < -90: degrees=-90
    maxDuty=9000
    minDuty=1000
    newDuty=((maxDuty+minDuty)/2)+(((maxDuty-minDuty)/2)*(degrees/90))
    print(degrees,'--->',int(newDuty))
    servoPIN.duty_u16(int(newDuty))

while True:
    if button_1.value() == 1:
        servo(-5)
        sleep(1)
    else:
        servo(10)
        sleep(1)
