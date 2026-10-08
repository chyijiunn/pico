from machine import Pin ,PWM
from utime import sleep
button_1 = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_2 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
servoPIN = PWM(Pin(16))
servoPIN.freq(50)
angle = 0
def servo(degrees):
    if degrees > 90: degrees=90
    if degrees < -90: degrees=-90
    maxDuty=9000
    minDuty=1000
    newDuty=((maxDuty+minDuty)/2)+(((maxDuty-minDuty)/2)*(degrees/90))
    print(degrees,'--->',int(newDuty))
    servoPIN.duty_u16(int(newDuty))

servo(angle)
while True:
    if button_1.value() == 1:
        angle = angle + 1
        if angle >= 15:
            angle = 15
        servo(angle)
        sleep(0.1)
    if button_2.value() == 1:
        angle = angle - 1
        if angle <= -5:
            angle = -5
        servo(angle)
        sleep(0.1)